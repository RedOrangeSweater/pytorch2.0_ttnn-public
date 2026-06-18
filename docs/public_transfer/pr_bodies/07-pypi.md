**PR title (copy into the title field):** Make package PyPI-buildable: torch-ttnn-shutov + ttnn-shutov

## Summary

Publication-channel change: rename distribution to `torch-ttnn-shutov`, repack runtime as `ttnn-shutov`, add manual TestPyPI/PyPI release workflows. **New packaging work** - not a 1:1 transfer of an upstream eager-op PR.

## These are the original commits (1:1 transfer)

_Not applicable - this is new packaging work, not a transfer of upstream eager-op commits._

## Commits added on top in this transfer

_None - this PR is new packaging work, not a transfer of upstream eager-op commits._

### What this PR adds (new work)

- Rename distribution to `torch-ttnn-shutov` (`VERSION` -> `0.1.0`); import stays `torch_ttnn`.
- Add `tools/repack_ttnn_shutov_wheel.py` and `release-ttnn-shutov.yaml` workflow.
- Replace direct URL in `[pypi]` extra with `ttnn-shutov==0.62.0.dev20250916`.
- Add `release-torch-ttnn-shutov.yaml` with TestPyPI/PyPI `workflow_dispatch`.
- Update CI wheel smoke to install repacked `ttnn-shutov` before wheel verification.

### Why `-shutov` (public PyPI constraint)

Public PyPI and TestPyPI reject wheels whose metadata contains direct URL dependencies (`ttnn @ https://...`). Same class of blocker as packaging bounty `github.com/tenstorrent/pytorch2.0_ttnn/issues/1036` (merged as `github.com/tenstorrent/pytorch2.0_ttnn/pull/1095`).

Fix: repack pinned internal `ttnn 0.62.0.dev20250916` as `ttnn-shutov` (SHA256-verified), publish `ttnn-shutov` first, then `torch-ttnn-shutov[pypi]`. Import names stay `ttnn` and `torch_ttnn`.

## Stack pointers

- **Base:** `d0585f8cabb073bbc3d49666f652124bbbf7b3fc` (`public/50-reduction`)
- **Tip:** `8272307bfdccdb69a15b42b164e845b48a7d3af8` (`public/70-pypi`)
