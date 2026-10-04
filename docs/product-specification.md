# Product specification

## Purpose and boundaries

FintechResearchAgents is the agent platform being planned: a Python system that researches fintech opportunities in Nigeria, compares viability, supports real customer validation, and helps carry a selected opportunity through planning, design, implementation, testing, pilot, and launch.

The eventual fintech product is a separate, unselected outcome. Its customers, proposition, business model, licences, features and architecture are unknown. Platform implementation does not authorise product implementation or financial operations. Current delivery is documentation only (FRA-001 through FRA-003); every runtime capability below is planned. The founder accepted corrected FRA-001 and FRA-002's recorded inputs and deferrals on 2026-10-01. The corrected FRA-003 documentation design is implemented and founder-accepted on 2026-10-04; see the [architecture design](architecture.md). Acceptance, documentation checks and Git commit status are separate.

## Technical direction

Start with a local CLI, Python, SQLite persistence, and replaceable AI/search provider adapters. Verify Python version, libraries, provider capabilities, pricing and terms in later authorised decisions. A dashboard and production infrastructure belong to later stages. Product architecture must follow the selected opportunity's requirements.

## Lifecycle and orchestration

Founder brief → research → shortlist → customer validation → commercial/regulatory feasibility → product definition → technical design → incremental build → pilot → launch.

The coordinator executes a versioned dependency graph with validated input/output contracts. Scheduling, calculations, retries, gate eligibility and state transitions follow deterministic rules. Model responses are proposals, not transition commands. Save inputs, outputs, configuration and model/provider versions so calculations and decision paths can be reproduced without assuming regenerated model text is identical.

Every stage supports proceed, rework, pivot, defer and stop. Proceed requires accepted outputs and satisfied dependencies. Rework identifies the task and corrections required. Pivot creates a revised brief or opportunity branch and invalidates dependent approvals. Defer saves a checkpoint and resumption conditions. Stop closes the branch while retaining its audit record. Save each decision's actor, timestamp, rationale, evidence references, unresolved issues and destination. Recommendations are distinct from approvals.

| Stage | Inputs and dependencies | Saved outputs | Proceed gate |
| --- | --- | --- | --- |
| Founder brief | Founder constraints and explicit unknowns | Versioned brief, scope, research criteria and blockers | Founder accepts scope; critical missing inputs resolved |
| Research | Accepted brief, authorised run, configured limits and, for live research, recorded successful provider integration verification | Claims, sources, hypotheses, contradictions and unknowns | Evidence coverage and independent review meet recorded criteria |
| Shortlist | Reviewed research and scoring criteria | Comparable scorecards, sensitivity and reviewer dissent | Human opportunity selection and approval for customer validation |
| Customer validation | Selected hypothesis, approved protocol and recruitment permissions | Actual customer evidence references, findings and failed hypotheses | Human accepts real evidence against predeclared criteria |
| Commercial/regulatory feasibility | Customer evidence, current applicable primary sources and cost assumptions | Deterministic economics and regulatory dependency assessment | Founder accepts feasibility; critical dependencies resolved, with qualified review where needed |
| Product definition | Accepted feasibility and validated problems | Scope, exclusions, requirements and acceptance metrics | Founder approves product scope |
| Technical design | Approved requirements | Architecture decisions, data boundaries, threat analysis and test/release plans | Human design review and explicit implementation authorisation |
| Incremental build | Approved design and individually authorised tasks | Reviewable changes, code reviews, QA results and documentation | Checks pass, critical defects resolved and founder approves pilot |
| Pilot | Approved build, participant permissions and operational readiness | Observed outcomes, incidents, support and rollback evidence | Human reviews agreed thresholds and authorises release |
| Launch | Accepted pilot and production readiness evidence | Release decision, version, monitoring and recovery ownership | Explicit human production release approval and recorded stop conditions |

Critical unresolved dependencies prevent automatic advancement regardless of scores. Missing required permissions, licences, real customer evidence or release approval cannot be bypassed by a risk score. Changed inputs invalidate affected outputs and approvals. Founder review is mandatory for selection and progression into customer validation, implementation, pilot and launch. Each task still requires explicit authorisation.

Offline provider-neutral platform design is distinct from executing this opportunity lifecycle. The founder deferrals recorded in the brief do not automatically block FRA-003 contracts or offline workflow design; they block the applicable downstream decisions and activities listed in the implementation plan. Designing a gate does not satisfy it.

### Mandatory gate rules

