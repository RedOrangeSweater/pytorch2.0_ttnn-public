**PR title (copy into the title field):** Register Binary OPs, eager mode, forward pass

## Summary

Registers binary eager ATen ops stacked on Unary. Same registration commit as the original upstream PR; one mechanical rename fix applied after Unary review feedback.

## These are the original commits (1:1 transfer)

Same commits authored by **Ilia Shutov** in the original upstream work (2025-10-08), transferred by rebase onto `5d71e464`. Verify any commit: `git show <sha>`.

Original upstream PR (same commits, fill in number when public): `github.com/tenstorrent/pytorch2.0_ttnn/pull/TBD`

| Commit (this PR) | Subject | Author | Authored | Verification |
| --- | --- | --- | --- | --- |
| `5a3d4e188` | Registering Binary OPs | Ilia Shutov | 2025-10-08 | byte-identical (patch-id) |

## Commits added on top in this transfer

These commits are **not** in the original upstream PR. They fix rebase/infra issues only; no eager-op behavior change.

1. **`79c0ebe75`** - Rename `tileify` -> `tilize`, `make_empty_like_tt` -> `make_empty_like_ttnn`
   - Commit subject: fix: rename utility API to match Unary review (tileify->tilize, make_empty_like_tt->make_empty_like_ttnn)
   - Author: Ilia Shutov | Authored: 2026-06-17
   - Why: Binary wrappers were authored before Unary review renamed shared helpers in `eager_common.hpp`. 25 call-sites in `binary_eager_wrappers.hpp` plus 2 lines in `unary_eager_wrappers.hpp`. No op logic changed.

## Stack pointers

- **Base:** `5d71e4649df0f933da42a22c8d970712f0b47d25` (`public/10-unary`)
- **Tip:** `79c0ebe750a76c775e7da5dc67b65bf777d504dd` (`public/20-binary`)
