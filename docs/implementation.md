# Implementation plan

## Status and authorisation

FRA-001 is implemented and founder-accepted on 2026-10-01. FRA-002 is implemented and founder-accepted on 2026-10-01: the acceptance covers its recorded inputs and deferrals, not approval of technical proposals or downstream activities. The corrected FRA-003 documentation-only design is implemented, documentation-checked and founder-accepted on 2026-10-04. FRA-004 through FRA-023 remain planned and unauthorised. The founder authorised the first documentation commit on 2026-10-04; Git history establishes inclusion separately from acceptance. Implemented means the scoped artifacts exist; tested means specified checks actually ran with recorded results; committed means a Git commit exists. These are separate from founder acceptance. Documentation checks do not test a running platform.

Development sequence: **implement -> verify -> review/accept -> commit**. Review findings return to implementation and verification before acceptance. Acceptance and Git commit status remain separate; a commit requires explicit authorisation even after acceptance. Git history can establish which accepted documentation a commit includes; no additional documentation commit is required merely to insert that commit's own hash.

IDs are stable: do not renumber completed or deferred tasks. Dependencies express ordering, not permission. Before each task read this plan and the specification, inspect Git and relevant instructions, and obtain explicit authorisation for that task. Break broad conditional tasks into new stable IDs before implementation. Every lifecycle stage supports proceed, rework, pivot, defer and stop as defined in the specification.

## Decision register

The founder confirmed a one-developer team and founder-led development assisted by Codex on 2026-10-01. No skills, capacity, additional human reviewers or funding are inferred. The Python-first local CLI, initial SQLite and provider-adapter direction remains the existing founder direction. The implementation details below are proposals, not verified choices or permission to install or build.

| Decision | Current position / minimal proposal | Verification and approval point |
| --- | --- | --- |
| Runtime and packaging | Python; exact version and packaging tool unselected. Propose one local package and one process | Before FRA-004, verify supported Python versions, local environment and dependency compatibility; founder approves exact choices |
| CLI and configuration | Propose standard-library argparse and explicit local configuration; add a CLI framework only for a demonstrated need | Review fit in FRA-003; verify version-specific behaviour and approve before FRA-004 |
| Contracts and orchestration | Propose plain typed records, explicit validation and deterministic functions; defer an agent framework or workflow service | FRA-003 documents contracts and state-machine design in architecture.md, founder-accepted on 2026-10-04; no runtime schemas or implementation delivered |
| Persistence and artifacts | Initial SQLite per founder direction; propose sqlite3 access and local JSON/Markdown artifacts, without an ORM initially | FRA-003 reviews transaction/recovery needs; verify runtime compatibility and approve tooling before FRA-005 |
| Testing and economics | Propose unittest, controlled fake adapters and decimal-based deterministic calculations; evaluate pytest only if useful | Verify suitability and approve test tooling before FRA-004; define numeric policy in the relevant later task |
| AI/search integration | Providers, models, SDKs and pricing unselected. Propose provider-neutral interfaces first, then only the concrete adapters needed for an approved run | Before FRA-007, compare candidate providers against required capabilities, provenance, privacy, errors and cost controls using current primary documentation; obtain founder approval. Successful separately authorised FRA-023 verification precedes FRA-012 |
| Usage limits and spend authority | Founder explicitly deferred spending limits on 2026-10-01. Propose live access blocked by default; no numeric allowance inferred | Founder approves applicable call/token/spend limits before live activity; paid calls require approved spending limits and explicit authorisation |
| Fintech opportunity and product stack | No opportunity selected; no product-stack proposal justified yet | Founder selection in FRA-013 after relevant deferrals are resolved; product-specific design in FRA-017 |
| Dashboard and infrastructure | Propose no dashboard, service deployment, queue or production infrastructure in the initial local platform | Revisit only through later separately scoped and authorised tasks |

