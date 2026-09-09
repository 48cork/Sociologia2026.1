# Workflow: Revisar Lote — Aulas 24–30

Máquina de estados documental para reconstrução, revisão, QA e commits locais. Este
arquivo não é um executável e não deve ser apresentado como CLI nativa.

## Estados

| Estado | Significado | Saídas permitidas |
|---|---|---|
| `PENDENTE` | aula ainda não selecionada | `EM_RECONSTRUCAO`, `AGUARDA_HUMANO`, `FALHA_TECNICA` |
| `EM_RECONSTRUCAO` | único HTML autorizado em edição | `EM_REVISAO`, `AGUARDA_HUMANO`, `FALHA_TECNICA` |
| `EM_REVISAO` | pareceres independentes/Aprovador em curso | `PRONTO`, `PRECISA_REVISAR`, `AGUARDA_HUMANO`, `FALHA_TECNICA` |
| `PRECISA_REVISAR` | ajustes rastreáveis pendentes | `EM_REVISAO`, `AGUARDA_HUMANO`, `FALHA_TECNICA` |
| `PRONTO` | Aprovador e QA passaram | `COMMITADO`, `FALHA_TECNICA` |
| `PRONTO_AGUARDANDO_PAR` | primeira aula do gate aprovada, com hash bloqueado | `COMMITADO`, `FALHA_TECNICA` |
| `AGUARDA_HUMANO` | falta insumo/decisão ou duas rodadas falharam | retomada humana explícita |
| `COMMITADO` | gate local concluído | próximo gate ou conclusão |
| `FALHA_TECNICA` | hash, Git, script ou integridade falhou | diagnóstico humano; sem restauração automática |

Transições devem ser registradas em `config/estado.yaml` e em relatório datado com HEAD,
hash da aula e motivo. Estado não substitui evidência.

## Algoritmo do lote

1. **Pré-voo:** confirmar raiz do repositório, branch esperada e árvore limpa. Registrar
   HEAD, `git status --short` e SHA-256 das 30 aulas. Divergência não explicada gera
   `FALHA_TECNICA`; não limpar nem restaurar.
2. **Mapa:** executar somente o Revisor de Progressão, que lê as 30 aulas sem alterar
   HTML e grava `mapa-progressao.md`. Validar estado `COMPLETO`, HEAD e 30 entradas.
3. **Fila:** processar 24, 25, 26, 27, 28, 29 e 30 nessa ordem. Aulas 01–23 permanecem
   protegidas; aulas futuras permanecem somente leitura.
4. **Seleção:** definir uma única `aula_selecionada`. Em gate unitário, capturar o HTML
   selecionado. Em gate de par, autorizar explicitamente os dois HTMLs; se a primeira
   aula já estiver `PRONTO_AGUARDANDO_PAR`, informar seu SHA-256 com `--hash-aprovado`.
   Mudar somente a aula selecionada para `EM_RECONSTRUCAO`.
5. **Reconstrução:** permitir escrita somente nessa aula. Infraestrutura só muda na
   manutenção do squad, nunca durante processamento editorial.
6. **Revisão:** seguir `revisar-aulas.md`; os quatro pareceres são independentes e usam
   obrigatoriamente o mapa.
7. **Aprovação:** entregar pareceres e mapa ao mesmo Aprovador. `PRONTO` conduz ao QA;
   `PRECISA_REVISAR` conduz ao reparo rastreável.
8. **Reparo:** máximo de duas rodadas automáticas. Reexecutar agentes de origem e o
   Aprovador. Conflito conceitual, insumo ausente ou terceira necessidade de reparo gera
   `AGUARDA_HUMANO`.
9. **QA:** executar auditor, validação de escopo e `git diff --check`. No primeiro item
   de um par, registrar caminho, SHA-256, veredito e QA e mudar para
   `PRONTO_AGUARDANDO_PAR`. Antes e depois do segundo item, validar novamente o hash
   aprovado da primeira aula. Falha gera
   `FALHA_TECNICA` e interrompe o lote.
10. **Gate sequencial:** só selecionar a aula seguinte depois de `PRONTO` e QA aprovado.
11. **Commit:** aplicar a política abaixo quando todas as aulas do gate estiverem
    `PRONTO`, sem decisão humana pendente e com escopo Git exato.
12. **Conclusão:** parar depois do último commit local. Não executar operação remota.

## Política de reparo

- Cada ajuste contém `[Fonte: Nome do agente]`, trecho/seção e resultado esperado.
- O parecer pós-reparo cita novo SHA-256 e a pendência anterior.
- Revisor Teórico retorna para erro conceitual; Revisor de Progressão para progressão;
  Revisor Pedagógico para didática; Revisor de Fluidez para prosa; Conteudista para
  cobertura, material ou referência.
- Aprovador retorna em toda rodada e é o único veredito final.
- Agente que propôs ou aplicou reparo não se autoaprova.
- Duas rodadas sem aprovação encerram automação em `AGUARDA_HUMANO`.

## Allowlist e concorrência

Durante uma aula, alterações permitidas são:

1. o HTML exato selecionado;
2. `config/estado.yaml`, explicitamente autorizado;
3. relatórios com prefixo `relatorios/aula-NN/`, explicitamente autorizados;
4. `mapa-progressao.md` apenas na etapa do Revisor de Progressão ou reparo de progressão.

Outro HTML modificado, hash protegido divergente ou arquivo inesperado gera
`FALHA_TECNICA`. Não restaurar automaticamente.

Em gates de par, os dois HTMLs do gate podem constar simultaneamente da allowlist. A
primeira aula aprovada não é ignorada: seu hash fica em `hashes_aprovados` no baseline
do par e deve permanecer idêntico em toda validação da segunda. A allowlist rejeita
aulas de gates diferentes. Estado e relatório da primeira aula continuam exigindo
`--permitir` explícito.

Proibido: `git add -A`, `git add .`, `git reset`, `git restore`, `git checkout --`,
`git clean` e equivalentes. Não permitir dois escritores na mesma worktree. Para
paralelismo com escrita, usar worktrees separadas e reconciliar somente após gates.

## Gates de commit local

| Gate | Pré-condição | Stage exato | Mensagem |
|---|---|---|---|
| Aula 24 | 24 `PRONTO` + QA | `aula-24.html` | `feat: reconstruir texto-base da aula 24` |
| 25–26 | ambas `PRONTO` + QA | `aula-25.html aula-26.html` | `feat: reconstruir textos-base das aulas 25 e 26` |
| 27–28 | ambas `PRONTO` + QA | `aula-27.html aula-28.html` | `feat: reconstruir textos-base das aulas 27 e 28` |
| 29–30 | ambas `PRONTO` + QA | `aula-29.html aula-30.html` | `feat: reconstruir textos-base das aulas 29 e 30` |

Antes de cada commit, confirmar `git diff --check`, lista exata no índice e hashes dos
protegidos. O workflow pode criar somente esses commits locais. `PRONTO` isolado não
autoriza commit antes de completar o par correspondente.

## Gate humano remoto

Push, merge, pull request, deploy, GitHub Pages e qualquer publicação pública ficam fora
desta máquina de estados. Mesmo após `COMMITADO`, uma solicitação humana explícita e
separada é obrigatória.
