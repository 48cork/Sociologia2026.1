# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## O que é este repositório

Site estático de materiais acadêmicos para o semestre 2026.1, com duas disciplinas ministradas pelo professor Sergio Farias:

- **Introdução à Sociologia** — Turma 1 (Ter/Qua, 2h/aula, 30 encontros) e Turma 2 (Seg noite, 3h20/aula, 18 encontros)
- **Fundamentos do Pensamento Sociológico** — Turma 3 (Seg manhã, 3h20/aula, 18 encontros)

Não há framework, build system, servidor ou dependências externas. Tudo é HTML + CSS inline. Para visualizar, basta abrir qualquer `.html` diretamente no browser.

## Estrutura

```
index.html                                        ← landing page geral
introducao-sociologia/
  turma1/
    index.html                                    ← plano de aulas da turma (cronograma completo)
    plano_aulas.md                                ← fonte em Markdown do plano
    aulas/aula-01.html … aula-30.html            ← roteiros individuais (30 aulas × 2h)
  turma2/
    index.html
    plano_aulas.md
    aulas/aula-01.html … aula-18.html            ← roteiros individuais (18 aulas × 3h20)
fundamentos-pensamento-sociologico/
  turma3/
    index.html
    plano_aulas.md
    aulas/aula-01.html … aula-18.html            ← roteiros individuais (18 aulas × 3h20)
materiais-gerais/                                 ← pasta reservada para materiais compartilhados
```

## Arquitetura visual (CSS inline)

Todo o CSS vive dentro de `<style>` em cada arquivo HTML. Não há folha de estilos compartilhada. O sistema de design é consistente entre os arquivos e usa estas variáveis CSS:

```css
--bg: #0a0a0f          /* fundo global */
--surface: #12121c     /* superfície secundária */
--card: #1a1a2e        /* cards */
--border: #2a2a4a      /* bordas */
--purple-lt: #a855f7   /* accent Turma 1 e Turma 2 */
--blue-lt: #818cf8
--teal-lt: #2dd4bf     /* accent Turma 3 (Fundamentos) */
--amber-lt: #fbbf24
--rose-lt: #fb7185
--text: #e2e8f0
--muted: #94a3b8
```

Ao criar ou editar arquivos, copie as variáveis CSS do arquivo mais próximo do mesmo tipo — não invente novas variáveis.

## Padrões dos roteiros de aula (`aulas/aula-NN.html`)

Cada roteiro tem sempre estas seções, nesta ordem:
1. **Objetivos da Aula** (3–4 itens)
2. **Conteúdo Programático** (tópicos com subtópicos)
3. **Plano de Aula com Tempo** (timeline com minutos — total: 120 min para Turma 1; 200 min para Turmas 2 e 3, incluindo 10 min de intervalo)
4. **Textos para Leitura Prévia** (2–3 referências reais)
5. **Atividades em Sala** (descrição pedagógica detalhada)
6. **Recursos Necessários** (tags)

Aulas de seminário (apresentações) acrescentam seção de **Orientações para Entrega Final** ou **Critérios de Avaliação**.

### Cores dos blocos por turma (badge e accent da seção)

| Bloco | Conteúdo | Cor |
|-------|----------|-----|
| I | Origem / fundamentos | `--purple-lt` |
| II | Pensamento clássico / Durkheim | `--blue-lt` |
| III | Marx | `--teal-lt` |
| IV | Weber / cultura | `--amber-lt` |
| V | Teoria séc. XX / instituições | `#c084fc` (violet) |
| VI | Mudança social / seminários | `--rose-lt` |

### Navegação entre aulas

Cada aula tem nav com links `← Anterior` / `Próxima →`. A primeira aula não tem "← Anterior"; a última não tem "Próxima →".

- Turma 1: link de retorno para `../index.html`
- Turma 2: link de retorno para `../index.html`
- Turma 3: link de retorno para `../index.html`

## Datas e calendário

| Turma | Dia | Duração/aula | Início | Término | Total |
|-------|-----|-------------|--------|---------|-------|
| Turma 1 | Ter + Qua | 2h | 14/04/2026 | 29/07/2026 | 30 encontros · 60h |
| Turma 2 | Segunda (noite) | 3h20 | 13/04/2026 | 10/08/2026 | 18 encontros · 60h |
| Turma 3 | Segunda (manhã) | 3h20 | 13/04/2026 | 10/08/2026 | 18 encontros · 60h |

Feriados relevantes para Turma 1: Tiradentes (21/04), São João (24/06), Fundação da Paraíba (05/08).

## Sistema de avaliação (todas as turmas)

100% Seminário em Grupo (até 5 alunos), dividido em 4 entregas de 25% cada:
1. Pesquisa bibliográfica — entregue no encontro de orientação (~enc. 9 ou 12 conforme turma)
2. Apresentação oral — enc. penúltimo e antepenúltimo
3. Relatório escrito — até 7 laudas, ABNT — enc. final
4. Vídeo — 5 a 10 minutos — enc. final

Nota mínima: 6,0 | Frequência mínima: 75%

## Convenções ao editar

- Sempre leia o arquivo existente mais similar antes de criar um novo (mesma turma, bloco próximo).
- Os `plano_aulas.md` de cada turma são a fonte canônica dos dados (datas, conteúdos, carga horária). Consulte-os antes de editar datas ou ementas nos HTMLs.
- Não crie arquivos CSS, JS ou de configuração separados — o projeto é intencionalmente self-contained por arquivo.
