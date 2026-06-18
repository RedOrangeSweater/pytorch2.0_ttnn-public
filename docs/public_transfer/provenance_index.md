# Provenance index

## Provenance: 01-base (c81f7e56c96c1056ef9a0343682fe02db8508b28)

- **PR title:** tt-metal main branch compatibility fixes (rebased)
- **Public tip:** `c81f7e56c96c1056ef9a0343682fe02db8508b28`
- **Public base:** `77e16a33c27a4b39816a9551157fc432981ee5e0` (`github/main`)
- **Original upstream (non-mention):** `github.com/tenstorrent/pytorch2.0_ttnn/pull/1293`

## Provenance: 02-unary (public/10-unary)

- **PR title:** Register Unary OPs, forward pass
- **Public tip:** `5d71e4649df0f933da42a22c8d970712f0b47d25`
- **Public base:** `c81f7e56c96c1056ef9a0343682fe02db8508b28` (`fix/tt_metal_bump`)
- **Original upstream (non-mention):** `github.com/tenstorrent/pytorch2.0_ttnn/pull/TBD`

### Original commits

| Commit (this PR) | Subject | Author | Authored | Verification |
| --- | --- | --- | --- | --- |
| `b498407e1` | Registering Unary OPs, forward pass, fallbacks | Ilia Shutov | 2025-10-08 | same op code; include-context delta from rebase |
| `e01983dde` | PR fix: renamed to tilize | Ilia Shutov | 2025-10-09 | byte-identical (patch-id) |
| `d8f37e47f` | PR fix: renamed to make_empty_like_ttnn | Ilia Shutov | 2025-10-09 | byte-identical (patch-id) |

### On-top commits

- `1e2bc63c9`: Remove stale `unary.cpp` from `CMakeLists.txt` sources
- `5d71e4649`: Add `third-party/tt-metal/ttnn/cpp` to CMake include path

## Provenance: 03-binary (public/20-binary)

- **PR title:** Register Binary OPs, eager mode, forward pass
- **Public tip:** `79c0ebe750a76c775e7da5dc67b65bf777d504dd`
- **Public base:** `5d71e4649df0f933da42a22c8d970712f0b47d25` (`public/10-unary`)
- **Original upstream (non-mention):** `github.com/tenstorrent/pytorch2.0_ttnn/pull/TBD`

### Original commits

| Commit (this PR) | Subject | Author | Authored | Verification |
| --- | --- | --- | --- | --- |
| `5a3d4e188` | Registering Binary OPs | Ilia Shutov | 2025-10-08 | byte-identical (patch-id) |

### On-top commits

- `79c0ebe75`: Rename `tileify` -> `tilize`, `make_empty_like_tt` -> `make_empty_like_ttnn`

## Provenance: 04-conv-pool (public/30-conv)

- **PR title:** Register Conv/Pool OPs, eager mode, forward pass
- **Public tip:** `38b01dd3081de9f456fe99682b116ceb667aafae`
- **Public base:** `79c0ebe750a76c775e7da5dc67b65bf777d504dd` (`public/20-binary`)
- **Original upstream (non-mention):** `github.com/tenstorrent/pytorch2.0_ttnn/pull/TBD`

### Original commits

| Commit (this PR) | Subject | Author | Authored | Verification |
| --- | --- | --- | --- | --- |
| `5d74c98dd` | Registering Conv Pool OPs | Ilia Shutov | 2025-10-08 | same op code; include-context delta from rebase |

### On-top commits

- `38b01dd30`: Rename `tileify` -> `tilize` in conv/pool wrappers

## Provenance: 05-random (public/40-random)

- **PR title:** Register Random OPs, eager mode, forward pass
- **Public tip:** `f9d3dec6394e83202b494289786e02520cf1d1cb`
- **Public base:** `38b01dd3081de9f456fe99682b116ceb667aafae` (`public/30-conv`)
- **Original upstream (non-mention):** `github.com/tenstorrent/pytorch2.0_ttnn/pull/TBD`

### Original commits

| Commit (this PR) | Subject | Author | Authored | Verification |
| --- | --- | --- | --- | --- |
| `d89955b23` | Registering Random OPs | Ilia Shutov | 2025-10-08 | same op code; include-context delta from rebase |

### On-top commits

- `f9d3dec63`: Rename `tileify` -> `tilize`, `make_empty_like_tt` -> `make_empty_like_ttnn`

## Provenance: 06-reduction (public/50-reduction)

- **PR title:** Register Reduction OPs, eager mode, forward pass
- **Public tip:** `d0585f8cabb073bbc3d49666f652124bbbf7b3fc`
- **Public base:** `f9d3dec6394e83202b494289786e02520cf1d1cb` (`public/40-random`)
- **Original upstream (non-mention):** `github.com/tenstorrent/pytorch2.0_ttnn/pull/TBD`

### Original commits

| Commit (this PR) | Subject | Author | Authored | Verification |
| --- | --- | --- | --- | --- |
| `0e303d283` | Registering Reduction OPs | Ilia Shutov | 2025-10-08 | same op code; include-context delta from rebase |

### On-top commits

- `d0585f8ca`: Rename `tileify` -> `tilize`, `make_empty_like_tt` -> `make_empty_like_ttnn`

## Provenance: 07-pypi (public/70-pypi)

- **PR title:** Make package PyPI-buildable: torch-ttnn-shutov + ttnn-shutov
- **Public tip:** `8272307bfdccdb69a15b42b164e845b48a7d3af8`
- **Public base:** `d0585f8cabb073bbc3d49666f652124bbbf7b3fc` (`public/50-reduction`)
- **Original upstream (non-mention):** `github.com/tenstorrent/pytorch2.0_ttnn/issues/1036` (packaging bounty)
