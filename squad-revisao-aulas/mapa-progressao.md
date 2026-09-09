# Mapa de Progressão — Introdução à Sociologia 2026.2

**Estado do documento:** COMPLETO (cobre as Aulas 01–30).
**Situação estrutural do curso (reauditoria atual):** CONCERNS — 26 de 30 aulas conformes ao
padrão determinístico do squad; 4 pendências estruturais reais e localizadas (Aulas 01, 02, 03
e 09). Nenhuma delas está nas Aulas 24–30 nem impede o veredito já emitido para essas aulas.
**HEAD da reauditoria atual:** `82b894ac457bd6f7359226ec6d848ccc81278a66`
**HEAD do diagnóstico original (histórico, ver seção abaixo):** `ed45724eea0c9df260b323d8e8f4b0e2095a6ddd`
**Arquivos:** `aula-01.html` a `aula-30.html`

## Leitura geral do arco

As Aulas 01–23 constroem um arco aprovado: imaginação e método sociológicos; formação
histórica da disciplina; clássicos; cultura, socialização, grupos e normas; instituições;
e estratificação. A progressão funciona quando uma aula retoma uma operação anterior
para formular problema novo, sem repetir definição. As Aulas 24–27 passam da
estratificação para desigualdades, marcadores e ação coletiva. As Aulas 28–30 transformam
o conteúdo em argumentação pública, revisão e síntese.

### Diagnóstico histórico (registrado em HEAD `ed45724`, anterior à reconstrução)

O diagnóstico original das Aulas 24–30 encontrou um molde repetido de oito subseções,
parágrafos quase idênticos, atividades dependentes de materiais ausentes, paginações
frágeis e nenhum gabarito em `<details>`. A Aula 27 ainda confundia opinião agregada com
movimento social; a Aula 30 somava 110 minutos. Todas exigiam reconstrução. Este parágrafo
é preservado como registro histórico do estado que motivou o trabalho, não como descrição
do estado atual (ver "Estado atual" abaixo).

### Estado atual (reauditoria em HEAD `82b894a`)

As Aulas 24–30 foram integralmente reconstruídas nos commits `76e3a09`, `a121434`,
`0c3a5c1` e `aa05cb5`, revisadas de forma independente pelos seis papéis do squad
(Conteudista, Revisor Teórico, Revisor de Fluidez, Revisor Pedagógico, Revisor de
Progressão e Aprovador) e aprovadas com veredito **PRONTO** em rodada 0, sem reparos, para
todas as sete aulas. `squad-revisao-aulas/config/estado.yaml` registra as sete como
`COMMITADO`. O auditor determinístico (`auditar_aulas.py`) confirma hoje **OK** para as
sete, com gabarito presente, quatro pausas, 120 minutos de plano e nenhuma falha estrutural.
Os detalhes e as evidências específicas estão na seção "Evidências da resolução" abaixo.

## Mapa por aula