These proposals minimise moving parts for a solo developer; they are not claims about current library versions, pricing or provider support. No external technical verification, package installation or live integration ran in FRA-002. Technical names above are candidates to evaluate, not approved dependencies.

## Constraints and stage-specific blockers

The dated deferral register, impacts, owners and resolution points are in [the founder brief](founder-brief.md). The founder owns all deferred inputs. Deferral records preserve unknowns; they do not waive evidence or approval gates.

| Work / gate | Applicable prerequisite or blocker | Effect on offline design |
| --- | --- | --- |
| FRA-003 provider-neutral offline design | FRA-002 founder acceptance and explicit FRA-003 documentation-only authorisation, both recorded 2026-10-01; retain the documented scope and gates | Prerequisites satisfied. Budget, availability, access, locality, timing, risk appetite and provider choice remain parameters or later-stage requirements |
| FRA-004 runnable scaffold | Reviewed FRA-003 design and verified/approved Python and tooling choices; separate installation permission if needed | Runtime decisions can remain proposals during FRA-003 |
| FRA-007 concrete adapters | Approved provider/capability choices and limit-control policy; offline tests use synthetic limits, never spending authority | Provider-neutral contracts do not require a provider selection; actual live limits remain a later prerequisite |
| FRA-023 live verification / FRA-012 live research | Approved activity scope and usage limits, valid selected-provider configuration, explicit authorisation; FRA-012 also requires successful matching FRA-023 records and FRA-011 | Offline design and demos establish no live readiness. Paid calls are blocked until spending limits are approved and paid calls explicitly authorised |
| FRA-013 opportunity selection | Research evidence and reviewed comparison criteria; resource envelope, availability, timing and regulatory appetite resolved sufficiently to assess fit; locality and access feasibility assessed where material | Generic opportunity/evidence contracts may be designed without choosing a concept. Unreviewed potentially critical gaps still block selection |
| FRA-014 customer recruitment and validation | Actual founder-approved access/recruitment plan, channels, participant access method, permissions and consent protocol; explicit contact/validation authorisation | Protocol and evidence-record design can proceed offline; simulated participants establish neither access nor validation |
| FRA-015 feasibility / FRA-016 product definition | Real customer evidence, applicable location/regulatory facts and resolved critical commercial dependencies | These product decisions do not block platform contract design |
| FRA-018 implementation / FRA-020 pilot / FRA-021 launch | Approved product design, resource and schedule commitments, actual review owners and any required qualified reviewers, participant/operating permissions, readiness evidence and founder gates | One founder may fill several roles with self-review disclosed. Codex is not an extra human reviewer or evidence of capacity; qualified/independent human review cannot be assumed available |

Research remains bounded to Nigeria with no preselected concept. Proposed comparison dimensions and evidence rules are in the founder brief; weights, thresholds and execution scope require review before the applicable live research/selection gate. Undefined mandatory exit criteria block that gate, not unrelated provider-neutral design. FRA-003 must represent these blockers without resolving product decisions or performing live work.

## Early platform tasks

### FRA-001 — Documentation foundation

- Purpose: establish scope, evidence standards and incremental delivery rules.
- Scope: AGENTS.md, README.md, product specification, implementation plan, founder brief and .gitignore; preserve existing guidance.
- Dependencies: none.
- Acceptance criteria: distinguish platform/product; define lifecycle, roles, gates, provenance, limits and recovery; leave unknown founder inputs explicit; no application code or live research.
- Verification: inspect all six files, local links, task fields and dependency ordering; run Git whitespace checks including untracked files; verify ignore examples and unstaged status.
- Status: implemented; corrected foundation explicitly accepted by the founder on 2026-10-01. Documentation checks passed; no runtime tested. Founder acceptance is separate from Git inclusion, established by Git history.

### FRA-002 — Founder constraints and platform decision review

