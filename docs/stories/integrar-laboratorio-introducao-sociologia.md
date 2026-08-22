# Story — Integrar o Laboratório de Introdução à Sociologia ao portal e às turmas

## Identificação

- **ID:** integrar-laboratorio-introducao-sociologia
- **Tipo:** integração editorial e de navegação
- **Status:** Verificada; implementação aprovada na revisão humana final
- **Branch prevista:** `feat/laboratorio-introducao-sociologia`
- **Dependência:** `docs/stories/laboratorio-evidencias-algoritmicas.md`

## História

Como estudante de Introdução à Sociologia, quero encontrar o Laboratório a partir do portal principal e do índice da minha turma, com a correspondência pedagógica corretamente explicada, para acessar a atividade formativa sem confundi-la com disciplina, avaliação, obrigação ou parte oficial do cronograma.

## Contexto

O Laboratório já possui duas páginas aprovadas e implementadas:

- índice: `introducao-sociologia/laboratorio/index.html`;
- primeiro protótipo: `introducao-sociologia/laboratorio/laboratorio-evidencias-algoritmicas.html`.

O primeiro protótipo chama-se **Laboratório de Evidências Algorítmicas**. O Laboratório é uma camada prática complementar de Introdução à Sociologia, compartilhada pelas Turmas 1 e 2, inicialmente formativa, autônoma, sem peso próprio, sem prazo obrigatório e sem alocação automática de carga horária.

As páginas do Laboratório já oferecem retorno ao portal principal e aos índices das duas turmas. A integração futura deverá completar os caminhos de ida nos três pontos de entrada candidatos, sem alterar as páginas do Laboratório nesta story.

## Objetivo pedagógico

Contextualizar o acesso ao Laboratório dentro do percurso de cada turma, preservando a distinção entre correspondência pedagógica e integração curricular oficial. A navegação deve apoiar a prática de observação, problematização, interpretação, verificação e reflexão sem modificar conteúdos, cronogramas ou avaliações.

## Problema de navegação

Embora as páginas do Laboratório tenham links de retorno, o Laboratório ainda não é encontrável de modo direto e contextualizado a partir do portal principal e dos índices das Turmas 1 e 2. Essa assimetria dificulta a descoberta e pode levar estudantes a receber o link sem o contexto formativo e curricular necessário.

A integração resolverá o problema com chamadas mínimas e bidirecionais:

1. portal principal → índice do Laboratório;
2. índice da Turma 1 → índice do Laboratório;
3. índice da Turma 2 → índice do Laboratório;
4. índice e atividade do Laboratório → portal e índices das turmas, por meio dos retornos já existentes e verificados.

## Perfil dos estudantes

Estudantes matriculados nas Turmas 1 e 2 de Introdução à Sociologia, com diferentes repertórios, condições de acesso, preferências e necessidades de aprendizagem. A integração não deve presumir nem inferir renda, trabalho, idade, configuração familiar, domínio tecnológico, disponibilidade de equipamento ou qualquer outra característica socioeconômica.

## Escopo

### Incluído na futura implementação

- Uma chamada mínima e contextualizada no portal principal.
- Uma chamada específica no índice da Turma 1.
- Uma chamada específica no índice da Turma 2.
- Links dos três pontos de entrada para `introducao-sociologia/laboratorio/index.html`.
- Verificação dos retornos já existentes no índice e na atividade do Laboratório.
- Reutilização dos componentes, tokens, tipografia, espaçamentos e padrões responsivos de cada página editada.
- Registro dos testes e do lifecycle nesta story, se houver autorização explícita para atualizá-la durante a implementação.

### Exclusões

- Alteração do índice ou da atividade do Laboratório.
- Alteração de `Cronograma_Sociologia_2026-1.md`.
- Alteração dos 48 roteiros ou dos dois planos canônicos.
- Mudança de datas, conteúdos, carga horária, presença, entregas ou avaliações.
- Integração oficial do Laboratório a qualquer encontro ou cronograma.
- Criação de prazo, carga horária, frequência ou peso avaliativo para o Laboratório.
- Substituição de conteúdos, seminários, síntese, encerramento, entregas ou avaliações.
- Alteração das regras oficiais de avaliação 25/25/25/25.
- Mudança em outros cursos, arquivos de framework ou configuração.
- JavaScript, dependências externas, analytics, backend ou armazenamento de dados.
- Criação de novos protótipos nesta etapa.