| Aula | Função | Conceitos/operações | Exemplos/atividade | Retomada | Transição | Riscos/orientações |
|---|---|---|---|---|---|---|
| 01 | Abrir a imaginação sociológica | ciência, senso comum, problema, evidência | cenas cotidianas | início | contexto histórico | Aprovada; não copiar exemplos. |
| 02 | Situar matrizes históricas | revoluções, industrialização, Estado, mudança | documentos históricos | 01 | modernidade | Sem origem única. |
| 03 | Problematizar modernidade | Iluminismo, crise, ordem, progresso | fontes concorrentes | 02 | teorias iniciais | Evitar narrativa linear. |
| 04 | Examinar teorias iniciais | positivismo, evolução, hierarquia | comparação | 03 | institucionalização | Não naturalizar evolução. |
| 05 | Definir disciplina acadêmica | objeto, método, descrição/explicação | desenho de pesquisa | 01–04 | Durkheim | Método reaparece adiante. |
| 06 | Introduzir Durkheim | fato social, coerção, consciência | regras e práticas | 05 | solidariedade | Exterioridade não é só imposição visível. |
| 07 | Relacionar diferenciação e integração | solidariedades, divisão do trabalho | relações comparadas | 06 | anomia | Tipos não são etapas rígidas. |
| 08 | Aplicar explicação social | anomia, integração, regulação | estudo metodológico | 06–07 | Marx | Cuidado com tema sensível. |
| 09 | Introduzir Marx | relações, história, conflito | documentos de trabalho | 02–03 | classe/alienação | Sem determinismo base-superestrutura. |
| 10 | Examinar capitalismo e classe | produção, classe, alienação, exploração | relações de trabalho | 09 | Weber | Classe é relação, não rótulo. |
| 11 | Introduzir Weber | ação, sentido, tipo ideal | interpretação | 05 | racionalização | Tipo ideal não é retrato. |
| 12 | Relacionar racionalização e autoridade | burocracia, dominação, ética | organizações | 11 | comparação | Legitimidade não é justiça. |
| 13 | Comparar clássicos | problema, método, escala, explicação | matriz | 06–12 | pesquisa | Não harmonizar teorias. |
| 14 | Orientar pesquisa | pergunta, fonte, argumento, referência | projeto | 05/13 | cultura | Regime avaliativo pode mudar. |
| 15 | Definir cultura | significado, prática, natureza/cultura | cenas fictícias | 01 | etnocentrismo | Cultura não é essência. |
| 16 | Comparar perspectivas culturais | etnocentrismo, relativização, direitos | dilemas | 15 | identidade | Relativizar não é aprovar. |
| 17 | Examinar identidade e circulação | fronteira, identidade, cultura de massa | documentos | 15–16 | socialização | Identidades relacionais. |
| 18 | Explicar socialização | primária/secundária, agentes, trajetórias | casos | 15–17 | grupos | Não programa conduta. |
| 19 | Analisar grupos | pertencimento, referência, poder, agência | sete materiais | 18 | normas | Não repetir oficina. |
| 20 | Explicar regulação/classificação | normas, sanções, desvio, etiquetamento | seis casos | 19 | instituições | Seletividade requer evidência. |
| 21 | Introduzir instituições via família | relações, cuidado, redes, desigualdade | seis materiais | 18–20 | outras instituições | Família não é forma única. |
| 22 | Comparar instituições | funções, reprodução, legitimidade, contestação | seis documentos | 21 | estratificação | Instituição ≠ organização. |
| 23 | Definir estratificação | castas, estamentos, classes, recursos, mobilidade | seis materiais | 21–22 | desigualdade | Contexto da 24; renda não esgota classe. |
| 24 | Ler desigualdade brasileira | indicador, renda/riqueza, Gini, raça, território | seis boletins fictícios | 23 | racialização | Sem números sem fonte; reservar teoria racial. |
| 25 | Explicar racialização e racismo | raça, etnia, preconceito, discriminação, níveis, ação afirmativa | seis documentos | 24 | gênero | Raça sem essência; estrutural ≠ institucional. |
| 26 | Analisar gênero e sexualidade | gênero, normas, cuidado, patriarcado, interseccionalidade, feminismos | seis peças | 24–25 | ação coletiva | Evitar binarismo e soma de identidades. |
| 27 | Passar à ação coletiva | movimento, demanda, redes, recursos, repertório, contexto, digital | seis dossiês | 24–26 | apresentação | Opinião comum não prova movimento. |
| 28 | Socializar argumento | problema, tese, evidência, inferência, escuta | seis fichas | 27 | revisão | Não confirmar avaliação legada. |
| 29 | Transformar devolutiva em revisão | objeção, contraexemplo, alcance, resposta | seis devolutivas | 28 | síntese | Crítica ao argumento, não à pessoa. |
| 30 | Sintetizar o percurso | escala, indivíduo/instituição/estrutura, evidência, poder, agência, mudança | seis documentos | todo o arco | continuidade | Sem “próxima aula”; 120 minutos. |

## Repetições, antecipações e lacunas — diagnóstico histórico (resolvido nas Aulas 24–30)

As afirmações abaixo descrevem o estado registrado em HEAD `ed45724`, antes da
reconstrução. São preservadas porque orientaram o trabalho de reconstrução e permitem
auditar se cada ponto foi de fato tratado. Nenhuma delas descreve o estado atual do
arquivo. Ver "Estado atual" e "Evidências da resolução" para a situação em HEAD `82b894a`.

- Aulas 24–30 repetiam o mesmo molde textual; reconstruídas com arquiteturas específicas.
  **Resolvido:** os pareceres de Revisor de Fluidez de cada aula (25 a 30) registram
  explicitamente arquitetura própria e ausência de molde mecânico (ver evidências).
- Atividades prometiam dados, imagens, documentário, formulários ou trabalhos ausentes.
  **Resolvido:** os pareceres de Conteudista confirmam atividade, materiais e gabarito
  integrais em cada uma das sete aulas, sem material prometido e ausente.
- Aula 24 usava raça como dimensão dos dados e reservava racialização/racismo à Aula 25.
  **Mantido como decisão de sequência, não como problema.** O Revisor de Progressão
  confirmou essa reserva como coerente com o mapa em cada gate.
- Aula 25 anunciava relações entre marcadores, reservando gênero e sexualidade à Aula 26.
  **Mantido como decisão de sequência**, confirmado coerente pelo Revisor de Progressão.
- Aula 26 preparava ação coletiva sem antecipar a teoria da Aula 27.
  **Mantido como decisão de sequência**, confirmado coerente.
- Aula 27 não usa respostas do Experimento como prova de movimento social.
  **Resolvido e preservado:** o Revisor de Progressão confirmou essa distinção mantida na
  versão reconstruída.
