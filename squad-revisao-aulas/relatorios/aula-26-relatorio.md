# Relatório da Aula 26 — retry 1, rodada 0

- HEAD-base: `9e42f5a786e717252bd06a08f074cc2355f98570`
- SHA-256 revisado: `a18502ee6b2d1ea1c9c3e2c0423d07dfe5695a5ebe2f007f7a0cfd6b40ad4d49`
- Aula 25 bloqueada em: `c8f60b26719edd0699e3da41301d90b3e46688e2ef699ee6a8d7460c8c135d79`
- Arquitetura: normas e corpos → gênero/sexualidade → trabalho/cuidado → patriarcado → interseccionalidade → feminismos → decisão institucional → ação coletiva.

## Conteudista

**Completo.** Entrega gênero, sexualidade, heteronormatividade, divisão do trabalho, cuidado, patriarcado, interseccionalidade e feminismos. A oficina contém seis peças fictícias, oito perguntas, produto, tempos, cuidado e gabarito. A transição prepara movimentos sociais sem antecipar a teoria da Aula 27. Referências têm edição ou periódico identificados e nenhuma paginação presumida.

## Revisor Teórico

**Sólido.** Evita a dicotomia “sexo biológico versus gênero cultural”, distingue materialidade, classificação e norma, e não reduz identidade, expressão e sexualidade. Patriarcado tem mecanismos e limites; interseccionalidade não vira soma de identidades. Feminismos aparecem como debates históricos, com poder e agência. Sem conflito que exija decisão humana.

## Revisor de Fluidez

**Fluido.** A arquitetura difere do dossiê da Aula 25 e progride de classificações a uma decisão organizacional. Exemplos estão integrados ao argumento; quatro pausas cumprem funções específicas. Não há título vazio, molde mecânico bloqueante ou fragmentação excessiva.

## Revisor Pedagógico

**Adequado.** Conceitos precedem aplicação; texto e plano sustentam estudantes do primeiro período. A oficina é autossuficiente, não exige relatos pessoais e separa descrição, hipótese, mecanismo e avaliação. Plano soma 120 minutos; gabarito admite alternativas justificadas. Responsividade, foco, overflow e impressão presentes.

## Revisor de Progressão

**Coerente.** Retoma racialização da Aula 25 na interseccionalidade sem apagar sua especificidade. Relaciona normas, trabalho, cuidado, sexualidade, poder e agência conforme o mapa. A síntese distingue demanda de movimento e reserva redes, recursos e repertórios à Aula 27. Mapa não requer correção.

## Aprovador

**VEREDITO: PRONTO.** Nenhum parecer aponta bloqueante. Rodada 0; nenhum reparo solicitado. O veredito autoriza somente o QA determinístico do par.

## QA do gate 25–26

- `auditar_aulas.py`: duas aulas aprovadas; cada uma com quatro pausas, 120 minutos, 17 IDs únicos e 16 fragmentos válidos.
- Texto-base: Aula 25 com 2.447 palavras; Aula 26 com 2.326 palavras; ambas com nove subseções.
- Gabaritos: Aula 25 com 159 palavras e Aula 26 com 156, ambos fechados e com dois blocos substantivos.
- `validar_escopo.py`: `ESCOPO_OK`; Aula 25 bloqueada no SHA-256 aprovado; 28 aulas protegidas preservadas.
- Hash final da Aula 25: `c8f60b26719edd0699e3da41301d90b3e46688e2ef699ee6a8d7460c8c135d79`.
- Navegação recíproca Aula 24 → 25 → 26 → 27: OK.
- Responsividade, foco, proteção de overflow e impressão: presentes nas duas páginas.
- Subtítulos vazios: nenhum. `git diff --check`: OK.
- Aulas modificadas: somente 25 e 26. Reparos: nenhum.
