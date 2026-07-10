**PR title (copy into the title field):** Make package PyPI-buildable: torch-ttnn-shutov 0.2.0 + ttnn-shutov 0.65.0.dev20251204

## Summary

Publication-channel change on top of the eager op stack: `torch-ttnn-shutov==0.2.0`, `ttnn-shutov==0.65.0.dev20251204` (metal pin `8dfb324099a`; no PEP 440 `+local` — rejected by TestPyPI/PyPI), release workflows with `as_torch_device` gate and OpenMPI 5 ULFM runtime note.

Supersedes `archive/70-pypi-v1-0.1.0`.

## Stack pointers

- **Base:** `d0585f8cabb073bbc3d49666f652124bbbf7b3fc` (`public/50-reduction`)
- **Tip:** `58551cf975034621c62b8a04b89324ed7a276c19` (`public/70-pypi`)

## Verified on RedOrangeSweater

| Stage | Link | Result |
| --- | --- | --- |
| Metal none | https://github.com/RedOrangeSweater/ML.TT.Metal/actions/runs/29074577044 | green |
| Metal TestPyPI | https://github.com/RedOrangeSweater/ML.TT.Metal/actions/runs/29080934432 | green |
| Torch TestPyPI | https://github.com/RedOrangeSweater/ML.TT.PyTorchTtnn/actions/runs/29093775367 | green |
| Local clean pair-smoke | `TESTPYPI_PAIR_SMOKE_OK` | imports + `as_torch_device` |

## Wheel SHA256 (TestPyPI)

```
6328c55d12db443b53356ddfac85972d0bd775dbf13e4c7922fc3272855e9a92  ttnn_shutov-0.65.0.dev20251204-cp310-cp310-manylinux_2_34_x86_64.whl
1746d67042e6364e4d38741eadce3a9fc7bfc60c0d642164e672936217c36bf3  torch_ttnn_shutov-0.2.0-cp310-cp310-manylinux_2_35_x86_64.whl
```

## Runtime

Actions-built `ttnn` needs OpenMPI 5 ULFM (`MPIX_Comm_revoke`) on `LD_LIBRARY_PATH`. Host apt OpenMPI 4.x is insufficient.
