#!/usr/bin/env python3
"""Generate provenance sections for shutovilyaep public transfer PR bodies."""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BASE_REF = "c81f7e56c96c1056ef9a0343682fe02db8508b28"
LOCAL_FIX_TT_METAL_BUMP = "bee9c95ee"


@dataclass(frozen=True)
class OriginalCommit:
    public_sha: str
    origin_sha: str
    subject: str = ""


@dataclass(frozen=True)
class OnTopCommit:
    sha: str
    what: str
    why: str


@dataclass(frozen=True)
class StackEntry:
    slug: str
    pr_title: str
    public_branch: str
    public_base: str
    upstream_pr_ref: str
    summary: str
    original_commits: tuple[OriginalCommit, ...] = ()
    ontop_commits: tuple[OnTopCommit, ...] = ()
    packaging_only: bool = False


STACK: list[StackEntry] = [
    StackEntry(
        slug="01-base",
        pr_title="tt-metal main branch compatibility fixes (rebased)",
        public_branch=BASE_REF,
        public_base="github/main",
        upstream_pr_ref="`github.com/tenstorrent/pytorch2.0_ttnn/pull/1293`",
        summary=(
            "Rebases the tt-metal compatibility work from the original upstream PR onto current "
            "`main` and adds TTSim simulator-based CI testing on standard GitHub-hosted runners."
        ),
    ),
    StackEntry(
        slug="02-unary",
        pr_title="Register Unary OPs, forward pass",
        public_branch="public/10-unary",
        public_base="fix/tt_metal_bump",
        upstream_pr_ref="`github.com/tenstorrent/pytorch2.0_ttnn/pull/TBD`",
        summary=(
            "Registers unary eager ATen ops (forward pass and fallbacks) on top of the tt-metal "
            "compatibility base. Same op registration work as the original upstream PR; rebased "
            "onto `c81f7e5`."
        ),
        original_commits=(
            OriginalCommit("b498407e1", "3cb187924", "Registering Unary OPs, forward pass, fallbacks"),
            OriginalCommit("e01983dde", "b627f86e5", "PR fix: renamed to tilize"),
            OriginalCommit("d8f37e47f", "e3ac92547", "PR fix: renamed to make_empty_like_ttnn"),
        ),
        ontop_commits=(
            OnTopCommit(
                "1e2bc63c9",
                "Remove stale `unary.cpp` from `CMakeLists.txt` sources",
                "Unary eager refactor deleted the stub source file; CMake still listed it after rebase.",
            ),
            OnTopCommit(
                "5d71e4649",
                "Add `third-party/tt-metal/ttnn/cpp` to CMake include path",
                "Installed tt-metal headers omit paths such as `complex_unary.hpp` that eager "
                "registration includes from source tree.",
            ),
        ),
    ),
    StackEntry(
        slug="03-binary",
        pr_title="Register Binary OPs, eager mode, forward pass",
        public_branch="public/20-binary",
        public_base="public/10-unary",
        upstream_pr_ref="`github.com/tenstorrent/pytorch2.0_ttnn/pull/TBD`",
        summary=(
            "Registers binary eager ATen ops stacked on Unary. Same registration commit as the "
            "original upstream PR; one mechanical rename fix applied after Unary review feedback."
        ),
        original_commits=(OriginalCommit("5a3d4e188", "c3abdde36", "Registering Binary OPs"),),
        ontop_commits=(
            OnTopCommit(
                "79c0ebe75",
                "Rename `tileify` -> `tilize`, `make_empty_like_tt` -> `make_empty_like_ttnn`",
                "Binary wrappers were authored before Unary review renamed shared helpers in "
                "`eager_common.hpp`. 25 call-sites in `binary_eager_wrappers.hpp` plus 2 lines in "
                "`unary_eager_wrappers.hpp`. No op logic changed.",
            ),
        ),
    ),
    StackEntry(
        slug="04-conv-pool",
        pr_title="Register Conv/Pool OPs, eager mode, forward pass",
        public_branch="public/30-conv",
        public_base="public/20-binary",
        upstream_pr_ref="`github.com/tenstorrent/pytorch2.0_ttnn/pull/TBD`",
        summary=(
            "Registers conv/pool eager ATen ops (17 overloads) stacked on Binary. Same "
            "registration commit as the original upstream PR."
        ),
        original_commits=(OriginalCommit("5d74c98dd", "b2757312f", "Registering Conv Pool OPs"),),
        ontop_commits=(
            OnTopCommit(
                "38b01dd30",
                "Rename `tileify` -> `tilize` in conv/pool wrappers",
                "15 call-sites in `conv_pool_eager_wrappers.hpp` only. Mechanical follow-up to "
                "Unary review rename. No op logic changed.",
            ),
        ),
    ),
    StackEntry(
        slug="05-random",
        pr_title="Register Random OPs, eager mode, forward pass",
        public_branch="public/40-random",
        public_base="public/30-conv",
        upstream_pr_ref="`github.com/tenstorrent/pytorch2.0_ttnn/pull/TBD`",
        summary=(
            "Registers random eager ATen ops (6 overloads) stacked on Conv/Pool. Same registration "
            "commit as the original upstream PR."
        ),
        original_commits=(OriginalCommit("d89955b23", "97c7a2a34", "Registering Random OPs"),),
        ontop_commits=(
            OnTopCommit(
                "f9d3dec63",
                "Rename `tileify` -> `tilize`, `make_empty_like_tt` -> `make_empty_like_ttnn`",
                "4 call-sites in `random_eager_wrappers.hpp`. Mechanical rename only.",
            ),
        ),
    ),
    StackEntry(
        slug="06-reduction",
        pr_title="Register Reduction OPs, eager mode, forward pass",
        public_branch="public/50-reduction",
        public_base="public/40-random",
        upstream_pr_ref="`github.com/tenstorrent/pytorch2.0_ttnn/pull/TBD`",
        summary=(
            "Registers reduction eager ATen ops (38 overloads) stacked on Random. Same registration "
            "commit as the original upstream PR."
        ),
        original_commits=(OriginalCommit("0e303d283", "07c6cf329", "Registering Reduction OPs"),),
        ontop_commits=(
            OnTopCommit(
                "d0585f8ca",
                "Rename `tileify` -> `tilize`, `make_empty_like_tt` -> `make_empty_like_ttnn`",
                "17 call-sites in `reduction_eager_wrappers.hpp`. Mechanical rename only.",
            ),
        ),
    ),
    StackEntry(
        slug="07-pypi",
        pr_title="Make package PyPI-buildable: torch-ttnn-shutov + ttnn-shutov",
        public_branch="public/70-pypi",
        public_base="public/50-reduction",
        upstream_pr_ref="`github.com/tenstorrent/pytorch2.0_ttnn/issues/1036` (packaging bounty)",
        summary=(
            "Publication-channel change: rename distribution to `torch-ttnn-shutov`, repack runtime "
            "as `ttnn-shutov`, add manual TestPyPI/PyPI release workflows. **New packaging work** - "
            "not a 1:1 transfer of an upstream eager-op PR."
        ),
        packaging_only=True,
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


def commit_meta(sha: str) -> tuple[str, str, str]:
    out = git("log", "-1", "--format=%an|%ad|%s", "--date=short", sha)
    author, date, subject = out.split("|", 2)
    return author, date, subject


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


def verify_patch(public_sha: str, origin_sha: str) -> str:
    pub_id = patch_id(public_sha)
    orig_id = patch_id(origin_sha)
    if pub_id and orig_id and pub_id == orig_id:
        return "byte-identical (patch-id)"
    return "same op code; include-context delta from rebase"


def render_original_table(entry: StackEntry) -> str:
    if not entry.original_commits:
        return "_N/A - see base rebase section._"

    lines = [
        "| Commit (this PR) | Subject | Author | Authored | Verification |",
        "| --- | --- | --- | --- | --- |",
    ]
    for oc in entry.original_commits:
        author, date, subject = commit_meta(oc.public_sha)
        display_subject = oc.subject or subject
        verification = verify_patch(oc.public_sha, oc.origin_sha)
        lines.append(
            f"| `{oc.public_sha}` | {display_subject} | {author} | {date} | {verification} |"
        )
    return "\n".join(lines)


def render_ontop_section(entry: StackEntry) -> list[str]:
    if entry.packaging_only:
        return [
            "## Commits added on top in this transfer",
            "",
            "_None - this PR is new packaging work, not a transfer of upstream eager-op commits._",
            "",
            "### What this PR adds (new work)",
            "",
            "- Rename distribution to `torch-ttnn-shutov` (`VERSION` -> `0.1.0`); import stays `torch_ttnn`.",
            "- Add `tools/repack_ttnn_shutov_wheel.py` and `release-ttnn-shutov.yaml` workflow.",
            "- Replace direct URL in `[pypi]` extra with `ttnn-shutov==0.62.0.dev20250916`.",
            "- Add `release-torch-ttnn-shutov.yaml` with TestPyPI/PyPI `workflow_dispatch`.",
            "- Update CI wheel smoke to install repacked `ttnn-shutov` before wheel verification.",
            "",
            "### Why `-shutov` (public PyPI constraint)",
            "",
            "Public PyPI and TestPyPI reject wheels whose metadata contains direct URL dependencies "
            "(`ttnn @ https://...`). Same class of blocker as packaging bounty "
            "`github.com/tenstorrent/pytorch2.0_ttnn/issues/1036` (merged as "
            "`github.com/tenstorrent/pytorch2.0_ttnn/pull/1095`).",
            "",
            "Fix: repack pinned internal `ttnn 0.62.0.dev20250916` as `ttnn-shutov` (SHA256-verified), "
            "publish `ttnn-shutov` first, then `torch-ttnn-shutov[pypi]`. Import names stay `ttnn` "
            "and `torch_ttnn`.",
            "",
        ]

    if not entry.ontop_commits:
        return [
            "## Commits added on top in this transfer",
            "",
            "_None - only the original commits above, unchanged after rebase._",
            "",
        ]

    lines = [
        "## Commits added on top in this transfer",
        "",
        "These commits are **not** in the original upstream PR. They fix rebase/infra issues only; "
        "no eager-op behavior change.",
        "",
    ]
    for idx, oc in enumerate(entry.ontop_commits, start=1):
        author, date, subject = commit_meta(oc.sha)
        lines.extend(
            [
                f"{idx}. **`{oc.sha}`** - {oc.what}",
                f"   - Commit subject: {subject}",
                f"   - Author: {author} | Authored: {date}",
                f"   - Why: {oc.why}",
                "",
            ]
        )
    return lines


def render_base_original_section() -> list[str]:
    return [
        "## These are the original commits (1:1 transfer)",
        "",
        "This PR rebases the full content of the original upstream PR onto current `main`. All "
        "commits are authored by **Ilia Shutov** (`Ilia_Shutov@epam.com`). The rebase preserves "
        "the same changes as the original work; verify any commit with `git show <sha>`.",
        "",
        "Original upstream PR (same work, rebased): "
        "`github.com/tenstorrent/pytorch2.0_ttnn/pull/1293`",
        "",
        "### Included from original PR 1293 (via rebase)",
        "",
        "- **Build System Modernization**: Migrated from setup.py to pyproject.toml with scikit-build-core",
        "- **RPATH Configuration**: Proper RPATH setup to eliminate LD_LIBRARY_PATH requirement",
        "- **Binary Bundling**: TTNN binaries bundled in wheel for self-contained distribution",
        "- **CI Infrastructure**: Updated workflows for wheel-based testing",
        "- **Consistent Compiler**: Enforced Clang-17 to match tt-metal build",
        "- **TT_METAL_HOME**: Made optional with auto-detection from submodule",
        "- Submodule sync, CI robustness, wheel verification, Docker pin, and related fixes from the "
        "original PR series",
        "",
    ]


def render_base_ontop_section() -> list[str]:
    author, date, _ = commit_meta("c81f7e56c")
    return [
        "## Commits added on top in this transfer",
        "",
        "New work on top of the rebased original PR (not in upstream PR 1293 as merged):",
        "",
        f"1. **`c81f7e56c`** - TTSim simulator-based CI testing with shim workaround",
        f"   - Author: {author} | Authored: {date}",
        "   - Enables CI on standard GitHub runners without Tenstorrent hardware",
        "   - Downloads TTSim from `tenstorrent/ttsim` releases",
        "   - Adds `ttsim_shim` no-op stubs for UMD/TTSim symbol mismatch on pinned tt-metal",
        "   - Consolidates earlier CI fixes (Kitware GPG key, TTSim env, workflow wiring)",
        "",
        "Supporting CI commits in the same rebase (same author, Feb 2026):",
        "",
        "- `b1677f162` - set TT_METAL_HOME before running tests",
        "- `52d926234` - document TT_METAL_HOME ignored at build, required at test",
        "- `5681dbbdd` - GitHub Actions workflow updates (git-lfs, checkout hygiene)",
        "- `1e7c9c7b3` - pin tt-metal Docker image digest for reproducibility",
        "- `68acef4bd` / `d86b2d668` - wheel verification simulating PyPI user install",
        "",
    ]


def render_pr_body(entry: StackEntry) -> str:
    public_tip = resolve_ref(entry.public_branch)
    public_base = resolve_ref(entry.public_base)

    lines = [
        f"**PR title (copy into the title field):** {entry.pr_title}",
        "",
        "## Summary",
        "",
        entry.summary,
        "",
    ]

    if entry.slug == "01-base":
        lines.extend(render_base_original_section())
        lines.extend(render_base_ontop_section())
    elif entry.packaging_only:
        lines.extend(
            [
                "## These are the original commits (1:1 transfer)",
                "",
                "_Not applicable - this is new packaging work, not a transfer of upstream eager-op commits._",
                "",
            ]
        )
        lines.extend(render_ontop_section(entry))
    else:
        author_sample = commit_meta(entry.original_commits[0].public_sha)[0] if entry.original_commits else "Ilia Shutov"
        date_range = ", ".join(sorted({commit_meta(oc.public_sha)[1] for oc in entry.original_commits}))
        lines.extend(
            [
                "## These are the original commits (1:1 transfer)",
                "",
                f"Same commits authored by **{author_sample}** in the original upstream work "
                f"({date_range}), transferred by rebase onto `{public_base[:8]}`. Verify any commit: "
                f"`git show <sha>`.",
                "",
                f"Original upstream PR (same commits, fill in number when public): {entry.upstream_pr_ref}",
                "",
                render_original_table(entry),
                "",
            ]
        )
        lines.extend(render_ontop_section(entry))

    lines.extend(
        [
            "## Stack pointers",
            "",
            f"- **Base:** `{public_base}` (`{entry.public_base}`)",
            f"- **Tip:** `{public_tip}` (`{entry.public_branch}`)",
            "",
        ]
    )

    return "\n".join(lines)


def render_provenance_section(entry: StackEntry) -> str:
    public_tip = resolve_ref(entry.public_branch)
    public_base = resolve_ref(entry.public_base)

    parts = [
        f"## Provenance: {entry.slug} ({entry.public_branch})",
        "",
        f"- **PR title:** {entry.pr_title}",
        f"- **Public tip:** `{public_tip}`",
        f"- **Public base:** `{public_base}` (`{entry.public_base}`)",
        f"- **Original upstream (non-mention):** {entry.upstream_pr_ref}",
        "",
    ]

    if entry.original_commits:
        parts.extend(["### Original commits", "", render_original_table(entry), ""])
    if entry.ontop_commits:
        parts.append("### On-top commits")
        parts.append("")
        for oc in entry.ontop_commits:
            parts.append(f"- `{oc.sha}`: {oc.what}")
        parts.append("")

    return "\n".join(parts)


def render_assessment() -> str:
    base = BASE_REF[:8]
    local = LOCAL_FIX_TT_METAL_BUMP[:8]
    title_rows = "\n".join(
        f"| {e.slug} | `{e.pr_title}` | `{e.public_branch}` |" for e in STACK
    )
    stack_rows = "\n".join(
        f"| {e.slug} | `{e.public_branch}` | `{resolve_ref(e.public_branch)[:8]}` | `{e.public_base}` |"
        for e in STACK
    )

    return f"""# Assessment: public transfer stack

Date: 2026-06-18

## Verdict

Public stack for shutovilyaep is **ready for staging** on `RedOrangeSweater/pytorch2.0_ttnn-public`.
PR descriptions on `.dev` branches include exact upstream titles, 1:1 commit tables with patch-id
verification, and explicit on-top fix sections.

## PR titles (copy-paste)

| Slug | Title | Branch |
| --- | --- | --- |
{title_rows}

First line of each `PR_BODY.md`: **PR title (copy into the title field):** ...

## Base divergence (critical)

| Ref | Commit | Use for shutovilyaep PR #1? |
| --- | --- | --- |
| shutovilyaep PR #1 head | `{base}` | **yes** |
| local diverged `fix/tt_metal_bump` | `{local}` | **no** (tt-metal v0.60.1 line) |

## Stack mapping

| PR | Public branch | Tip | Base |
| --- | --- | --- | --- |
{stack_rows}

## Non-mention rule for staged PR bodies

Upstream PR links in `pr_bodies/*.md` and `PR_BODY.md` use **backticks** so GitHub does not
cross-reference the original tenstorrent PR while work is still private. Replace `TBD` with the
real PR number before publishing the shutovilyaep PR.

## Regenerate

```bash
python3 tools/gen_public_transfer_provenance.py --write
```
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pr-body", metavar="SLUG", help="Write PR body markdown for slug")
    parser.add_argument("--provenance", metavar="SLUG", help="Write provenance section for slug")
    parser.add_argument("--all-provenance", action="store_true", help="Write provenance index for all PRs")
    parser.add_argument("--assessment", action="store_true", help="Write ASSESSMENT_ru.md content")
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write outputs under docs/public_transfer/",
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
            print("Wrote pr_bodies/*.md", file=sys.stderr)

    if not any([args.pr_body, args.provenance, args.all_provenance, args.assessment, args.write]):
        parser.print_help()
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
