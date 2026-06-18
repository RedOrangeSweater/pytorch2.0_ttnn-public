# Runbook: перенос в shutovilyaep/pytorch2.0_ttnn

Дата: 2026-06-18
Staging repo: `RedOrangeSweater/pytorch2.0_ttnn-public`
Целевой remote: `git@github.com:shutovilyaep/pytorch2.0_ttnn.git`

## Модель веток

| Ветка | Назначение | Head PR? |
| --- | --- | --- |
| `fix/tt_metal_bump` | PR #1 код (base) | **да** |
| `public/10-unary` .. `public/70-pypi` | PR #2-#7 код (stacked) | **да** |
| `*.dev` (напр. `public/10-unary.dev`) | тот же код + `PR_BODY.md` для copy-paste | **нет** |
| `transfer-control` | RUNBOOK, STATUS, ASSESSMENT, генератор | **нет** |

`.dev` ветки **не** пушатся как head PR - только для чтения `PR_BODY.md` на другом компе.

## PR titles (copy-paste без раздумий)

Первая строка каждого `PR_BODY.md` на `.dev` ветке:

```text
**PR title (copy into the title field):** <title>
```

| shutovilyaep PR | `.dev` branch | Title (как в tenstorrent) |
| --- | --- | --- |
| #1 | `fix/tt_metal_bump.dev` | tt-metal main branch compatibility fixes (rebased) |
| #2 | `public/10-unary.dev` | Register Unary OPs, forward pass |
| #3 | `public/20-binary.dev` | Register Binary OPs, eager mode, forward pass |
| #4 | `public/30-conv.dev` | Register Conv/Pool OPs, eager mode, forward pass |
| #5 | `public/40-random.dev` | Register Random OPs, eager mode, forward pass |
| #6 | `public/50-reduction.dev` | Register Reduction OPs, eager mode, forward pass |
| #7 | `public/70-pypi.dev` | Make package PyPI-buildable: torch-ttnn-shutov + ttnn-shutov |

Title и body - **раздельно**: title из первой строки `PR_BODY.md`, body - весь файл целиком.

## Non-mention rule (пока работа тихая)

Ссылки на оригинальные tenstorrent PR в `PR_BODY.md` в **backticks**:

```text
`github.com/tenstorrent/pytorch2.0_ttnn/pull/TBD`
```

GitHub **не** создаёт cross-reference и **не** постит mention в оригинальный PR, пока ссылка в inline code. Перед публикацией shutovilyaep PR замените `TBD` на номер и при необходимости снимите backticks.

## Branch tips

| Branch | Commit | shutovilyaep PR |
| --- | --- | --- |
| `fix/tt_metal_bump` | `c81f7e56c` | PR #1 |
| `public/10-unary` | `5d71e4649` | PR #2 |
| `public/20-binary` | `79c0ebe75` | PR #3 |
| `public/30-conv` | `38b01dd30` | PR #4 |
| `public/40-random` | `f9d3dec63` | PR #5 |
| `public/50-reduction` | `d0585f8ca` | PR #6 |
| `public/70-pypi` | `8272307bf` | PR #7 |

## Copy-paste PR body (.dev flow)

```bash
git clone git@github.com:RedOrangeSweater/pytorch2.0_ttnn-public.git
cd pytorch2.0_ttnn-public
git checkout public/10-unary.dev
head -1 PR_BODY.md    # -> title
cat PR_BODY.md        # -> body
```

## Создать PR в shutovilyaep

```bash
git checkout public/10-unary.dev
TITLE=$(sed -n 's/^\*\*PR title (copy into the title field):\*\* //p' PR_BODY.md)
gh pr create --repo shutovilyaep/pytorch2.0_ttnn --base fix/tt_metal_bump --head public/10-unary \
  --title "$TITLE" --body-file PR_BODY.md
```

## Regenerate descriptions

```bash
git checkout transfer-control
python3 tools/gen_public_transfer_provenance.py --write
python3 tools/scan_public_transfer_refs.py
```
