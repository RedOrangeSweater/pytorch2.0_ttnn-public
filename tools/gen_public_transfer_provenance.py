#!/usr/bin/env python3
"""Generate provenance sections for shutovilyaep public transfer PR bodies."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BASE_REF = "c81f7e56c96c1056ef9a0343682fe02db8508b28"
LOCAL_FIX_TT_METAL_BUMP = "bee9c95ee"


@dataclass(frozen=True)
class StackEntry:
    slug: str
    public_branch: str
    public_base: str
    source_branch: str | None
    source_base: str | None
    upstream_pr: str
    title: str
    summary: str
    adjustment_hints: tuple[str, ...] = ()


STACK: list[StackEntry] = [
    StackEntry(
        slug="01-base",
        public_branch=BASE_REF,
        public_base="github/main",
        source_branch="epam/fix/tt_metal_bump",
        source_base="github/main",
        upstream_pr="tenstorrent/pytorch2.0_ttnn#1293 (rebased) + shutovilyaep PR #1",
        title="ci: tt-metal compatibility base",
        summary=(
            "Build-system modernization and tt-metal CI compatibility base on shutovilyaep PR #1 "
            "(`fix/tt_metal_bump` @ `c81f7e5`). Includes TTSim simulator CI and packaging groundwork."
        ),
    ),
    StackEntry(
        slug="02-unary",
        public_branch="public/10-unary",
        public_base=BASE_REF,
        source_branch="epam/feat/register_eager_ops",
        source_base="epam/fix/tt_metal_bump",
        upstream_pr="tenstorrent PR #TBD (unary eager)",
        title="feat: register unary eager ops",
        summary="Unary eager-op registration rebased onto `c81f7e5`.",
        adjustment_hints=(
            "remove stale unary.cpp from CMake",
            "tt-metal ttnn/cpp include path",
        ),
    ),
    StackEntry(
        slug="03-binary",
        public_branch="public/20-binary",
        public_base="public/10-unary",
        source_branch="epam/feat/ops.binary",
        source_base="epam/feat/register_eager_ops",
        upstream_pr="tenstorrent PR #TBD (binary eager)",
        title="feat: register binary eager ops",
        summary="Binary eager-op registration stacked on Unary.",
        adjustment_hints=("tileify->tilize", "make_empty_like_tt->make_empty_like_ttnn"),
    ),
    StackEntry(
        slug="04-conv-pool",
        public_branch="public/30-conv",
        public_base="public/20-binary",
        source_branch="epam/feat/ops.conv",
        source_base="epam/feat/ops.binary",
        upstream_pr="tenstorrent PR #TBD (conv/pool eager)",
        title="feat: register conv and pool eager ops",
        summary="Conv/Pool eager-op registration stacked on Binary.",
        adjustment_hints=("tileify->tilize",),
    ),
    StackEntry(
        slug="05-random",
        public_branch="public/40-random",
        public_base="public/30-conv",
        source_branch="epam/feat/ops.random",
        source_base="epam/feat/ops.conv",
        upstream_pr="tenstorrent PR #TBD (random eager)",
        title="feat: register random eager ops",
        summary="Random eager-op registration stacked on Conv/Pool.",
        adjustment_hints=("tileify->tilize", "make_empty_like_tt->make_empty_like_ttnn"),
    ),
    StackEntry(
        slug="06-reduction",
        public_branch="public/50-reduction",
        public_base="public/40-random",
        source_branch="epam/feat/ops.reduction",
        source_base="epam/feat/ops.random",
        upstream_pr="tenstorrent PR #TBD (reduction eager)",
        title="feat: register reduction eager ops",
        summary="Reduction eager-op registration stacked on Random.",
        adjustment_hints=("tileify->tilize", "make_empty_like_tt->make_empty_like_ttnn"),
    ),
    StackEntry(
        slug="07-pypi",
        public_branch="public/70-pypi",
        public_base="public/50-reduction",
        source_branch=None,
        source_base=None,
        upstream_pr="packaging follow-up to bounty #1036 / PR #1095",
        title="release: add PyPI-compliant public package workflow",
        summary=(
            "Publication-channel change: `torch-ttnn-shutov` + repacked `ttnn-shutov` for public "
            "PyPI/TestPyPI compliance. Not an eager-op behavior change."
        ),
    ),
]


def git(*args: str, check: bool = True) -> str:
    cmd = ["git", "-C", str(ROOT), *args]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if check and result.returncode != 0:
        raise RuntimeError(f"git failed ({' '.join(cmd)}): {result.stderr.strip()}")
    return result.stdout.strip()


def resolve_ref(ref: str) -> str:
    if ref == "github/main":
        return git("rev-parse", "github/main")
    return git("rev-parse", ref)


def log_oneline(base: str, tip: str) -> list[tuple[str, str]]:
    out = git("log", "--reverse", "--format=%h %s", f"{base}..{tip}")
    rows: list[tuple[str, str]] = []
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, _, subject = line.partition(" ")
        rows.append((sha, subject))
    return rows


def patch_id(commit: str) -> str | None:
    patch = git("format-patch", "-1", "--stdout", commit, check=False)
    if not patch:
        return None
    out = subprocess.run(
        ["git", "patch-id", "--stable"],
        input=patch,
        capture_output=True,
        text=True,
        check=False,
    )
    if out.returncode != 0 or not out.stdout.strip():
        return None
    return out.stdout.split()[0]


def classify_commits(entry: StackEntry) -> tuple[list[tuple[str, str]], list[tuple[str, str]]]:
    public_tip = resolve_ref(entry.public_branch)
    public_base = resolve_ref(entry.public_base)
    public_commits = log_oneline(public_base, public_tip)
    if not entry.source_branch or not entry.source_base:
        return public_commits, []

    source_tip = resolve_ref(entry.source_branch)
    source_base = resolve_ref(entry.source_base)
    source_commits = log_oneline(source_base, source_tip)
    source_ids = {patch_id(sha): (sha, subject) for sha, subject in source_commits if patch_id(sha)}

    faithful: list[tuple[str, str]] = []
    adjustments: list[tuple[str, str]] = []
    for sha, subject in public_commits:
        pid = patch_id(sha)
        if pid and pid in source_ids:
            faithful.append((sha, subject))
        else:
            adjustments.append((sha, subject))
    return faithful, adjustments


def range_diff_snippet(entry: StackEntry, limit: int = 12) -> str:
    if not entry.source_branch or not entry.source_base:
        return "_No upstream source branch; packaging-only PR._"
    left = f"{resolve_ref(entry.source_base)}..{resolve_ref(entry.source_branch)}"
    right = f"{resolve_ref(entry.public_base)}..{resolve_ref(entry.public_branch)}"
    out = git("range-diff", left, right, check=False)
    if not out:
        return "_range-diff unavailable (refs missing)._"
    lines = out.splitlines()[:limit]
    if len(out.splitlines()) > limit:
        lines.append("...")
    return "\n".join(f"    {line}" for line in lines)


def render_commit_table(commits: list[tuple[str, str]], empty: str) -> str:
    if not commits:
        return empty
    lines = ["| Commit | Subject |", "| --- | --- |"]
    for sha, subject in commits:
        lines.append(f"| `{sha}` | {subject} |")
    return "\n".join(lines)


def render_provenance_section(entry: StackEntry) -> str:
    public_tip = resolve_ref(entry.public_branch)
    public_base = resolve_ref(entry.public_base)
    faithful, adjustments = classify_commits(entry)

    parts = [
        f"## Provenance: {entry.slug} ({entry.public_branch})",
        "",
        f"- **Public tip:** `{public_tip}`",
        f"- **Public base:** `{public_base}` (`{entry.public_base}`)",
        f"- **Upstream placeholder:** {entry.upstream_pr}",
        "",
        "### Transfer model",
        "",
        "Commits were rebased (hard-reset equivalent) onto the public stack base, preserving patch "
        "content from the private/unmerged work where possible. Infra-only fixes on top are listed "
        "separately as adjustments.",
        "",
        "### Faithful commits (patch-id match to source branch)",
        "",
        render_commit_table(faithful, "_No patch-id matches (base PR or packaging-only)._"),
        "",
        "### Adjustments on top (not in source branch as-is)",
        "",
        render_commit_table(adjustments, "_None._"),
        "",
        "### range-diff excerpt",
        "",
        "```text",
        range_diff_snippet(entry),
        "```",
        "",
    ]
    return "\n".join(parts)


def render_pr_body(entry: StackEntry) -> str:
    public_tip = resolve_ref(entry.public_branch)
    public_base = resolve_ref(entry.public_base)
    _, adjustments = classify_commits(entry)

    lines = [
        "## Summary",
        "",
        entry.summary,
        "",
        "## Provenance",
        "",
        f"- **Stack base:** `{public_base}`",
        f"- **This PR tip:** `{public_tip}`",
        f"- **Source mapping:** {entry.upstream_pr}",
        "",
        "Transfer method: rebase onto public stack base (hard-reset equivalent). Faithful op logic "
        "comes from the private/unmerged branch; infra-only fixes are separate commits listed below.",
        "",
    ]

    if entry.slug == "01-base":
        lines.extend(
            [
                "### Included in base (shutovilyaep PR #1 @ `c81f7e5`)",
                "",
                "- `pyproject.toml` + scikit-build-core, RPATH, wheel bundling fixes",
                "- Pinned public tt-metal Docker image for CI",
                "- TTSim simulator job and shim workaround for UMD/TTSim symbol mismatch",
                "- Submodule and CI robustness fixes",
                "- Wheel verification path simulating end-user install",
                "",
                "### Not included",
                "",
                "- No Unary/Binary/Conv/Random/Reduction eager registrations (stacked PRs follow)",
                "",
            ]
        )
    elif entry.slug == "07-pypi":
        lines.extend(
            [
                "### Why `-shutov` distributions",
                "",
                "Public PyPI and TestPyPI reject wheels whose metadata contains direct URL "
                "dependencies (`ttnn @ https://...`). This was the core blocker in bounty "
                "[#1036](https://github.com/tenstorrent/pytorch2.0_ttnn/issues/1036) / "
                "PR [#1095](https://github.com/tenstorrent/pytorch2.0_ttnn/pull/1095).",
                "",
                "Fix (publication channel, not eager-op logic):",
                "",
                "1. Repack pinned internal `ttnn 0.62.0.dev20250916` as `ttnn-shutov` "
                "(`tools/repack_ttnn_shutov_wheel.py`, SHA256-verified).",
                "2. Publish `ttnn-shutov` first.",
                "3. Publish `torch-ttnn-shutov` with `[pypi]` extra -> `ttnn-shutov==0.62.0.dev20250916`.",
                "",
                "Import package names stay `torch_ttnn` and `ttnn`.",
                "",
            ]
        )
    else:
        lines.append("### Adjustments beyond faithful source commits")
        lines.append("")
        if adjustments:
            lines.append("| Commit | Subject | Likely reason |")
            lines.append("| --- | --- | --- |")
            for sha, subject in adjustments:
                reason = "infra / rebase fix"
                lower = subject.lower()
                for hint in entry.adjustment_hints:
                    if hint.lower() in lower or hint.lower() in subject.lower():
                        reason = hint
                        break
                lines.append(f"| `{sha}` | {subject} | {reason} |")
        else:
            lines.append("_None - all commits patch-match the source branch._")
        lines.append("")

    lines.extend(
        [
            "## Test plan",
            "",
        ]
    )
    if entry.slug == "07-pypi":
        lines.extend(
            [
                "1. Merge after Reduction PR is green.",
                "2. Configure GitHub environment `testpypi` with secret `TESTPYPI_API_TOKEN`.",
                "3. Run **Release ttnn-shutov** with `publish_target=testpypi`.",
                "4. Run **Release torch-ttnn-shutov** with `wheel_type=release`, "
                "`publish_target=testpypi`.",
                "5. Verify install from TestPyPI (see `docs/PYPI_torch_ttnn_shutov.md`).",
                "6. Do not publish to production PyPI until manual approval.",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "- `validate-pr` (pre-commit)",
                "- `cpp-extension-build`",
                "- `ttsim-tests`",
                "- `build-passed`",
                "",
            ]
        )

    return "\n".join(lines)


def render_assessment() -> str:
    base = BASE_REF[:8]
    local = LOCAL_FIX_TT_METAL_BUMP[:8]
    stack_rows = []
    for entry in STACK:
        tip = resolve_ref(entry.public_branch)[:8]
        stack_rows.append(f"| {entry.slug} | `{entry.public_branch}` | `{tip}` | `{entry.public_base}` |")
    stack_table = "\n".join(stack_rows)

    return f"""# Assessment: public transfer stack

