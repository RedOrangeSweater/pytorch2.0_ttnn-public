## Summary

Binary eager-op registration stacked on Unary.

## Provenance

- **Stack base:** `5d71e4649df0f933da42a22c8d970712f0b47d25`
- **This PR tip:** `79c0ebe750a76c775e7da5dc67b65bf777d504dd`
- **Source mapping:** tenstorrent PR #TBD (binary eager)

Transfer method: rebase onto public stack base (hard-reset equivalent). Faithful op logic comes from the private/unmerged branch; infra-only fixes are separate commits listed below.

### Adjustments beyond faithful source commits

| Commit | Subject | Likely reason |
| --- | --- | --- |
| `79c0ebe75` | fix: rename utility API to match Unary review (tileify->tilize, make_empty_like_tt->make_empty_like_ttnn) | tileify->tilize |

## Test plan

- `validate-pr` (pre-commit)
- `cpp-extension-build`
- `ttsim-tests`
- `build-passed`
