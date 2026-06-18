**PR title (copy into the title field):** Register Unary OPs, forward pass

## Summary

Registers unary eager ATen ops (forward pass and fallbacks) on top of the tt-metal compatibility base. Same op registration work as the original upstream PR; rebased onto `c81f7e5`.

## These are the original commits (1:1 transfer)

Same commits authored by **Ilia Shutov** in the original upstream work (2025-10-08, 2025-10-09), transferred by rebase onto `c81f7e56`. Verify any commit: `git show <sha>`.

Original upstream PR (same commits, fill in number when public): `github.com/tenstorrent/pytorch2.0_ttnn/pull/TBD`

| Commit (this PR) | Subject | Author | Authored | Verification |
| --- | --- | --- | --- | --- |
| `b498407e1` | Registering Unary OPs, forward pass, fallbacks | Ilia Shutov | 2025-10-08 | same op code; include-context delta from rebase |
| `e01983dde` | PR fix: renamed to tilize | Ilia Shutov | 2025-10-09 | byte-identical (patch-id) |
| `d8f37e47f` | PR fix: renamed to make_empty_like_ttnn | Ilia Shutov | 2025-10-09 | byte-identical (patch-id) |

## Commits added on top in this transfer

These commits are **not** in the original upstream PR. They fix rebase/infra issues only; no eager-op behavior change.

1. **`1e2bc63c9`** - Remove stale `unary.cpp` from `CMakeLists.txt` sources
   - Commit subject: fix: remove stale unary.cpp from CMake sources
   - Author: Ilia Shutov | Authored: 2026-06-16
   - Why: Unary eager refactor deleted the stub source file; CMake still listed it after rebase.

2. **`5d71e4649`** - Add `third-party/tt-metal/ttnn/cpp` to CMake include path
   - Commit subject: fix: add tt-metal ttnn/cpp include path for eager ops
   - Author: Ilia Shutov | Authored: 2026-06-16
   - Why: Installed tt-metal headers omit paths such as `complex_unary.hpp` that eager registration includes from source tree.

## Stack pointers

- **Base:** `c81f7e56c96c1056ef9a0343682fe02db8508b28` (`fix/tt_metal_bump`)
- **Tip:** `5d71e4649df0f933da42a22c8d970712f0b47d25` (`public/10-unary`)
