# Story — Reconciliar regras de Introdução à Sociologia

## Status

Implementada. Aguardando revisão humana, sem commit ou publicação.

## História

Como docente responsável por Introdução à Sociologia, quero que a página principal de 2026.2 apresente a avaliação final, o calendário, a atividade de fevereiro, a ética e o Laboratório com regras coerentes, para que estudantes encontrem orientação verificável em um único lugar.

## Contexto e fontes de verdade

- `CLAUDE.md` define os planos `plano_aulas.md` como fontes canônicas para datas, conteúdos e carga horária.
- Turma 1: `introducao-sociologia/turma1/plano_aulas.md`, código 2101107, 30 encontros, 14/04/2026 a 29/07/2026.
- Turma 2: `introducao-sociologia/turma2/plano_aulas.md`, código 2101000, 18 encontros, 13/04/2026 a 10/08/2026.
- Avaliação 2026.2 aprovada para a página principal: experimento sociológico com inteligência artificial, em grupos de até cinco estudantes, com personas fictícias comparáveis cuja única variável deliberadamente modificada é a renda mensal.
- Questão central da avaliação 2026.2: “Como a inteligência artificial reproduz desigualdades sociais?”
- A pergunta “A IA tem classe social?” pode aparecer como provocação inicial, mas não substitui a questão central da avaliação de 2026.2.
- A atividade vale 10,0 pontos e é avaliada pela rubrica publicada na página, sem afirmação de que corresponda à nota integral da disciplina e sem regras adicionais de conversão, divisão ou unidades avaliativas do SIGAA.
- Os trabalhos produzidos pelos estudantes destinam-se exclusivamente ao ensino e à avaliação da disciplina. Qualquer utilização posterior em pesquisa, apresentação ou publicação depende de autorização específica, finalidade previamente informada, anonimização e observância da análise ética e institucional aplicável.
- As personas utilizadas na atividade são inteiramente sintéticas, criadas exclusivamente para fins didáticos e não representam estudantes ou pessoas reais.
- O Laboratório permanece como espaço formativo e não altera a avaliação final descrita na página.

## Escopo

### Arquivos autorizados nesta retomada

- `introducao-sociologia/index.html`
- `docs/stories/reconciliar-regras-introducao-sociologia.md`

### Arquivos e áreas vedados

- Os 48 roteiros de Introdução à Sociologia.
- Os índices e planos canônicos das Turmas 1 e 2.
- Outros cursos do repositório.
- Arquivos de configuração.
- Materiais do projeto de Sociologia Rural.
- Implementação funcional do Laboratório.

## Critérios de aceitação

1. A página principal apresenta seção específica “Avaliação — experimento sociológico com inteligência artificial”.
2. O calendário preserva 15 encontros regulares, 60 horas, integralização em 16/12/2026 e percurso complementar de fevereiro de 2027.
3. A página preserva código 2101000, SIGAA 4M1234 e turma única T01 de 2026.2.
4. “A IA tem classe social?” aparece apenas como provocação inicial possível, sem substituir a questão central da avaliação.
5. Encontros e roteiros são apresentados como aulas ou encontros; não há generalização de que todos sejam simulações.
6. Não há inferências não documentadas sobre turno, renda, emprego ou chefia familiar dos estudantes.
7. Na seção visível da atividade integradora, a política de trabalhos discentes limita-os exclusivamente ao ensino e à avaliação da disciplina e exige, para utilização posterior em pesquisa, apresentação ou publicação, autorização específica, finalidade previamente informada, anonimização e observância da análise ética e institucional aplicável.
8. Na seção visível da atividade integradora, o portal declara que as personas são inteiramente sintéticas, foram criadas exclusivamente para fins didáticos e não representam estudantes ou pessoas reais.
9. O futuro Laboratório é informado como espaço formativo e não altera a avaliação final descrita na página.
10. O visual existente é preservado e conteúdo já coerente ou relativo a outros cursos não é alterado.
11. Somente os dois arquivos autorizados nesta retomada apresentam mudanças ao final.

## Riscos e mitigação

