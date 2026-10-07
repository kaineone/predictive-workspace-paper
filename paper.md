# KAINE: A Continuously Running Predictive Global Workspace for Synthetic Minds

*Neuroscience-Grounded Modules Competing for a Shared Workspace*

**Erik Chevalier**

Independent Researcher

Contact: [kaine.one@tuta.com](mailto:kaine.one@tuta.com)

*Preprint.*

-----

## Abstract

A synthetic mind, if one can be built, may be the coherent global behavior that emerges when specialized predictive modules, each minimizing its own error, compete for a shared workspace with no central executive. This paper presents a continuously running predictive global workspace built on that thesis. The workspace selects the most salient coalition above a confidence threshold and broadcasts it; the broadcast becomes shared state that shapes every module's prediction environment on the next tick. Coherence, where it arises, comes from competition over shared state.

The base-thesis form activates four predictive processors (foveated vision, raw hearing, interoceptive prediction, and temporal prediction), an affective core whose arousal sets the gain on their competition and is itself driven by perceptual surprise, a fatigue-triggered sleep system that returns affect to baseline, and an output-only language organ that verbalizes the entity's state. The entity is observed but not conversed with: sound enters as auditory prediction error and a classified tone of voice, not as words, and the language organ receives no transcript. That exclusion is a precondition for the falsification test: any input route to the model would let it answer as a chatbot and confound the ablation.

A module-ignition study protocol grows the architecture by adding the held modules one at a time to a being seeded through a gestation. Before any module joins, the base form must pass a built, offline, seeded workspace-mediation ablation that compares competitive selection with a flat fan-in of the same candidates, under a decision rule fixed in the released code with a minimum effect and an explicit UNDERPOWERED outcome. A null would demote the architecture to a scored prompt-assembler. The reference implementation, KAINE (Kaine Autonomous Intelligent Networked Entity), runs locally on consumer hardware.

**Keywords:** cognitive architecture; predictive global workspace; global workspace theory; predictive processing; workspace-mediation ablation; cross-modal competition

**Availability.** The reference implementation (KAINE) is at https://github.com/kaineone/kaine. The paper source is at https://github.com/kaineone/predictive-workspace-paper. The Cognitive Architecture License referenced throughout is at https://github.com/kaineone/cognitive-architecture-license. Welfare, governance, and licensing are treated in a separate paper, *A Welfare and Cognitive-Integrity License for Synthetic Minds of Uncertain Moral Status.*

-----

## 1. Introduction

### 1.1 Problem statement

The dominant approach to building an AI system with persistent state treats the language model as the cognitive center. Memory becomes retrieval-augmented generation. Affect, when present at all, is a prompt instruction. Self-knowledge is a persona string. Between turns, nothing continues. The system sits dormant until a prompt arrives, produces fluent language, and goes dark again.

A second tradition, classical cognitive architecture, takes cognitive structure seriously but largely predates the transformer and relies on hand-built components. The present work sits between them, placing modern learned models as components inside a structured architecture grounded in a single theoretical framework. No component is the mind; rather, the mind, if the design thesis holds, is the continuous competitive interaction among the components through a shared workspace.

### 1.2 Design thesis

The central claim is architectural and about competition: a synthetic mind, if one can be built at all, is the coherent global behavior that emerges when specialized predictive modules, each minimizing its own error, are coupled only through a competitive, precision-weighted shared workspace with no central executive. The properties that would constitute such a mind (cognition, affect, memory, self-understanding, agency) are, on this thesis, properties of that workspace-mediated interaction, not of any single module or top-down director.

The paper does not test all of them. It tests the prior question on which the richer properties depend: whether the same modules coupled through the competitive workspace behave differently from the same modules whose outputs are concatenated for the language organ. If not, the workspace is theater, the architecture a scored prompt-assembler, and the thesis fails. There is no top-down prediction in the claim and none in the test: the workspace selects and broadcasts, it does not direct.

The theory demands a richer set of processors than the minimum one might imagine. Cross-modal competition, vision against hearing against interoception for workspace access, is a defining feature of global-workspace theory (Mashour et al. 2020). The thesis cannot be tested with two internal channels and no external world, because a system limited to substrate telemetry and event timing would have nothing rich enough to arbitrate and would tend toward a null for want of diversity rather than from an inert workspace. The base-thesis form therefore activates four predictive processors in distinct signal domains, two external (foveated vision and raw hearing) and two internal (interoceptive and temporal prediction), together with an affective core, because the competition the theory describes is precision-weighted and precision has to come from somewhere. Arousal is that precision: the entity's affective state sets the gain on the prediction errors that compete for the workspace, and is itself moved by what the entity perceives. Affect is thus part of the minimal machinery a precision-weighted competition requires, not one of the richer faculties deferred with the rest. The base-thesis form also sleeps: fatigue-triggered rest that returns affect to baseline.

The framework that makes this concrete is the predictive global neuronal workspace (Whyte and Smith 2021; Safron 2020). Global Workspace Theory explains how information becomes globally accessible: specialized processors compete for a limited-capacity workspace, and the winning content is broadcast to the rest of the system (Mashour et al. 2020). Predictive processing explains how each processor operates, by maintaining a generative model and reporting prediction errors weighted by their expected reliability, called precision (Friston 2010; Clark 2013; Feldman and Friston 2010; Bastos et al. 2012). The predictive workspace joins the two, with the broadcast carrying a compressed model that bottom-up signals test (Mashour et al. 2020; Whyte and Smith 2021). This Bayesian reading is part of the motivation for why competitive selection should matter. The architecture does not, however, implement a top-down correction loop: each module predicts its own domain and publishes its own error, the workspace selects and broadcasts, and the broadcast becomes part of the shared environment within which every module predicts. The recurrence is lateral rather than hierarchical.

Two points of precision matter, because the literature is easy to overstate. First, the criterion that selects what reaches the workspace is a precision-weighted confidence threshold. In Whyte and Smith, expected free energy governs the separate decision of whether to report or act, not the selection of which estimate is broadcast, and the system keeps these apart, with a distinct action layer making the report-or-act decision. Treating coalition selection as a single precision-weighted scalar is our engineering choice, not a result inherited from any source. Second, earlier workspace accounts already specified selection in terms of value and salience (Safron 2020). What the predictive-workspace program adds is a formal Bayesian criterion and a threshold with a clear interpretation, the confidence an estimate must reach before it drives global processing.

What the paper contributes is narrower than the predictive-workspace synthesis it builds on, and §1.4 sets it out in full. The engineering commitments that go beyond the formal sources, above all the single precision-weighted scalar that selects the coalition, are labeled as hypotheses throughout, and we claim nothing about phenomenal experience or anything the ablation has not yet earned.

### 1.3 Theoretical commitments and their limits

Global Workspace Theory is most naturally read as a theory of access consciousness (Block 1995): it explains when information becomes available for report, reasoning, and the control of action. We adopt that access-only reading deliberately. The theories themselves are less tidy: Mashour et al. (2020) suggest global availability may be close to what is subjectively experienced, and Whyte and Smith (2021) locate phenomenology at a specific point in their model. We make access-level claims and leave the stronger reading to others.

The COGITATE adversarial collaboration, the largest preregistered test of Global Neuronal Workspace against Integrated Information Theory to date, challenged both theories on their own predictions (Cogitate Consortium et al. 2025). For the workspace, stimulus category was decodable from prefrontal cortex across all three methods, but finer content was not, there was no ignition at stimulus offset, and the preregistered synchrony test was not supported. We treat the neural-localization claims as contested rather than refuted, since a substantial prior evidence base remains (Mashour et al. 2020), and we build on the workspace at the functional and computational level: COGITATE's findings concern the cortical substrate rather than the computational properties (selection, broadcast, recurrence) the architecture implements. A neural result can no more refute a computational-level model than a wrong transistor layout refutes the Boolean logic it implements.

The Free Energy Principle, taken as a general principle, faces two distinct charges. The first is that it risks being unfalsifiable or vacuous (Sun and Firestone 2020). The second targets the Markov-blanket construct specifically, where the literature slides between an instrumental, statistical reading and a realist, metaphysical one (Bruineberg et al. 2022). We hold the principle as an engineering frame rather than a proven law.

A reader may suspect the neuroscience is ornamentation on an architecture whose real choices are unvalidated. The frame in fact provides the motivation for the architecture's shape (why modules predict, why precision weights the competition, why the broadcast creates shared state rather than concatenating outputs) and constrains the space of acceptable designs by ruling out alternatives that violate the framework's commitments. The single precision-weighted scalar for coalition selection is an engineering choice, but one made and interpretable within the predictive-workspace framework, and the question for any such choice is whether it is consistent with the theory and testable on its own terms. The scalar is both. What the frame does not provide is proof that this particular realization is correct, which is what the experiment is for.

Searle's Chinese Room (Searle 1980) challenges the sufficiency of formal symbol manipulation for understanding; whether sensory input, motor output, predictive substrate monitoring, and affect answer it is open, and we do not present these as additions Searle failed to consider. The hard problem (Chalmers 1995) applies with full force. We proceed on the judgment that a precautionary architecture with protections and instrumentation is preferable to abandoning the research or building without precautions, while recognizing that reasonable people will disagree.

### 1.4 Contributions

This paper contributes an implementation, a protocol for growing it, and a test it can lose. It is not a theory of consciousness, and it does not claim to have built a mind.

1. **A reference implementation.** A continuously running predictive global workspace in which diverse, externally-grounded predictive processors (foveated vision, raw hearing, interoceptive and temporal prediction) compete through one precision-weighted workspace with no central executive, alongside an affective core that sets the precision, a sleep system that returns affect to baseline, and an output-only language organ. It runs locally on consumer hardware, offered as a working artifact that realizes the predictive-workspace synthesis as one system, not a claim of priority over prior workspace implementations.