## Arquivos candidatos da futura implementação

1. `index.html`
2. `introducao-sociologia/turma1/index.html`
3. `introducao-sociologia/turma2/index.html`

As páginas do Laboratório são destinos e fontes de links de retorno, mas não são candidatas a modificação. Qualquer atualização desta story para registrar implementação e testes dependerá de autorização expressa na etapa correspondente.

## Requisitos funcionais

1. O portal principal deve oferecer link direto e identificável para o índice do Laboratório.
2. O índice da Turma 1 deve oferecer link direto para o índice do Laboratório junto a uma explicação da correspondência pedagógica dessa turma.
3. O índice da Turma 2 deve oferecer link direto para o índice do Laboratório junto a uma explicação da correspondência pedagógica dessa turma.
4. Os três novos links devem apontar para o mesmo índice compartilhado, sem duplicar ou bifurcar o protótipo por turma.
5. A navegação deve permitir o percurso de ida e retorno entre portal, turmas, índice do Laboratório e primeiro protótipo.
6. A integração deve preservar todos os links, fragmentos e controles existentes nas três páginas candidatas.
7. A implementação deve permanecer em HTML e CSS interno, sem JavaScript ou dependências.

## Requisitos editoriais

### Portal principal

- Apresentar o **Laboratório de Introdução à Sociologia** como camada prática complementar da disciplina.
- Identificar **Laboratório de Evidências Algorítmicas** como o primeiro protótipo.
- Informar que novos laboratórios poderão ser desenvolvidos futuramente, sem prometer quantidade ou prazo.
- Declarar seu caráter formativo, autônomo, sem peso próprio e sem prazo obrigatório.
- Não apresentá-lo como disciplina, avaliação, entrega ou atividade obrigatória.

### Turma 1

- Usar a formulação **“relação pedagógica direta com o Encontro 27”**.
- Explicitar que essa relação não constitui integração oficial ao encontro ou ao cronograma.
- Não afirmar que o Laboratório substitui ou altera o conteúdo do Encontro 27.

### Turma 2

- Usar a formulação **“relação conceitual com os Encontros 17–18”**.
- Identificá-lo como **“atividade formativa autônoma”**.
- Explicitar que não substitui conteúdos, seminários, síntese, encerramento, entregas ou avaliações.
- Não afirmar integração oficial aos Encontros 17–18 ou ao cronograma.

### Regras comuns

- Não prometer prazo, carga horária, frequência ou peso avaliativo.
- Manter pesquisa bibliográfica, apresentação oral, relatório e vídeo com 25% cada.
- Informar que qualquer incorporação formal futura dependerá da observação pedagógica do protótipo e de decisão docente em oferta futura.
- Evitar inferências sobre estudantes e evitar linguagem que transforme correspondência pedagógica em causalidade, obrigação ou agendamento.
- Preservar o conteúdo já coerente e a voz editorial de cada página.

## Requisitos de acessibilidade

- Usar link com texto acessível e suficientemente descritivo; evitar “clique aqui” isolado.
- Integrar a chamada à hierarquia de títulos e aos landmarks existentes sem criar níveis incoerentes.
- Garantir navegação por teclado, ordem de foco lógica e foco visível.
- Manter contraste mínimo WCAG AA para texto, bordas essenciais, estados de foco e controles.
- Não depender apenas de cor, posição ou ícone para comunicar que o Laboratório é formativo ou que há um link.
- Preservar o link “Pular para o conteúdo” onde já existir e não introduzir armadilhas de teclado.
- Garantir alvo interativo mínimo de 44 × 44 px para os novos links ou botões.
- Manter nomes acessíveis coerentes entre chamadas visualmente equivalentes.

## Requisitos de responsividade

