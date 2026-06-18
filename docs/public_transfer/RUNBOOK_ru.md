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

## Branch tips (verify после clone staging repo)

| Branch | Commit | shutovilyaep PR |
| --- | --- | --- |
| `fix/tt_metal_bump` | `c81f7e56c` | PR #1 (обновить title/body) |
| `public/10-unary` | `5d71e4649` | PR #2 |
| `public/20-binary` | `79c0ebe75` | PR #3 |
| `public/30-conv` | `38b01dd30` | PR #4 |
| `public/40-random` | `f9d3dec63` | PR #5 |
| `public/50-reduction` | `d0585f8ca` | PR #6 |
| `public/70-pypi` | `8272307bf` | PR #7 |

Проверка:

```bash
git clone git@github.com:RedOrangeSweater/pytorch2.0_ttnn-public.git
cd pytorch2.0_ttnn-public
git rev-parse fix/tt_metal_bump public/70-pypi
```

## Copy-paste PR body (.dev flow)

На машине с доступом к shutovilyaep:

```bash
git clone git@github.com:RedOrangeSweater/pytorch2.0_ttnn-public.git
cd pytorch2.0_ttnn-public
git checkout public/10-unary.dev   # пример для PR #2
cat PR_BODY.md                     # copy-paste в GitHub PR description
```

Для PR #1: `git checkout fix/tt_metal_bump.dev` -> `PR_BODY.md`.

## Push stacked branches в shutovilyaep (если ещё не на remote)

```bash
git remote add shutov git@github.com:shutovilyaep/pytorch2.0_ttnn.git
git push shutov fix/tt_metal_bump public/10-unary public/20-binary public/30-conv public/40-random public/50-reduction public/70-pypi
```

## Обновить PR #1 (base)

```bash
gh pr edit 1 --repo shutovilyaep/pytorch2.0_ttnn \
  --title "ci: tt-metal compatibility base" \
  --body-file PR_BODY.md
# PR_BODY.md из fix/tt_metal_bump.dev после checkout
```

## Создать PR #2-#7

```bash
gh pr create --repo shutovilyaep/pytorch2.0_ttnn --base fix/tt_metal_bump --head public/10-unary \
  --title "feat: register unary eager ops" --body-file PR_BODY.md
# PR_BODY.md из public/10-unary.dev

gh pr create --repo shutovilyaep/pytorch2.0_ttnn --base public/10-unary --head public/20-binary \
  --title "feat: register binary eager ops" --body-file PR_BODY.md

gh pr create --repo shutovilyaep/pytorch2.0_ttnn --base public/20-binary --head public/30-conv \
  --title "feat: register conv and pool eager ops" --body-file PR_BODY.md

gh pr create --repo shutovilyaep/pytorch2.0_ttnn --base public/30-conv --head public/40-random \
  --title "feat: register random eager ops" --body-file PR_BODY.md

gh pr create --repo shutovilyaep/pytorch2.0_ttnn --base public/40-random --head public/50-reduction \
  --title "feat: register reduction eager ops" --body-file PR_BODY.md

gh pr create --repo shutovilyaep/pytorch2.0_ttnn --base public/50-reduction --head public/70-pypi \
  --title "release: add PyPI-compliant public package workflow" --body-file PR_BODY.md
```

## Проверки перед merge / publish

На `transfer-control`:

```bash
git checkout transfer-control
python3 tools/scan_public_transfer_refs.py
python3 tools/gen_public_transfer_provenance.py --write
git diff --check
```

TestPyPI only (после merge PR #7 в shutovilyaep main):

```bash
gh workflow run release-ttnn-shutov.yaml --repo shutovilyaep/pytorch2.0_ttnn --ref main -f publish_target=testpypi
gh workflow run release-torch-ttnn-shutov.yaml --repo shutovilyaep/pytorch2.0_ttnn --ref main \
  -f wheel_type=release -f publish_target=testpypi
```

Production PyPI - только вручную после TestPyPI smoke (см. `docs/PYPI_torch_ttnn_shutov.md` на `public/70-pypi`).

## Порядок merge

1. PR #1 base -> green CI
2. PR #2 Unary -> green CI
3. PR #3 Binary
4. PR #4 Conv/Pool
5. PR #5 Random
6. PR #6 Reduction
7. PR #7 Packaging/PyPI -> TestPyPI rehearsal

## Что не переносить в shutovilyaep PR descriptions

- private CI run IDs
- `Made-with: Cursor` markers
- RU control docs (`docs/public_transfer/*_ru.md`) - они только в staging repo на `transfer-control`