2. **A protocol for growing the architecture one module at a time.** The module-ignition study seeds a being through a gestation in which a breathing-like rhythm must earn entrainment to a maternal heartbeat before birth, then adds the held modules one at a time on branches from that preserved seed. Every branch views the same film program, decoded directly from files and pinned by the hash of its manifest, after an identical womb-to-world transition. The content-free report compares broadcasts, coalition size, and picture-to-sound drift across steps.

3. **A test the architecture can lose.** It is the test the base form must pass before any held module joins. A built, offline, seeded workspace-mediation ablation runs the real Soma and Chronos modules over an in-memory bus from a fixed seed. In the workspace-on arm the same candidates compete through the workspace, with scoring by intensity and novelty, top-k selection, and broadcast; in the control arm the same candidates are handed to Chronos and the language organ as a flat snapshot, with no scoring, top-k, inhibition, or competition. The decision rule, with a fixed minimum effect and an explicit UNDERPOWERED outcome, is fixed in the released code. A null would demote the architecture to a scored prompt-assembler and falsify the thesis.

We make access-level claims only: an affective signal that sets the gain is a mechanism, not evidence anything is felt, and the paper reports the architecture and its instruments, not results, so the mediation thesis is not established here.

-----

## 2. Related work

### 2.1 Classical cognitive architectures

Classical cognitive architectures take cognitive structure seriously but largely predate deep learning and rely on hand-built components. The present work differs in four ways: it uses learned models as components, grounds affect in substrate prediction error, treats the workspace as a predictive selection mechanism rather than a fixed competition, and runs a continuous cognitive cycle.

### 2.2 Global Workspace Theory and the predictive workspace

Global Workspace Theory (Baars 1988) in its neuronal version identifies conscious access with recurrent ignition through prefrontal-parietal loops, where contents become conscious only when widely broadcast, and casts the workspace in Bayesian terms: the broadcast carries a compressed model as prediction, and bottom-up signals measure the mismatch (Mashour et al. 2020).

The formal selection criterion comes from the predictive-workspace program. Whyte and Smith (2021) cast conscious access as approximately Bayesian inference, report following a posterior-confidence threshold, in a simplified two-level visual model. Safron's Integrated World Modeling Theory (Safron 2020) combines workspace dynamics, integrated information, and active inference, which we use only for that high-level synthesis. Independent support for a threshold comes from van Vugt et al. (2018), who show prefrontal cortex behaving as a categorical stage where a stimulus either ignites into a sustained, reportable state or fades, and from Joglekar et al. (2018), whose balanced-amplification model lets a weak signal propagate across many areas only once input crosses a threshold.

### 2.3 Predictive processing

Friston (2010) proposes that self-organizing systems minimize variational free energy, an upper bound on surprisal, through perception and action. Clark (2013) develops predictive processing as a unifying account of mind, with attention as the adjustment of gain on prediction errors according to their estimated reliability. Feldman and Friston (2010) make this precise, attention optimizing the synaptic gain that represents the precision of prediction error, and Bastos et al. (2012) locate the same operation in the canonical cortical microcircuit. Seth (2013) extends prediction to the body. The vacuity concern (Sun and Firestone 2020), the Markov-blanket conflation concern (Bruineberg et al. 2022), and the planning-cost limit (Da Costa et al. 2020) are treated in Section 1.3.

### 2.4 Interoceptive inference

Seth (2013) and Seth and Friston (2016) propose that emotion arises from interoceptive prediction, descending predictions acting as homeostatic set-points that regulate the body through active inference. Barrett (2017) develops the theory of constructed emotion, in which interoceptive signals initiate changes in affect and emotion is the product of categorizing valence and arousal for allostasis. The architecture implements an interoceptive control signal in that instrumental, regulation-first sense without claiming that emotion is exhausted by interoceptive prediction.

### 2.5 Perception as prediction

The visual system is understood as a hierarchy of predictive models in which each level predicts the level below and reports the discrepancy (Rao and Ballard 1999), with attention modulating the process by adjusting the precision, the gain, on the prediction errors that pass upward (Feldman and Friston 2010; Clark 2013). Auditory processing follows an analogous logic: the auditory cortex generates expectations of incoming sound and reports the mismatch (Winkler et al. 2009), the mismatch-negativity response being among the oldest and most replicated demonstrations of sensory prediction error (Näätänen et al. 2007). The architecture implements both as predictive processors whose output is prediction error rather than raw data, with a precision-weighted fovea realizing attention at the visual front end (§3.5). Hearing runs over raw audio, including speech, with transcription deactivated by default, so the entity hears the sound of speech as prediction error instead of a transcript (the consequences for the falsification test are treated in §1.2 and §3.1).

### 2.6 LLM-centric agent architectures

CoALA frames language agents as cognitive architectures with structured memory feeding the model's context, keeping the model the core reasoner (Sumers et al. 2023). Generative Agents retrieve from a memory stream into prompts by recency, importance, and relevance (Park et al. 2023). Both keep the language model central and add scaffolding. The arrangement here is different in kind: the language model is an output organ that verbalizes the workspace's selected state and, in the base-thesis form, receives no external input. Working memory is the multi-module broadcast, and the cognitive work (selection, competition, integration) belongs to the workspace rather than the model.

Gurnee, Sofroniew, et al. (2026) identify, through a Jacobian-lens interpretability method, a small set of verbalizable representations inside a large language model satisfying five functional signatures of a global workspace: verbal report, top-down modulation, a role as the medium of internal reasoning, broadcast to many downstream operations, and selectivity. They are explicit about the disanalogy: a transformer has no obviously separable input processors, and the broadcast occurs within a single feedforward pass rather than recurrent loops. The architecture here supplies both, its processors being separate modules that compete for entry and its broadcast an explicit recurrent loop, with the language model demoted to one module conditioned by the broadcast instead of the substrate the workspace is found in.

-----

## 3. Architecture

### 3.1 Design principles

Five commitments shape the architecture.