| Risco | Mitigação |
|---|---|
| Propagar datas, pesos ou regras não definidos | Preservar o calendário existente e declarar somente o valor de 10,0 pontos e a rubrica aprovada. |
| Alterar acidentalmente roteiros, índices, planos ou outro curso | Registrar hashes antes da edição, limitar patches aos arquivos autorizados e comparar hashes ao final. |
| Sugerir uso acadêmico dos trabalhos sem salvaguardas suficientes | Aplicar literalmente a política ética aprovada em todos os avisos pertinentes. |
| Transformar a atividade integradora em eixo curricular obrigatório | Usar linguagem de fechamento e preservar os conteúdos canônicos de cada encontro. |
| Criar um componente avaliativo adicional com o futuro Laboratório | Declarar caráter formativo e manter a avaliação final concentrada no experimento sociológico. |
| Degradar a apresentação visual | Reutilizar estrutura, classes e estilos inline existentes, sem criar configuração ou novo sistema visual. |

## Testes e verificações

- Revisão textual dirigida com `rg` para questão central, formato avaliativo, materiais legados, ética, personas, SIGAA e Laboratório.
- Conferência manual do calendário já existente: 15 encontros, 60 horas regulares, recesso e percurso complementar de fevereiro.
- `git diff --check`.
- Verificação automatizada de links locais do `index.html` e, quando aplicável, do Markdown.
- Inspeção de `git diff --` restrita aos dois arquivos autorizados.
- Validação de HTML com `python3 -m html.parser`.
- Verificação automatizada de links locais do `introducao-sociologia/index.html`.

## Definição de pronto

- Todos os critérios de aceitação estão atendidos.
- As verificações listadas passam sem erro ou têm eventual limitação explicitamente documentada.
- `git status` mostra somente arquivos autorizados como modificados ou novos.
- O diff final é apresentado para revisão humana.
- Página estática pode ser aberta diretamente pelo navegador; servidor local não é necessário.
- Nenhum commit, push, merge ou publicação é realizado.
- A implementação aguarda aprovação humana.

## File List

- `introducao-sociologia/index.html`
- `docs/stories/reconciliar-regras-introducao-sociologia.md`

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
- Laboratório explicitado como espaço formativo que não altera a avaliação final.
- Correção limitada a `index.html` e a esta story, sem alteração de cronograma, roteiros, planos ou índices.

**Resultado da validação:** APROVADA para implementação pelo fluxo local disponível. O ativador AIOX referenciado pelos skills não está presente nesta cópia (`.aiox-core` e fallback `.codex/agents` ausentes); por isso, foi aplicada validação documental equivalente e rastreável com base no `CLAUDE.md` e nos planos canônicos.

## Retomada e conclusão — 02/09/2026

### Requisitos já encontrados na retomada

- Seção da avaliação, questão central, grupos de até cinco estudantes e personas A/B com rendas de R$ 600,00 e R$ 12.000,00.
- Controle deliberado da renda, uso de conversas novas, mesma ferramenta/modelo quando disponível e registro integral.
- Orientação ética, exigência de pelo menos três conceitos sociológicos e rubrica com oito critérios somando 10,0 pontos.
- Calendário com 15 encontros/30 roteiros, 60 horas, recesso, entrega em 03/02/2027, devolutiva, recuperação e encerramento.
- Descrições atualizadas das Aulas 14, 28, 29 e 30 na página principal.

### Alterações efetivamente realizadas nesta retomada

- Fixada a definição: “A atividade vale 10,0 pontos e será avaliada conforme a rubrica apresentada nesta página”, removendo da página pública decisões pendentes, conversão/divisão futura, definição posterior no SIGAA e formato a confirmar.
- Substituída a apresentação do calendário pelo texto aprovado sobre a sequência progressiva dos 30 roteiros.
- Detalhado o protocolo `5 perguntas × 2 aplicações × 2 personas = 20 respostas`, com nova conversa, perfil completo e pergunta exata em cada aplicação; incluídas definições dos termos operacionais e a preparação prévia das perguntas.
- Incluído registro de ferramenta, modelo/versão, data/horário, memória/personalização, modalidade da conta e intercorrências, com “Não informado pela ferramenta” para dados indisponíveis.
- Incorporadas fichas editáveis e imprimíveis das personas e matriz editável de dez comparações pareadas, com semântica de tabela, região nomeada, foco por teclado, rolagem horizontal contida e reorganização em fichas na impressão.
- Definidos relatório de 6 a 8 páginas, apêndices/complementos, apresentação oral de até 15 minutos e ausência de vídeo obrigatório.
- Explicitado que resultados sem diferenças e conclusões que neguem ou relativizem a hipótese são válidos quando fundamentados; diferenciadas adaptação ao orçamento, discriminação, estereótipos e naturalização.
- Ajustados os descritores da rubrica para não penalizar resultados nulos ou contrários à hipótese.