- Adotar abordagem compatível com os estilos responsivos já existentes em cada página.
- Manter a chamada utilizável em 320, 375, 768 e 1440 px.
- Não introduzir overflow horizontal global ou local.
- Preservar conteúdo e funcionalidade em zoom de 200%.
- Permitir quebra de texto sem truncar nome, correspondência pedagógica ou estado formativo.
- Manter versão impressa legível, sem URLs ou controles sobrepostos.
- Respeitar `prefers-reduced-motion` quando a página possuir transições ou animações; a integração não deve criar movimento novo.

## Política de uso crítico e transparente da IA

- A chamada deve apresentar a IA como objeto de investigação e ferramenta opcional, nunca como fonte automática de verdade.
- A integração não deve sugerir que o uso de IA é necessário para acessar, realizar ou concluir o percurso formativo.
- Deve permanecer disponível a alternativa equivalente sem IA descrita no protótipo.
- Nenhuma chamada deve solicitar dados pessoais, credenciais, prompts ou envio de trabalhos.
- A transparência sobre uso ou não uso de IA, a verificação independente e a autoria discente permanecem regidas pelo protótipo aprovado.
- A integração não autoriza uso de trabalhos discentes em pesquisa, apresentação ou publicação e não altera as políticas éticas já aprovadas.

## Riscos e medidas de mitigação

| Risco | Medida de mitigação |
|---|---|
| A chamada parecer uma quinta avaliação | Exibir “formativo”, “autônomo” e “sem peso próprio”; conferir que os quatro componentes oficiais continuam em 25% cada. |
| Correspondência ser interpretada como integração oficial | Usar literalmente as formulações aprovadas e incluir ressalva explícita sobre o cronograma. |
| Sobrecarregar o fechamento da Turma 2 | Declarar autonomia e listar os componentes que o Laboratório não substitui. |
| Criar dois laboratórios divergentes por turma | Fazer os três pontos de entrada apontarem para o mesmo índice compartilhado. |
| Quebrar navegação relativa | Testar cada link a partir de sua página de origem e todos os retornos existentes. |
| Degradar identidade visual ou responsividade | Reutilizar componentes locais e testar quatro viewports, zoom, impressão e overflow. |
| Alterar arquivos canônicos ou outros cursos | Registrar hashes antes da implementação e limitar patches aos arquivos candidatos autorizados. |
| Sugerir IA como verdade ou requisito | Usar linguagem crítica e opcional alinhada ao protótipo aprovado. |
| Prometer expansão ou calendário inexistente | Informar apenas que novos laboratórios poderão ser desenvolvidos futuramente. |

## Critérios de aceitação

1. O portal principal contém chamada visível para o índice do Laboratório e o apresenta como camada prática complementar de Introdução à Sociologia.
2. A chamada do portal identifica Laboratório de Evidências Algorítmicas como primeiro protótipo e informa que outros poderão ser desenvolvidos futuramente.
3. O portal não apresenta o Laboratório como disciplina, avaliação, entrega ou obrigação.
4. O índice da Turma 1 contém chamada com a frase “relação pedagógica direta com o Encontro 27” e ressalva que não há integração oficial ao encontro ou cronograma.
5. O índice da Turma 2 contém as frases “relação conceitual com os Encontros 17–18” e “atividade formativa autônoma”.
6. A chamada da Turma 2 informa que o Laboratório não substitui conteúdos, seminários, síntese, encerramento, entregas ou avaliações.
7. As três chamadas apontam para `introducao-sociologia/laboratorio/index.html` por caminhos relativos válidos.
8. Os retornos do índice e da atividade do Laboratório para portal e turmas continuam válidos, sem necessidade de editar essas páginas.
9. As chamadas informam, no contexto apropriado, que o Laboratório é formativo, autônomo, sem peso próprio e sem prazo obrigatório.
10. Nenhum texto promete carga horária ou incorporação ao cronograma; eventual incorporação formal fica condicionada à observação pedagógica e decisão docente futura.
11. A integração identifica IA como objeto de investigação e ferramenta opcional, nunca fonte automática de verdade.
12. Os novos links possuem texto descritivo, alvo mínimo de 44 × 44 px, foco visível e contraste WCAG AA.
13. As páginas permanecem utilizáveis em 320, 375, 768 e 1440 px e com zoom de 200%, sem overflow horizontal.
14. A impressão permanece legível e `prefers-reduced-motion` é preservado quando aplicável.
15. Pesquisa bibliográfica, apresentação oral, relatório e vídeo continuam com 25% cada; nenhum quinto peso é criado.
16. Os 48 roteiros, dois planos canônicos, páginas do Laboratório, cronograma, outros cursos e arquivos de framework permanecem inalterados.
17. A identidade visual e a estrutura principal de cada página candidata são preservadas.
18. O diff da implementação fica restrito aos três HTMLs candidatos e, somente se autorizada, a esta story para registro do lifecycle e dos testes.