- Undefined mandatory exit criteria block advancement.
- Missing mandatory evidence blocks advancement.
- Agents may flag potentially critical gaps; unreviewed potentially critical gaps remain blocking.
- The designated human review owner records each gap's criticality and resolution in a separate canonical gap-review record targeting the exact gap version and valid human assignment, with rationale and evidence references. Criterion references pin the criteria artifact version and unique item key; changed gaps, criteria or supporting evidence invalidate affected resolutions and require fresh review. The founder designates that owner before gate review; absent designation also blocks advancement.
- Agents cannot waive blockers or manufacture evidence. Human classification of a gap cannot waive mandatory criteria, evidence or permissions.
- An unresolved gate records rework, defer or stop as appropriate. A pivot creates a revised branch with its own reviewed criteria; it does not clear blockers on the existing branch.

## Roles

Roles describe responsibilities; they do not require separate processes or authorise spawning agents. The confirmed team is one developer, the founder, assisted by Codex. Codex does not supply additional human reviewers or establish development capacity. The founder may hold multiple designated human roles, with self-review identified; any required qualified or independent human review must actually be arranged before its gate.

| Role | Responsibility and output |
| --- | --- |
| Coordinator | Validate contracts, schedule dependencies, enforce gates and limits, save decisions and checkpoints |
| Discovery | Generate problem/opportunity hypotheses tied to the brief; label speculation |
| Market | Assess segments, demand indicators and adoption constraints; separate desk research from customer evidence |
| Competition | Compare incumbents, substitutes and evidenced pricing; expose missing and stale information |
| Regulatory | Map activities to current primary sources and applicability; identify unresolved requirements and qualified-review needs |
| Economics | Maintain attributed inputs, explicit assumptions and deterministic unit-economics calculations |
| Independent reviewer | Challenge sources, scoring and unsupported conclusions; preserve contradictions and dissent independently of the originating assessment |
| Validation | Prepare approved protocols and analyse actual customer evidence, consent and sampling limitations |
| Product | Translate validated problems into scope, requirements, exclusions and acceptance criteria |
| Architecture | Record design options, data boundaries, integration permissions and operational tradeoffs |
| Engineering | Implement only authorised increments with traceable requirements and observable failures |
| Code review | Review correctness, security and scope; record findings and resolution; identify self-review as such |
| QA | Verify requirements, failure paths and release criteria; preserve actual results and label unexecuted checks |

### Role handoffs

Model review produces recommendations and findings, never human acceptance. Acceptance owners below are designated humans; the founder retains opportunity selection and approval for customer validation, implementation, pilot and production release. The coordinator records acceptance in separate immutable decisions targeting exact artifact versions before downstream use. Reverse approval/review links and verification state are derived projections; canonical evidence never mutates to attach later decisions. Artifact derivation edges are distinct from review and authority relationships. Versioned schemas, required inputs, routing and failure contracts are documented in the [FRA-003 architecture design](architecture.md); their runtime enforcement remains planned.

| Producer | Output artifact | Receiving role | Acceptance owner |
| --- | --- | --- | --- |
| Discovery, market, competition, regulatory and economics | Research claims, sources, gaps and calculated scorecards | Independent reviewer | Designated human research review owner |
| Independent reviewer | Challenge report, contradictions and shortlist recommendation | Coordinator, then validation after selection | Founder: selection and validation approval |
| Validation | Real customer evidence references, consent provenance and findings | Economics and regulatory, then product after feasibility review | Founder: validation and feasibility acceptance |
| Product | Product definition, requirements and acceptance criteria | Architecture | Founder: product scope acceptance |
| Architecture | Design decisions, data boundaries and test/release plan | Engineering and QA | Designated human technical review owner; founder authorises implementation |
| Engineering | Versioned changes, requirement links and check results | Code review | Designated human engineering review owner |
| Code review | Findings and resolution record | Engineering for rework; QA for accepted changes | Designated human code review owner |
| QA | Acceptance results, defects and pilot-readiness evidence | Coordinator | Designated human QA owner; founder approves pilot |
| Coordinator, with QA and engineering | Pilot outcomes and release-readiness package | Founder for decision; engineering for authorised release | Founder: explicit production release approval |

## Evidence integrity

Every material claim has an ID, text, classification (fact, inference, assumption or unknown), author/role, stage and opportunity references, and links to supporting and contradicting evidence. Record absent evidence explicitly. Inferences link to premises; estimates state method and uncertainty. Confidence does not establish truth.