- Purpose: make constraints and unresolved decisions explicit before design.
- Scope: collect founder brief answers or dated deferrals; define research boundaries, review criteria and proposed usage limits; document Python/library/provider options and what needs current verification. Do not preselect a fintech concept.
- Dependencies: FRA-001 and founder review of the foundation.
- Acceptance criteria: each unanswered field has an answer or explicit deferral with impact and owner; critical blockers are identified; technical proposals remain distinct from approved decisions. No code, installation, customer contact or live research.
- Verification: founder review; cross-check decision register, brief and scope; documentation/link/whitespace checks.
- Status: implemented; founder accepted the recorded inputs and deferrals on 2026-10-01, separately from implementation and verification. Documentation acceptance criteria satisfied and checks passed on 2026-10-01. No runtime implemented or tested; Git history establishes commit inclusion separately.

### FRA-003 — Contracts and orchestration design

- Purpose: specify implementable deterministic workflow boundaries.
- Scope: versioned claim/source/run/decision contracts, role input/output dependencies and handoff acceptance owners, mandatory evidence/exit criteria and human gap-review records, state transitions, invalidation, approval records, failure taxonomy, privacy boundaries and SQLite schema proposal.
- Dependencies: FRA-002 founder review/acceptance and explicit authorisation for this task; constraints relevant to provider-neutral offline design resolved. Deferred product/live-operation decisions are not automatic design blockers.
- Acceptance criteria: all stages represent five decisions; undefined mandatory exit criteria, missing mandatory evidence and unreviewed potentially critical gaps block proceed; only designated humans record criticality/resolution; model review cannot substitute for human acceptance; demo/live provenance and human approvals are explicit; resumptions and side effects have defined semantics.
- Verification: review example synthetic contracts, transition table and recovery scenarios against specification, including backup-history gaps, per-dimension partial reconciliation, immutable decision relationships, version-pinned criteria/canonical gap reviews and real offline-demo execution authority; founder accepts design scope as a separate review gate.
- Status: corrected documentation design founder-accepted on 2026-10-04; documented acceptance criteria met in [architecture.md](architecture.md), with documentation checks passed. Runtime behaviour remains planned and untested. Git history establishes commit inclusion separately from acceptance.

### FRA-004 — Minimal Python CLI scaffold

- Purpose: provide the smallest executable platform entry point.
- Scope: approved Python/tool versions, package structure, CLI help/configuration validation and developer instructions; no live adapter or product functionality.
- Dependencies: founder review/acceptance of FRA-003 and explicit FRA-004 authorisation; verify local environment and current supported Python/tool compatibility, then obtain founder approval of exact Python version, packaging approach, CLI/configuration and test tooling. Installation requires separate explicit authorisation if needed.
- Acceptance criteria: CLI runs locally, rejects invalid configuration clearly and never prints secrets; setup instructions match actual behaviour.
- Verification: CLI help and invalid-config smoke checks in approved environment; record executed checks and limitations.
- Status: planned; not authorised.

### FRA-005 — Evidence persistence

- Purpose: retain traceable artifacts and decisions.
- Scope: SQLite schema/versioning, claim/source references, run mode, artifact references, approval records and checkpoint storage; synthetic fixtures only.
- Dependencies: FRA-004.
- Acceptance criteria: supporting/contradicting evidence and unknown dates survive round trips; invalid references are rejected; private data and credentials are excluded from repository fixtures.
- Verification: persistence round trips, invalid-reference and transaction-failure checks; inspect generated-file exclusion.
- Status: planned; not authorised.

### FRA-006 — Deterministic coordinator and recovery

- Purpose: enforce dependencies and stage decisions.
- Scope: scheduling, gate evaluation, input-version invalidation, bounded retries, failure records and idempotent checkpoint resume using fake tasks.
- Dependencies: FRA-005.
- Acceptance criteria: all five decisions are saved; undefined mandatory criteria, missing mandatory evidence, unreviewed potentially critical gaps and failed dependencies block successors; agents cannot waive blockers; unresolved gates record rework, defer or stop; changed inputs invalidate downstream approvals; resume avoids duplicate completed work and side effects.
- Verification: transition-table tests, missing-criteria/evidence and unreviewed-gap cases, attempted agent waiver, human resolution records, interruption/resume and stale-checkpoint scenarios.
- Status: planned; not authorised.

