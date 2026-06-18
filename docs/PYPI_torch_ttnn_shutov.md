# PyPI: torch-ttnn-shutov + ttnn-shutov

Unofficial provenance build of the eager-op stack for `shutovilyaep/pytorch2.0_ttnn`.
Import package names stay `torch_ttnn` and `ttnn`; PyPI distribution names are
`torch-ttnn-shutov` and `ttnn-shutov`.

## Why `-shutov` distributions exist

Upstream bounty [#1036](https://github.com/tenstorrent/pytorch2.0_ttnn/issues/1036)
(packaging workflow, merged as PR
[#1095](https://github.com/tenstorrent/pytorch2.0_ttnn/pull/1095)) made
`torch-ttnn` pip-installable, but public PyPI **rejects** wheels whose metadata
contains direct URL dependencies (`ttnn @ https://...`).

The eager stack CI originally used a direct URL to an internal Tenstorrent wheel
index for install smoke tests. That pattern works in private CI but is **not**
a stable public dependency surface.

Publication fix (channel change, not eager-op logic):

1. Repack pinned internal `ttnn 0.62.0.dev20250916` as `ttnn-shutov`
   (`tools/repack_ttnn_shutov_wheel.py`, SHA256-verified source wheel).
2. Publish `ttnn-shutov` first.
3. Publish `torch-ttnn-shutov` with `[pypi]` extra ->
   `ttnn-shutov==0.62.0.dev20250916`.

### Option A (not available today)

If a compatible `ttnn` wheel were on public PyPI, `torch-ttnn-shutov[pypi]` could
depend on it directly without a repack layer.

### Option B (chosen)

Internal/runtime wheel is republished as `ttnn-shutov` on public PyPI/TestPyPI.
Import name remains `ttnn`.

## Workflows

| Workflow | Purpose |
| --- | --- |
| `release-ttnn-shutov.yaml` | Download + SHA256 verify + repack + publish `ttnn-shutov` |
| `release-torch-ttnn-shutov.yaml` | Build tt-metal + wheel + publish `torch-ttnn-shutov` |

Both use `workflow_dispatch` input `publish_target`: `testpypi` or `pypi`.
Default path is **TestPyPI only** until manual approval.

## One-time setup: TestPyPI

1. Create TestPyPI projects: `ttnn-shutov`, `torch-ttnn-shutov`.
2. GitHub -> **Settings -> Environments** -> `testpypi`.
3. Secret `TESTPYPI_API_TOKEN` (token from `test.pypi.org`).

## One-time setup: production PyPI

1. Create PyPI projects: `ttnn-shutov`, `torch-ttnn-shutov`.
2. Trusted publisher per workflow (environment `pypi`) or API token fallback.
3. Target repo for public proof: `shutovilyaep/pytorch2.0_ttnn`.

## Publish order (TestPyPI rehearsal)

1. Actions -> **Release ttnn-shutov (repack for public PyPI)** ->
   `publish_target=testpypi`
2. Actions -> **Release torch-ttnn-shutov (fork, no HW runners)** ->
   `wheel_type=release`, `publish_target=testpypi`

Do **not** run production `publish_target=pypi` until TestPyPI install smoke is green.

## Post-publish verification (TestPyPI)

```bash
pip install \
  --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ \
  torch-ttnn-shutov[pypi]
python -c "import torch_ttnn; print(torch_ttnn.__file__)"
python -c "import ttnn; print(ttnn.__file__)"
pip show torch-ttnn-shutov ttnn-shutov
```

## Post-publish verification (production PyPI)

```bash
pip install torch-ttnn-shutov[pypi]
python -c "import torch_ttnn; print(torch_ttnn.__file__)"
python -c "import ttnn; print(ttnn.__file__)"
```

Compare `pip show` version with `VERSION` file and workflow log `Built from commit:`.

## Local repack (debug)

```bash
python3 -m pip install wheel twine
python3 tools/repack_ttnn_shutov_wheel.py --output-dir dist
twine check dist/ttnn_shutov-*.whl
```

## auditwheel note

`release-torch-ttnn-shutov.yaml` runs `auditwheel repair` with PyTorch shared libs
excluded from vendoring (`libtorch*.so`, `libc10.so`). PyTorch remains a normal
pip dependency; the wheel carries the TT extension and bundled TT runtime helpers.
