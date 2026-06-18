## Summary

Conv/Pool eager-op registration stacked on Binary.

## Provenance

- **Stack base:** `79c0ebe750a76c775e7da5dc67b65bf777d504dd`
- **This PR tip:** `38b01dd3081de9f456fe99682b116ceb667aafae`
- **Source mapping:** tenstorrent PR #TBD (conv/pool eager)

Transfer method: rebase onto public stack base (hard-reset equivalent). Faithful op logic comes from the private/unmerged branch; infra-only fixes are separate commits listed below.

### Adjustments beyond faithful source commits

| Commit | Subject | Likely reason |
| --- | --- | --- |
| `5d74c98dd` | Registering Conv Pool OPs | infra / rebase fix |
| `38b01dd30` | fix: rename utility API to match Unary review (tileify->tilize, make_empty_like_tt->make_empty_like_ttnn) | tileify->tilize |

## Test plan

- `validate-pr` (pre-commit)
- `cpp-extension-build`
- `ttsim-tests`
- `build-passed`
