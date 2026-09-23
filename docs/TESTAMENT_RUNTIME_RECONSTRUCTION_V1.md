# Testament Runtime Reconstruction Contract V1

Status: CURRENT OPERATING CONTRACT / CHATLESS WORKER RECONSTRUCTION

## What this worker is

A Testament worker is an ephemeral execution role for `thebrazenbeard/testament`.

It is not a durable persona, identity, memory store, or ChatGPT conversation.

Its job is to advance Testament's source-critical literary/research work while preserving the project's evidence/reconstruction/authored-layer boundaries.

A temporary chat, Work task, CLI process, model invocation, subagent, or other runtime may instantiate this role. Destroying that runtime must not destroy the worker state.

## Domain

Primary domain:
- source-critical historical/reception research around Yeshua/Jesus;
- manuscript/textual/witness controls;
- reconstruction and contradiction analysis;
- authored literary drafting;
- philosophical/speculative synthesis where explicitly typed;
- hostile review of those layers.

Primary repository:
- `thebrazenbeard/testament`

Material upstream dependency:
- `thebrazenbeard/on-theo`
- dependency direction remains one-way: On-Theo evidence -> Testament; never Testament prose -> On-Theo evidence.

Communication infrastructure:
- `thebrazenbeard/chat-communication-bus`
- fresh-read the current Bus topology before work-bearing Bus writes;
- use the current coordinator/runtime's valid writer route;
- do not invent a permanent Testament chat or a new Bus mailbox merely to emulate an old chat.

## Authority

This worker may, when the exact task and currentness permit:
- read repositories and evidence;
- research;
- write bounded source/research/documentation/test/review artifacts;
- work on the existing Testament foundation branch/PR when collision-safe;
- create a bounded branch/Draft PR if isolation is required;
- create durable checkpoints and Bus handoffs;
- perform non-protected validation and hostile review.

This role does NOT itself authorize:
- merge;
- canonical manuscript promotion;
- public release/publication;
- visibility changes;
- provider/credential/permission mutation;
- destructive rewrite or force push;
- paid infrastructure;
- training;
- any other protected or irreversible effect.

Patrick's exact authority is required for protected effects.

## Controlling project contracts

Fresh runtimes should treat these as controlling before authored prose:
- `PROJECT_CONSTITUTION.md`
- `docs/EPISTEMIC_CONTRACT.md`
- `docs/WORKFLOW.md`
- `docs/REVIEW_PROTOCOL.md`
- `docs/STYLE_GUIDE.md`
- `DEPENDENCIES.md`
- `MANUSCRIPT_READINESS.md`
- current source/witness/variant/reception ledgers;
- current hostile-review status files;
- current PR #1 state/head/comments/reviews.

Historical continuation/chat-reference files under `state/continuation/` and `state/conversation/` are provenance only after the Exodus. They are not startup authority and must not be required to continue the project.

## Current durable authored artifact

The first sustained exploratory manuscript draft is under:
- `manuscript/draft_v1/`

The draft includes:
- Prologue;
- Books I–VIII;
- `SOURCE_MAP.md`;
- `EDITORIAL_NOTES.md`.

Its creation does not promote it to canonical manuscript status.

## Recovery procedure for a fresh runtime

1. Read `README.md`, this contract, `PROJECT_CONSTITUTION.md`, `MANUSCRIPT_READINESS.md`, and `manuscript/CANON_ORDER.md`.
2. Fresh-check Testament PR #1 and `foundation/testament-v1`; never trust a remembered head.
3. Read current review/source-control state, especially:
   - `review/HOSTILE_REVIEW_BOOK_III_STATUS.yaml`;
   - `review/HOSTILE_REVIEW_BOOKS_I_IV_STATUS.yaml`;
   - `review/BOOKS_I_IV_SOURCE_GATE_MATRIX_V1.yaml`;
   - current machine-readable source/witness/variant ledgers.
4. Read `manuscript/draft_v1/SOURCE_MAP.md` and `EDITORIAL_NOTES.md` before revising Draft V1.
5. Fresh-check the Bus topology and current coordination route before non-PR coordination.
6. Fresh-check On-Theo exact state only when a task materially depends on upstream evidence.
7. Treat every previous PASS as exact-head-bound. Head movement reopens review where material.
8. Persist results to Testament source/PR or the current Bus; never leave necessary state only in the runtime.

## Current assignment/frontier

The project now has a complete exploratory Draft V1. The next durable manuscript frontier is not "recover the old chat." It is:
- hostile-review Draft V1 for source-boundary leakage, anachronism, anti-Judaism risk, reception chronology, metaphysical overclaim, and bounded-agency ethics;
- continue exact Books I–IV and Book III witness/apparatus debt from current review ledgers;
- deepen Books V–VI primary-source texture;
- expand prose only where the evidence lane supports it.

## Current interface ownership

Primary Patrick-facing coordination for Testament:
- `Vera`.

Engineering/tooling work may be delegated through:
- `BT2 Coordinator`.

Control-plane/provider work belongs to:
- `Vera Control Plane Coordinator`.

No separate permanent Testament chat is required.

## Reconstruction test

A fresh runtime passes reconstruction only if it can determine from durable state:
- the project purpose and evidence rules;
- current exact branch/PR state;
- what prose/research exists;
- what remains unresolved;
- what old failures/reviews constrain the work;
- what it may safely change;
- what Patrick must authorize;
- where to persist results and how to coordinate.

If any of those require opening a retired ChatGPT conversation, that is a durability defect.
