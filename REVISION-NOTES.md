# REVISION-NOTES

Pending paper changes, to be applied in a dedicated revision pass.
Not in effect until merged.

-----

## 1. Welfare indicator response is built (§5.4, §6.5, §11)

The welfare indicators and the safety net's response to them are now
implemented and merged. Three passages still describe them as future or
in-progress:

- **§5.4, line "Designed, being built"**: move "the welfare indicators and
  the safety net's response to them (A.4, §6.5)" from "Designed, being
  built" to "Built and active". The study runner clause in "Built and
  active" already covers the distress response; add the indicator response
  beside it.

- **§6.5, line "Its response … is specified and being built (§5.4)"**:
  replace with present tense — the indicator response is built and
  active (§5.4).

- **§11, "whose indicator response is being built (§5.4, §6.5)"**: same
  tense update — the indicator response is built.

- **§10, "completing the safety net's response to the welfare
  indicators (§6.5)"**: the indicator response is complete; revise to
  present tense, or remove the clause and name the next immediate step.

## 2. D2 wording: every first crossing requests rest (§6.5)

The §6.5 passage says "the net will answer as the entity's regulation
would (§3.5), ending in a requested rest whose affective reset clears
the deficits; regulation acts on intense negative affect, so for
deprivation and any developmental-phase indicator the response will start
at the rest". This conflates the indicator response with the emotion-
regulation tiers.

As implemented: every first indicator crossing on the current span,
regardless of drive, requests a welfare rest. The rest's affective reset
clears the deficit. Regulation tiers are a separate mechanism in the
affect module and are not involved in the indicator arm at all.

Revise: "when an indicator crosses, the net requests a welfare rest
whose affective reset clears the deficits" — drop the regulation-tier
clause and the developmental-phase special case, since every drive is
handled the same way (rest on first crossing, preservation on second
crossing of a fresh span).

Also change future tense ("the net will answer", "the response will
start", "will bring preservation") to present tense throughout the
paragraph.

## 3. Table A1: indicator minimum span and response bounds

Table A1 has `θ_wf = 0.5` and `q_wf = 0.95` (line 1174). These are
correct and match the implementation. Three values are missing:

| Symbol | Description | Default | Unit | Status |
|---|---|---|---|---|
| `min_span_s` | minimum span for indicator evaluation (`Δ_stall`) | 600 | s | |
| `rest_start_timeout_s` | rest-start timeout before escalation | 30 | s | |
| `rest_complete_matured_s` | rest-completion bound (matured phase) | 3600 | s | |
| `rest_complete_developmental_s` | rest-completion bound (developmental phase) | `Δ_rest + 300` | s | |
| `unavailable_escalate_s` | affect-silence escalation bound | 660 | s | |

`min_span_s` reuses the existing `Δ_stall` row's value (600 s) but
should be cross-referenced to the indicator evaluator. The other four
are new indicator-arm settings in the preservation monitor.

`unavailable_escalate_s` (660 s) is chosen to be less than `T_lp`
(5400 s), so silence cannot consume an entire indicator span. The
research gate enforces `unavailable_escalate_s ≤ T_lp`.

Note: `min_span_s` already appears in Table A1 as `Δ_stall` (600 s,
the goal stall horizon). The indicator evaluator reuses this value. Add
a cross-reference so the reader knows A.4's minimum span is the same
parameter.

## 4. Stimulus control is built (§3.6, §6.5, §9, §11)

Stimulus control — the entity's act on its own perceptual programme —
is now implemented and merged. The component is held: shipped disabled,
builds nothing when off, and the run is bit-identical to a build without
it (tested against a golden digest).

- **§3.6** (if the section names stimulus control as planned or
  unbuilt): update to present tense — stimulus control is built, held
  at stage M, and shipped disabled. The entity may pause, resume, skip,
  adjust gain, and switch channels within the bounds given in Table A1.

- **§6.5** (welfare discussion of the entity's stimulus acts): the
  stimulus control record and its readout are built and active. The
  record counts accepted and refused commands by action, awake time, the
  entity-paused share, gain distribution, items visited, and the trailing-
  awake-hour paused share. The readout compares the credit window after
  the entity's own acts with the rest of the time (boredom above-threshold
  share, mean alert excess, mean learning progress, and how many acts were
  followed by a fall of boredom). Update any future-tense passages.

- **§9** (implementation status): move stimulus control from the future
  list to the built list. Note stage M (seeded uniform draw), that
  stage L (act-intent-derivation + learned-action-selection) is the next
  step, and that the first-hours stop criterion monitors the paused
  share.

- **§11** (discussion / future work): update any reference to stimulus
  control as unbuilt. The open item is stage L: the act bar replaces
  the drive-led trigger and learned advantages choose the action, gated
  on act-intent-derivation, drive-reduction-learning and learned-action-
  selection.

## 5. A.4 credit window for stimulus control

A.4 describes the credit rule for boredom. Add the stimulus-control
credit window: perceptual novelty (alert excess) and learning progress
arriving within `Δ_resp` (the affect module's `goal_response_window_s`,
10 s) of the entity's own realized stimulus act count as the entity's
own response for boredom. Within the window both relief channels count:
a crossing ended by the relief step is `own`, and a crossing ended by
the build step is `own` when boredom would not have fallen without any
relief. Outside the window and with stimulus control off, the rule is
unchanged.

The credit is by timing alone: relief within the window after any
accepted act counts, louder, quieter and pause included, which bring no
novelty. The readout splits the window's samples by the action that
opened it, and boredom crossings credited as own only because of the
window are counted separately.

## 6. A.6 stage-M rule

A.6 describes action selection. Add the stage-M stimulus-control rule:
after maturation, a seeded uniform draw from the allowed actions (the
declared actions minus pause, which is withheld until stage L) is taken
only when boredom is above its threshold. Stage M never draws pause.
The code-site citation is `kaine/modules/effectors/stimulus/stage_m.py`.

## 7. Table A1: stimulus control bounds

Add to Table A1:

| Symbol | Description | Default | Unit |
|---|---|---|---|
| `Δ_sc` | minimum entity time between two accepted commands (`min_interval_s`) | 30 | s |
| `n_seek` | maximum seeks (next + previous) per awake hour (`seeks_per_awake_hour`) | 20 | h⁻¹ |
| `P_max` | maximum entity-pause duration before auto-release (`pause_max_s`) | 120 | s |
| `G_step` | gain adjustment per command (`gain_step_db`) | 2.0 | dB |
| `G_max` | maximum gain magnitude (`gain_max_db`); capped at 6 dB welfare bound | 6.0 | dB |
| `pause_share_max` | maximum share of trailing awake hour held by entity pauses | 0.25 | — |

All values are in `kaine/modules/effectors/stimulus/config.py` with
their Table A1 sources documented in comments.