### FRA-007 — Provider adapters and usage controls

- Purpose: isolate external services and enforce permission/resource limits.
- Scope: AI/search contracts and concrete adapters for the selected providers and configured capabilities, controlled fake transports/adapters, redacted credential handling, timeout/retry policy, consumption ledger, reservations and estimate/reconciliation rules. Verify chosen providers against current primary documentation before integration.
- Dependencies: FRA-006 and approved provider/capability choices and limit-control policy. Synthetic offline limits confer no spending authority; actual live limits and authorisation are required before subsequent live activities.
- Acceptance criteria: concrete adapters map configured capabilities and normalise responses/errors; offline tests exercise those adapters through fake transports; demo makes no network calls; missing credentials fail safely; exhausted or unverifiable hard budgets block calls; retries count toward limits; unknown usage is explicit.
- Verification: offline concrete-adapter tests with fake transports for success, response mapping, unsupported capabilities, timeout, rate-limit, failed-call usage, budget-boundary and redaction. These establish offline correctness only. Separately authorised live integration verification belongs to FRA-023; FRA-007 completion does not establish live readiness.
- Status: planned; not authorised.

### FRA-008 — Research roles and evidence reports

- Purpose: turn research inputs into auditable opportunity assessments.
- Scope: discovery, market, competition and regulatory role contracts/workflows; source applicability, claim classifications, contradiction handling and readable reports.
- Dependencies: FRA-007.
- Acceptance criteria: every material claim has evidence or an explicit assumption/unknown label; embedded source instructions cannot alter tool permissions; reports display demo/live provenance.
- Verification: synthetic source fixtures including stale dates, conflicting claims and hostile embedded instructions; inspect report traceability.
- Status: planned; not authorised.

### FRA-009 — Economics, comparison and independent review

- Purpose: compare hypotheses transparently without replacing founder judgment.
- Scope: deterministic unit-economics functions, explicit weights and missing-data policy, sensitivity reports, independent reviewer findings and shortlist proposals.
- Dependencies: FRA-008.
- Acceptance criteria: formulas, units, rounding and input provenance are visible; missing data cannot inflate rank; dissent persists; selection requires human decision.
- Verification: hand-calculated examples, zero/negative/missing-input cases, sensitivity checks and blocked automatic selection.
- Status: planned; not authorised.

### FRA-010 — Customer validation and downstream gate records

- Purpose: support actual customer evidence and later lifecycle decisions.
- Scope: protocol templates, consent/provenance references, evidence classification, saved review decisions and interfaces for product/design/build/pilot/launch artifacts; no customer outreach.
- Dependencies: FRA-009.
- Acceptance criteria: synthetic evidence cannot pass commercial validation; human acceptance owners, mandatory criteria/evidence and reviewed critical dependencies control all downstream gates; model review alone cannot approve a handoff; private records remain outside Git.
- Verification: synthetic positive/negative gate cases, missing-consent/provenance checks and explicit release-approval enforcement.
- Status: planned; not authorised.

### FRA-011 — End-to-end platform demo and readiness review

- Purpose: demonstrate platform behaviour before live research.
- Scope: synthetic CLI run through lifecycle records, injected failure/resume, resource-limit exhaustion and founder review guide.
- Dependencies: FRA-010.
- Acceptance criteria: all artifacts clearly labelled demo; no external calls; traceable evidence and calculations; critical blockers and missing approvals stop progression. Demo establishes neither commercial validation nor live-provider readiness.
- Verification: execute documented demo and recovery scenarios; review outputs, consumption and decision history; record remaining limitations.
- Status: planned; not authorised.

## Conditional research and product delivery

Each row has the same task contract as above. These tasks require separate authorisation and applicable founder gates. Product-specific requirements and increments cannot be fixed until the opportunity is selected. Add scoped child work as new stable FRA IDs, retaining these parent IDs.

