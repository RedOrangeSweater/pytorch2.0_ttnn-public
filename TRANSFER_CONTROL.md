# Transfer control — pytorch2.0_ttnn-public

Staging for mechanical transfer into `shutovilyaep/pytorch2.0_ttnn`.

## Branch pairs

Each `public/*` / `fix/*` code branch has a `.dev` sibling that is **exactly one commit ahead** adding only `PR_BODY.md`.

| Order | Code | Meta | Notes |
| --- | --- | --- | --- |
| 0 | `fix/tt_metal_bump` | `.dev` | tt-metal compatibility base |
| 1–5 | `public/10-unary` … `50-reduction` | `.dev` | eager op stack |
| 6 | `public/70-pypi` | `.dev` | **0.2.0** matched packaging tip `36a52ae5` |
| archive | `archive/70-pypi-v1-0.1.0` | — | old 0.1.0 draft; do not transfer |

## Operator recipe

1. Open PR from code branch; paste title+body from matching `.dev/PR_BODY.md`
2. Merge; verify tip SHA matches staging
3. Next row

## Packaging tip facts

- `torch-ttnn-shutov==0.2.0`
- `ttnn-shutov==0.65.0.dev20251204` (no PEP 440 `+local`)
- submodule `8dfb324099a1bf6b8839cffd5740e22a4d621385`
- ROS Metal TestPyPI: https://github.com/RedOrangeSweater/ML.TT.Metal/actions/runs/29080934432
- ROS Torch TestPyPI: https://github.com/RedOrangeSweater/ML.TT.PyTorchTtnn/actions/runs/29093775367
- Local marker: `TESTPYPI_PAIR_SMOKE_OK`
- Wheel SHA256:
  - `6328c55d…` `ttnn_shutov-0.65.0.dev20251204-…manylinux_2_34…`
  - `1746d670…` `torch_ttnn_shutov-0.2.0-…manylinux_2_35…`
