## Summary

Build-system modernization and tt-metal CI compatibility base on shutovilyaep PR #1 (`fix/tt_metal_bump` @ `c81f7e5`). Includes TTSim simulator CI and packaging groundwork.

## Provenance

- **Stack base:** `77e16a33c27a4b39816a9551157fc432981ee5e0`
- **This PR tip:** `c81f7e56c96c1056ef9a0343682fe02db8508b28`
- **Source mapping:** tenstorrent/pytorch2.0_ttnn#1293 (rebased) + shutovilyaep PR #1

Transfer method: rebase onto public stack base (hard-reset equivalent). Faithful op logic comes from the private/unmerged branch; infra-only fixes are separate commits listed below.

### Included in base (shutovilyaep PR #1 @ `c81f7e5`)

- `pyproject.toml` + scikit-build-core, RPATH, wheel bundling fixes
- Pinned public tt-metal Docker image for CI
- TTSim simulator job and shim workaround for UMD/TTSim symbol mismatch
- Submodule and CI robustness fixes
- Wheel verification path simulating end-user install

### Not included

- No Unary/Binary/Conv/Random/Reduction eager registrations (stacked PRs follow)

## Test plan

- `validate-pr` (pre-commit)
- `cpp-extension-build`
- `ttsim-tests`
- `build-passed`
