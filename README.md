# Jovani Pink

> Enterprise AI Architect | Data-Intensive Workflows

I architect and build data-intensive AI workflows that teams can operate,
evaluate, and decide to scale. My work closes the gap between a working demo and
a dependable production system by making source authority, human review,
failure handling, observability, and release evidence explicit.

[Portfolio](https://jovanipink.com) |
[Project catalog](https://jovanipink.com/projects) |
[Public evidence standard](https://jovanipink.com/evidence)

## About

I work with teams in regulated and data-intensive environments where a wrong,
late, or unsupported result has an operational cost. I connect data and platform
architecture, AI and agent behavior, workflow state, evaluation, and product
delivery so the system can be trusted by the people responsible for running it.

My primary tools include Google Cloud, BigQuery, Snowflake, Azure, SQL, Python,
TypeScript, and Go. I approach architecture as a product and operating
discipline: technical choices should support a defined business decision, the
people accountable for it, and a maintainable path through production.

## Current work

- [Measured Studios](https://measuredstudios.com) is my independent consulting
  studio. A two-week AI Workflow Value and Readiness Sprint tests whether one
  high-value workflow justifies a production pilot. A six-to-ten-week Governed
  AI Production Pilot implements the approved slice inside the client's
  environment.
- [Rehearsal](https://jovanipink.com/posts/simulation-is-not-evidence-rehearsing-consequential-decisions)
  is a private-source research prototype with two synthetic workflow scenarios
  and a shared deterministic kernel. It generates inspectable hypotheses; it
  does not establish customer adoption, external calibration, or real-world
  outcomes.
- [Mainland Dispatch](https://github.com/JovaniPink/Mainland-Dispatch) is a
  separate public research lane for contextual China and U.S.-China coverage.
  It is evidence of research method, not consulting delivery or customer impact.

The public project catalog keeps project type, evidence context, maturity,
evidence level, confidentiality, business model, distribution mode, and runtime
state separate. Repository activity, deployment, commercial intent, and customer
outcomes are not treated as interchangeable proof.

## Selected projects

| Project | Focus |
| --- | --- |
| [JovaniPink Skills](https://github.com/JovaniPink/skills) | Portable agent skills with provenance, security boundaries, trigger evaluation, validation, and cross-client packaging. |
| [MCP Browser Use](https://github.com/JovaniPink/mcp-browser-use) | Testable FastAPI and Model Context Protocol boundary for browser-agent orchestration, limits, cleanup, and secret redaction. |
| [Data Playbook](https://github.com/JovaniPink/data-playbook) | Google Cloud data-engineering patterns, including a create-only archive publisher with hashes, generation preconditions, and completion manifests. |
| [xstate-python](https://github.com/JovaniPink/xstate-python) | Hierarchical Python statecharts with XState/Stately JSON compatibility and SCXML-oriented semantics. |
| [Earthquake Atlas](https://github.com/JovaniPink/mapping-earthquakes) | Public MapLibre source for filtering and inspecting recent USGS observations with source-linked details. Its prior public deployment returned 404 on August 30, 2026, so no live runtime is claimed. |

[Browse all repositories](https://github.com/JovaniPink?tab=repositories).

## Core capabilities

- Enterprise AI workflow architecture and implementation
- Data authority, platform integration, and state ownership
- Agent evaluation, human review, and escalation design
- API, event, and state-machine contracts
- Production observability, security, release, and cost controls
- Technical strategy translated into testable product and operating decisions

## Engineering principles

- Prefer evidence over implied readiness: source, tests, CI, deployment, and
  live behavior are separate claims.
- Make contracts executable at system boundaries through schemas, validation,
  tests, and observable failure modes.
- Keep changes reproducible, dependency-aware, and small enough to review
  without losing the larger architecture.
- Build tools around the teams and decisions they serve, not around technology
  for its own sake.

## Validation

This profile repository has no runtime dependencies. Its standard-library
validator protects the README structure, link syntax, canonical GitHub targets,
relative files, and duplicate-link contract.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_readme.py README.md
```

The validator does not claim that remote content is current or available.
External links and project descriptions still require manual review when they
change.

## License

This repository is available under the [MIT License](LICENSE).
