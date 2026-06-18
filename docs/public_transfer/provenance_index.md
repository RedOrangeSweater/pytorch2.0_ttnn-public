# Provenance index

## Provenance: 01-base (c81f7e56c96c1056ef9a0343682fe02db8508b28)

- **Public tip:** `c81f7e56c96c1056ef9a0343682fe02db8508b28`
- **Public base:** `77e16a33c27a4b39816a9551157fc432981ee5e0` (`github/main`)
- **Upstream placeholder:** tenstorrent/pytorch2.0_ttnn#1293 (rebased) + shutovilyaep PR #1

### Transfer model

Commits were rebased (hard-reset equivalent) onto the public stack base, preserving patch content from the private/unmerged work where possible. Infra-only fixes on top are listed separately as adjustments.

### Faithful commits (patch-id match to source branch)

| Commit | Subject |
| --- | --- |
| `6049e8538` | Manually update TT-NN to 0.62.0rc36.dev247+g627c4eed5b (#1247) |
| `aca17c5de` | Fix pow: Support negative exponents (#1250) |
| `c573d0820` | [auto][on-merge-queue] Update metrics report in README.md (#1266) |
| `87e921725` | Update TT-NN wheel update workflow to use python3.10 wheel (#1269) |
| `c90d6652e` | Split baddbmm test into separate functions (#1251) |
| `b73088ace` | Fix expand: Support squeezed input shapes (#1252) |
| `ab678a6ee` | Add support to binary eltwise ops if first operand is scalar and second is tensor (#1253) |
| `670eb0033` | [auto][on-merge-queue] Update metrics report in README.md (#1278) |
| `f14bf0133` | Upgrade Pytorch to 2.7.1 (#1261) |
| `e3cd52541` | [auto][on-merge-queue] Update metrics report in README.md (#1289) |
| `f5e2fdc1a` | Update README to indicate this project is deprecated and direct users to TT-Forge instead (#1310) |
| `79d173d38` | [Bounty]  Support Mamba 2.8B model (#1168) |
| `ffd3b0ead` | Remove cron jobs from CI workflows |
| `4a3126930` | Get Falcon 7B running E2E (#1265) |
| `7ba2867e8` | [Bounty] Support Llama3.2 1B, Llama3.2 3B and Llama3.1 8B models (#1335) |
| `7fb5bbaaf` | Add model: Mistral 7B (#1280) |
| `bcb8f99a7` | build: modernize build system and eliminate LD_LIBRARY_PATH requirement |
| `69b772b91` | PR fix: refactor Tensor construction to use from_borrowed_data() factory |
| `74f43840e` | PR fix: test: simplify tensor creation with PyTorch 2.7.1 randint improvements |
| `46ba0a7a3` | PR fix: clang-format workaround removed |
| `a9da0d94a` | PR fix: ttnn_device_mode.py docs |
| `df39c0ae8` | PR check: removed retry on initial git submodules sync |
| `0bfd71651` | PR fix: revert to using base Docker image ghcr.io/tenstorrent/pytorch2.0_ttnn |
| `68f7d1016` | Revert "PR fix: revert to using base Docker image ghcr.io/tenstorrent/pytorch2.0_ttnn" |
| `12f2caec9` | fix: update-docker-container.yaml fix - using pyproject.toml, not requirements.txt |
| `fd9fad99d` | comments update |
| `872398e85` | fix: sync .gitmodules with ttnn wheel version and respect it in CI |
| `fea1b19d0` | fix: improve README.md installation instructions |
| `bf16e7a22` | fix: update CI action files to use pyproject.toml instead of requirements-dev.txt |
| `4b7a6b5a8` | fix: update header path for tt-metal v0.62.0-dev20250916 |
| `95a26929b` | fix: make TT_METAL_HOME optional with auto-detection |
| `ae60e2b8c` | fix: add pure Python installation support via SKIP_CPP_EXTENSION |
| `c43f857d6` | docs: document SKIP_CPP_EXTENSION for Python-only installation |
| `d495c679f` | feat: enable verbose logging for scikit-build-core |
| `df65e639a` | fix: handle BFloat16 precision limits in test_add_cpp_extension |
| `3347a47fe` | ci: add Docker registry authentication for tt-metal container |
| `6e050df32` | fix: update installation scripts to actively ignore TT_METAL_HOME env variable |
| `8edbe2046` | fix: CI fetch robustness |
| `241617857` | CI fix attempt |
| `8226b2108` | refactor: streamline CI submodule handling for tt-metal |
| `0a1ff7986` | docs: updated deprecated docs related to TT_METAL_HOME and binaries bundling |
| `95bf198e3` | fix: - Added workaround for broken auto-detection in tt-metal source builds. |
| `e3757b0ae` | fix: add conditional include for assert header to support tt-metal compatibility testing |
| `55ff8df3d` | fix: enhance C++ extension build and test workflow, docs are updated - build_cpp_extension.sh, run_cpp_extension_tests.sh are created with Release, Debug modes |
| `6516b7d14` | quickfix: llk-related updates do not allow to cleanly perform checkout when repo is created, perform a clean checkout via GitHub actions |
| `5786f3c78` | chore: update dependencies in pyproject.toml for improved clarity and organization |
| `1e7c9c7b3` | chore(ci): pin tt-metal Docker image for project freeze |
| `68acef4bd` | feat(ci): add wheel verification simulating PyPI user experience |
| `d86b2d668` | feat(ci): add wheel verification and fix packaging |
| `bc64b85f7` | fix: bundling binaries to torch-ttnn to fix wheel for end-users, documentation with reasoning is created |
| `d9a309f38` | (build) CMake files cleanup |
| `5681dbbdd` | (ci) fix: GitHub Actions worflows updates |
| `b7d1f8ac6` | (ci) Installing tt-metal dependencies including sfpi |
| `59fe2e736` | (ci) install_full_dependencies checkbox added |
| `8f8567cb4` | (ci) possible error fix |
| `52d926234` | (docs) Make it clear that TT_METAL_HOME is ignored during build, but MUST be set when running tests |
| `b1677f162` | (ci) setting TT_METAL_HOME env variable before running tests |
| `c81f7e56c` | ci: add TTSim simulator-based testing with shim workaround |

### Adjustments on top (not in source branch as-is)

_None._

### range-diff excerpt

```text
    1:  6049e8538 =  1:  6049e8538 Manually update TT-NN to 0.62.0rc36.dev247+g627c4eed5b (#1247)
     2:  aca17c5de =  2:  aca17c5de Fix pow: Support negative exponents (#1250)
     3:  c573d0820 =  3:  c573d0820 [auto][on-merge-queue] Update metrics report in README.md (#1266)
     4:  87e921725 =  4:  87e921725 Update TT-NN wheel update workflow to use python3.10 wheel (#1269)
     5:  c90d6652e =  5:  c90d6652e Split baddbmm test into separate functions (#1251)
     6:  b73088ace =  6:  b73088ace Fix expand: Support squeezed input shapes (#1252)
     7:  ab678a6ee =  7:  ab678a6ee Add support to binary eltwise ops if first operand is scalar and second is tensor (#1253)
     8:  670eb0033 =  8:  670eb0033 [auto][on-merge-queue] Update metrics report in README.md (#1278)
     9:  f14bf0133 =  9:  f14bf0133 Upgrade Pytorch to 2.7.1 (#1261)
    10:  e3cd52541 = 10:  e3cd52541 [auto][on-merge-queue] Update metrics report in README.md (#1289)
    11:  f5e2fdc1a = 11:  f5e2fdc1a Update README to indicate this project is deprecated and direct users to TT-Forge instead (#1310)
    12:  79d173d38 = 12:  79d173d38 [Bounty]  Support Mamba 2.8B model (#1168)
    ...
```

## Provenance: 02-unary (public/10-unary)

- **Public tip:** `5d71e4649df0f933da42a22c8d970712f0b47d25`
- **Public base:** `c81f7e56c96c1056ef9a0343682fe02db8508b28` (`c81f7e56c96c1056ef9a0343682fe02db8508b28`)
- **Upstream placeholder:** tenstorrent PR #TBD (unary eager)

### Transfer model

Commits were rebased (hard-reset equivalent) onto the public stack base, preserving patch content from the private/unmerged work where possible. Infra-only fixes on top are listed separately as adjustments.

### Faithful commits (patch-id match to source branch)

| Commit | Subject |
| --- | --- |
| `e01983dde` | PR fix: renamed to tilize |
| `d8f37e47f` | PR fix: renamed to make_empty_like_ttnn |

### Adjustments on top (not in source branch as-is)

| Commit | Subject |
| --- | --- |
| `b498407e1` | Registering Unary OPs, forward pass, fallbacks |
| `1e2bc63c9` | fix: remove stale unary.cpp from CMake sources |
| `5d71e4649` | fix: add tt-metal ttnn/cpp include path for eager ops |

### range-diff excerpt

```text
    1:  3cb187924 ! 1:  b498407e1 Registering Unary OPs, forward pass, fallbacks
        @@ torch_ttnn/cpp_extension/ttnn_cpp_extension/include/ttnn_cpp_extension/utils/una
         
          ## torch_ttnn/cpp_extension/ttnn_cpp_extension/src/open_registration_extension.cpp ##
         @@
        --#include <ATen/native/DispatchStub.h>
        --#include <torch/csrc/utils/pybind.h>
        --#include <torch/extension.h>
        --
        + #include <torch/library.h>
        + #include <torch/extension.h>
        + 
    ...
```

## Provenance: 03-binary (public/20-binary)

- **Public tip:** `79c0ebe750a76c775e7da5dc67b65bf777d504dd`
- **Public base:** `5d71e4649df0f933da42a22c8d970712f0b47d25` (`public/10-unary`)
- **Upstream placeholder:** tenstorrent PR #TBD (binary eager)

### Transfer model

Commits were rebased (hard-reset equivalent) onto the public stack base, preserving patch content from the private/unmerged work where possible. Infra-only fixes on top are listed separately as adjustments.

### Faithful commits (patch-id match to source branch)

| Commit | Subject |
| --- | --- |
| `5a3d4e188` | Registering Binary OPs |

### Adjustments on top (not in source branch as-is)

| Commit | Subject |
| --- | --- |
| `79c0ebe75` | fix: rename utility API to match Unary review (tileify->tilize, make_empty_like_tt->make_empty_like_ttnn) |

### range-diff excerpt

```text
    1:  c3abdde36 = 1:  5a3d4e188 Registering Binary OPs
    -:  --------- > 2:  79c0ebe75 fix: rename utility API to match Unary review (tileify->tilize, make_empty_like_tt->make_empty_like_ttnn)
```

## Provenance: 04-conv-pool (public/30-conv)

- **Public tip:** `38b01dd3081de9f456fe99682b116ceb667aafae`
- **Public base:** `79c0ebe750a76c775e7da5dc67b65bf777d504dd` (`public/20-binary`)
- **Upstream placeholder:** tenstorrent PR #TBD (conv/pool eager)

### Transfer model

Commits were rebased (hard-reset equivalent) onto the public stack base, preserving patch content from the private/unmerged work where possible. Infra-only fixes on top are listed separately as adjustments.

### Faithful commits (patch-id match to source branch)

_No patch-id matches (base PR or packaging-only)._

### Adjustments on top (not in source branch as-is)

| Commit | Subject |
| --- | --- |
| `5d74c98dd` | Registering Conv Pool OPs |
| `38b01dd30` | fix: rename utility API to match Unary review (tileify->tilize, make_empty_like_tt->make_empty_like_ttnn) |

### range-diff excerpt

```text
    1:  b2757312f ! 1:  5d74c98dd Registering Conv Pool OPs
        @@ torch_ttnn/cpp_extension/ttnn_cpp_extension/include/ttnn_cpp_extension/utils/con
         
          ## torch_ttnn/cpp_extension/ttnn_cpp_extension/src/open_registration_extension.cpp ##
         @@
        - 
          #include "ttnn_cpp_extension/utils/device.hpp"
          #include "ttnn_cpp_extension/utils/unary_eager_register.hpp"
        + #include "ttnn_cpp_extension/utils/binary_eager_register.hpp"
         +#include "ttnn_cpp_extension/utils/conv_pool_eager_register.hpp"
          
          #include <ttnn/operations/eltwise/unary/unary.hpp>
    ...
```

## Provenance: 05-random (public/40-random)

- **Public tip:** `f9d3dec6394e83202b494289786e02520cf1d1cb`
- **Public base:** `38b01dd3081de9f456fe99682b116ceb667aafae` (`public/30-conv`)
- **Upstream placeholder:** tenstorrent PR #TBD (random eager)

### Transfer model

Commits were rebased (hard-reset equivalent) onto the public stack base, preserving patch content from the private/unmerged work where possible. Infra-only fixes on top are listed separately as adjustments.

### Faithful commits (patch-id match to source branch)

_No patch-id matches (base PR or packaging-only)._

### Adjustments on top (not in source branch as-is)

| Commit | Subject |
| --- | --- |
| `d89955b23` | Registering Random OPs |
| `f9d3dec63` | fix: rename utility API to match Unary review (tileify->tilize, make_empty_like_tt->make_empty_like_ttnn) |

### range-diff excerpt

```text
    1:  97c7a2a34 ! 1:  d89955b23 Registering Random OPs
        @@ torch_ttnn/cpp_extension/ttnn_cpp_extension/include/ttnn_cpp_extension/utils/ran
         
          ## torch_ttnn/cpp_extension/ttnn_cpp_extension/src/open_registration_extension.cpp ##
         @@
        - 
        - #include "ttnn_cpp_extension/utils/device.hpp"
          #include "ttnn_cpp_extension/utils/unary_eager_register.hpp"
        + #include "ttnn_cpp_extension/utils/binary_eager_register.hpp"
        + #include "ttnn_cpp_extension/utils/conv_pool_eager_register.hpp"
         +#include "ttnn_cpp_extension/utils/random_eager_register.hpp"
          
    ...
```

## Provenance: 06-reduction (public/50-reduction)

- **Public tip:** `d0585f8cabb073bbc3d49666f652124bbbf7b3fc`
- **Public base:** `f9d3dec6394e83202b494289786e02520cf1d1cb` (`public/40-random`)
- **Upstream placeholder:** tenstorrent PR #TBD (reduction eager)

### Transfer model

Commits were rebased (hard-reset equivalent) onto the public stack base, preserving patch content from the private/unmerged work where possible. Infra-only fixes on top are listed separately as adjustments.

### Faithful commits (patch-id match to source branch)

_No patch-id matches (base PR or packaging-only)._

### Adjustments on top (not in source branch as-is)

| Commit | Subject |
| --- | --- |
| `0e303d283` | Registering Reduction OPs |
| `d0585f8ca` | fix: rename utility API to match Unary review (tileify->tilize, make_empty_like_tt->make_empty_like_ttnn) |

### range-diff excerpt

```text
    1:  07c6cf329 ! 1:  0e303d283 Registering Reduction OPs
        @@ torch_ttnn/cpp_extension/ttnn_cpp_extension/include/ttnn_cpp_extension/utils/red
         
          ## torch_ttnn/cpp_extension/ttnn_cpp_extension/src/open_registration_extension.cpp ##
         @@
        - 
        - #include "ttnn_cpp_extension/utils/device.hpp"
        - #include "ttnn_cpp_extension/utils/unary_eager_register.hpp"
        + #include "ttnn_cpp_extension/utils/binary_eager_register.hpp"
        + #include "ttnn_cpp_extension/utils/conv_pool_eager_register.hpp"
        + #include "ttnn_cpp_extension/utils/random_eager_register.hpp"
         +#include "ttnn_cpp_extension/utils/reduction_eager_register.hpp"
    ...
```

## Provenance: 07-pypi (public/70-pypi)

- **Public tip:** `8272307bfdccdb69a15b42b164e845b48a7d3af8`
- **Public base:** `d0585f8cabb073bbc3d49666f652124bbbf7b3fc` (`public/50-reduction`)
- **Upstream placeholder:** packaging follow-up to bounty #1036 / PR #1095

### Transfer model

Commits were rebased (hard-reset equivalent) onto the public stack base, preserving patch content from the private/unmerged work where possible. Infra-only fixes on top are listed separately as adjustments.

### Faithful commits (patch-id match to source branch)

| Commit | Subject |
| --- | --- |
| `8272307bf` | release: add PyPI-compliant public package workflow |

### Adjustments on top (not in source branch as-is)

_None._

### range-diff excerpt

```text
_No upstream source branch; packaging-only PR._
```