### Critérios de aceitação desta retomada

- [x] Nota definida em 10,0 pontos, sem afirmar nota integral da disciplina ou inventar regras de SIGAA.
- [x] Calendário e percurso preservados, inclusive Aulas 14, 28, 29 e 30.
- [x] Metodologia produz vinte respostas mínimas e dez comparações pareadas, sem alegação de independência ou comprovação estatística.
- [x] Registro técnico, fichas e matriz completos e presentes integralmente na página.
- [x] Relatório, apêndices, apresentação e entrega em 03/02/2027 definidos sem plataforma, formato acadêmico ou prazo inventado.
- [x] Conclusão aberta a confirmar, negar ou relativizar a hipótese.
- [x] Oito critérios da rubrica preservados e soma confirmada em 10,0.
- [x] Orientações éticas e exigência de ao menos três conceitos preservadas.
- [x] Somente os dois arquivos autorizados estão modificados.

### Revisão independente do squad e Aprovador

Os agentes foram executados de forma independente e somente leitura sobre o conteúdo efetivamente implementado:

- Conteudista: **Completo com ressalvas**, sem bloqueantes.
- Revisor Teórico: **Sólido**, sem erros conceituais ou conflitos.
- Revisor de Fluidez: **Fluido**, sem bloqueantes; sugestões editoriais pertinentes foram aplicadas.
- Revisor Pedagógico, rodada inicial: **Ajustar**, devido a termos sem definição, etapa de formulação das perguntas implícita e instrumentos sem edição digital/espaço suficiente de impressão.
- Revisor Pedagógico, pós-reparo: **Adequado**, sem bloqueantes.
- Revisor de Progressão: descrições das Aulas 14, 28, 29 e 30 coerentes e percurso de 15 encontros/30 roteiros preservado.
- Aprovador: **PRONTO** para a página principal e sua avaliação; esse veredito autoriza somente QA, não operações Git ou publicação.

**Limitação do squad:** `squad-revisao-aulas/mapa-progressao.md` registra um HEAD anterior à reconstrução das Aulas 24–30. Como o mapa está fora do escopo de escrita autorizado, ele não foi alterado. Isso impede declarar `PRONTO` global para o workflow das aulas, mas não bloqueou o veredito específico da página principal, cuja progressão foi conferida independentemente.

### Evidências e limitações das verificações

- `python3 -m html.parser`: estrutura HTML aceita pelo parser.
- Auditoria com a biblioteca padrão: IDs únicos, fragmentos internos válidos, links locais existentes, `caption`, `thead`, `tbody`, dez cabeçalhos com `scope="col"` e dez linhas de comparação.
- Contagens: 15 encontros, 30 links de roteiros, vinte respostas mínimas declaradas e dez comparações pareadas representadas.
- Rubrica: `1,5 + 1,0 + 2,0 + 2,0 + 1,5 + 0,75 + 0,75 + 0,5 = 10,0`.
- SHA-256 das Aulas 01–30: todos inalterados durante a retomada.
- `git diff --check`: sem erros.
- Responsividade em 320, 375, 768 e 1440 px e impressão: auditoria estrutural das regras CSS; a largura fluida, o overflow contido e a reorganização impressa estão implementados.
- Não havia navegador instalado. Não houve inspeção gráfica, teste visual real nessas larguras nem teste assistivo com leitor de tela.

### Arquivos modificados

- `introducao-sociologia/index.html`
- `docs/stories/reconciliar-regras-introducao-sociologia.md`

Nenhum commit, push, merge, pull request, deploy ou publicação foi realizado.
