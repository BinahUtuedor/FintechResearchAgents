# FintechResearchAgents

A planned Python agent platform for researching fintech opportunities in Nigeria, comparing their viability, supporting real customer validation, and carrying a selected opportunity through product planning, technical design, implementation, testing, pilot, and launch.

The platform will help a founder make evidence-based decisions. It will distinguish desk research from customer evidence and keep consequential decisions under human review.

## Current status

The documentation foundation and FRA-004 minimal local CLI scaffold are implemented; FRA-004 is verified and founder-accepted. There are no research agents, persistence, orchestration, provider adapters, or live capabilities.

## Documentation

- [Working instructions](AGENTS.md): scope, incremental workflow, and evidence practices.
- [Product specification](docs/product-specification.md): purpose, intended capabilities, outputs, and success criteria.
- [Implementation plan](docs/implementation.md): proposed stages, dependencies, and review gates.
- [Founder brief](docs/founder-brief.md): accepted inputs and deferred decisions.
- [Architecture design](docs/architecture.md): FRA-003 contracts, handoffs, gates, persistence, permissions and recovery; runtime implementation remains planned.

## Getting started

Use the verified local CPython 3.14.7 interpreter from the repository root (PowerShell):

```powershell
$python = 'C:\Python314\python.exe'
$env:PYTHONDONTWRITEBYTECODE = '1'
& $python -m fintech_research_agents --help
& $python -m fintech_research_agents --version
& $python -m fintech_research_agents validate-config .\config.example.toml
& $python -m unittest discover -s tests -v
```

Validation prints `Configuration valid.` and exits 0 on success. Invalid commands or configurations produce a sanitised diagnostic and exit 2. The only supported configuration is the exact pair `schema_version = 1` and `mode = "demo"`; see [config.example.toml](config.example.toml).

This scaffold validates local TOML only. It creates no database or research artifacts and does not provide persistence, orchestration, research roles, AI/search adapters, live research, or financial operations. Configuration validation is not product or regulatory approval.

Keep credentials and private customer records outside the repository. The roadmap describes future work; it does not authorise execution.

## Next task

The founder accepted corrected FRA-001 and FRA-002's recorded inputs and deferrals on 2026-10-01. The corrected FRA-003 documentation-only design was accepted by the founder on 2026-10-04. Documentation checks passed. The FRA-004 scaffold is implemented and its runtime checks are recorded in the implementation plan. Acceptance, implementation, verification and Git status are separate; Git history establishes inclusion in the authorised first documentation commit.

FRA-004 is implemented, verified and founder-accepted. No installation or third-party dependency was needed. Proposed next task: separately authorised FRA-005 persistence. FRA-005 and later runtime work remain planned and require separate authorisation. Deferred founder inputs remain blockers at the applicable live research, selection, validation or delivery gates.

The initial direction is a Python-first local CLI, SQLite persistence and provider adapters. A dashboard and production infrastructure belong to later stages. The eventual fintech product has not been selected.

The FRA-001 correction defines role handoffs and human acceptance, blocks advancement on missing mandatory criteria/evidence or unreviewed potentially critical gaps, and requires separately authorised, successful provider integration verification (FRA-023) before live research (FRA-012). Concrete adapters remain planned under FRA-007. A synthetic demo does not establish live readiness. FRA-005 through FRA-023 remain planned and unauthorised.

The confirmed team is one developer, the founder, using Codex assistance. That assistance establishes neither additional human review nor development capacity. Python 3.14.7, standard-library argparse/tomllib/dataclasses/unittest, and one repository-root package were approved for FRA-004; later libraries and providers remain unselected. Paid calls remain blocked until spending limits and explicit authority are approved; recruitment requires an actual approved customer access plan.
