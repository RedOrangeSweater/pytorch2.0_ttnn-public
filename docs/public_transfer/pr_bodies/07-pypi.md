## Summary

Publication-channel change: `torch-ttnn-shutov` + repacked `ttnn-shutov` for public PyPI/TestPyPI compliance. Not an eager-op behavior change.

## Provenance

- **Stack base:** `d0585f8cabb073bbc3d49666f652124bbbf7b3fc`
- **This PR tip:** `8272307bfdccdb69a15b42b164e845b48a7d3af8`
- **Source mapping:** packaging follow-up to bounty #1036 / PR #1095

Transfer method: rebase onto public stack base (hard-reset equivalent). Faithful op logic comes from the private/unmerged branch; infra-only fixes are separate commits listed below.

### Why `-shutov` distributions

Public PyPI and TestPyPI reject wheels whose metadata contains direct URL dependencies (`ttnn @ https://...`). This was the core blocker in bounty [#1036](https://github.com/tenstorrent/pytorch2.0_ttnn/issues/1036) / PR [#1095](https://github.com/tenstorrent/pytorch2.0_ttnn/pull/1095).

Fix (publication channel, not eager-op logic):

1. Repack pinned internal `ttnn 0.62.0.dev20250916` as `ttnn-shutov` (`tools/repack_ttnn_shutov_wheel.py`, SHA256-verified).
2. Publish `ttnn-shutov` first.
3. Publish `torch-ttnn-shutov` with `[pypi]` extra -> `ttnn-shutov==0.62.0.dev20250916`.

Import package names stay `torch_ttnn` and `ttnn`.

## Test plan

1. Merge after Reduction PR is green.
2. Configure GitHub environment `testpypi` with secret `TESTPYPI_API_TOKEN`.
3. Run **Release ttnn-shutov** with `publish_target=testpypi`.
4. Run **Release torch-ttnn-shutov** with `wheel_type=release`, `publish_target=testpypi`.
5. Verify install from TestPyPI (see `docs/PYPI_torch_ttnn_shutov.md`).
6. Do not publish to production PyPI until manual approval.
