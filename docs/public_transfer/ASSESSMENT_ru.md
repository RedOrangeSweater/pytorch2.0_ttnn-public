# Assessment: public transfer stack

Date: 2026-06-18

## Verdict

Public stack for shutovilyaep is **ready for staging** on `RedOrangeSweater/pytorch2.0_ttnn-public`.
PR descriptions on `.dev` branches include exact upstream titles, 1:1 commit tables with patch-id
verification, and explicit on-top fix sections.

## PR titles (copy-paste)

| Slug | Title | Branch |
| --- | --- | --- |
| 01-base | `tt-metal main branch compatibility fixes (rebased)` | `c81f7e56c96c1056ef9a0343682fe02db8508b28` |
| 02-unary | `Register Unary OPs, forward pass` | `public/10-unary` |
| 03-binary | `Register Binary OPs, eager mode, forward pass` | `public/20-binary` |
| 04-conv-pool | `Register Conv/Pool OPs, eager mode, forward pass` | `public/30-conv` |
| 05-random | `Register Random OPs, eager mode, forward pass` | `public/40-random` |
| 06-reduction | `Register Reduction OPs, eager mode, forward pass` | `public/50-reduction` |
| 07-pypi | `Make package PyPI-buildable: torch-ttnn-shutov + ttnn-shutov` | `public/70-pypi` |

First line of each `PR_BODY.md`: **PR title (copy into the title field):** ...

## Base divergence (critical)

| Ref | Commit | Use for shutovilyaep PR #1? |
| --- | --- | --- |
| shutovilyaep PR #1 head | `c81f7e56` | **yes** |
| local diverged `fix/tt_metal_bump` | `bee9c95e` | **no** (tt-metal v0.60.1 line) |

## Stack mapping

| PR | Public branch | Tip | Base |
| --- | --- | --- | --- |
| 01-base | `c81f7e56c96c1056ef9a0343682fe02db8508b28` | `c81f7e56` | `github/main` |
| 02-unary | `public/10-unary` | `5d71e464` | `fix/tt_metal_bump` |
| 03-binary | `public/20-binary` | `79c0ebe7` | `public/10-unary` |
| 04-conv-pool | `public/30-conv` | `38b01dd3` | `public/20-binary` |
| 05-random | `public/40-random` | `f9d3dec6` | `public/30-conv` |
| 06-reduction | `public/50-reduction` | `d0585f8c` | `public/40-random` |
| 07-pypi | `public/70-pypi` | `8272307b` | `public/50-reduction` |

## Non-mention rule for staged PR bodies

Upstream PR links in `pr_bodies/*.md` and `PR_BODY.md` use **backticks** so GitHub does not
cross-reference the original tenstorrent PR while work is still private. Replace `TBD` with the
real PR number before publishing the shutovilyaep PR.

## Regenerate

```bash
python3 tools/gen_public_transfer_provenance.py --write
```
