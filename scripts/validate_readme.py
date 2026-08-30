#!/usr/bin/env python3
"""Validate the profile README's local documentation contract."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


EXPECTED_TITLE = "Jovani Pink"
EXPECTED_SECTIONS = [
    "About",
    "Current work",
    "Selected projects",
    "Core capabilities",
    "Engineering principles",
    "Validation",
    "License",
]
MINIMUM_SECTION_LINKS = {
    "Current work": 2,
    "Selected projects": 3,
}
REQUIRED_LINKS = {
    "https://jovanipink.com",
    "https://jovanipink.com/projects",
    "https://measuredstudios.com",
    "LICENSE",
}
REQUIRED_POSITIONING = {
    "Enterprise AI Architect | Data-Intensive Workflows",
    "AI Workflow Value and Readiness Sprint",
    "Governed AI Production Pilot",
}

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\)")
NUMBERED_AUTOLINK_RE = re.compile(r"^-\s+\d+\s+<https?://", re.MULTILINE)


def _section_bodies(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.MULTILINE))
    bodies: dict[str, str] = {}
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        bodies[match.group(1)] = text[start:end]
    return bodies


def _validate_link(path: Path, label: str, target: str) -> list[str]:
    errors: list[str] = []
    if not label.strip():
        errors.append("Markdown links must have descriptive labels")

    if target.startswith("#"):
        return errors

    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        if parsed.scheme != "https":
            errors.append(f"External link must use HTTPS: {target}")
        if not parsed.netloc:
            errors.append(f"External link is missing a host: {target}")
        if parsed.netloc.lower() == "github.com":
            parts = [part for part in parsed.path.split("/") if part]
            if len(parts) >= 2 and parts[0].lower() == "jovanipink":
                canonical = f"https://github.com/JovaniPink/{parts[1]}"
                if target != canonical:
                    errors.append(
                        f"Use the canonical GitHub repository URL: {canonical}"
                    )
        return errors

    relative_target = unquote(target.split("#", 1)[0])
    if not relative_target:
        return errors

    root = path.parent.resolve()
    resolved = (root / relative_target).resolve()
    if resolved != root and root not in resolved.parents:
        errors.append(f"Relative link escapes the repository: {target}")
    elif not resolved.exists():
        errors.append(f"Relative link does not exist: {target}")
    return errors


def validate_readme(path: Path) -> list[str]:
    """Return all contract violations found in a profile README."""
    text = path.read_text(encoding="utf-8")
    normalized_text = " ".join(text.split())
    errors: list[str] = []

    headings = [(marks, title) for marks, title in HEADING_RE.findall(text)]
    h1_titles = [title for marks, title in headings if marks == "#"]
    if h1_titles != [EXPECTED_TITLE]:
        errors.append(f"Expected exactly one '# {EXPECTED_TITLE}' heading")

    level_two = [title for marks, title in headings if marks == "##"]
    if level_two != EXPECTED_SECTIONS:
        errors.append(
            "Level-two sections must be exactly: " + " -> ".join(EXPECTED_SECTIONS)
        )

    links = LINK_RE.findall(text)
    targets = [target for _, target in links]
    duplicate_targets = sorted(
        {target for target in targets if targets.count(target) > 1}
    )
    if duplicate_targets:
        errors.append("Duplicate link targets: " + ", ".join(duplicate_targets))

    missing_required = sorted(REQUIRED_LINKS.difference(targets))
    if missing_required:
        errors.append("Missing required links: " + ", ".join(missing_required))

    missing_positioning = sorted(
        phrase for phrase in REQUIRED_POSITIONING if phrase not in normalized_text
    )
    if missing_positioning:
        errors.append(
            "Missing required positioning: " + ", ".join(missing_positioning)
        )

    for label, target in links:
        errors.extend(_validate_link(path, label, target))

    section_bodies = _section_bodies(text)
    for section, minimum in MINIMUM_SECTION_LINKS.items():
        section_links = LINK_RE.findall(section_bodies.get(section, ""))
        if len(section_links) < minimum:
            errors.append(f"Section '{section}' must contain at least {minimum} links")

    if "\u25cf" in text:
        errors.append(
            "Use Markdown list markers instead of decorative bullet characters"
        )
    if NUMBERED_AUTOLINK_RE.search(text):
        errors.append(
            "Replace numbered autolink entries with descriptive Markdown links"
        )
    if "Lots of items" in text:
        errors.append("Remove placeholder checklist copy")
    if re.search(r"Earthquake Atlas[^\n]*\|\s*Live\s+MapLibre", text, re.IGNORECASE):
        errors.append(
            "Earthquake Atlas must not be labeled live without a current verified deployment"
        )

    return list(dict.fromkeys(errors))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("readme", nargs="?", default="README.md", type=Path)
    args = parser.parse_args(argv)

    errors = validate_readme(args.readme)
    if errors:
        print(f"{args.readme}: validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    link_count = len(LINK_RE.findall(args.readme.read_text(encoding="utf-8")))
    print(f"{args.readme}: OK ({link_count} unique links)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