Date: 2026-06-18

## Verdict

Public stack for shutovilyaep is **ready for staging** on a dedicated RedOrangeSweater repo.
Code branches `public/10-unary` .. `public/50-reduction` are linear on **`{base}`** (shutovilyaep PR #1 head).
Local `fix/tt_metal_bump` at **`{local}`** (tt-metal v0.60.1 line) **must not** be used as PR #1 base.

## Base divergence (critical)

| Ref | Commit | Use for shutovilyaep PR #1? |
| --- | --- | --- |
| shutovilyaep PR #1 / `origin/fix/tt_metal_bump` (epam) | `{base}` | **yes** |
| local `fix/tt_metal_bump` | `{local}` | **no** - diverged v0.60.1 CI line |

Evidence: `git merge-base --is-ancestor {base} fix/tt_metal_bump` fails locally.

## Stack mapping (public <- private source)

| PR | Public branch | Tip | Base |
| --- | --- | --- | --- |
{stack_table}

| PR | Private source branch | Notes |
| --- | --- | --- |
| 02-unary | `epam/feat/register_eager_ops` | Rebased; +2 infra commits (CMake, include path) |
| 03-binary | `epam/feat/ops.binary` | +1 rename fix after Unary review |
| 04-conv-pool | `epam/feat/ops.conv` | +1 rename fix |
| 05-random | `epam/feat/ops.random` | +1 rename fix |
| 06-reduction | `epam/feat/ops.reduction` | +1 rename fix |
| 07-pypi | _(packaging only)_ | From `release/auditwheel-exclude` proven fixes |

## shutovilyaep PR #1 status

- Existing PR: https://github.com/shutovilyaep/pytorch2.0_ttnn/pull/1
- Head should remain **`{base}`** (`fix/tt_metal_bump`).
- Update title/body from `PR_BODY.md` on `fix/tt_metal_bump.dev` (copy-paste).

## What to create manually (other machine)

PR #2-#7 in shutovilyaep using `public/*` heads and `.dev` branch `PR_BODY.md` texts.

## Regenerate provenance

```bash
python3 tools/gen_public_transfer_provenance.py --all-provenance > docs/public_transfer/provenance_index.md
python3 tools/gen_public_transfer_provenance.py --pr-body 02-unary > /tmp/pr_body.md
```
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pr-body", metavar="SLUG", help="Write PR body markdown for slug (e.g. 02-unary)")
    parser.add_argument("--provenance", metavar="SLUG", help="Write provenance section for slug")
    parser.add_argument("--all-provenance", action="store_true", help="Write provenance index for all PRs")
    parser.add_argument("--assessment", action="store_true", help="Write ASSESSMENT_ru.md content")
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write outputs under docs/public_transfer/ (assessment, pr_bodies, provenance_index)",
    )
    args = parser.parse_args()

    by_slug = {e.slug: e for e in STACK}

    if args.assessment or args.write:
        text = render_assessment()
        if args.assessment:
            print(text)
        if args.write:
            out = ROOT / "docs/public_transfer/ASSESSMENT_ru.md"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(text, encoding="utf-8")
            print(f"Wrote {out}", file=sys.stderr)

    if args.pr_body:
        entry = by_slug.get(args.pr_body)
        if not entry:
            print(f"Unknown slug: {args.pr_body}", file=sys.stderr)
            return 1
        body = render_pr_body(entry)
        if args.write:
            path = ROOT / "docs/public_transfer/pr_bodies" / f"{args.pr_body}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(body, encoding="utf-8")
            print(f"Wrote {path}", file=sys.stderr)
        else:
            print(body)

    if args.provenance:
        entry = by_slug.get(args.provenance)
        if not entry:
            print(f"Unknown slug: {args.provenance}", file=sys.stderr)
            return 1
        print(render_provenance_section(entry))

    if args.all_provenance or (args.write and not args.pr_body and not args.assessment):
        sections = ["# Provenance index\n"]
        for entry in STACK:
            sections.append(render_provenance_section(entry))
        text = "\n".join(sections)
        if args.all_provenance:
            print(text)
        if args.write:
            out = ROOT / "docs/public_transfer/provenance_index.md"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(text, encoding="utf-8")
            print(f"Wrote {out}", file=sys.stderr)
            for entry in STACK:
                body_path = ROOT / "docs/public_transfer/pr_bodies" / f"{entry.slug}.md"
                body_path.parent.mkdir(parents=True, exist_ok=True)
                body_path.write_text(render_pr_body(entry), encoding="utf-8")
            print(f"Wrote pr_bodies/*.md", file=sys.stderr)

    if not any([args.pr_body, args.provenance, args.all_provenance, args.assessment, args.write]):
        parser.print_help()
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
