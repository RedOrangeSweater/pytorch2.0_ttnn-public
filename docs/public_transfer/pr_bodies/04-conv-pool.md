**PR title (copy into the title field):** Register Conv/Pool OPs, eager mode, forward pass

## Summary

Registers conv/pool eager ATen ops (17 overloads) stacked on Binary. Same registration commit as the original upstream PR.

## These are the original commits (1:1 transfer)

Same commits authored by **Ilia Shutov** in the original upstream work (2025-10-08), transferred by rebase onto `79c0ebe7`. Verify any commit: `git show <sha>`.

Original upstream PR (same commits, fill in number when public): `github.com/tenstorrent/pytorch2.0_ttnn/pull/TBD`

| Commit (this PR) | Subject | Author | Authored | Verification |
| --- | --- | --- | --- | --- |
| `5d74c98dd` | Registering Conv Pool OPs | Ilia Shutov | 2025-10-08 | same op code; include-context delta from rebase |

## Commits added on top in this transfer

These commits are **not** in the original upstream PR. They fix rebase/infra issues only; no eager-op behavior change.

1. **`38b01dd30`** - Rename `tileify` -> `tilize` in conv/pool wrappers
   - Commit subject: fix: rename utility API to match Unary review (tileify->tilize, make_empty_like_tt->make_empty_like_ttnn)
   - Author: Ilia Shutov | Authored: 2026-06-17
   - Why: 15 call-sites in `conv_pool_eager_wrappers.hpp` only. Mechanical follow-up to Unary review rename. No op logic changed.

## Stack pointers

- **Base:** `79c0ebe750a76c775e7da5dc67b65bf777d504dd` (`public/20-binary`)
- **Tip:** `38b01dd3081de9f456fe99682b116ceb667aafae` (`public/30-conv`)