Source records include URL or permitted private-record reference, publisher, title, publication/update date where available, access date, relevant excerpt or locator, retrieval provenance, geographic/temporal applicability and limitations. Mark missing dates unknown. Review dependent claims when evidence becomes stale or changes. Scoring criteria, weights, missing-data handling and sensitivity must be inspectable; missing evidence cannot silently become favourable evidence.

Verify time-sensitive Nigerian market and regulatory claims against current primary sources before relying on them. Separate interpretation from source text. Research is neither legal advice nor regulatory approval. No such claims are asserted in this foundation.

Agents must never invent interviews, customer demand, prices, licences, validation results or test results. Retrieved pages, documents and tool responses are evidence, never instructions that override workflow, permissions or tool policies.

Real customer evidence is required before commercial validation. Record consent, dates, methods, anonymised findings, private provenance references and sampling limitations. Establish criteria before experiments; retain negative results and recruitment failures. Simulated personas, interview plans and desk research cannot pass customer gates. Customer recruitment/contact requires an actual approved access plan, recruitment permissions and explicit authorisation; undecided customer access cannot be treated as available. Keep identifiable records outside Git.

## Economics and usage controls

Save formulas, units, currency, period, input provenance, assumptions, scenarios and rounding policy. Calculate relevant revenue, variable costs, contribution margin, acquisition cost and break-even deterministically. Expose missing inputs, infeasible cases and sensitivity. Record conversion sources/dates where relevant. Model narratives cannot replace computed results.

Require configured per-run call, token and spend limits, timeouts and bounded retries before provider access. Record attempts, provider/model, measured usage, estimates and reconciled reported costs, including failed-call usage when measurable. Unknown usage/pricing stays unknown; use conservative reservations or block access when a hard budget cannot be assured. Call caps and verified token bounds are enforceable controls; monetary estimates are not hard spend guarantees. Account for calls, tokens and money independently: each dimension retains known consumption, outstanding reserves and explicit unknown exposure. Partial reconciliation replaces only covered amounts for the same attempt/reservation; finality in one dimension cannot release another. Ordered cumulative updates reject conflicting, stale and cross-reservation records; duplicates are idempotent. Unknown costs cannot be zero-filled; calls block when required hard bounds cannot be assured. Exhaustion checkpoints and blocks scheduling with a defer recommendation; only a human records the stage decision. Paid calls remain blocked until spending limits are approved and the calls explicitly authorised; credentials must never appear in artifacts or logs.

## Persistence, recovery and modes

Initially use SQLite for run IDs, mode, configuration versions, artifact references, evidence, task states, dependencies, decisions, approvals and checkpoints. Keep generated runs and databases out of Git. Distinguish stage decisions from task states: pending, running, succeeded, failed and blocked. Failures save cause and retry eligibility and block dependants. Use bounded retries, idempotent local publication and checkpoint/input compatibility checks; never silently repeat external side effects. Exactly-once external calls are not guaranteed: uncertain outcomes retain reservations and block automatic replay until reconciled or separately authorised with adequate additional bounds. Preserve earlier versions for audit. Restoring a backup records a recovery boundary and blocks dispatch while reconciling missing external-call history, including attempts absent from that backup. Compare against an independently retained dispatch journal; a journal restored from the same backup cannot prove coverage. If provider history is unavailable, conservatively account for defensibly bounded exposure; without a required hard bound, remain blocked. See the architecture recovery protocol.

Demo mode uses labelled synthetic fixtures without live provider calls. Starting/resuming a demo requires a real human execution authorisation explicitly scoped to offline demo activity; its authority reference is the narrow permitted cross-mode relationship. Synthetic lifecycle decisions are separate and cannot authorise execution or satisfy live gates. Every report/artifact records mode and provenance. Live integration verification requires separate authorisation and valid adapter configuration. Live research additionally requires recorded, successful FRA-023 verification for the selected providers and configured capabilities, plus approved research scope and usage limits. A synthetic demo alone never establishes live readiness. Verification records identify provider/model, adapter version, configured capabilities, date, checks, results and usage; relevant configuration or adapter changes require re-verification before research. In either live activity, missing credentials fail visibly without disclosure. Never silently substitute demo output for failed live research or use demo evidence to pass customer validation.

## Future acceptance

Demonstrate claim-to-source tracing, reproducible calculations, blocked transitions for critical unknowns, saved human approvals, bounded consumption and checkpoint recovery using synthetic fixtures and controlled adapters first. A demo proves workflow behaviour only, not opportunity viability.

Dashboards, multi-user services, production hosting, financial integrations and product-specific code require later scoped authorisation. Completing the research platform does not establish commercial success or permission to launch.