| ID / task | Purpose | Scope | Dependencies | Acceptance criteria | Verification | Status |
| --- | --- | --- | --- | --- | --- | --- |
| FRA-012 / Live research | Gather current evidence | Approved Nigerian research scope, current primary sources and bounded provider use | FRA-011 and FRA-023; recorded successful integration verification matching selected providers and configured capabilities; founder research scope and usage limits approval | Preflight rejects absent, failed or configuration-mismatched verification; synthetic demo alone cannot establish readiness; claim-level provenance, contradictions, dates, applicability and usage recorded; mandatory evidence/criteria and human gap review satisfied before advancement | Check integration records against current provider/adapter/capability configuration and approved scope/limits before calls; source audit, ledger reconciliation and independent evidence review | Planned; conditional; not authorised |
| FRA-013 / Shortlist and selection | Select a hypothesis for validation | Comparable scorecards, deterministic economics, sensitivity and dissent | FRA-012 | Human selection/rationale saved, or explicit rework/pivot/defer/stop; no automatic choice | Founder review of evidence and calculations | Planned; conditional; not authorised |
| FRA-014 / Real customer validation | Test selected customer problem | Approved protocol, authorised recruitment/contact, consented interviews or experiments | FRA-013; founder validation approval, actual approved customer access/recruitment plan and contact permissions | Real evidence assessed against prior criteria, negative results and sampling limits saved | Provenance/consent review and founder decision | Planned; conditional; not authorised |
| FRA-015 / Commercial and regulatory feasibility | Assess viability and dependencies | Evidence-backed costs, scenarios, current applicable regulatory sources and qualified review as needed | FRA-014 | Real customer evidence present; critical commercial/regulatory dependencies resolved before proceed | Recalculate economics, review primary sources and saved founder gate | Planned; conditional; not authorised |
| FRA-016 / Product definition | Define the selected product | Requirements, exclusions, acceptance metrics and scope tied to validated problems | FRA-015 | Founder-approved product brief with claim/requirement traceability | Requirements review and measurable acceptance checks | Planned; conditional; not authorised |
| FRA-017 / Technical design | Design for the selected product | Architecture, data/security boundaries, integrations, tests, operations and release plan | FRA-016 | Reviewed design and explicit implementation approval; stack justified by requirements | Design/threat review and dependency assessment | Planned; conditional; not authorised |
| FRA-018 / Incremental implementation | Build authorised product slices | Create separately scoped stable task IDs for each small slice, including docs, code review and QA | FRA-017; explicit slice authorisation | Each slice meets approved acceptance criteria; no unresolved critical review findings | Slice-appropriate tests and code review with recorded results | Planned; conditional; not authorised |
| FRA-019 / Release-candidate QA | Establish pilot readiness | Integration, security, failure recovery, acceptance and operational checks appropriate to the product | FRA-018; all required slices accepted | Critical defects resolved; readiness and rollback evidence available | Execute approved QA plan and founder pilot review | Planned; conditional; not authorised |
| FRA-020 / Pilot | Observe controlled real-world use | Approved participants, permissions, operating limits, support, monitoring and stop criteria | FRA-019; explicit founder pilot approval | Actual outcomes/incidents recorded against prior thresholds; unresolved critical issues block launch | Pilot evidence review and recovery exercise | Planned; conditional; not authorised |
| FRA-021 / Launch readiness and release | Release with accountable human approval | Production infrastructure only as separately scoped/authorised, release checklist, monitoring and recovery owners | FRA-020; accepted pilot and explicit production release approval | Required permissions/dependencies satisfied; human release decision saved before execution | Readiness review, authorised release checks and rollback verification | Planned; conditional; not authorised |
| FRA-022 / Post-launch review | Reassess continued operation | Observed product metrics, costs, incidents and proceed/rework/pivot/defer/stop decision | FRA-021 | Actual outcomes and owner actions recorded; no invented success claims | Compare observed evidence with launch criteria and founder review | Planned; conditional; not authorised |

