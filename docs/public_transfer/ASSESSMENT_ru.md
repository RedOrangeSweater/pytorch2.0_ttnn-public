# Assessment: public transfer stack

Date: 2026-06-18

## Verdict

Public stack for shutovilyaep is **ready for staging** on a dedicated RedOrangeSweater repo.
Code branches `public/10-unary` .. `public/50-reduction` are linear on **`c81f7e56`** (shutovilyaep PR #1 head).
Local `fix/tt_metal_bump` at **`bee9c95e`** (tt-metal v0.60.1 line) **must not** be used as PR #1 base.

## Base divergence (critical)

| Ref | Commit | Use for shutovilyaep PR #1? |
| --- | --- | --- |
| shutovilyaep PR #1 / `origin/fix/tt_metal_bump` (epam) | `c81f7e56` | **yes** |
| local `fix/tt_metal_bump` | `bee9c95e` | **no** - diverged v0.60.1 CI line |

Evidence: `git merge-base --is-ancestor c81f7e56 fix/tt_metal_bump` fails locally.

## Stack mapping (public <- private source)

| PR | Public branch | Tip | Base |
| --- | --- | --- | --- |
| 01-base | `c81f7e56c96c1056ef9a0343682fe02db8508b28` | `c81f7e56` | `github/main` |
| 02-unary | `public/10-unary` | `5d71e464` | `c81f7e56c96c1056ef9a0343682fe02db8508b28` |
| 03-binary | `public/20-binary` | `79c0ebe7` | `public/10-unary` |
| 04-conv-pool | `public/30-conv` | `38b01dd3` | `public/20-binary` |
| 05-random | `public/40-random` | `f9d3dec6` | `public/30-conv` |
| 06-reduction | `public/50-reduction` | `d0585f8c` | `public/40-random` |
| 07-pypi | `public/70-pypi` | `8272307b` | `public/50-reduction` |

| PR | Private source branch | Notes |
| --- | --- | --- |
| 02-unary | `epam/feat/register_eager_ops` | Rebased; +2 infra commits (CMake, include path) |
| 03-binary | `epam/feat/ops.binary` | +1 rename fix after Unary review |
| 04-conv-pool | `epam/feat/ops.conv` | +1 rename fix |
| 05-random | `epam/feat/ops.random` | +1 rename fix |
| 06-reduction | `epam/feat/ops.reduction` | +1 rename fix |
| 07-pypi | _(packaging only)_ | From `release/auditwheel-exclude` proven fixes |

## shutovilyaep PR #1 status

- Existing PR: https://github.com/shutovilyaep/pytorch2.0_ttnn/pull/1
- Head should remain **`c81f7e56`** (`fix/tt_metal_bump`).
- Update title/body from `PR_BODY.md` on `fix/tt_metal_bump.dev` (copy-paste).

## What to create manually (other machine)

PR #2-#7 in shutovilyaep using `public/*` heads and `.dev` branch `PR_BODY.md` texts.

## Regenerate provenance

```bash
python3 tools/gen_public_transfer_provenance.py --all-provenance > docs/public_transfer/provenance_index.md
python3 tools/gen_public_transfer_provenance.py --pr-body 02-unary > /tmp/pr_body.md
```
