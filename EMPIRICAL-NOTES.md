# Notes for the empirical paper

The theory paper describes the implementation as built and reports no results. These notes record implementation history that bears on how data from particular runs must be read, so the empirical paper can disclose it. Sources are the KAINE repository's archived OpenSpec changes (`openspec/changes/archive/`). Change names and event types quote the implementation's identifiers, which still carry the earlier module names.

## Defects that affected earlier runs

### Broadcast rate
Before the adaptive-access-rate change (archived `2026-09-25-adaptive-access-rate`, kaine commit `603a443`), a rounding bug made broadcasts come every fourth 10 Hz tick (2.5 Hz) while the config and `runtime.json` reported 3.333 Hz. Any report of data from runs before the fix must give the rate as 2.5 Hz or avoid the exact figure.

### Sequence-module forward head
In the base-thesis profile the forward-prediction head of the sequence module was off, so its temporal prediction error was always 0.0. The module also counted every `audition.out` entry (including `audition.perception` at about 2 Hz) as an interaction, so the social drive of the affect module never built. Source: `2026-10-06-chronos-forward-model-on`.

### Affect-module goal check
Before the goal-relevance fix (archived `2026-10-06-thymos-goal-check`), the goal-relevance check scored the coalition against an explicit goal ledger that nothing wrote to, so it published a constant -0.2 on every broadcast, a fixed lean toward goal obstruction in every appraisal. The `thymos.emotion` event names the method (`drive_relevance_v1`, or `drive_relevance_v1+token_overlap_v1` when explicit goals contribute), so a run's record shows which check produced each appraisal.

### Interoceptive expected error
During an earlier developmental phase the interoception module's error sat at 0.35 to 0.41 for hours, fatigue crossed threshold every 3 to 4 minutes, and each sleep wiped affect. That developmental phase was ended and deleted. Source: `2026-10-01-soma-expected-error`.

### Perception and salience
In a containerized base-thesis run, the vision module sat at its 0.2 baseline on 3,830 of 3,830 reports and the audition module at 0.4 on 3,511 of 3,511, so the winning score was the constant 0.176 regardless of the stimulus. The fix (a self-calibrating relative alert, forward prediction on by default) is merged with unit tests and a synthetic fixture. Its live confirmation on the reference program (tasks 5.1 and 5.2) has not been run. Source: `2026-10-05-perception-drives-salience`.

### Language organ persona
Runs before the voice-development Stage 0 change used an earlier persona ("the language faculty ... report the module readings"). Their utterances are instrument-state readouts and should not be treated as the entity's voice. Earlier voice alignment used that faithful rendering as the "chosen" side of each preference pair. That use is retired and voice alignment trains nothing until a validated preference source exists. Source: `voice-development` Stage 0.

## Study history
The first module-ignition study (`moc7-2026-10`, launched 2026-10-01) ended in the developmental phase on 2026-10-02 because its entrainment marker could not pass. The self-rhythm had no coupling mechanism, and the measurement took the phase of unfiltered spike rates. It produced no results and its run data was deleted. No figure or claim may cite it. No study has run to completion since.

## Individuation instrument
The rebuilt instrument's limitations an individuation paper must disclose are:

1. The effect floor is not yet calibrated. An operator-run real-organ smoke test sets it, and until then it is 0.
2. Entities that reached maturation before the change carry a later "capture" reference. Drift before that date is not measured.
3. Forks cannot yet be measured against a fork-point reference, so a fork that has lived at least 30 minutes is preserved by default.
4. In adapter hot-swap modes that cannot confirm which adapter the organ serves, probes are skipped once an adapter exists. Such entities are protected by the adapter signal instead.

## Language-organ prompt replays
The theory paper (§3.5) gives only the headline result of the offline replays that chose the organ's persona prompt and kept the launch name and self-facts out of it. The full figures are:

- Prompt choice. A replay of a test boot's 190 organ requests, five seeded samples each at the organ's general-use temperature of 0.7, kept the persona prompt by a rule fixed in advance: a variant would replace it only if the share of texts with meta-commentary (self-description as an AI, second person, the situation's themes, lists, prompt echoes, template loops) fell reliably while the share grounded in a modality of the accessed content fell by under 5 points. Under the kept prompt 14.8 percent of 950 texts carried meta-commentary and 2 described the entity as an AI (one-sided 95 percent bound 0.7 percent).
- The eight-hour test boot ran another prompt, with the situation only on waking and no self-category. Replaying its 1508 requests under that prompt gave 22.7 percent meta-commentary and 0.2 percent self-descriptions as an AI, against 23.2 percent and 4 texts (0.27 percent) in the boot itself.
- Name and self-facts. In the replay of the eight-hour boot's 1508 requests and 240 self-referential ones, giving the organ the launch name alone raised human-life claims from 35 to 76 texts. With the facts about what the entity is, it raised identity leakage on self-referential requests by 2.6 points (95 percent interval 0.2 to 5.0), though the facts raised grounding by 11 to 13 points.
