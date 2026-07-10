# PyPI: torch-ttnn-shutov + ttnn-shutov

Unofficial provenance build of the eager-op stack.
Import package names stay `torch_ttnn` and `ttnn`; PyPI distribution names are `torch-ttnn-shutov` and `ttnn-shutov`.

Full analysis (RU): `docs/analysis/2026-06-17_pypi_publish_blocker_ru.md`

## Why two packages

Public PyPI/TestPyPI reject uploaded wheels whose metadata contains direct URL dependencies (`ttnn @ https://...`).
The eager stack originally used that pattern for CI install smoke tests only.

Publication fix (separate from eager-op code):

1. Build `ttnn` from tt-metal pin `8dfb324099a` (ML.TT.Metal workflow
   `release-ttnn-shutov-from-source`) and publish as
   `ttnn-shutov==0.65.0.dev20251204+g8dfb324099`.
2. Publish `torch-ttnn-shutov==0.2.0` with `[pypi]` pinning that matching runtime.
3. Default CI is artifact-only; TestPyPI then prod after pair-smoke.

## Unified PyPI / TestPyPI pipeline

**Goal:** identical package names and versions on both indexes. The only difference when installing is the index URL.

| Package | Version | PyPI | TestPyPI |
| --- | --- | --- | --- |
| `ttnn-shutov` | `0.65.0.dev20251204+g8dfb324099` | yes | yes |
| `torch-ttnn-shutov` | `0.2.0` | yes | yes |

### Why from-source matching wheel

Eager Execution passes Python `ttnn` Device objects into the C++ extension.
A mismatched `0.62` runtime + v0.65 extension is a cross-ABI call even with
SONAME isolation. Building `ttnn-shutov` from the same Merge pin restores one ABI.

## Workflows

| Workflow | Purpose |
| --- | --- |
| `release-ttnn-shutov.yaml` | Download + SHA256 verify + repack + publish `ttnn-shutov` |
| `release-torch-ttnn-shutov.yaml` | Build tt-metal + wheel + publish `torch-ttnn-shutov` |
| `verify-shutov-packaging.yaml` | Fast PR gate: repack smoke + isolation tool check |

Both release workflows use `workflow_dispatch` input `publish_target`: `testpypi` or `pypi`. Same wheel artifact for both targets.

## One-time setup: TestPyPI

1. Create TestPyPI projects: `ttnn-shutov`, `torch-ttnn-shutov` (or let first upload recreate them).
2. GitHub -> **Settings -> Environments** -> `testpypi`.
3. Secret `TESTPYPI_API_TOKEN` (token from `test.pypi.org`).

## One-time setup: production PyPI

1. Create PyPI projects: `ttnn-shutov`, `torch-ttnn-shutov`.
2. Trusted publisher per workflow (environment `pypi`) or API token fallback.
3. For public proof: prefer owner `shutovilyaep`, repo `pytorch2.0_ttnn`.

## Publish order (TestPyPI rehearsal and production)

1. Actions -> **Release ttnn-shutov (repack for public PyPI)** -> `publish_target=testpypi`, then `pypi`
2. Actions -> **Release torch-ttnn-shutov (fork, no HW runners)** -> `wheel_type=release`, `publish_target=testpypi`, then `pypi`

## Post-publish verification

```bash
# TestPyPI rehearsal (index-url is the only difference)
pip install \
  --index-url https://test.pypi.org/simple/ \
  'torch-ttnn-shutov[pypi]==0.2.0'

python -c "import torch_ttnn; print(torch_ttnn.__file__)"
python -c "import ttnn; print(ttnn.__file__)"
python -c "from torch_ttnn.cpp_extension import ttnn_module; print(ttnn_module.__file__)"
pip show torch-ttnn-shutov ttnn-shutov
```

```bash
# Production PyPI (same command without --index-url)
pip install 'torch-ttnn-shutov[pypi]==0.2.0'

python -c "import torch_ttnn; print(torch_ttnn.__file__)"
python -c "import ttnn; print(ttnn.__file__)"
python -c "from torch_ttnn.cpp_extension import ttnn_module; print(ttnn_module.__file__)"
pip show torch-ttnn-shutov ttnn-shutov
```

Compare `pip show` version with `VERSION` file and workflow log `Built from commit:`.

## Local repack (debug)

```bash
python3 -m pip install wheel twine
python3 tools/repack_ttnn_shutov_wheel.py --output-dir dist
twine check dist/ttnn_shutov-*.whl
```

Defaults: `--source-version 0.62.0.dev20250916`, `--publish-version 0.62.0.dev20250916+pypi.repack`.