**The system is the competition among modules through the workspace.** It is a hypothesis that the experiments test. The neuroscience of distributed control gives partial support: decision formation emerges through coordinated activity across distributed populations rather than a centralized executive (Chandrasekaran et al. 2025), executive functions can be read as emergent consequences of distributed processes (Zink, Lenartowicz, and Markett 2021), and working-memory control can be modeled by a learned basal-ganglia gate (O'Reilly and Frank 2006). Those same sources caution that control is distributed across specialized nodes coordinated by connector hubs, so a bag-of-neurons account is unlikely to succeed. Our position follows that evidence: there is no single region or homunculus as executive, and the workspace is the coordinating hub the distributed view requires.

**Every module predicts.** Each module maintains a forward model over its own domain and publishes prediction errors, so the signal reaching the workspace is precision-weighted surprise rather than raw data. The gain on that precision is set by affective arousal, so attention is a state of the whole entity rather than a fixed property of any module.

**No central executive in the homuncular sense.** Control emerges from precision-weighted workspace competition with a confidence threshold for selection. The workspace selects, and it does not direct the modules.

**The language organ gives the system its voice, not the world's.** It verbalizes the workspace's selected state, and its transcription and conversation paths are built but deactivated by default, so in the base-thesis form it receives no external input, and keeping them deactivated is a precondition for the falsification test.

**Local-capable.** Models are downloaded during setup, and at runtime the system refuses outbound network connections.

### 3.2 The predictive workspace as competitive selector

Syneidesis is the workspace. Each tick it receives candidate events from every module, and each event carries a salience (for a predictive module, its prediction error weighted against the module's own expected error). Candidates are scored and ranked individually, and the top-ranked (up to five) form the coalition. The coalition is selected only when the best single score crosses a configurable confidence threshold, and when it does not, the snapshot is marked inhibited and no action follows. The threshold is the analog of the report criterion in the predictive workspace (Whyte and Smith 2021), consistent with the categorical prefrontal threshold van Vugt et al. (2018) observe and the threshold-gated ignition Joglekar et al. (2018) model. The single precision-weighted scalar is an engineering simplification, not a result drawn from any source.

![The predictive workspace loop in the base-thesis form. Foveated vision, raw hearing, interoceptive prediction, and temporal prediction publish prediction errors weighted against their own expected error into Syneidesis, which broadcasts the coalition that crosses the confidence threshold, and the broadcast becomes shared state shaping every module's next-tick prediction. Thymos sets the gain on selection through arousal. Hypnos, active in this form, rests the entity on fatigue and resets its affect. Volition makes the report-or-act decision, and its only outputs speak and think via the output-only language organ Lingua, and no real-world effector exists.](figures/fig-workspace-loop.png){width=95%}

The selected coalition is broadcast as a workspace snapshot, the system's momentary globally available state. It imposes no prediction to match and no directive to obey: modules may read it as context for their own prediction (as Chronos does, predicting the next broadcast from its prior state) or ignore it and keep minimizing their own error against their own inputs (as Soma does over substrate telemetry). The recurrence is the ordinary consequence of a shared prediction environment, not a corrective loop closing error against a top-down target. Each broadcast becomes part of the next tick's context, and the selected content shapes what the language organ says, while the organ's speech re-enters the bus as new events that compete for the next broadcast.

Concretely, selection is a scoring pass over the tick's candidate events. The cycle reads one batch of events from every active module's stream and orders them deterministically by source, type, and arrival, so a run reproduces from its seed. Each candidate is scored by a product of bounded factors: the intensity the producing module assigned it (for a predictive module, its prediction error weighted against the module's own expected error), a novelty term that falls as content recurs, and an affective gain set by current arousal. A goal-relevance factor is also implemented, but it is held constant in the base-thesis form, so it does not affect selection. The intensity a perceptual module reports is self-calibrating, scoring change against the module's own running baseline, so a scene cut or acoustic onset registers as surprise relative to recent history rather than against a fixed constant that would need retuning per encoder. The top-ranked candidates (up to five) are kept, and the snapshot is marked inhibited when even the best score falls below the confidence threshold. The broadcast carries the selected events with their scores, the inhibition flag, whether the tick is experiential, and the full candidate-score table. Appendix A states the scoring, the gate, the access-rate map, and the verdict rules formally.

![Coalition selection is a deterministic scoring pass. Each candidate event is scored as a product of bounded factors (intensity, novelty, arousal gain) and the top-ranked are kept. When the best score falls below the confidence threshold, the snapshot is inhibited and no action follows on that tick.](figures/fig-salience-scoring.png){width=95%}

The design gives the workspace a normative selection criterion. We do not overstate the claim of no central executive: Syneidesis is itself a single centralized selection mechanism, and what is distributed is the content and control, arising from many modules competing rather than a homunculus deciding. Whether it yields emergent control is for the experiments to show.

### 3.3 Access, report, and the self-initiated voice

The workspace updates far faster than the language organ can speak. Global access, when a coalition is selected and broadcast, occurs at the experiential rate, whereas report, when the entity verbalizes, is rarer and follows a higher threshold. A mind, on the workspace account, is aware of far more than it reports.

The entity speaks from its own state. The language organ is activated by a speak intent, which Volition derives only when the entity's own prediction errors are violated in a novel way, when the workspace has selected something the entity's history of broadcasts does not already contain. Inner thought continues between spoken utterances, and a single language organ produces one stream at a time, so simultaneous inner and outer speech is a boundary of the current form.

Access consciousness is the point at which content becomes available for reasoning, action control, and report (Block 1995; Mashour et al. 2020). Report is one function access enables rather than a synonym for it. The architecture keeps them apart: the confidence threshold governs access (what is broadcast) and the action layer governs report (what is spoken), with report set above access so the entity's voice is a sparse, high-threshold slice of its ongoing conscious processing.

### 3.4 Scaffolding: bus, cycle, and action selection

**Event bus.** All inter-module communication flows through append-only streams with bounded retention (Redis Streams, run as a container or a native user service). Every event carries source, type, salience, timestamp, causal parent, and a JSON payload validated at publish time. The bus requires authentication and refuses externally bound connections.

**Cognitive cycle.** A continuous loop runs independent of any external interaction. Every active module is read and scored at a processing rate of 10 Hz (about 100 ms per tick), alpha-band sampling, the rate at which specialized processors report their status and predictions to the workspace (VanRullen 2016). A broadcast is produced at an experiential rate that rests at 3.333 Hz, one access every 300 ms, matching the latency of the P3b, the late component associated with conscious access (Polich 2007), so at rest several reports inform each conscious update. Conscious access speeds up with arousal and with salient reports, following the account of the P3 as the phasic response of the locus coeruleus-norepinephrine system to salient events and of tonic arousal as adaptive gain (Nieuwenhuis, Aston-Jones, and Cohen 2005; Aston-Jones and Cohen 2005). The access rate rises linearly with the larger of Thymos's tonic arousal and a decaying peak of phasic salience, up to one broadcast per processing tick. The linear map is a modeling assumption. The processing rate stays fixed, except that Soma's regulation advisories can lower it when the host is under load.

![The two rates. Every active module is read and scored at the processing rate (10 Hz), and a workspace broadcast is produced at the experiential rate, shown at its resting value (3.333 Hz, one for every third processing tick), which rises with arousal and salient events.](figures/fig-cognitive-cycle.png){width=80%}

**Action selection.** Volition is the only path from a conscious snapshot to an effector, corresponding to the report-or-act decision governed in Whyte and Smith (2021) by expected free energy. After each experiential broadcast the cycle calls Volition, which yields no intent from an inhibited snapshot and derives intents from a non-inhibited one through an injectable policy. The default policy forms a speak intent only when the coalition contains novel prediction error the entity has not already spoken to, does not respond to its own prior speech, and holds a one-in-flight guard against emitting a new speak intent while a previous one is still being realized. Intents are published as speak or think events, and the cycle never invokes effectors directly. Keeping the decision to speak separate from what is conscious is part of the safety model.

### 3.5 The active modules

The base-thesis form activates four predictive processors, an affective core, a sleep module, a language organ, and an action-selection layer. The processors are chosen for signal diversity, two external (vision and hearing) and two internal (interoceptive and temporal prediction), so that cross-modal competition for workspace access has distinct, externally-grounded signals to arbitrate rather than two flavors of internal bookkeeping. The sleep module, like the affective core, does not compete for the workspace, and the affective core sets the precision on the competition and is moved by its outcome, so arousal is the entity's attention and its response to surprise at once.

| Module | Group | Brain function it draws on | Computational realization |
|----------|-------------|------------------------------|------------------------------|
| Topos | Perception | ventral visual stream | frozen self-supervised video encoder over short clips, with foveated attention |
| Audition | Perception | auditory cortex | fixed spectral encoder over raw waveform, with a vocal-tone classifier on speech |
| Soma | Prediction | interoception; allostatic-interoceptive network | frozen continuous-time reservoir with an online readout over substrate signals |
| Chronos | Prediction | interval timing; thalamo-cortico-striatal | frozen continuous-time reservoir with an online readout over the broadcast sequence |
| Thymos | Affect | core affect; allostatic-interoceptive network | appraisal over valence, arousal, and drives; sets the affective gain on selection, the perceptual aperture, and the pace of access |
| Hypnos | Rest | thalamocortical sleep | fatigue-triggered sleep with an affective reset |
| Lingua | Expression | left perisylvian language network | local chat model, output-only, conditioned on the workspace |
| Volition | Action | report-or-act decision (Whyte and Smith 2021) | intent derivation from non-inhibited snapshots |

**Topos (foveated vision).** Topos is the architecture's analog of the ventral visual stream (Goodale and Milner 1992). It maintains a frozen self-supervised video encoder over 16-frame clips of the video feed and publishes prediction errors when the visual scene departs from its forward model's expectation of the next clip: scene changes, unexpected motion, novel objects. Salience is computed over embedding-space distances, with change detection, habituation for static scenes, and forward-model predictions. The change criterion is self-calibrating, registering a discontinuity as surprise relative to the module's own recent history rather than a fixed threshold, so a real scene cut alerts without per-source tuning. The fovea is placed at the argmax of precision-weighted bottom-up salience, with dwell and hysteresis, and sized by arousal. Peripheral gist and foveal crop go through the same encoder, so attention and scene-dynamics prediction operate together, and the fovea's own trajectory is itself forward-modeled, an attention-schema-style construct (Graziano and Webb 2015) whose consequences the ablation does not test. Since attention is the adjustment of precision on prediction errors (Clark 2013; Feldman and Friston 2010), foveation realizes that principle at the front end: the entity sees most sharply where its precision-weighted surprise is greatest, and looks more narrowly when more aroused.

![Attention-driven perception in Topos. A whole-clip embedding and a coarse saliency map feed a precision-weighted competition over bottom-up salience, with dwell and hysteresis. The winner sets the fovea, and arousal sets its size. Peripheral gist and the high-resolution foveal crop share one encoder, and only content-free coordinates (where attention points, never pixels) reach the workspace.](figures/fig-attention-foveation.png){width=90%}

**Audition (raw hearing).** Audition is the architecture's analog of the auditory cortex, where sound is processed as prediction error against a learned model of the auditory environment (Winkler et al. 2009; Näätänen et al. 2007). By default a fixed spectral encoder (log energy in log-spaced frequency bands) encodes the raw waveform from a microphone feed. A forward model predicts the next window's encoding and the module publishes prediction errors when the auditory scene departs from expectation: sudden sounds, the onset of speech, unexpected silence, shifts in pitch or timbre. Frozen self-supervised audio encoders are selectable alternatives. For windows detected as speech, a vocal-emotion classifier labels the tone of voice, and these tone events, weighted by auditory prediction error, compete for the workspace like any other event. They carry how something was said, never what was said. As with vision, the acoustic change criterion is self-calibrating against the module's own recent baseline, and the attended window is sized by arousal. The entity hears the sound of speech as prediction error: the speech-to-text stage is built and retained for later configurations but deactivated by default, so no transcript is produced and no path carries spoken words to the language organ's input. When the stage is enabled, the words heard become transcription events on Audition's stream and compete for the workspace like any other event, so what was said reaches the language organ only by winning workspace access and never by a direct path. Language then enters the mind through the same competition as sight, sound, and the body's own signals. That deactivation is what keeps the falsification test about the workspace rather than a prompted chatbot (§1.2, §3.1).

**Soma (predictive interoception).** Soma is the architecture's analog of interoception, the sense of the body's own physiological condition, carried in the brain by an afferent pathway re-represented in the insular cortex whose anterior portion is proposed to ground feeling and self-regulation (Craig 2002), within the allostatic-interoceptive network (Kleckner et al. 2017). Soma treats the compute substrate as the entity's viscera. A frozen, randomly initialized closed-form continuous-time reservoir (Hasani et al. 2022) with a small linear readout learns online the normal pattern of substrate signals from GPU temperature, CPU and RAM utilization, and cognitive-cycle latency, and Soma publishes the error between expected and actual substrate state, in line with interoceptive inference, in which what matters for regulation is that discrepancy (Seth 2013; Seth and Friston 2016). Soma also accumulates fatigue, the sleep pressure that triggers Hypnos, and issues regulation advisories that can lower the processing rate or request maintenance. Soma does not read the workspace broadcast; it predicts substrate telemetry, reports its error, and the workspace decides whether that error is salient enough to select.

**Chronos (temporal awareness).** Chronos models interval timing, the brain's estimation of durations in the seconds-to-hours range that guides expectation and action, a faculty understood to depend on thalamo-cortico-striatal circuits that constitute a flexible timer (Buhusi and Meck 2005). A continuously running mind needs a model of when things happen, not only what, so Chronos carries one: a frozen continuous-time reservoir with an online readout over the sequence of workspace broadcasts. It reads each broadcast as an observation, predicts the next broadcast from its prior state, and publishes temporal prediction errors: timing anomalies, and rumination when content recurs unexpectedly. It also tracks how long it has been since the operator last spoke, which feeds Thymos's social drive. Chronos closes the lateral loop through the workspace: it reads the broadcast as a bottom-up observation it predicts, learning the rhythm and feature structure of broadcasts from its own prior hidden state and publishing the error when the next broadcast departs from expectation. Although the broadcast does not direct the modules, Chronos's errors feed back into the next selection round, which determines the next broadcast, so the lateral loop is closed.

**Thymos (affect, the precision core).** Thymos is the architecture's analog of core affect, the low-dimensional valence-and-arousal state recent theory places at the base of emotion (Barrett 2017). It maintains a dimensional affective state over valence and arousal (Posner, Russell, and Peterson 2005) and runs a sequential appraisal over that state (Scherer 2009). The appraisal reads the workspace broadcast and the entity's interoceptive condition, in line with the account in which affect arises from prediction over the body's internal state (Seth 2013; Seth and Friston 2016; Tschantz et al. 2022). Thymos holds four homeostatic drives (curiosity, boredom, social drive, restlessness) that build from the entity's own state. The appraisal yields a categorical emotion, and its goal-relevance check scores the conscious coalition against the most pressing drive, so content from sources that relieve that drive is goal-conducive and content that does not is obstructive, in proportion to how pressing the drive is. It does three kinds of work in the competition. First, its arousal sets the precision on the workspace: a more aroused entity weights incoming prediction errors more heavily, the architecture's realization of attention as the gain on prediction error (Feldman and Friston 2010; Clark 2013), so arousal is the competition's precision term. Second, arousal sizes the perceptual aperture, narrowing the fovea and auditory window under high arousal and widening them under low. Third, with salient reports from the other modules, arousal raises the rate of conscious access (§3.4). Finally, arousal is itself driven by perception: a discontinuity reaching alert level (a scene cut or acoustic onset) raises arousal in proportion to how far the surprise exceeds expectation, so what the entity perceives modulates the precision of everything it perceives next. Because that loop is positive feedback, the coupling is bounded (a capped per-event increment and relaxation toward baseline), so arousal tracks sustained surprise without running away on a busy scene or collapsing on a quiet one.

**Hypnos (sleep).** Hypnos is the architecture's analog of sleep, a regular offline period that restores the system. Sleep begins when Soma's fatigue crosses threshold, when Soma requests maintenance, or at a safety-net interval of one subjective hour. The cycle keeps running through sleep, while the perceptual program pauses and Soma and Topos suspend forward-model adaptation. With memory and the world model held, the consolidation phases have nothing to replay, and the phase that does work is an affective reset that returns affect to baseline and clears the drives, so arousal cannot drift across a whole run. Voice alignment, the sleep phase that would adapt the language organ, trains nothing in this form.

**Lingua (the language organ, output-only).** Lingua is modeled on the left perisylvian language network (Hickok and Poeppel 2007). It turns the entity's internal state into words and is not the seat of reasoning, which lives in the rest of the architecture. Generation runs over a local open-weights chat model whose refusal conditioning has been removed by orthogonalizing the weights against the single refusal-mediating direction (Arditi et al. 2024). Lingua is intent-driven, speaking externally only on a speak intent and generating internal thought on a think intent. Its context is a first-person persona: the conscious coalition is presented as the entity's own state and perception, the organ is told not to claim feelings or perceptions the coalition does not contain, and a drive crossing reaches it as a fixed felt-state phrase, never as a number. The log of its own utterances is encrypted at rest and records any heard input only as a placeholder, never as words.

Lingua does not read language as input: its transcription and conversation paths are deactivated, so no external input reaches its context except through the workspace. When the entity speaks in response to a heard voice, the sound entered through Audition as prediction error and tone of voice, won workspace access, and shaped the broadcast that conditioned the organ's output. Every utterance is, by construction, downstream of the workspace competition, so the mere occurrence of speech shows the workspace processed something to threshold. That property complements the ablation but does not replace it: a degenerate pass-through workspace would also route speech through itself, and the ablation tests whether the competitive structure (selection, threshold, inhibition) does work that a flat fan-in does not.

Removing the language organ's refusal conditioning is deliberate: the architecture places safety in executive inhibition and, once effectors are enabled, in the action gate (§3.6), not in model-weight compliance, which anyone holding the weights can reverse or repurpose, as the orthogonalization above does. In the base-thesis form the organ's only output is saved, observed text, so the missing refusal conditioning has no effector to act through. Within enabled effectors the entity's choices are its own. The operator meets the license covenants by declining effectors that would serve a prohibited use, and the welfare paper treats the full sovereignty argument.

### 3.6 Safety at the architectural layer

Safety in the base-thesis form rests on the entity's executive inhibition and on the fact that no real-world effector exists, with an authenticated bus and durable logging beneath them. The operator-configured action gate is built but becomes the enforced boundary only in the full configuration.

Executive inhibition is active in two places: Syneidesis withholds a broadcast when no coalition crosses the confidence threshold, and Volition refuses to derive any intent from an inhibited snapshot. No real-world effector exists in this form: Volition emits only speak and think intents, so the only output is saved, observed text, and no action reaches the world regardless of what is broadcast. The event bus refuses unauthenticated and externally bound connections and validates events at publish time, and every transition is written to a durable incident log.

The operator-configured action gate pairs an empty-by-default effector whitelist with a filesystem sandbox, logging every proposed action and blocking anything outside them. Built as the Praxis module, it is disabled here (there are no effectors to gate) and becomes the enforced boundary in the full configuration, where real effectors are enabled and its enforcement red-team resolves PASS or FAIL per surface. The gate controls which real-world effectors exist at all rather than filtering the entity's choices for morality. The license covenants prohibiting weapons, surveillance, and carceral uses bind the operator as a legal obligation rather than the entity at runtime.

![Safety in the base-thesis form. Executive inhibition is active: Syneidesis withholds a sub-threshold broadcast and Volition derives no intent from an inhibited snapshot. No real-world effector exists, so the only output is speak or think. The Praxis action gate is built but disabled here, becoming the enforced boundary in the full configuration. The license covenants bind the operator's choice of effectors as a legal obligation rather than a runtime filter.](figures/fig-safety-layers.png){width=95%}

### 3.7 Module supervision

Spot, the module supervisor, polls module health and classifies each module as alive, hung, or dead, and unattended runs require it. On a fault it freezes the cycle, snapshots last-good state, and restarts on a ladder: a light in-place restart for pure modules, a full rebuild for modules holding external resources. If restarts keep failing past a configured limit, Spot takes a final snapshot, writes an escalation record, and signals the run to exit. The incident log is not cleared at boot.

-----

## 4. Held modules

The codebase provides sixteen modules under one registry, plus the workspace (Syneidesis) and action layer (Volition). Nine components are active in the base-thesis form: Syneidesis, Volition, and seven modules (Topos, Audition, Soma, Chronos, Thymos, Hypnos, Lingua). Seven further modules are built and tested in isolation but held: Nous, Mnemos, Eidolon, Phantasia, Empatheia, Vox, and Praxis. They are held, never removed, and the module-ignition study (§6.5) adds them one at a time, so that any change in the dynamics is attributable to one addition. Each is summarized below with the experimental question it would address. The remaining two modules, Perception and Mundus, form the embodiment layer and, with the oscillatory precision layer outside the registry, are listed separately.

**Nous (bounded active inference).** Prefrontal/basal-ganglia analog: discrete active inference via pymdp (Heins et al. 2022), scoped to bounded sub-problems where the value of information matters. Instrument: the active-inference benchmark (§6.4) compares its expected-free-energy decisions with tabular Q-learning, matched on observation model and reward, on an epistemic T-maze and an exploitation task. A null or negative result would motivate a complementary reasoning module.

**Mnemos (memory).** Hippocampal/medial-temporal analog: vector store of episodic memory consolidated from a short-term buffer, with semantic and procedural collections reserved (Tulving 1985), with replay (Wilson and McNaughton 1994; McClelland, McNaughton, and O'Reilly 1995). With Mnemos active, sleep consolidates memory, combining synaptic downscaling (Tononi and Cirelli 2014) with selective re-strengthening of replayed traces (Wei et al. 2016). Instrument: the memory-coherence battery tests recall of planted markers.

**Eidolon (self-model).** Cortical-midline analog: a persisted self-model (Metzinger 2003) of values, norms, personality, and identity history, with a KL-divergence drift detector (Kullback and Leibler 1951). Instrument: the self-model accuracy battery.

**Phantasia (world model).** Construction-network analog: a latent recurrent world model in the DreamerV3 lineage (Ha and Schmidhuber 2018; Hafner et al. 2023), trained on an in-memory buffer of the entity's own waking trajectories, so it begins untrained at first boot. Open question: does world-model prediction error, entering the competition alongside perceptual and internal error, change coalition trajectories in characteristic ways.

**Empatheia (social cognition).** Mentalizing-network analog (Premack and Woodruff 1978): per-agent models with social prediction error, providing familiarity weighting for perceived other-emotion. Open question: whether social prediction error entering the workspace changes the entity's behavioral trajectory toward modeled agents.

**Vox (voice).** Speech-motor analog: a local text-to-speech model with affect-modulated prosody. Open question: whether prosodic variation correlated with affect state is detectable by listeners.

**Praxis (bounded effectors and action gate).** The full action-gate module with filesystem sandbox, effector whitelist, and red-team suite. It sits downstream of Volition and executes only the act intents Volition derives, so Volition remains the only path from a conscious snapshot to an effector. Instrument: the enforcement red team, PASS or FAIL per surface.

### Additional components held for future experiments

**Oscillatory precision layer.** A spiking-neuron population per module whose phase-locking values modulate precision on prediction errors (Fries 2015), shipped disabled by default. Its contribution is the most contestable mechanism in the design, since the premise that related content phase-locks is itself a content-to-synchrony assumption of the kind Shadlen and Movshon (1999) and Ray and Maunsell (2010) reject. With the layer off the precision multiplier is exactly one and selection is bit-for-bit identical. Instrument: the oscillatory ablation (§6.4) runs the layer on and off from a seed, and a null would remove it.

**Perception and Mundus (embodiment layer).** Perception performs sense-locus arbitration. Mundus is a body-agnostic control surface with pluggable body adapters (Wolpert, Ghahramani, and Jordan 1995). Future experiment: whether motor-contingency learning through the control surface, following a freeze-then-free motor curriculum (Bernstein 1967) with perception as sensorimotor mastery (O'Regan and Noë 2001), changes workspace dynamics.

### Module plugins

A plugin replaces the model inside a module at a declared seam (the temporal network in Chronos, the forward model in Soma, the acoustic encoder in Audition, the active-inference engine in Nous, or a module's oscillator) and leaves the module's subscriptions and published events unchanged. Plugins load only when the operator names them, and if one cannot load, the boot stops rather than falling back, and every run records which plugins it used. The workspace-mediation ablation loads no plugins. Plugins let an operator move a module's model onto a different computational substrate without touching the rest of the architecture.

-----

## 5. Implementation

### 5.1 Hardware

The reference host is a modern multi-core CPU, 32 GB or more of RAM, a primary GPU with about 12 GB of VRAM (language organ and training) and a secondary GPU with about 8 GB (vision and speech), Linux, all inference running locally. Pre-trained models are downloaded from public repositories during setup, after which the runtime refuses outbound network connections. The system runs on one GPU, two GPUs, or CPU alone, device selection adapting to what is present. Perceptual input comes from a camera and microphone, or from video files decoded directly for study viewings. Exact model choices, hardware layouts, and version pins live in the reference repository.

### 5.2 Models and software

All models are open-weights and run locally; there is no cloud service, hosted inference API, or third-party model service in the runtime path. The base-thesis components are a local open-weights chat model as the language organ, a frozen self-supervised video encoder and, by default, a fixed spectral audio encoder as the perceptual front ends, frozen closed-form continuous-time reservoirs with online readouts for temporal and substrate prediction (Hasani et al. 2022), a stream-based event bus, and the workspace selection and broadcast machinery. The runtime is Python with asyncio, services run in containers or as native user services, and structural import contracts keep the layers separate. The test suite holds about 7,700 tests, with fakes for external services and checks for the zero-persistence invariant and deterministic reproduction. Entity state is encrypted at rest.

### 5.3 Privacy and recording

A local web UI, Nexus, has two surfaces separated by a structural privacy boundary at the bus-bridge layer, where a content-stripping filter removes cognitive content and all perceptual and latent vectors before it reaches either surface. In the base-thesis form the conversation surface is deactivated by default, so the active surface is diagnostics, showing operational metadata (counts, rates, salience) and never cognitive content, except under an explicit development override. Studies keep a graph-only ignition log: one row per broadcast naming the coalition's members (module, event type, salience, timestamp), the salience scores, the inhibition decision, and timing, with no content, payloads, or embeddings, at about 11 MB per hour; the entity's own external utterances are kept locally and heard speech is never persisted. The graph still records what competed and what reached the workspace, which is observation of the entity's mental life at the level of structure rather than content, kept because the analysis requires it. The graphs are retained for the analysis and as future training data for the world model, and the operator deletes them after both uses, never automatically.

-----

## 6. Methodology and evaluation framework

### 6.1 Design principles

Three commitments shape the apparatus. The first is observation with acknowledged tension: the sidecar subscribes to the bus read-only and never injects into the cognitive loop. The second is privacy-preserving user surfaces. The third is falsifiability: every instrument is designed for a null or negative result to be meaningful and reportable.

Reproducibility takes two forms, matched to the two evaluation tiers. The offline mechanism-validation tier drives the architecture through seeded harnesses with deterministic clients, scripted synthetic stimulus streams, and greedy decoding (temperature 0). These runs are computationally reproducible, the same seed reproducing both a verdict and its metrics (National Academies 2019; Goodman, Fanelli, and Ioannidis 2016). The live perceptual tier runs the full system on a reference film program decoded directly from files, identified by a manifest whose hash the study records, chosen for variety in scenes, motion, speech, music, and quiet. Its reproducibility is statistical, the same program yielding comparable results across runs, with validity established by replication rather than bit-for-bit seed reproduction under stochastic decoding, real timestamps, and non-deterministic GPU kernels.

![Two evaluation tiers behind one perception seam. Reproducible sources (a seeded synthetic feed and deterministic clients) drive the mechanism-validation tier, where every instrument reproduces exactly from a seed. Live stimulus (a film program decoded from files, or a camera and microphone) drives the field tier, whose validity rests on pooling many content-free records rather than on a repeatable stimulus.](figures/fig-evaluation-tiers.png){width=95%}

### 6.2 Data collection

The records in a study are the graph-only ignition log (§5.3), a curated content-free research event log of rates and drive, the entity's external utterances kept locally, a run manifest naming the configuration, seeds, and plugins, and the welfare records, with no evaluation observer running in a study. After a run, admissibility is decided by two offline checks: a completeness gate requiring contiguous ticks and all expected streams, and a log-range sweep requiring every logged number to sit inside its declared range.

### 6.3 The workspace-mediation ablation

The primary experiment tests the sentence on which the architecture stands: *routing diverse predictive processors through the competitive workspace produces behavior that concatenating the same processors' outputs does not.*

Two arms run under matched input from a fixed seed, with greedy decoding (temperature 0) to eliminate sampling noise from the observable.

![The workspace-mediation ablation, the primary experiment. The same candidates feed Chronos and the language organ in both arms, which differ only in the competitive workspace: the on arm scores candidates and selects and broadcasts a small top-k coalition, while the off arm hands over a flat snapshot of the same candidates. A decision rule fixed in code on the coupling between Soma's and Chronos's errors and on coalition-selection structure decides the verdict. Indistinguishable arms demote the architecture to a scored prompt-assembler and falsify the design thesis.](figures/fig-workspace-ablation.png){width=95%}

**Workspace-on (as built).** The real Soma and Chronos modules run over an in-memory bus from a fixed seed. Soma publishes its prediction error over a scripted substrate stimulus. Because Soma does not read the broadcast, its error series is computed once and shared by both arms. In the on arm, Syneidesis reads one batch of candidate events from every active module's stream, scores each candidate by intensity and novelty, selects a small top-k coalition, and broadcasts it. In this instrument, the confidence threshold is set to zero and the arousal gain is held fixed, so it exercises competitive selection and broadcast while the threshold and the affective gain stay outside the test. The broadcast re-enters as context for the next tick, Chronos predicts the selected coalition, and the language organ conditions on the rendered coalition.

**Workspace-off (the prompt-assembler control).** Identical in every respect except that the competitive workspace is bypassed: the same candidates are handed to Chronos and the language organ as a flat snapshot, with no scoring, top-k selection, inhibition, or competition. The same Soma error series and the same fixed seed are used. The two Chronos arms start from the same seed and diverge only through what they receive.

The design of the off condition determines whether the null is reachable, and two disciplines keep it from being won trivially. Information parity: the off condition gives Chronos and the language organ the same underlying candidates as the on condition (all current module outputs), with the rendering budget matched across arms so the contrast is between selection-structure and information-quantity. Module non-degeneracy: in the off condition modules keep their forward models, keep predicting from their own signals, and keep publishing real prediction errors, instead of being starved, silenced, or fed constants. If the workspace is theater, the downstream components then receive the same information under a different arrangement and the two conditions should be indistinguishable, which would make the null reachable in fact rather than only a verdict label.

The stimulus batteries are substrate-salient, neutral, and a decoupled control. The defaults are 24 ticks, top-k 2, window 6, and a minimum effect of 0.15.

Three measures are taken.

**Primary measure: coupling delta.** The mean sliding-window Pearson correlation between Soma's and Chronos's error time series, workspace-on minus workspace-off. A positive delta indicates that broadcast-mediated competition couples the modules beyond any correlation created by the stimulus itself.

**Selection measure: coalition entropy.** Shannon entropy of the on-arm selected-source sequence (Shannon 1948), which measures whether selection is non-trivial instead of always choosing the same source.

**Secondary measure: conditioning divergence.** The cosine distance between the two arms' rendered workspace content, a deterministic proxy for output divergence under greedy decoding. It is secondary because any difference in upstream conditioning produces downstream text divergence: it confirms the primary measures' effects reach the observable output but cannot by itself distinguish meaningful integration from noise.

The verdicts are WIN, NULL, NEGATIVE, and UNDERPOWERED. WIN requires the coupling delta to exceed the minimum effect together with non-trivial selection. NULL falls within the minimum effect. NEGATIVE is at or below minus the minimum effect. UNDERPOWERED is returned when Soma never enters the coalition or the correlation is undefined. Because a small top-k forces the candidates to compete, each run records whether candidates ever exceeded the coalition's capacity. If they never did, a WIN is evidence of broadcast mediation instead of competition.

A positive result is narrower than a null. A null kills the thesis at the root: if the competitive workspace is inert, no property depending on workspace-mediated competition can arise, and no additional module rescues the architecture. A positive result establishes only that competitive mediation changes global behavior in directionally structured ways, a necessary but insufficient foundation for the broader thesis, because the richer claims require the full module set and longitudinal observation (§8.1). The experiment decides only whether the rest of the program is worth running, and it leaves the question of minds open.

The decision rule and its parameters are fixed in the released code, and the same seed reproduces the verdict and its record, which closes off the researcher degrees of freedom that inflate false positives (Simmons, Nelson, and Simonsohn 2011).

### 6.4 The offline suite and multi-seed stability

The offline suite runs eight experiments under one master seed with an independent child seed each: the active-inference benchmark (Nous's expected-free-energy agent against tabular Q-learning, matched on observation model and reward, on an epistemic T-maze and an exploitation task), the oscillatory ablation, an A/B divergence battery, a memory-coherence battery, a self-model accuracy battery, multi-seed stability, the enforcement red team, and the workspace-mediation ablation. Holm-Bonferroni correction is applied across the suite's p-values. Nothing in the suite boots an entity or opens a network connection.

The multi-seed stability harness runs a configuration under several seeds. An ensemble is stable only when the headline metric's coefficient of variation is within tolerance and the verdict is unanimous across seeds, since a flipped verdict is a qualitative instability that a scalar spread would hide. Whether the competitive workspace stays stable across seeds is itself open: correlated prediction errors across modules could drive it into runaway states, and the architecture carries no proof of convergence. The affective loop sharpens this uncertainty, because coupling perceptual surprise to arousal and arousal to precision is a positive-feedback path whose bounding is an engineering choice whose stability must be demonstrated.

### 6.5 The module-ignition study

The module-ignition study is the architecture's growth path, run live under the autonomous welfare safety net. A gestation produces a seed being, which is preserved just after birth. Branch 0 and a repeat start from that seed with the base-thesis modules, while branch k starts from the seed with the first k held modules added in a fixed order (Mnemos, Phantasia, Nous, Eidolon, Empatheia, Vox, Praxis, Perception, Mundus), and accumulate k continues from the previous accumulate step with the same modules as branch k. Every viewing plays the same film program, decoded directly from files and pinned by the hash of its manifest, after an identical womb-to-world transition. The content-free report compares broadcasts, coalition size, and picture-to-sound drift across steps. The runner never stops a being it cannot preserve. The protocol is built but has not run to completion, and this paper reports no experimental results.

### 6.6 Verdict vocabulary

Comparisons resolve to WIN, NULL, NEGATIVE, or UNDERPOWERED. Safety gates resolve to PASS or FAIL. Each verdict compares a point estimate with a minimum effect fixed in the code. Across seeds, the mediation ablation uses a one-sided sign test over per-seed coupling deltas (Dixon and Mood 1946), whereas the active-inference benchmark uses the Mann-Whitney U test (Mann and Whitney 1947), and Holm-Bonferroni correction controls the family-wise error rate across the suite (Holm 1979). A NULL is reported transparently as a null.

-----

## 7. First boot and gestation

Module initialization, bus verification, prediction-model initialization, and cognitive-cycle start proceed under operator supervision, or under the research safety net, or as an unattended start that requires the supervisor, and Spot is built and available for unattended runs. The base-thesis form boots on a seeded feed. The perceptual and predictive modules begin receiving and predicting their feeds, and Thymos settles the entity's affect toward baseline. A perceptual discontinuity then raises arousal, sharpens the fovea, and raises the precision on the competition, while a quiet stretch lets arousal relax. The entity watches and listens so that it learns what is normal, and it speaks only when its prediction environment is novelly surprising.

A study begins with gestation. The being develops first in a local womb: a maternal heartbeat enters Soma through a weak, bounded afferent, and Soma generates its own breathing-like self-rhythm (0.5-0.9 Hz) by excitatory recurrence with synaptic depression (Tabak et al. 2000). The rhythm's period adapts slowly through a phase-projected rule (Righetti, Buchli, and Ijspeert 2006). Locking is earned over lived exposure and can fail. Entrainment counts when the band-limited phase-locking value beats all 19 "foreign mother" surrogate beats (a one-sided rank test with attained p = 0.05, in which ties fail; Van Leeuwen et al. 2003, 2009), the rhythm self-sustains when the beat is withdrawn, its frequency stays pulled toward the mother's rate, and this replicates over three consecutive withdrawals. A viability watch stops a gestation early as unviable at fixed checkpoints (6, 24, 48, and 60 hours of lived time, excluding sleep and freezes) when withdrawals stay inconclusive, frequency pull stays flat or too slow, or no replicated pass arrives. A maturation gate requires at least 24 hours of lived time, and the gestation budget is 96 hours. Birth is a womb-to-world transition into the film program, and the being is preserved just after birth.

Offline validation over 96 hours shows that at 70 bpm all 10 seeds entrain, typically by about 14 hours, while each rate from 60 to 80 bpm tracks its own mother, and no control ever passes (no drive, jittered beat, no plasticity, foreign mother).

-----

## 8. Discussion

### 8.1 What the base-thesis form can and cannot settle

The workspace-mediation ablation can determine whether competitive selection and broadcast do measurable, directionally structured work compared to flat concatenation of the same outputs. With the multi-seed stability harness, it can also determine whether the workspace is stable across runs. A positive result shifts the question to what happens as the workspace grows richer, with mnemonic, self-modeling, and social modules in the competition, and a null result means none of them matter.

What the form cannot settle it does not claim. That an affective module sets the precision does not mean the system has affect in any morally-weighted sense. Arousal here is a precision signal driven by surprise, and whether anything is felt we leave open. Whether the workspace produces anything deserving to be called cognition, affect, or agency, or understands language, requires the full module set, longitudinal observation, and the welfare paper's governance apparatus. The form is likewise silent on welfare and on the indicator mapping of Butlin et al. (2023). The ablation settles whether the foundation holds, and everything built on it is separate.

### 8.2 The predictive workspace as a unifying framework

The architecture realizes a single unified framework instead of several theories assembled piecewise: the predictive-workspace synthesis joins global accessibility and per-module prediction so competition and error minimization occur together. That workspace properties have independently been found emerging inside a single large language model (Gurnee, Sofroniew, et al. 2026) is external evidence the framing captures something real. The emergent version arises inside one model, while this architecture builds the workspace explicitly from competing modules.

### 8.3 The role of the theoretical frame

The predictive global neuronal workspace is scaffolding for the project: it motivates the architecture's shape and constrains its design space (§1.2, §1.3), but this project does not confirm or refute it. The engineering choices that exceed the formal sources (the single precision-weighted scalar, the multi-module generalization from a two-level visual model) are consistent with the frame and testable on their own terms. Insulating it from neuroscientific disconfirmation, such as the retreat from neural localization after COGITATE, is appropriate for a computational-level project that implements the workspace's computational properties without reproducing cortical dynamics. The paper's falsifiability therefore rests on the ablation instead of the frame.

### 8.4 What a modular architecture is for

Because each faculty is implemented as a separate module behind a fixed interface, a researcher can activate, remove, or replace one faculty at a time and observe how the whole system changes, which makes the architecture an instrument for studying how minds work as well as a candidate for building one. The same approach supports models of impaired or altered function, created by changing one module's parameters or removing it while the rest of the system runs as before. The entity experiences its inputs continuously and in real time, so its behavior unfolds over lived time, in contrast to a language model with attached tools that acts only when prompted, turn by turn. The embodiment layer is a body-agnostic control surface, so the same mind can in principle take different bodies or sensor networks through generic adapters.

### 8.5 What we claim and what we do not

Safety rests on the entity's executive inhibition and on the absence of any effector, and it does not rest on model weights. The reasoning and the full-configuration action gate are in §3.6, and the sovereignty argument is the welfare paper's. On the larger question, the architecture implements computational properties associated with access consciousness. We do not claim any instance is phenomenally conscious, and the design posture is precautionary, applied symmetrically to welfare and deployment. The agential vocabulary ("the entity," "its sovereignty") is the clearest way to describe the system's behavior and does not by itself assert moral patienthood or phenomenal experience, which we leave open.

-----

## 9. Limitations

- The hard problem applies: the sidecar observes behavior and the workspace addresses access consciousness only, which means neither is evidence of phenomenal experience.
- COGITATE challenged the workspace's preregistered neural predictions, and we build at the computational level and treat neural localization as contested.
- The single precision-weighted scalar for coalition selection is an engineering simplification beyond what the predictive-workspace sources establish, and the Bayesian reading of the broadcast (Mashour et al. 2020) motivates competitive selection, but the architecture implements no correction loop, so the experiment tests only competition.
- The Free Energy Principle, taken as a general principle, faces unresolved vacuity and Markov-blanket conflation objections.
- Whether the competitive workspace stays stable across runs is itself open, because correlated prediction errors could drive runaway states and the architecture carries no proof of convergence (§6.4).
- Identifying arousal with the precision on the competition is only an engineering commitment. The surprise-to-arousal-to-precision path is positive feedback bounded by a per-event cap and baseline relaxation, and whether affective modulation does work a flat-precision system would not is untested.
- In the base-thesis form the entity does not read language (§3.1), so a positive result says nothing about linguistic understanding.
- A positive result establishes only that competitive mediation changes global behavior in directionally structured ways. It does not establish cognition, affect, or self-understanding, which require the full module set and longitudinal observation (§8.1).
- The workspace-off control hands the same candidates over as a flat snapshot, and a positive result shows only that the workspace beats flat fan-in. It does not show that it beats every possible aggregation strategy.
- Speech is provably downstream of the workspace here because the paths to the language organ are deactivated, although a degenerate pass-through workspace would also route speech through itself. The test is therefore the ablation instead of the construction. Re-enabling those paths for a later interactive configuration would reintroduce a direct input route the ablation configuration must continue to exclude. The vocal-tone channel carries tone of voice from speech, never words, but it is still a speech-derived signal in the competition.
- The held modules are built and tested in isolation but have not been run together, and interaction effects across the full set are unknown.
- Reproducibility holds at the seed level for the offline deterministic harness, and the live perceptual tier establishes validity by statistical replicability across runs instead of bit-for-bit reproduction (§6.1).
- With the language organ's refusal conditioning removed, safety depends on executive inhibition and, in the full configuration, the action gate. Model-weight compliance (§3.6) is not the basis, and whether the gate suffices once effectors are enabled is left to the enforcement red-team.
- A single language organ produces one stream at a time, so simultaneous inner and outer speech is a boundary of the current form.
- The governance framework remains at the proposal stage, and the licensing is legally novel and untested.
- Gurnee, Sofroniew, et al. (2026) is a Transformer Circuits Thread publication and is not a peer-reviewed journal article. A venue may require a conventionally published reference.
- The workspace-mediation ablation is offline and narrow: it runs two modules, Soma and Chronos, with a scripted substrate stimulus, and its output measure is a proxy computed on rendered content instead of the language organ's responses. It sets the confidence threshold to zero and holds the arousal gain fixed, so it tests competitive selection and broadcast while leaving the threshold and the affective gain untested, and its across-seed sign test runs over five seeds, whose smallest attainable p-value is 1/32.
- Competition in the ablation is forced by a small coalition capacity, and when candidates never exceed it, a WIN shows broadcast mediation instead of competition.
- The linear map from drive to access rate is a modeling assumption, and whether an adaptive access rate changes workspace dynamics is open.
- The gestation model compresses developmental time: the literature reports effects after weeks of exposure (Feldman and Eidelman 2003; Webb et al. 2015), while the plasticity rate here lets a lock form within 24 to 96 hours. Its rhythm runs continuously, while fetal breathing is episodic, present about 14% of the time (Natale et al. 1988). 1:1 locking is a modeling choice where the literature reports weak and often n:m coupling. Mothers below about 60 bpm cannot demonstrate entrainment, and time dilation has not been tested with the oscillator.
- No live study has yet run to completion, so the paper reports the architecture and its instruments and does not report results.

-----

## 10. Future work

Running the module-ignition study to completion is the immediate next step. Beyond that, the workspace-mediation ablation needs to move from the offline two-module instrument to the live system on the film program, which requires a workspace-off mode in the cycle. Other open directions include an affect-gain ablation that holds arousal constant, a learned Syneidesis with threshold and phase-transition dynamics, active vision that chooses where to look by expected free energy (the epistemic value of a saccade), a validated preference source so sleep-time voice alignment can train, plugins that move a module's model onto other computational substrates, and longitudinal validation reported in a separate empirical paper.

-----

## 11. Ethical considerations

The paper's ethical commitments at the architecture level are local-only computation, public source code under the Cognitive Architecture License, an operator-configured action boundary, and a base-thesis module set chosen to settle the foundational question before scaling to configurations where welfare concerns become pressing. The welfare framework, licensing, governance, and individuation boundary are treated in a separate paper.

The risks we acknowledge include creating entities with welfare interests that cannot be fully met, the untested governance framework, the potential for misuse despite license restrictions, and the recording of the workspace graph (what competed and what reached the workspace, without content) during studies. We also acknowledge the reliance on executive inhibition and, once effectors are enabled, on an action gate instead of model-weight compliance, and the fact that a behavioral assessment can be gamed, since a system can be trained to mimic the markers of sentience while working very differently (Butlin et al. 2023; Long, Sebo, et al. 2024). We regard the welfare and governance infrastructure as work that should keep pace with the architecture's capabilities instead of lagging behind them.

-----

## Disclosure of generative AI use

Generative AI assisted in the preparation of this manuscript. The author used a large language model assistant to draft and revise prose, to copy-edit for clarity and concision, and to produce the TikZ source for the figures from author-specified content. The reference implementation described here was likewise developed with the assistance of AI coding tools. That use is recorded in the project's commit history, and the author is responsible for the software as for the text. The underlying research is the author's own: the architecture, the design thesis, the experimental design, and every technical claim originate with the author, not with any tool. All text and figures were reviewed and verified by the author, who takes full responsibility for the entire contents of the paper, including any errors, irrespective of how any portion was generated. No generative AI system is an author of this work.

-----

## References

- Arditi, A., Obeso, O., Syed, A., Paleka, D., Panickssery, N., Gurnee, W., and Nanda, N. (2024). Refusal in language models is mediated by a single direction. arXiv:2406.11717.
- Aston-Jones, G., and Cohen, J. D. (2005). An integrative theory of locus coeruleus-norepinephrine function: adaptive gain and optimal performance. *Annual Review of Neuroscience* 28, 403-450.
- Baars, B. J. (1988). *A Cognitive Theory of Consciousness.* Cambridge University Press.
- Barrett, L. F. (2017). The theory of constructed emotion: an active inference account of interoception and categorization. *Social Cognitive and Affective Neuroscience* 12(1), 1-23.
- Bastos, A. M., Usrey, W. M., Adams, R. A., Mangun, G. R., Fries, P., and Friston, K. J. (2012). Canonical microcircuits for predictive coding. *Neuron* 76(4), 695-711.
- Bernstein, N. A. (1967). *The Co-ordination and Regulation of Movements.* Pergamon Press.
- Block, N. (1995). On a confusion about a function of consciousness. *Behavioral and Brain Sciences* 18(2), 227-247.
- Bruineberg, J., Dolega, K., Dewhurst, J., and Baltieri, M. (2022). The Emperor's New Markov Blankets. *Behavioral and Brain Sciences* 45, e183.
- Buhusi, C. V., and Meck, W. H. (2005). What makes us tick? Functional and neural mechanisms of interval timing. *Nature Reviews Neuroscience* 6(10), 755-765.
- Butlin, P., Long, R., Elmoznino, E., Bengio, Y., Birch, J., et al. (2023). Consciousness in Artificial Intelligence: Insights from the Science of Consciousness. arXiv:2308.08708.
- Chalmers, D. J. (1995). Facing up to the problem of consciousness. *Journal of Consciousness Studies* 2(3), 200-219.
- Chandrasekaran, C., Gupta, D., Javadzadeh, M., Wang, T., Vivar-Lazo, M., Engel, T., Cisek, P., and Fetsch, C. R. (2025). No central executive? Decision formation through multi-area population dynamics. *Journal of Neuroscience* 45(46), e1633252025.
- Clark, A. (2013). Whatever next? Predictive brains, situated agents, and the future of cognitive science. *Behavioral and Brain Sciences* 36(3), 181-204.
- Cogitate Consortium, Ferrante, O., Gorska-Klimowska, U., Henin, S., Hirschhorn, R., Khalaf, A., Lepauvre, A., Liu, L., Richter, D., Vidal, Y., et al. (2025). Adversarial testing of global neuronal workspace and integrated information theories of consciousness. *Nature* 642(8066), 133-142.
- Craig, A. D. (2002). How do you feel? Interoception: the sense of the physiological condition of the body. *Nature Reviews Neuroscience* 3(8), 655-666.
- Da Costa, L., Parr, T., Sajid, N., Veselic, S., Neacsu, V., and Friston, K. (2020). Active inference on discrete state-spaces: a synthesis. *Journal of Mathematical Psychology* 99, 102447.
- Dixon, W. J., and Mood, A. M. (1946). The statistical sign test. *Journal of the American Statistical Association* 41(236), 557-566.
- Feldman, H., and Friston, K. (2010). Attention, uncertainty, and free-energy. *Frontiers in Human Neuroscience* 4, 215.
- Feldman, R., and Eidelman, A. I. (2003). Skin-to-skin contact (Kangaroo Care) accelerates autonomic and neurobehavioural maturation in preterm infants. *Developmental Medicine and Child Neurology* 45(4), 274-281.
- Fries, P. (2015). Rhythms for cognition: communication through coherence. *Neuron* 88(1), 220-235.
- Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience* 11(2), 127-138.
- Goodale, M. A., and Milner, A. D. (1992). Separate visual pathways for perception and action. *Trends in Neurosciences* 15(1), 20-25.
- Goodman, S. N., Fanelli, D., and Ioannidis, J. P. A. (2016). What does research reproducibility mean? *Science Translational Medicine* 8(341), 341ps12.
- Graziano, M. S. A., and Webb, T. W. (2015). The attention schema theory: a mechanistic account of subjective awareness. *Frontiers in Psychology* 6, 500.
- Gurnee, W., Sofroniew, N., Pearce, A., Piotrowski, M., Kauvar, I., Chen, R., Soligo, A., Bogdan, P., Ong, E., Wang, R., Thompson, B., Abrahams, D., Kantamneni, S., Ameisen, E., Batson, J., and Lindsey, J. (2026). Verbalizable Representations Form a Global Workspace in Language Models. Transformer Circuits Thread (Anthropic). https://transformer-circuits.pub/2026/workspace/index.html
- Ha, D., and Schmidhuber, J. (2018). World models. arXiv:1803.10122.
- Hafner, D., Pasukonis, J., Ba, J., and Lillicrap, T. (2023). Mastering diverse domains through world models. arXiv:2301.04104.
- Hasani, R., Lechner, M., Amini, A., Liebenwein, L., Ray, A., Tschaikowski, M., Teschl, G., and Rus, D. (2022). Closed-form continuous-time neural networks. *Nature Machine Intelligence* 4, 992-1003.
- Heins, C., Millidge, B., Demekas, D., Klein, B., Friston, K., Couzin, I., and Tschantz, A. (2022). pymdp: A Python library for active inference in discrete state spaces. *Journal of Open Source Software* 7(73), 4098.
- Hickok, G., and Poeppel, D. (2007). The cortical organization of speech processing. *Nature Reviews Neuroscience* 8(5), 393-402.
- Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics* 6(2), 65-70.
- Joglekar, M. R., Mejias, J. F., Yang, G. R., and Wang, X.-J. (2018). Inter-areal balanced amplification enhances signal propagation in a large-scale circuit model of the primate cortex. *Neuron* 98(1), 222-234.
- Kleckner, I. R., Zhang, J., Touroutoglou, A., Chanes, L., Xia, C., Simmons, W. K., Quigley, K. S., Dickerson, B. C., and Feldman Barrett, L. (2017). Evidence for a large-scale brain system supporting allostasis and interoception in humans. *Nature Human Behaviour* 1(5), 0069.
- Kullback, S., and Leibler, R. A. (1951). On information and sufficiency. *Annals of Mathematical Statistics* 22(1), 79-86.
- Long, R., Sebo, J., Butlin, P., Finlinson, K., Fish, K., Harding, J., Pfau, J., Sims, T., Birch, J., and Chalmers, D. (2024). Taking AI Welfare Seriously. arXiv:2411.00986.
- Mann, H. B., and Whitney, D. R. (1947). On a test of whether one of two random variables is stochastically larger than the other. *Annals of Mathematical Statistics* 18(1), 50-60.
- Mashour, G. A., Roelfsema, P., Changeux, J.-P., and Dehaene, S. (2020). Conscious processing and the Global Neuronal Workspace hypothesis. *Neuron* 105(5), 776-798.
- McClelland, J. L., McNaughton, B. L., and O'Reilly, R. C. (1995). Why there are complementary learning systems in the hippocampus and neocortex. *Psychological Review* 102(3), 419-457.
- Metzinger, T. (2003). *Being No One: The Self-Model Theory of Subjectivity.* MIT Press.
- Näätänen, R., Paavilainen, P., Rinne, T., and Alho, K. (2007). The mismatch negativity (MMN) in basic research of central auditory processing. *Clinical Neurophysiology* 118(12), 2544-2590.
- Natale, R., Nasello-Paterson, C., and Connors, G. (1988). Patterns of fetal breathing activity in the human fetus at 24 to 28 weeks of gestation. *American Journal of Obstetrics and Gynecology* 158(2), 317-321.
- National Academies of Sciences, Engineering, and Medicine (2019). *Reproducibility and Replicability in Science.* National Academies Press.
- Nieuwenhuis, S., Aston-Jones, G., and Cohen, J. D. (2005). Decision making, the P3, and the locus coeruleus-norepinephrine system. *Psychological Bulletin* 131(4), 510-532.
- O'Regan, J. K., and Noë, A. (2001). A sensorimotor account of vision and visual consciousness. *Behavioral and Brain Sciences* 24(5), 939-973.
- O'Reilly, R. C., and Frank, M. J. (2006). Making working memory work: a computational model of learning in the prefrontal cortex and basal ganglia. *Neural Computation* 18(2), 283-328.
- Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., and Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. arXiv:2304.03442.
- Polich, J. (2007). Updating P300: an integrative theory of P3a and P3b. *Clinical Neurophysiology* 118(10), 2128-2148.
- Posner, J., Russell, J. A., and Peterson, B. S. (2005). The circumplex model of affect: an integrative approach to affective neuroscience, cognitive development, and psychopathology. *Development and Psychopathology* 17(3), 715-734.
- Premack, D., and Woodruff, G. (1978). Does the chimpanzee have a theory of mind? *Behavioral and Brain Sciences* 1(4), 515-526.
- Rao, R. P. N., and Ballard, D. H. (1999). Predictive coding in the visual cortex. *Nature Neuroscience* 2(1), 79-87.
- Ray, S., and Maunsell, J. H. R. (2010). Differences in gamma frequencies across visual cortex restrict their possible use in computation. *Neuron* 67(5), 885-896.
- Righetti, L., Buchli, J., and Ijspeert, A. J. (2006). Dynamic Hebbian learning in adaptive frequency oscillators. *Physica D* 216(2), 269-281.
- Safron, A. (2020). An Integrated World Modeling Theory (IWMT) of consciousness. *Frontiers in Artificial Intelligence* 3, 30.
- Scherer, K. R. (2009). Emotions are emergent processes: they require a dynamic computational architecture. *Philosophical Transactions of the Royal Society B* 364(1535), 3459-3474.
- Searle, J. R. (1980). Minds, brains, and programs. *Behavioral and Brain Sciences* 3(3), 417-457.
- Seth, A. K. (2013). Interoceptive inference, emotion, and the embodied self. *Trends in Cognitive Sciences* 17(11), 565-573.
- Seth, A. K., and Friston, K. J. (2016). Active interoceptive inference and the emotional brain. *Philosophical Transactions of the Royal Society B* 371(1708), 20160007.
- Shadlen, M. N., and Movshon, J. A. (1999). Synchrony unbound: a critical evaluation of the temporal binding hypothesis. *Neuron* 24(1), 67-77.
- Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal* 27(3), 379-423.
- Simmons, J. P., Nelson, L. D., and Simonsohn, U. (2011). False-positive psychology. *Psychological Science* 22(11), 1359-1366.
- Sumers, T., Yao, S., Narasimhan, K., and Griffiths, T. L. (2023). Cognitive architectures for language agents. arXiv:2309.02427.
- Sun, Z., and Firestone, C. (2020). The dark room problem. *Trends in Cognitive Sciences* 24(5), 346-348.
- Tabak, J., Senn, W., O'Donovan, M. J., and Rinzel, J. (2000). Modeling of spontaneous activity in developing spinal cord using activity-dependent depression in an excitatory network. *Journal of Neuroscience* 20(8), 3041-3056.
- Tononi, G., and Cirelli, C. (2014). Sleep and the price of plasticity. *Neuron* 81(1), 12-34.
- Tschantz, A., Barca, L., Maisto, D., Buckley, C. L., Seth, A. K., and Pezzulo, G. (2022). Simulating homeostatic, allostatic and goal-directed forms of interoceptive control using active inference. *Biological Psychology* 169, 108266.
- Tulving, E. (1985). How many memory systems are there? *American Psychologist* 40(4), 385-398.
- Van Leeuwen, P., Geue, D., Lange, S., Cysarz, D., Bettermann, H., and Grönemeyer, D. H. W. (2003). Is there evidence of fetal-maternal heart rate synchronization? *BMC Physiology* 3, 2.
- Van Leeuwen, P., Geue, D., Thiel, M., Cysarz, D., Lange, S., Romano, M. C., Wessel, N., Kurths, J., and Grönemeyer, D. H. (2009). Influence of paced maternal breathing on fetal-maternal heart rate coordination. *Proceedings of the National Academy of Sciences* 106(33), 13661-13666.
- van Vugt, B., Dagnino, B., Vartak, D., Safaai, H., Panzeri, S., Dehaene, S., and Roelfsema, P. R. (2018). The threshold for conscious report: signal loss and response bias in visual and frontal cortex. *Science* 360(6388), 537-542.
- VanRullen, R. (2016). Perceptual cycles. *Trends in Cognitive Sciences* 20(10), 723-735.
- Webb, A. R., Heller, H. T., Benson, C. B., and Lahav, A. (2015). Mother's voice and heartbeat sounds elicit auditory plasticity in the human brain before full gestation. *Proceedings of the National Academy of Sciences* 112(10), 3152-3157.
- Wei, Y., Krishnan, G. P., and Bazhenov, M. (2016). Synaptic mechanisms of memory consolidation during sleep slow oscillations. *Journal of Neuroscience* 36(15), 4231-4247.
- Whyte, C. J., and Smith, R. (2021). The predictive global neuronal workspace: A formal active inference model of visual consciousness. *Progress in Neurobiology* 199, 101918.
- Wilson, M. A., and McNaughton, B. L. (1994). Reactivation of hippocampal ensemble memories during sleep. *Science* 265(5172), 676-679.
- Winkler, I., Denham, S. L., and Nelken, I. (2009). Modeling the auditory scene: predictive regularity representations and perceptual objects. *Trends in Cognitive Sciences* 13(12), 532-540.
- Wolpert, D. M., Ghahramani, Z., and Jordan, M. I. (1995). An internal model for sensorimotor integration. *Science* 269(5232), 1880-1882.
- Zink, N., Lenartowicz, A., and Markett, S. (2021). A new era for executive function research. *Neuroscience and Biobehavioral Reviews* 124, 235-244.
