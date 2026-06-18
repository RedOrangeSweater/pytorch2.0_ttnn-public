**PR title (copy into the title field):** tt-metal main branch compatibility fixes (rebased)

## Summary

Rebases the tt-metal compatibility work from the original upstream PR onto current `main` and adds TTSim simulator-based CI testing on standard GitHub-hosted runners.

## These are the original commits (1:1 transfer)

This PR rebases the full content of the original upstream PR onto current `main`. All commits are authored by **Ilia Shutov** (`Ilia_Shutov@epam.com`). The rebase preserves the same changes as the original work; verify any commit with `git show <sha>`.

Original upstream PR (same work, rebased): `github.com/tenstorrent/pytorch2.0_ttnn/pull/1293`

### Included from original PR 1293 (via rebase)

- **Build System Modernization**: Migrated from setup.py to pyproject.toml with scikit-build-core
- **RPATH Configuration**: Proper RPATH setup to eliminate LD_LIBRARY_PATH requirement
- **Binary Bundling**: TTNN binaries bundled in wheel for self-contained distribution
- **CI Infrastructure**: Updated workflows for wheel-based testing
- **Consistent Compiler**: Enforced Clang-17 to match tt-metal build
- **TT_METAL_HOME**: Made optional with auto-detection from submodule
- Submodule sync, CI robustness, wheel verification, Docker pin, and related fixes from the original PR series

## Commits added on top in this transfer

New work on top of the rebased original PR (not in upstream PR 1293 as merged):

1. **`c81f7e56c`** - TTSim simulator-based CI testing with shim workaround
   - Author: Ilia Shutov | Authored: 2026-02-27
   - Enables CI on standard GitHub runners without Tenstorrent hardware
   - Downloads TTSim from `tenstorrent/ttsim` releases
   - Adds `ttsim_shim` no-op stubs for UMD/TTSim symbol mismatch on pinned tt-metal
   - Consolidates earlier CI fixes (Kitware GPG key, TTSim env, workflow wiring)

Supporting CI commits in the same rebase (same author, Feb 2026):

- `b1677f162` - set TT_METAL_HOME before running tests
- `52d926234` - document TT_METAL_HOME ignored at build, required at test
- `5681dbbdd` - GitHub Actions workflow updates (git-lfs, checkout hygiene)
- `1e7c9c7b3` - pin tt-metal Docker image digest for reproducibility
- `68acef4bd` / `d86b2d668` - wheel verification simulating PyPI user install

## Stack pointers

- **Base:** `77e16a33c27a4b39816a9551157fc432981ee5e0` (`github/main`)
- **Tip:** `c81f7e56c96c1056ef9a0343682fe02db8508b28` (`c81f7e56c96c1056ef9a0343682fe02db8508b28`)
