# Squad de Revisão de Aulas — Introdução à Sociologia 2026.2

Adaptação portátil do Squad de Revisão de Aulas de Sociologia Rural para as 30 páginas
de `introducao-sociologia/turma1/aulas/`. O mecanismo preserva os seis papéis da origem,
inclusive o mesmo **Aprovador**, e acrescenta proteção de escopo, estados, reparos
limitados e QA determinístico.

O squad é documental: não há comando CLI nativo ou runtime AIOX registrado neste
repositório. Codex, Claude ou uma pessoa executora devem ler os arquivos abaixo e
orquestrar suas etapas. Nenhum agente edita por conta própria; somente o orquestrador,
dentro da allowlist vigente, aplica uma reconstrução ou reparo.

## Estrutura

```text
squad-revisao-aulas/
├── README.md
├── mapa-progressao.md
├── agentes/
│   ├── conteudista.md
│   ├── revisor-teorico.md
│   ├── revisor-fluidez.md
│   ├── revisor-pedagogico.md
│   ├── revisor-progressao.md
│   └── aprovador.md
├── config/
│   ├── curso.yaml
│   ├── criterios.yaml
│   └── estado.yaml
├── workflows/
│   ├── revisar-aulas.md
│   └── revisar-lote.md
├── scripts/
│   ├── auditar_aulas.py
│   └── validar_escopo.py
└── relatorios/
```

Os arquivos `.yaml` usam o subconjunto JSON válido em YAML 1.2. Isso permite parsing
determinístico apenas com `json`, da biblioteca padrão do Python, sem PyYAML.

## Escopo inicial

- Aulas 01–23: aprovadas, contexto obrigatório e sempre somente leitura.
- Aulas 24–30: fila inicial de processamento.
- Aula selecionada: único HTML com permissão de escrita durante sua etapa. Em gate de
  par, o HTML anterior aprovado pode permanecer modificado, bloqueado por SHA-256.
- Página anterior e seguinte: contexto somente leitura.
- Infraestrutura do squad: somente pode mudar em tarefa explícita de manutenção.

Antes de qualquer escrita, capturar o estado com `validar_escopo.py`. Depois, validar
hashes e alterações; o script nunca restaura arquivos. A captura cria um baseline novo
e recusa sobrescrever um arquivo existente; a validação é sempre somente leitura.

## Agentes e dependências

1. O Revisor de Progressão lê as 30 aulas e produz o mapa.
2. Conteudista, Revisor Teórico, Revisor de Fluidez e Revisor Pedagógico produzem
   pareceres independentes, todos usando o mapa.
3. O Aprovador recebe os quatro pareceres e os apontamentos do mapa e emite somente
   `PRONTO` ou `PRECISA REVISAR`.
4. `PRONTO` permite executar QA; não autoriza Git nem publicação.

As Aulas 24–30 devem preservar o padrão alcançado nas Aulas 01–23, mas cada página deve
ter arquitetura e exemplos próprios. Aulas de seminário ou encerramento podem justificar
uma estrutura pedagógica distinta; a exceção deve aparecer no parecer do Conteudista e
ser aceita pelo Aprovador.

## QA determinístico

```bash
python3 squad-revisao-aulas/scripts/auditar_aulas.py \
  introducao-sociologia/turma1/aulas/aula-24.html

python3 squad-revisao-aulas/scripts/auditar_aulas.py --intervalo 24-30
```

O auditor é somente leitura, usa apenas a biblioteca padrão e retorna código diferente
de zero quando encontra falha. Ele não substitui os pareceres qualitativos.

## Proteção de escopo

```bash
python3 squad-revisao-aulas/scripts/validar_escopo.py capturar \
  --arquivo introducao-sociologia/turma1/aulas/aula-24.html \
  --saida squad-revisao-aulas/relatorios/aula-24-baseline.json

python3 squad-revisao-aulas/scripts/validar_escopo.py validar \
  --arquivo introducao-sociologia/turma1/aulas/aula-24.html \
  --baseline squad-revisao-aulas/relatorios/aula-24-baseline.json \
  --permitir squad-revisao-aulas/relatorios/aula-24 \
  --permitir squad-revisao-aulas/config/estado.yaml
```

Para um gate em par, a interface repetível registra ambos os HTMLs e bloqueia a primeira
aula já aprovada no digest registrado pelo parecer/QA:

```bash
python3 squad-revisao-aulas/scripts/validar_escopo.py capturar \
  --autorizar-aula introducao-sociologia/turma1/aulas/aula-25.html \
  --autorizar-aula introducao-sociologia/turma1/aulas/aula-26.html \
  --hash-aprovado introducao-sociologia/turma1/aulas/aula-25.html=SHA256_APROVADO \
  --saida squad-revisao-aulas/relatorios/aula-26-baseline.json

python3 squad-revisao-aulas/scripts/validar_escopo.py validar \
  --autorizar-aula introducao-sociologia/turma1/aulas/aula-25.html \
  --autorizar-aula introducao-sociologia/turma1/aulas/aula-26.html \
  --baseline squad-revisao-aulas/relatorios/aula-26-baseline.json \
  --permitir squad-revisao-aulas/config/estado.yaml \
  --permitir squad-revisao-aulas/relatorios/aula-25-relatorio.md \
  --permitir squad-revisao-aulas/relatorios/aula-26-relatorio.md
```

Somente caminhos explicitamente passados em `--permitir` podem acompanhar os HTMLs
autorizados. Outra aula só entra por `--autorizar-aula`, deve pertencer ao mesmo gate e,
se já aprovada e modificada, exige `--hash-aprovado`. Relatórios devem usar prefixo
específico da aula para evitar uma autorização ampla.

São proibidos no workflow: `git add -A`, `git add .`, `git reset`, `git restore`,
`git checkout --`, `git clean` e equivalentes. Se houver paralelismo com escrita, usar
worktrees separadas; dois agentes não editam a mesma árvore simultaneamente.

## Política de commits

| Gate | Arquivos | Mensagem |
|---|---|---|
| 1 | Aula 24 | `feat: reconstruir texto-base da aula 24` |
| 2 | Aulas 25–26 | `feat: reconstruir textos-base das aulas 25 e 26` |
| 3 | Aulas 27–28 | `feat: reconstruir textos-base das aulas 27 e 28` |
| 4 | Aulas 29–30 | `feat: reconstruir textos-base das aulas 29 e 30` |

Commit local só pode ocorrer quando todas as aulas do gate estiverem `PRONTO`, o QA
passar, o escopo Git estiver correto e não houver decisão humana pendente. Adicionar ao
índice somente os caminhos exatos do gate.

Push, merge, pull request, deploy e publicação pública nunca são automáticos. Exigem
autorização humana explícita posterior e não fazem parte deste workflow.

## Ponto único de entrada

> Execute o workflow local `squad-revisao-aulas/workflows/revisar-lote.md` para as Aulas
> 24–30, respeitando `config/curso.yaml`, `config/criterios.yaml` e
> `config/estado.yaml`. Use os seis agentes existentes, incluindo o Aprovador. Pare
> somente em AGUARDA_HUMANO, FALHA_TECNICA ou conclusão. Commits locais conforme a
> política; nenhuma operação remota.

Esse texto é um prompt de orquestração, não um comando CLI.

## Manutenção

Mudanças nos agentes, configurações, scripts ou workflows constituem tarefa de
manutenção do squad e não podem ser misturadas ao processamento de uma aula. O
Aprovador local deve continuar sendo adaptação rastreável do agente original; não criar
outro agente de aprovação final.