## Testes obrigatórios da futura implementação

### Estrutura e navegação

- Validar os três HTMLs modificados e as duas páginas do Laboratório.
- Verificar todos os links e fragmentos locais afetados.
- Testar os percursos portal → Laboratório → portal; Turma 1 → Laboratório → Turma 1; Turma 2 → Laboratório → Turma 2; índice do Laboratório → protótipo → índice do Laboratório.
- Confirmar que nenhum link existente foi removido ou quebrado.

### Acessibilidade e apresentação

- Navegar por teclado e confirmar ordem de foco e foco visível.
- Verificar contraste WCAG AA dos novos textos, links, fundos e estados de foco.
- Medir alvos interativos em pelo menos 44 × 44 px.
- Testar viewports de 320, 375, 768 e 1440 px.
- Testar zoom de 200% sem perda de conteúdo ou funcionalidade.
- Confirmar ausência de overflow horizontal global e local.
- Testar impressão das três páginas candidatas.
- Verificar `prefers-reduced-motion`, quando aplicável.

### Conteúdo e regressão

- Verificar literalmente os nomes e as correspondências pedagógicas aprovadas para cada turma.
- Buscar linguagem que sugira obrigação, avaliação, prazo, carga horária ou integração oficial e revisar qualquer falso positivo em contexto.
- Confirmar no portal e nos índices que a avaliação oficial permanece 25/25/25/25.
- Confirmar que nenhum texto apresenta IA como fonte automática de verdade ou ferramenta obrigatória.
- Executar `git diff --check`.
- Comparar hashes dos 48 roteiros, dois planos, duas páginas do Laboratório, cronograma e demais arquivos protegidos.
- Inspecionar `git diff --name-only` e `git status` para confirmar o escopo autorizado.
- Realizar revisão visual humana antes de qualquer commit ou publicação.

## Definição de pronto

- Todos os 18 critérios de aceitação estão atendidos e rastreáveis aos testes.
- Os caminhos de ida e retorno funcionam a partir de suas páginas reais.
- As três chamadas são editorialmente distintas conforme o contexto do portal, da Turma 1 e da Turma 2.
- A identidade visual de cada página é preservada.
- Acessibilidade, responsividade, zoom, overflow, impressão e movimento reduzido passam pelos gates disponíveis.
- A avaliação oficial permanece inequivocamente 25/25/25/25.
- Os hashes dos arquivos protegidos permanecem idênticos.
- O diff contém apenas arquivos expressamente autorizados para a implementação e eventual registro da story.
- Limitações de ferramentas são documentadas e compensadas por revisão humana quando necessário.
- Nenhum commit, push, merge, PR ou publicação ocorre sem autorização específica.

## Checklist

### Planejamento

- [x] Contexto e dependências identificados.
- [x] Problema de navegação descrito.
- [x] Objetivo pedagógico e perfil discente definidos.
- [x] Escopo, exclusões e arquivos candidatos delimitados.
- [x] Requisitos funcionais, editoriais, de acessibilidade e responsividade definidos.
- [x] Política crítica e transparente de IA preservada.
- [x] Riscos possuem medidas de mitigação correspondentes.
- [x] Critérios de aceitação são observáveis e testáveis.
- [x] Testes obrigatórios e definição de pronto estão completos.

### Implementação concluída

- [x] Registrar hashes dos arquivos protegidos antes das alterações.
- [x] Implementar somente nos arquivos autorizados.
- [x] Validar conteúdo e navegação bidirecional.
- [x] Executar gates de HTML, acessibilidade e responsividade.
- [x] Confirmar avaliação 25/25/25/25.
- [x] Comparar hashes e revisar diff/status.
- [x] Obter aprovação humana.

