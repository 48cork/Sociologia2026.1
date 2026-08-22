# Story — Reconciliar regras de Introdução à Sociologia

## Status

Pronta para implementação.

## História

Como docente responsável por Introdução à Sociologia, quero que o portal geral e o cronograma consolidado reproduzam as regras e datas dos planos canônicos das duas turmas, para que estudantes encontrem informações coerentes sobre avaliação, calendário, atividade integradora, ética e futuro Laboratório.

## Contexto e fontes de verdade

- `CLAUDE.md` define os planos `plano_aulas.md` como fontes canônicas para datas, conteúdos e carga horária.
- Turma 1: `introducao-sociologia/turma1/plano_aulas.md`, código 2101107, 30 encontros, 14/04/2026 a 29/07/2026.
- Turma 2: `introducao-sociologia/turma2/plano_aulas.md`, código 2101000, 18 encontros, 13/04/2026 a 10/08/2026.
- Avaliação aprovada: pesquisa bibliográfica, apresentação oral, relatório e vídeo, cada qual com 25%.
- “A IA Tem Classe Social?” é atividade integradora no fechamento, não eixo obrigatório de todos os encontros.
- Os trabalhos produzidos pelos estudantes destinam-se exclusivamente ao ensino e à avaliação da disciplina. Qualquer utilização posterior em pesquisa, apresentação ou publicação depende de autorização específica, finalidade previamente informada, anonimização e observância da análise ética e institucional aplicável.
- As personas utilizadas na atividade são inteiramente sintéticas, criadas exclusivamente para fins didáticos e não representam estudantes ou pessoas reais.
- O futuro Laboratório começa como atividade formativa, sem peso próprio ou alteração dos quatro pesos oficiais.

## Escopo

### Arquivos autorizados

- `index.html`
- `Cronograma_Sociologia_2026-1.md`
- `docs/stories/reconciliar-regras-introducao-sociologia.md`

### Arquivos e áreas vedados

- Os 48 roteiros de Introdução à Sociologia.
- Os índices e planos canônicos das Turmas 1 e 2.
- Outros cursos do repositório.
- Arquivos de configuração.
- Materiais do projeto de Sociologia Rural.
- Implementação funcional do Laboratório.

## Critérios de aceitação

1. O portal e o cronograma apresentam pesquisa bibliográfica, apresentação oral, relatório e vídeo com 25% cada, totalizando 100%.
2. Prazos e encontros distinguem as turmas e coincidem com os planos canônicos:
   - Turma 1: pesquisa em 02/06; apresentações em 22/07 e 28/07; relatório e vídeo em 29/07.
   - Turma 2: pesquisa em 08/06; apresentações em 03/08 e 10/08; relatório e vídeo em 10/08.
3. Turma 1 aparece como código 2101107 e Turma 2 como código 2101000, sem identificação repetida ou trocada.
4. “A IA Tem Classe Social?” é descrita como atividade integradora no fechamento, sem afirmar que organiza obrigatoriamente todos os encontros.
5. Encontros e roteiros são apresentados como aulas ou encontros; não há generalização de que todos sejam simulações.
6. Não há inferências não documentadas sobre turno, renda, emprego ou chefia familiar dos estudantes.
7. Na seção visível da atividade integradora, a política de trabalhos discentes limita-os exclusivamente ao ensino e à avaliação da disciplina e exige, para utilização posterior em pesquisa, apresentação ou publicação, autorização específica, finalidade previamente informada, anonimização e observância da análise ética e institucional aplicável.
8. Na seção visível da atividade integradora, o portal declara que as personas são inteiramente sintéticas, foram criadas exclusivamente para fins didáticos e não representam estudantes ou pessoas reais.
9. O futuro Laboratório é informado como inicialmente formativo, sem peso próprio na nota e sem alterar o sistema 25/25/25/25.
10. O visual existente é preservado e conteúdo já coerente ou relativo a outros cursos não é alterado.
11. Somente os três arquivos autorizados apresentam mudanças ao final.

## Riscos e mitigação

| Risco | Mitigação |
|---|---|
| Propagar datas gerais incorretas para turmas com calendários diferentes | Exibir prazos separados por turma e confrontá-los com cada plano canônico. |
| Alterar acidentalmente roteiros, índices, planos ou outro curso | Registrar hashes antes da edição, limitar patches aos arquivos autorizados e comparar hashes ao final. |
| Sugerir uso acadêmico dos trabalhos sem salvaguardas suficientes | Aplicar literalmente a política ética aprovada em todos os avisos pertinentes. |
| Transformar a atividade integradora em eixo curricular obrigatório | Usar linguagem de fechamento e preservar os conteúdos canônicos de cada encontro. |
| Criar um quinto componente avaliativo com o futuro Laboratório | Declarar caráter formativo e ausência de peso próprio. |
| Degradar a apresentação visual | Reutilizar estrutura, classes e estilos inline existentes, sem criar configuração ou novo sistema visual. |

## Testes e verificações

- Revisão textual dirigida com `rg` para pesos, datas, códigos, “simulação”, ética, personas e Laboratório.
- Conferência manual de todos os prazos contra os dois `plano_aulas.md` canônicos.
- `git diff --check`.
- Verificação automatizada de links locais do `index.html` e, quando aplicável, do Markdown.
- Comparação SHA-256 dos 48 roteiros, dois planos e dois índices antes e depois.
- Inspeção de `git diff --` restrita aos três arquivos autorizados.
- Inicialização de servidor HTTP local e resposta HTTP bem-sucedida para as páginas HTML revisadas.
- Revisão visual do portal servido localmente, preservando layout e legibilidade.

## Definição de pronto

- Todos os critérios de aceitação estão atendidos.
- As verificações listadas passam sem erro ou têm eventual limitação explicitamente documentada.
- `git status` mostra somente arquivos autorizados como modificados ou novos.
- O diff final é apresentado para revisão humana.
- Servidor local permanece disponível e sua URL é informada.
- Nenhum commit, push, merge ou publicação é realizado.
- A implementação aguarda aprovação humana.

## Validação da story

- [x] História identifica usuário, necessidade e benefício.
- [x] Fontes de verdade e decisões aprovadas estão explícitas.
- [x] Escopo autorizado e exclusões estão delimitados.
- [x] Critérios são específicos, observáveis e testáveis.
- [x] Datas e códigos foram confrontados com os planos canônicos.
- [x] Riscos possuem mitigação correspondente.
- [x] Testes cobrem conteúdo, integridade, links, diff e revisão local.
- [x] Definição de pronto inclui aprovação humana e proíbe operações remotas.

## Registro da correção editorial mínima

- Frase sobre personas ampliada e exibida junto aos dois perfis da atividade integradora.
- Política de trabalhos discentes reformulada e mantida em alerta visual na mesma seção.
- Correção limitada a `index.html` e a esta story, sem alteração de cronograma, roteiros, planos ou índices.

**Resultado da validação:** APROVADA para implementação pelo fluxo local disponível. O ativador AIOX referenciado pelos skills não está presente nesta cópia (`.aiox-core` e fallback `.codex/agents` ausentes); por isso, foi aplicada validação documental equivalente e rastreável com base no `CLAUDE.md` e nos planos canônicos.
