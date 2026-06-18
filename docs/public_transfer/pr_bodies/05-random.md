## Summary

Random eager-op registration stacked on Conv/Pool.

## Provenance

- **Stack base:** `38b01dd3081de9f456fe99682b116ceb667aafae`
- **This PR tip:** `f9d3dec6394e83202b494289786e02520cf1d1cb`
- **Source mapping:** tenstorrent PR #TBD (random eager)

Transfer method: rebase onto public stack base (hard-reset equivalent). Faithful op logic comes from the private/unmerged branch; infra-only fixes are separate commits listed below.

### Adjustments beyond faithful source commits

| Commit | Subject | Likely reason |
| --- | --- | --- |
| `d89955b23` | Registering Random OPs | infra / rebase fix |
| `f9d3dec63` | fix: rename utility API to match Unary review (tileify->tilize, make_empty_like_tt->make_empty_like_ttnn) | tileify->tilize |

## Test plan

- `validate-pr` (pre-commit)
- `cpp-extension-build`
- `ttsim-tests`
- `build-passed`
