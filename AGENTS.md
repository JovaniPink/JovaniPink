# AGENTS.md

## Purpose

This is Jovani Pink's GitHub profile repository. The README is the product: it
should be concise, current, evidence-safe, and useful to people evaluating the
work without requiring them to interpret a long historical project dump.

## Canonical commands

```sh
python3 -m unittest discover -s tests -v
python3 scripts/validate_readme.py README.md
```

The validator uses only the Python standard library and supports Python 3.11 or
newer.

## README contract

- Keep one `# Jovani Pink` heading.
- Keep the level-two sections in the order enforced by the validator.
- Use descriptive Markdown links and HTTPS for external destinations.
- Link GitHub repositories through canonical `github.com/JovaniPink/<repo>`
  URLs.
- Do not restore numbered coursework dumps, decorative bullet characters,
  placeholder checklists, or repeated project links.
- Keep current work separate from selected examples and general capabilities.
- Verify new external links manually before merging.

## Evidence boundary

A passing validator proves local structure, syntax, link uniqueness, canonical
GitHub paths, and relative-file existence. It does not prove that a remote page
responds, that a project is currently maintained, or that a description remains
accurate. Those claims require a fresh source or live review.
