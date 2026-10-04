# FintechResearchAgents

A planned Python agent platform for researching fintech opportunities in Nigeria, comparing their viability, supporting real customer validation, and carrying a selected opportunity through product planning, technical design, implementation, testing, pilot, and launch.

The platform will help a founder make evidence-based decisions. It will distinguish desk research from customer evidence and keep consequential decisions under human review.

## Current status

Documentation foundation only. No application, agents, dependencies, or runtime commands have been implemented.

## Documentation

- [Working instructions](AGENTS.md): scope, incremental workflow, and evidence practices.
- [Product specification](docs/product-specification.md): purpose, intended capabilities, outputs, and success criteria.
- [Implementation plan](docs/implementation.md): proposed stages, dependencies, and review gates.
- [Founder brief](docs/founder-brief.md): accepted inputs and deferred decisions.
- [Architecture design](docs/architecture.md): FRA-003 contracts, handoffs, gates, persistence, permissions and recovery; runtime implementation remains planned.

## Getting started

1. Read `AGENTS.md`, then the product specification and implementation plan before each task.
2. Review the confirmed founder inputs and dated deferrals in the founder brief.
3. Authorise a specific next task before implementation begins.

Keep credentials and private customer records outside the repository. The roadmap describes future work; it does not authorise execution.

## Next task

The founder accepted corrected FRA-001 and FRA-002's recorded inputs and deferrals on 2026-10-01. The corrected FRA-003 documentation-only design was accepted by the founder on 2026-10-04. Documentation checks passed; no runtime has been implemented or tested. Acceptance, implementation, verification and Git status are separate; Git history establishes inclusion in the authorised first documentation commit.

Proposed next task: FRA-004 minimal Python CLI scaffold, with FRA-003 acceptance complete but FRA-004 unstarted and still requiring explicit authorisation, local environment/current compatibility verification and founder approval of exact Python, packaging, CLI/configuration and test-tool choices. Installation requires separate permission if needed. Deferred founder inputs remain blockers at the applicable live research, selection, validation or delivery gates.

The initial direction is a Python-first local CLI, SQLite persistence and provider adapters. A dashboard and production infrastructure belong to later stages. The eventual fintech product has not been selected.

The FRA-001 correction defines role handoffs and human acceptance, blocks advancement on missing mandatory criteria/evidence or unreviewed potentially critical gaps, and requires separately authorised, successful provider integration verification (FRA-023) before live research (FRA-012). Concrete adapters remain planned under FRA-007. A synthetic demo does not establish live readiness. FRA-004 through FRA-023 remain planned and unauthorised.

The confirmed team is one developer, the founder, using Codex assistance. That assistance establishes neither additional human review nor development capacity. Exact Python version, libraries and providers remain proposals pending verification/approval. Paid calls remain blocked until spending limits and explicit authority are approved; recruitment requires an actual approved customer access plan.
