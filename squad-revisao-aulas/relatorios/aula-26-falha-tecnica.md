# Falha técnica no pré-voo da Aula 26

- HEAD: `76e3a09ff2676ae052220f8c5c3a5122887e0f28`
- Aula 25: `PRONTO`, QA aprovado, ainda sem commit conforme a política do gate 25–26.
- Aula 26: não editada.
- Comando: `validar_escopo.py validar` sobre o baseline recém-capturado da Aula 26.

## Evidência

O baseline da Aula 26 registrou quatro caminhos já modificados pelo processamento aprovado da Aula 25. Mesmo sem qualquer alteração da Aula 26, o validador retornou `FALHA_TECNICA` e classificou como fora da allowlist:

- `introducao-sociologia/turma1/aulas/aula-25.html`;
- `squad-revisao-aulas/relatorios/aula-25-baseline.json`;
- `squad-revisao-aulas/relatorios/aula-25-relatorio.md`.

O script proíbe autorizar outra aula por `--permitir`. As alternativas seriam um commit individual da Aula 25, proibido nesta execução, alteração de infraestrutura, ou manipulação do baseline; nenhuma está autorizada. Nenhum arquivo foi restaurado, descartado ou alterado fora da allowlist editorial. Processamento interrompido antes da reconstrução da Aula 26.