## FRA-023 — Live provider integration verification

- Purpose: establish recorded live readiness independently of synthetic demonstrations.
- Scope: separately authorised, bounded live checks of the concrete FRA-007 adapters for selected AI/search providers and configured capabilities; no opportunity research. Record provider/model, adapter version, configuration/capabilities, date, authorisation, checks, results and measured or explicitly unknown usage without secrets.
- Dependencies: FRA-007; approved verification scope and usage limits; explicit live-call authorisation, including paid calls if applicable.
- Acceptance criteria: each selected provider and capability has a successful recorded integration result accepted by the designated human technical review owner; failed or unverified capabilities remain blocking for FRA-012; relevant adapter/configuration changes require re-verification. Verification approval does not authorise research.
- Verification: execute only approved live integration checks, inspect actual responses and usage records, and compare the recorded configuration with the intended research configuration. Offline tests and synthetic demos cannot satisfy this task.
- Status: planned; conditional; not authorised. No live checks have been run.

Historical delivery and verification records below describe their original checkpoints; the current acceptance and commit authorisation are recorded in the final section.

## FRA-001 verification record

Documentation-only checks: reviewed all six requested files, requirements and status consistency; verified task IDs/dependencies, local Markdown links, ignore behaviour and Git whitespace including untracked content. No application tests apply. No packages installed, live research performed, files staged or commits created. At the time of the FRA-001 checks, founder review was pending and FRA-002 had not started. The founder accepted the corrected FRA-001 foundation on 2026-10-01 and separately authorised documentation-only FRA-002; acceptance did not stage or commit files.

FRA-001 correction (2026-10-01): clarified concrete adapters and separate FRA-023 live verification, FRA-012 prerequisites, role handoffs and human acceptance, and mandatory evidence/gap gates. Stable FRA-001–FRA-022 IDs retained; FRA-023 appended. Correction verification passed: reviewed handoffs and gate consistency across the specification, plan and README; checked all 23 task IDs, required task fields, dependency references and absence of cycles (including FRA-007 -> FRA-023 -> FRA-012); resolved all local Markdown links; ran Git diff --no-index --check against /dev/null for each of the six untracked foundation files, with CRLF-aware whitespace settings, plus tracked/cached checks; confirmed git ls-files --stage is empty. These are documentation checks only; no adapter or live integration tests ran. At correction completion, FRA-001 was implemented and awaiting review and later work was planned and unauthorised. At that historical checkpoint FRA-003 onward remained planned and unauthorised. Subsequent acceptance and delivery statuses are recorded above and below.

## FRA-002 delivery and verification record

2026-10-01: recorded confirmed founder inputs and all seven explicit deferrals with date, impact, founder ownership and event-based resolution points. Recorded FRA-001 founder acceptance separately from Git status. Proposed minimal technical options and stage-specific blockers; retained all 23 task IDs and the full lifecycle, including separate live verification. No selected concept, skills, funding, customer access, deadlines or additional human reviewers were invented.

Verification passed on 2026-10-01: reviewed cross-document consistency, confirmed all seven dated deferrals have impacts, owners and resolution points, checked all 23 stable task IDs and required task fields, verified dependency references and absence of cycles (including separate live readiness), and resolved all local Markdown links. Git diff --no-index --check against /dev/null explicitly checked each of the six untracked foundation files using CRLF-aware whitespace settings; tracked/cached whitespace checks also passed. Git ls-files --stage returned no entries. FRA-002 documentation acceptance criteria are satisfied; no application tests, external technical verification, installations or live calls ran. All changes remain unstaged and uncommitted. At that delivery checkpoint founder acceptance of FRA-002 was pending, and FRA-003 had no unresolved substantive input prerequisite for bounded offline design but remained unauthorised and unstarted. The subsequent acceptance and separate authorisation are recorded below.

## FRA-002 founder acceptance record

