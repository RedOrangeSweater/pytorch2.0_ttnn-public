**PR title (copy into the title field):** Register Random OPs, eager mode, forward pass

## Summary

Registers random eager ATen ops (6 overloads) stacked on Conv/Pool. Same registration commit as the original upstream PR.

## These are the original commits (1:1 transfer)

Same commits authored by **Ilia Shutov** in the original upstream work (2025-10-08), transferred by rebase onto `38b01dd3`. Verify any commit: `git show <sha>`.

Original upstream PR (same commits, fill in number when public): `github.com/tenstorrent/pytorch2.0_ttnn/pull/TBD`

| Commit (this PR) | Subject | Author | Authored | Verification |
| --- | --- | --- | --- | --- |
| `d89955b23` | Registering Random OPs | Ilia Shutov | 2025-10-08 | same op code; include-context delta from rebase |

## Commits added on top in this transfer

These commits are **not** in the original upstream PR. They fix rebase/infra issues only; no eager-op behavior change.

1. **`f9d3dec63`** - Rename `tileify` -> `tilize`, `make_empty_like_tt` -> `make_empty_like_ttnn`
   - Commit subject: fix: rename utility API to match Unary review (tileify->tilize, make_empty_like_tt->make_empty_like_ttnn)
   - Author: Ilia Shutov | Authored: 2026-06-17
   - Why: 4 call-sites in `random_eager_wrappers.hpp`. Mechanical rename only.

## Stack pointers

- **Base:** `38b01dd3081de9f456fe99682b116ceb667aafae` (`public/30-conv`)
- **Tip:** `f9d3dec6394e83202b494289786e02520cf1d1cb` (`public/40-random`)