- Aula 28 trabalha exposição/escuta; Aula 29, revisão rastreável; Aula 30, síntese.
  **Preservado como estrutura válida**, confirmado pelo Revisor de Progressão em cada gate.

## Orientações obrigatórias para as Aulas 24–30 (diagnóstico histórico que orientou a reconstrução — cumprido)

As orientações abaixo foram escritas antes da reconstrução, para guiar o trabalho. Estão
preservadas como registro do que foi exigido; cada uma foi verificada como cumprida pelos
pareceres do squad citados na seção de evidências.

### Aula 24
Ensinar construção e limites de indicadores, distinguir renda, riqueza e condições de
vida e articular raça/território sem causa única. Seis boletins, oito perguntas e seis
comentários. Transição: como categorias raciais são produzidas.
**Cumprido** — ver parecer de Conteudista e Revisor Teórico, `aula-24-relatorio.md`.

### Aula 25
Distinguir raça, etnia, racialização, preconceito, discriminação e racismo; relacionar
interações, organizações e estrutura. Ação afirmativa por problema, desenho e evidência.
**Cumprido** — ver `aula-25-relatorio.md`.

### Aula 26
Evitar dicotomia sexo biológico/gênero cultural. Relacionar normas, trabalho, cuidado,
sexualidade, poder e agência; explicar usos/limites de patriarcado e interseccionalidade.
**Cumprido** — ver `aula-26-relatorio.md`.

### Aula 27
Definir movimento por dimensões investigáveis. Relacionar redes, recursos, repertórios,
autoridades, contexto e mediação digital. O Experimento serve apenas de contraste
metodológico: interpretação agregada não demonstra mobilização.
**Cumprido** — ver `aula-27-relatorio.md`.

### Aula 28
Primeira sessão de seminários autossuficiente: problema, tese, evidência, limite e escuta.
Reservar comparação e reparo para a Aula 29.
**Cumprido** — ver `aula-28-relatorio.md`.

### Aula 29
Trabalhar devolutiva, evidência contrária, contraexemplo, alcance e decisão de revisar ou
manter justificadamente. Produzir memorando rastreável.
**Cumprido** — ver `aula-29-relatorio.md`.

### Aula 30
Fechar problema–conceito–evidência–mecanismo–limite. Conectar blocos sem teoria única,
separar avaliação anônima da exposição estudantil e terminar sem anunciar próxima aula.
**Cumprido** — ver `aula-30-relatorio.md`.

## Evidências da resolução (Aulas 24–30)

| Aula | Commit de reconstrução | Aprovador | Rodada de reparo | `estado.yaml` | Auditor atual |
|---|---|---|---|---|---|
| 24 | `76e3a09` | PRONTO | 0 | COMMITADO | OK — gabarito 146 palavras/3 blocos |
| 25 | `a121434` | PRONTO | 0 | COMMITADO | OK — gabarito 159 palavras/2 blocos |
| 26 | `a121434` | PRONTO | 0 | COMMITADO | OK — gabarito 156 palavras/2 blocos |
| 27 | `0c3a5c1` | PRONTO | 0 | COMMITADO | OK — gabarito 146 palavras/2 blocos |
| 28 | `0c3a5c1` | PRONTO | 0 | COMMITADO | OK — gabarito 201 palavras/2 blocos |
| 29 | `aa05cb5` | PRONTO | 0 | COMMITADO | OK — gabarito 168 palavras/2 blocos |
| 30 | `aa05cb5` | PRONTO | 0 | COMMITADO | OK — gabarito 158 palavras/2 blocos |

Fonte: `squad-revisao-aulas/relatorios/aula-24-relatorio.md` a `aula-30-relatorio.md`,
`squad-revisao-aulas/config/estado.yaml` e execução de
`python3 squad-revisao-aulas/scripts/auditar_aulas.py --intervalo 24-30` em HEAD `82b894a`.

Não foi refeita, nesta reconciliação, uma nova comparação textual palavra a palavra entre
as sete aulas. A conclusão de ausência de molde repetido apoia-se nos pareceres de Revisor
de Fluidez já registrados em cada relatório individual (ver citações na seção anterior),
não em uma nova análise de similaridade textual executada nesta tarefa. Isso é uma
limitação da reauditoria, não uma lacuna no trabalho de reconstrução.

## Regularização da Aula 06

A Aula 06 não pertencia ao lote original 24–30, mas uma auditoria de retomada (2026-09-09)
identificou que ela era a única aula entre 04 e 30 sem o bloco de gabarito/orientação
docente em `<details>`, e que também não tinha regra `@media print`. As duas lacunas foram
corrigidas em dois commits distintos e sequenciais:

- `2e132521b84d956525f85bd0b80bbb34f25a876d` — acrescentou o bloco `<details
  class="teacher-guidance">` com gabarito comentado (386 palavras, 6 blocos) e o CSS mínimo
  necessário, sem alterar texto-base, objetivos, plano de aula ou navegação.
- `82b894ac457bd6f7359226ec6d848ccc81278a66` — acrescentou
  `@media print { .teacher-guidance { break-inside: avoid; } }`, mesma proteção usada em
  `aula-07.html`, sem alterar conteúdo visível.

**Estado atual:** `auditar_aulas.py` retorna **OK** para `aula-06.html`, com texto-base em
2.800 palavras (limite superior do intervalo permitido, sem exceder), quatro pausas, plano
de 120 minutos, um `<details>` fechado por padrão e nenhuma falha estrutural. A Aula 06
deve ser considerada regularizada quanto aos critérios estruturais do squad.

## Auditoria estrutural determinística de todo o curso (01–30) — HEAD `82b894a`

Execução de `python3 squad-revisao-aulas/scripts/auditar_aulas.py --intervalo 01-30`,
somente leitura, nesta reconciliação:

```
Resumo: 26 aprovada(s), 4 com falha(s), 30 auditada(s).
```

| Resultado | Aulas |
|---|---|
| OK | 04–08, 10–30 (26 aulas) |
| FALHA | 01, 02, 03, 09 (4 aulas) |

Detalhe das falhas:

- **Aula 01:** `<details>` esperado exatamente 1, encontrado 0 (nenhum bloco de
  gabarito/orientação docente); regra `@media print` ausente.
- **Aula 02:** mesma dupla falha da Aula 01.
- **Aula 03:** mesma dupla falha da Aula 01.
- **Aula 09:** regra `@media print` ausente. O gabarito já existe e é válido (178
  palavras, 6 blocos); esta é a única falha da aula.

Estas quatro aulas nunca fizeram parte do lote de reconstrução do squad (que cobriu 24–30)
nem da correção pontual da Aula 06. As Aulas 01–03 foram escritas na primeira leva de
textos-base (commit `3943a1f`), anterior à adoção do padrão de gabarito em `<details>`, que
só passou a ser aplicado a partir da Aula 04 em diante. A Aula 09 já segue o padrão de
gabarito, mas não recebeu a regra de impressão que as aulas vizinhas (07, 08, 10) têm.

## Pendências reais (não resolvidas por este documento)

Esta reconciliação é exclusivamente documental: nenhuma aula foi alterada. As pendências
abaixo são reais, verificáveis pelo auditor determinístico, e permanecem em aberto:

1. **Aulas 01, 02 e 03** não têm bloco de gabarito/orientação docente (`<details>`) nem
   regra `@media print`. Correção equivalente à aplicada na Aula 06 ainda não foi
   autorizada nem executada para essas três aulas.
2. **Aula 09** não tem regra `@media print`. O gabarito já está correto; falta apenas a
   regra de impressão, equivalente à segunda correção aplicada na Aula 06.

Nenhuma dessas pendências afeta as Aulas 24–30, que permanecem integralmente aprovadas, nem
a Aula 06, que está regularizada.

## Limitações da reauditoria

- Esta reconciliação apoiou-se no auditor determinístico (`auditar_aulas.py`) e nos
  relatórios e configurações já produzidos pelo squad. Não houve nova leitura qualitativa
  completa das 30 aulas por revisores humanos ou por uma nova rodada dos seis papéis do
  squad.
- A confirmação de ausência de "molde repetido" nas Aulas 24–30 apoia-se nos pareceres de
  Revisor de Fluidez já registrados em cada relatório individual, não em uma nova
  comparação textual palavra a palavra executada nesta tarefa.
- As Aulas 10–23, fora do escopo original do squad, foram auditadas apenas pelo verificador
  determinístico (que confirmou conformidade estrutural); não foram submetidas a uma nova
  revisão qualitativa nesta reconciliação.
- Este documento não verifica correção teórica, fluidez ou adequação pedagógica além do que
  o auditor determinístico mede. Essas dimensões, para as Aulas 24–30, continuam
  sustentadas pelos pareceres qualitativos já registrados nos relatórios individuais.

## Conclusão e prioridades (atualizado)

As Aulas 24–30 estão concluídas, aprovadas e commitadas, sem pendência qualitativa ou
estrutural conhecida. A Aula 06 está regularizada quanto aos critérios estruturais do
squad. **Não se emite veredito `PRONTO` global para o curso completo (01–30)**, porque as
Aulas 01, 02, 03 e 09 apresentam pendências estruturais reais e verificáveis, listadas
acima. O Aprovador continua autorizado a emitir `PRONTO` por aula individual após conferir
a entrada correspondente neste mapa; qualquer veredito de curso completo deve aguardar a
regularização estrutural das quatro aulas pendentes.