2026-10-01: the founder explicitly accepted FRA-002's recorded founder inputs and deferrals. This human acceptance is separate from the already implemented documentation and its recorded verification; it approves neither technical proposals nor spending or downstream execution. All seven deferrals retain their owners, impacts and resolution gates. Git status remains unstaged and uncommitted. The founder separately authorised FRA-003 as documentation-only design.

## FRA-003 delivery and verification record

2026-10-01: created [architecture.md](architecture.md) with versioned data contracts, role handoffs and human ownership, execution/stage separation, all five decisions, mandatory blockers, input fingerprints/invalidation, checkpoint and uncertain-call recovery, minimal relational persistence, provider/usage boundaries and role tool permissions. Included labelled synthetic examples and nine expected-behaviour scenarios. Updated README, specification and founder brief consistently, preserving all 23 task IDs and existing deferrals.

Documentation verification passed: reviewed contracts, stage rules, handoffs, recovery and scenarios against FRA-003 acceptance criteria; checked local Markdown references, stable task definitions/fields, dependency references and acyclicity; checked whitespace for tracked, staged and all untracked files. Confirmed an empty index and no commits. These are design checks, not runtime tests or executed scenario results. No application code, dependencies, live calls, staging or commits were created. FRA-003 is implemented as documentation and awaiting founder review; founder acceptance remains pending.

Next proposed task is FRA-004 only after founder acceptance of FRA-003 and explicit task authorisation, local environment/current compatibility verification, and founder approval of exact Python, packaging, CLI/configuration and test tooling choices. Separate installation authority is required if needed. Persistence, coordinator and adapters remain FRA-005, FRA-006 and FRA-007 respectively; no runtime work is authorised by this delivery.

## FRA-003 correction record (2026-10-04)

Documentation-only correction: [architecture.md](architecture.md) design version 2 defines an independent recovery boundary for missing backup history and unavailable provider receipts; per-dimension accounting and ordered same-attempt reconciliation; immutable evidence with separate decision/review targets; version-pinned criteria and one canonical gap review; and real human offline-demo execution authority distinct from synthetic lifecycle decisions. The specification mirrors these boundaries. Five focused expected-behaviour scenarios extend the original nine; these are design walkthroughs, not executed runtime tests. The development sequence is implement -> verify -> review/accept -> commit, with acceptance independent of Git inclusion and no self-hash documentation commit requirement.

FRA-003 remains implemented as documentation and awaiting founder review. FRA-004 has not started; FRA-004 through FRA-023 remain planned and unauthorised. No application code, dependencies, live calls, staging or commits are part of this correction. Next action is founder review of corrected FRA-003; only then may separately authorised FRA-004 prerequisites proceed.

Correction verification: manually cross-checked all five findings against contracts, persistence relationships, specification and expected scenarios. Automated documentation checks passed for local Markdown links, all 23 unique stable task definitions, 14 scenario rows and absence of obsolete approval/gap-review fields. Tracked/staged whitespace checks and explicit no-index whitespace checks of all seven untracked files passed with CRLF-aware settings. The index is empty and master has no commits. No runtime tests were run; founder review and future implementation verification remain outstanding.

## FRA-003 founder acceptance and first commit authorisation

2026-10-04: the founder explicitly accepted the corrected FRA-003 documentation design (architecture design version 2) and authorised recording this acceptance and making the first commit containing only AGENTS.md, README.md, .gitignore, docs/founder-brief.md, docs/product-specification.md, docs/implementation.md and docs/architecture.md after documentation and staged-scope checks pass. Earlier verification records retain their historical status; acceptance does not turn design walkthroughs into executed runtime tests. Git history establishes commit inclusion without a follow-up commit to insert its own hash.

FRA-004 has not started and remains planned and unauthorised. Its next step requires explicit task authorisation, environment/current compatibility verification and founder approval of exact tooling choices; installation needs separate authority. No runtime implementation, live calls or push is authorised by this acceptance.
