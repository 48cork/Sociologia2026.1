# Relatório da Aula 28 — rodada 0

- HEAD-base: `a121434f654bccc8a2e09dc95fd4565a15aaf0b9`
- Função: socializar um argumento sociológico por meio de problema, tese, evidência, inferência, limite e escuta.
- Arquitetura: investigação → pergunta delimitada → tese → evidência → inferência → alcance → oralidade → escuta → passagem à revisão.

## Conteudista
**Completo.** O texto distingue os seis componentes do argumento, mobiliza exemplos fictícios claramente rotulados e oferece seis fichas, oito perguntas, produto e materiais integrais. Não confirma avaliação legada.

## Revisor Teórico
**Sólido.** Separa tema de problema, opinião de tese, exemplo de evidência, sequência de causalidade e conclusão empírica de juízo normativo. Generalizações são calibradas ao alcance das fontes.

## Revisor de Fluidez
**Fluido.** As nove subseções avançam sem repetição estrutural: construção do argumento, comunicação e escuta. As quatro pausas têm funções distintas e a síntese conduz à Aula 29.

## Revisor Pedagógico
**Adequado.** O plano soma 120 minutos; a oficina é autossuficiente, admite participação oral ou escrita e contém protocolo, cuidados, perguntas e gabarito substantivo em um único `details` fechado.

## Revisor de Progressão
**Coerente.** Retoma a análise de movimentos da Aula 27 como possível conteúdo, desloca o foco para a socialização pública e reserva comparação, objeções e reparos sistemáticos à Aula 29.

## Aprovador
**VEREDITO: PRONTO.** Não há bloqueantes nos cinco pareceres. Rodada 0, sem reparos; autorizado o QA determinístico do par.

## Reparos
Nenhum reparo pós-parecer. A reconstrução eliminou antes da revisão as afirmações legadas de nota, ordem de apresentação e obrigação não confirmada.

## QA conjunto
- `auditar_aulas.py`: Aulas 27 e 28 aprovadas; quatro pausas e plano de 120 minutos em cada uma; gabaritos fechados com 146 e 201 palavras.
- Texto-base: Aula 27 com aproximadamente 2.571 palavras; Aula 28 com aproximadamente 2.312; nove subseções em cada página.
- Estrutura: IDs únicos, fragmentos válidos, nenhum subtítulo vazio, responsividade, controle de overflow e impressão presentes.
- Navegação: Aula 26 → 27 → 28 → 29 íntegra.
- `validar_escopo.py`: `ESCOPO_OK`; 28 aulas protegidas e Aula 27 bloqueada no SHA-256 aprovado.
- `git diff --check`: OK; somente Aulas 27 e 28 modificadas no diretório de aulas.
