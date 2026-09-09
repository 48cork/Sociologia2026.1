# Workflow: Revisar uma Aula

Fluxo unitário compatível com a lógica do workflow de Sociologia Rural, reforçado com
revisão pós-reparo e proteção determinística. Deve ser chamado por `revisar-lote.md`.

## Pré-condições

1. Ler `config/curso.yaml`, `config/criterios.yaml` e `config/estado.yaml`.
2. Confirmar que a aula está entre 24 e 30 e foi selecionada pelo lote.
3. Confirmar árvore limpa no início do lote ou contendo apenas mudanças autorizadas e
   registradas pelo próprio workflow.
4. Confirmar Mapa de Progressão `COMPLETO`, com HEAD e entrada da aula.
5. Capturar baseline Git e SHA-256 das 30 aulas com `validar_escopo.py`. Em gate de
   par, autorizar os dois HTMLs e bloquear por `--hash-aprovado` qualquer primeira aula
   já aprovada e modificada.
6. Permitir escrita apenas no HTML selecionado. O outro HTML do par só pode permanecer
   modificado quando estiver bloqueado pelo hash aprovado; vizinhas e demais aulas são leitura.

## Reconstrução

O orquestrador lê a aula inteira, suas vizinhas, o mapa e os critérios; registra o
diagnóstico e muda o estado para `EM_RECONSTRUCAO`. A reconstrução preserva título,
função, data, encontro, navegação, identidade visual e rodapé corretos. Não copia
mecanicamente arquitetura, exemplos ou progressões anteriores.

Depois da escrita, mudar para `EM_REVISAO` e produzir, em arquivos separados dentro de
`relatorios/aula-NN/rodada-R/`, os quatro pareceres independentes:

1. Conteudista;
2. Revisor Teórico;
3. Revisor de Fluidez;
4. Revisor Pedagógico.

Todos recebem a versão identificada por SHA-256 e o mesmo mapa. Nenhum parecer pode
editar o HTML.

## Gate do Aprovador

O Aprovador recebe os quatro pareceres, o SHA-256 e os apontamentos da aula no mapa.
Emite apenas `PRONTO` ou `PRECISA REVISAR` no formato de `agentes/aprovador.md`.

### PRONTO

1. Mudar estado para `PRONTO` provisório.
2. Executar `auditar_aulas.py` sobre a aula.
3. Executar `validar_escopo.py validar` contra o baseline.
4. Executar `git diff --check`.
5. Se qualquer verificação falhar, mudar para `FALHA_TECNICA`; `PRONTO` não prevalece.
6. Se todas passarem, manter `PRONTO` e devolver controle ao workflow do lote.

Quando a aula for a primeira de um gate de par, o relatório deve registrar caminho,
SHA-256 aprovado, veredito `PRONTO`, resultado de QA e estado
`PRONTO_AGUARDANDO_PAR`. O baseline seguinte inclui esse caminho em
`arquivos_autorizados` e o mesmo digest em `hashes_aprovados`. O validador deve ser
executado antes e depois da segunda aula; qualquer diferença no digest é
`FALHA_TECNICA`.

### PRECISA_REVISAR

1. Mudar estado para `PRECISA_REVISAR`.
2. Aplicar somente ajustes obrigatórios rastreáveis, no HTML selecionado.
3. Incrementar `rodadas_reparo`.
4. Reexecutar pelo menos cada agente que originou pendência e sempre o Aprovador.
5. Erro conceitual: Revisor Teórico obrigatório.
6. Progressão: Revisor de Progressão obrigatório sobre aula, vizinhas e mapa.
7. Problema pedagógico: Revisor Pedagógico obrigatório.
8. Fluidez: Revisor de Fluidez obrigatório.
9. Cobertura/material/referência: Conteudista obrigatório.
10. Repetir o gate com nova versão e novo SHA-256.

Após duas rodadas automáticas sem `PRONTO`, mudar para `AGUARDA_HUMANO`. Falta de
insumo, decisão docente ou conflito conceitual não resolvido também gera
`AGUARDA_HUMANO` imediatamente. Nunca escolher silenciosamente uma posição.

## Restrições

- Nenhum agente aprova o próprio reparo como veredito final.
- O Aprovador não repara e o reparador não substitui o Aprovador.
- Não restaurar arquivos automaticamente em caso de falha.
- Não selecionar outra aula antes do gate final.
- Nenhuma operação remota.
