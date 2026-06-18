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

## Upstream drift while PR #1293 waited (factual timeline)

Original upstream PR `tenstorrent/pytorch2.0_ttnn#1293` was opened **2025-11-19** (head `254f2642`, 41 commits on `main`). Required checks passed (C++ Extension Tests, validate-pr). The PR was never reviewed or merged. While it remained open, `main` advanced through the same files this PR edits (`README.md`, `docs/README.md.in`, CI workflows), which produced the GitHub banner **"This branch has conflicts that must be resolved"** on an otherwise-green PR.

### Merges into `main` that overlap PR #1293 files

| Date | Upstream merge | Author | Files touched | Overlap with PR #1293 |
| --- | --- | --- | --- | --- |
| 2025-12-08 | `#1310` deprecation notice | Joe Malone | `README.md`, `docs/README.md.in` | PR rewrites install/docs in both files |
| 2025-12-18 | Remove cron jobs from CI workflows | Joe Malone | `.github/workflows/run-accuracy-tests.yaml`, `update-readme.yaml`, `update-ttnn-wheel.yaml` | PR edits all three workflows |
| 2025-12-18 | `#1168` Mamba 2.8B bounty | pollachisaravanan | `README.md` (metrics) | PR rewrites `README.md` |
| 2025-12-31 | `#1265` Falcon 7B E2E | Jamie Zhuang | `README.md` (metrics) | PR rewrites `README.md` |
| 2026-02-20 | `#1335` Llama3 bounty | pollachisaravanan | `README.md` (metrics) | PR rewrites `README.md` |
| 2026-02-24 | `#1280` Mistral 7B | Saïd | `README.md` (metrics) | PR rewrites `README.md` |

PR #1293 touches **10 files** vs `main` at open time: `README.md` (377 lines), `docs/README.md.in` (77 lines), and **8** workflow files under `.github/workflows/`.

### Concrete delta absorbed by this rebase

The rebased PR (`c81f7e56c`) already includes `#1310` and cron-removal in its ancestry and re-applies the build/CI/install changes on top. Example hunk from `#1310` now present in this branch:

```diff
 # PyTorch 2.0 TTNN Compiler
+# Visit [TT-Forge](https://github.com/tenstorrent/tt-forge) for our latest compiler project
+
+**Pytorch 2.0 TT-NN** is no longer maintained, please consider using [TT-Forge](https://github.com/tenstorrent/tt-forge) instead.
+
 The PyTorch 2.0 TT-NN Compiler enables seamless execution...
```

Cron schedule lines removed by maintainer merge (`ffd3b0e`) in the three workflows above are reconciled in this rebase. **No build, CI, or eager-op behavior change** was introduced solely to resolve these conflicts.

### SHA equivalence vs original submission

| Comparison | Result |
| --- | --- |
| Original `#1293` head `254f2642` vs this tip `c81f7e56c` | Different SHAs (rebase onto current `main`) |
| Shared commit subjects (51 in `#1293`) | **48/51** byte-identical by patch-id; 3 differ only in rebase context (`build: modernize...`, Docker pin, CI checkbox) |
| This tip vs `shutovilyaep/pytorch2.0_ttnn#1` head | **Same SHA** (`c81f7e56c`, mergeable) |

## Stack pointers

- **Base:** `77e16a33c27a4b39816a9551157fc432981ee5e0` (`github/main`)
- **Tip:** `c81f7e56c96c1056ef9a0343682fe02db8508b28` (`c81f7e56c96c1056ef9a0343682fe02db8508b28`)
