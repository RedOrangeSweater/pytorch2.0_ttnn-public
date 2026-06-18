# Статус подготовки public transfer

Дата: 2026-06-18

## Staging repo

`RedOrangeSweater/pytorch2.0_ttnn-public` - только stacked ветки + `.dev` + `transfer-control`.

## Готово (code branches)

| Branch | Commit | Содержимое |
| --- | --- | --- |
| `fix/tt_metal_bump` | `c81f7e56c` | Base CI (shutovilyaep PR #1 head) |
| `public/10-unary` | `5d71e4649` | Unary eager ops |
| `public/20-binary` | `79c0ebe75` | Binary |
| `public/30-conv` | `38b01dd30` | Conv/Pool |
| `public/40-random` | `f9d3dec63` | Random |
| `public/50-reduction` | `d0585f8ca` | Reduction |
| `public/70-pypi` | `8272307bf` | Packaging + PyPI workflows (clean, EN-only) |

## Copy-paste docs (.dev branches)

| PR | `.dev` branch | `PR_BODY.md` source |
| --- | --- | --- |
| #1 | `fix/tt_metal_bump.dev` | generated `01-base` |
| #2 | `public/10-unary.dev` | `02-unary` |
| #3 | `public/20-binary.dev` | `03-binary` |
| #4 | `public/30-conv.dev` | `04-conv-pool` |
| #5 | `public/40-random.dev` | `05-random` |
| #6 | `public/50-reduction.dev` | `06-reduction` |
| #7 | `public/70-pypi.dev` | `07-pypi` |

Control docs (RUNBOOK, ASSESSMENT, provenance index): ветка `transfer-control`.

## Очистка public code branches

- Нет `docs/public_transfer/` на `public/10-unary` .. `public/50-reduction`
- `public/70-pypi`: только `docs/PYPI_torch_ttnn_shutov.md` (EN), без RU analysis
- `pyproject.toml` Repository -> `shutovilyaep/pytorch2.0_ttnn`
- CI runners: `ubuntu-22.04` (fork-safe, без private `ttnn-big`)

## Локальная ветка fix/tt_metal_bump (НЕ использовать)

Локальный `fix/tt_metal_bump` @ `bee9c95e` (tt-metal v0.60.1) **не** совпадает с shutovilyaep PR #1.
Для transfer используем только `c81f7e56c`.

## Следующий шаг (ручно, другой комп)

1. Clone `RedOrangeSweater/pytorch2.0_ttnn-public`
2. Push `public/*` + `fix/tt_metal_bump` в shutovilyaep (если нужно)
3. PR #1 body из `fix/tt_metal_bump.dev`
4. Создать PR #2-#7 по RUNBOOK