## File list

### Criado nesta etapa de planejamento

- `docs/stories/integrar-laboratorio-introducao-sociologia.md`

### Candidatos da futura implementação

- `index.html`
- `introducao-sociologia/turma1/index.html`
- `introducao-sociologia/turma2/index.html`

### Dependências somente para leitura e testes

- `introducao-sociologia/laboratorio/index.html`
- `introducao-sociologia/laboratorio/laboratorio-evidencias-algoritmicas.html`
- `docs/stories/laboratorio-evidencias-algoritmicas.md`
- `docs/stories/reconciliar-regras-introducao-sociologia.md`
- `CLAUDE.md`

## Validação e quality gate da story

- [x] Título, ID, status, história e dependência presentes.
- [x] Contexto aprovado reproduzido sem transformar correspondência em integração oficial.
- [x] Portal e duas turmas possuem requisitos editoriais específicos.
- [x] Os nomes “Laboratório de Evidências Algorítmicas”, “relação pedagógica direta com o Encontro 27”, “relação conceitual com os Encontros 17–18” e “atividade formativa autônoma” estão explícitos.
- [x] Ausência de prazo, carga horária e peso próprio está explícita.
- [x] Preservação do sistema 25/25/25/25 está coberta por critério e teste.
- [x] Escopo futuro está limitado aos três HTMLs candidatos.
- [x] Páginas do Laboratório estão protegidas contra alteração e incluídas nos testes de navegação.
- [x] Acessibilidade cobre semântica, teclado, foco, contraste, alvos, zoom e informação não dependente de cor.
- [x] Responsividade cobre 320, 375, 768 e 1440 px, overflow, impressão e movimento reduzido.
- [x] Riscos, testes, definição de pronto, checklist e file list estão presentes.
- [x] Nenhum requisito depende de JavaScript ou nova dependência.

**Quality gate documental e de implementação:** APROVADA após validação técnica disponível e revisão humana final.

## Registro da implementação e validação final

### Arquivos implementados

- `index.html`
- `introducao-sociologia/turma1/index.html`
- `introducao-sociologia/turma2/index.html`

### Resultado dos quality gates

- Estrutura HTML, links, fragmentos e navegação bidirecional validados.
- Contraste mínimo dos novos componentes aprovado em WCAG AA.
- Foco visível e alvos interativos mínimos de 44 × 44 px confirmados.
- Regras responsivas, zoom, ausência de overflow horizontal e impressão A4 verificados pelo fluxo disponível.
- Avaliação oficial preservada em quatro entregas de 25% cada.
- Os 52 arquivos protegidos permaneceram íntegros por SHA-256.

### Aprovação humana final

- Portal aprovado em desktop e em viewport de 375 px.
- Índice da Turma 1 aprovado em desktop.
- Índice da Turma 2 aprovado em desktop e em viewport de 375 px.
- Textos legíveis, componentes contidos e sem overflow horizontal.
- Links e botões visualmente adequados.
- Integração humana final aprovada.

## Lifecycle

Na ausência de arquivo de Constitution ou ativadores AIOX nesta cópia, aplica-se o lifecycle documental rastreável adotado pelo projeto:

1. **Rascunho** — requisitos reunidos e story criada.
2. **Validada** — completude, consistência, testabilidade e escopo conferidos.
3. **Aprovada** — aprovação humana autoriza iniciar a implementação delimitada.
4. **Em implementação** — somente os arquivos autorizados são editados e os testes são executados.
5. **Implementada** — critérios atendidos, diff e resultados registrados, sem inferir autorização para commit.
6. **Verificada** — revisão humana aprova a implementação e seus quality gates.
7. **Encerrada** — commit ou outra ação final ocorre apenas mediante autorização específica; push, merge, PR e publicação exigem autorização própria.

**Estado atual do lifecycle:** Verificada; integração implementada, quality gates concluídos e revisão humana final aprovada. O commit local desta etapa foi autorizado; push, merge, PR e publicação permanecem vedados.
