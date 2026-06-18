## Summary

Unary eager-op registration rebased onto `c81f7e5`.

## Provenance

- **Stack base:** `c81f7e56c96c1056ef9a0343682fe02db8508b28`
- **This PR tip:** `5d71e4649df0f933da42a22c8d970712f0b47d25`
- **Source mapping:** tenstorrent PR #TBD (unary eager)

Transfer method: rebase onto public stack base (hard-reset equivalent). Faithful op logic comes from the private/unmerged branch; infra-only fixes are separate commits listed below.

### Adjustments beyond faithful source commits

| Commit | Subject | Likely reason |
| --- | --- | --- |
| `b498407e1` | Registering Unary OPs, forward pass, fallbacks | infra / rebase fix |
| `1e2bc63c9` | fix: remove stale unary.cpp from CMake sources | remove stale unary.cpp from CMake |
| `5d71e4649` | fix: add tt-metal ttnn/cpp include path for eager ops | tt-metal ttnn/cpp include path |

## Test plan

- `validate-pr` (pre-commit)
- `cpp-extension-build`
- `ttsim-tests`
- `build-passed`
