## Summary

Reduction eager-op registration stacked on Random.

## Provenance

- **Stack base:** `f9d3dec6394e83202b494289786e02520cf1d1cb`
- **This PR tip:** `d0585f8cabb073bbc3d49666f652124bbbf7b3fc`
- **Source mapping:** tenstorrent PR #TBD (reduction eager)

Transfer method: rebase onto public stack base (hard-reset equivalent). Faithful op logic comes from the private/unmerged branch; infra-only fixes are separate commits listed below.

### Adjustments beyond faithful source commits

| Commit | Subject | Likely reason |
| --- | --- | --- |
| `0e303d283` | Registering Reduction OPs | infra / rebase fix |
| `d0585f8ca` | fix: rename utility API to match Unary review (tileify->tilize, make_empty_like_tt->make_empty_like_ttnn) | tileify->tilize |

## Test plan

- `validate-pr` (pre-commit)
- `cpp-extension-build`
- `ttsim-tests`
- `build-passed`
