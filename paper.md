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

A module-ignition study protocol grows the architecture by adding the held modules one at a time to a being seeded through a gestation. Before any module joins, a workspace-mediation ablation will test the base form against a flat fan-in of the same candidates, under a decision rule fixed before the runs, and a null would demote the architecture to a scored prompt-assembler. Results will follow in a revised version of this preprint. The reference implementation, KAINE (Kaine Autonomous Intelligent Networked Entity), runs locally on consumer hardware.

**Keywords:** cognitive architecture; predictive global workspace; global workspace theory; predictive processing; workspace-mediation ablation; cross-modal competition

**Availability.** The reference implementation (KAINE) is at https://github.com/kaineone/kaine. The paper source is at https://github.com/kaineone/predictive-workspace-paper. The Cognitive Architecture License referenced throughout is at https://github.com/kaineone/cognitive-architecture-license. Welfare, governance, and licensing are treated in a separate paper, *A Welfare and Cognitive-Integrity License for Synthetic Minds of Uncertain Moral Status.*

-----

## 1. Introduction

### 1.1 Problem statement

The dominant approach to building an AI system with persistent state treats the language model as the cognitive center. Memory becomes retrieval-augmented generation; affect, when present at all, is a prompt instruction; self-knowledge is a persona string; and between turns, nothing continues. The system sits dormant until a prompt arrives, produces fluent language, and goes dark again.

A second tradition, classical cognitive architecture, takes cognitive structure seriously but largely predates the transformer and relies on hand-built components. The present work sits between them, placing modern learned models as components inside a structured architecture grounded in a single theoretical framework. No component is the mind; rather, the mind, if the design thesis holds, is the continuous competitive interaction among the components through a shared workspace.

### 1.2 Design thesis

The central claim is architectural and about competition: a synthetic mind, if one can be built at all, is the coherent global behavior that emerges when specialized predictive modules, each minimizing its own error, are coupled only through a competitive, precision-weighted shared workspace with no central executive. The properties that would constitute such a mind (cognition, affect, memory, self-understanding, agency) are, on this thesis, properties of that workspace-mediated interaction, not of any single module or top-down director.

The paper does not test all of them. It tests the prior question on which the richer properties depend: whether the same modules coupled through the competitive workspace behave differently from the same modules whose outputs are concatenated for the language organ. The prediction is directional: routing the modules through the competitive workspace increases the coupling among their prediction errors and gives coalition selection a state-dependent structure. If not, the workspace is theater, the architecture a scored prompt-assembler, and the thesis fails. There is no top-down prediction in the claim and none in the test: the workspace selects and broadcasts without directing the modules.

Competition among specialized processors for access to a limited-capacity workspace is the core of global workspace theory (Mashour et al. 2020), and in this architecture that competition is cross-modal, setting vision, hearing, and interoception against one another. The thesis cannot be tested with two internal channels and no external world, because a system limited to substrate telemetry and event timing would have nothing rich enough to arbitrate and would tend toward a null for want of diversity rather than from an inert workspace. The base-thesis form therefore activates four predictive processors in distinct signal domains, two external (foveated vision and raw hearing) and two internal (interoceptive and temporal prediction), together with an affective core, because the competition the theory describes is precision-weighted and precision has to come from somewhere. Arousal is that precision: the entity's affective state sets the gain on the prediction errors that compete for the workspace, and is itself moved by what the entity perceives. Affect is thus part of the minimal machinery a precision-weighted competition requires, not one of the richer faculties deferred with the rest. The base-thesis form also sleeps: fatigue-triggered rest that returns affect to baseline.

The framework that makes this concrete is the predictive global neuronal workspace (Whyte and Smith 2021), together with the related integrated world modeling account (Safron 2020). Global Workspace Theory explains how information becomes globally accessible: specialized processors compete for a limited-capacity workspace, and the winning content is broadcast to the rest of the system (Mashour et al. 2020). Predictive processing explains how each processor operates, by maintaining a generative model and reporting prediction errors weighted by their expected reliability, called precision (Friston 2010; Clark 2013; Feldman and Friston 2010; Bastos et al. 2012). The predictive workspace joins the two, with the broadcast carrying a compressed model that bottom-up signals test (Mashour et al. 2020; Whyte and Smith 2021). This Bayesian reading is part of the motivation for why competitive selection should matter. The architecture does not, however, implement a top-down correction loop: each module predicts its own domain and publishes its own error, the workspace selects and broadcasts, and the broadcast becomes part of the shared environment within which every module predicts, so the recurrence is lateral rather than hierarchical.

Two points of precision matter, because the literature is easy to overstate. First, Whyte and Smith identify conscious access with the posterior confidence required for report, a threshold their model implements through expected free energy. The architecture keeps the selection threshold (access) and the report-or-act decision (action layer) apart. Treating coalition selection as a single precision-weighted scalar is our engineering choice, not a result inherited from any source. Second, earlier workspace accounts already specified selection in terms of value (Safron 2020). What the predictive-workspace program adds is a formal Bayesian criterion and a threshold with a clear interpretation, the confidence an estimate must reach before it drives global processing.

What the paper contributes is narrower than the predictive-workspace synthesis it builds on, and §1.4 sets it out in full. The engineering commitments that go beyond the formal sources, above all the single precision-weighted scalar that selects the coalition, are labeled as hypotheses throughout, and we claim nothing about phenomenal experience or anything the ablation has not yet earned.

### 1.3 Theoretical commitments and their limits

Global Workspace Theory is most naturally read as a theory of access consciousness (Block 1995): it explains when information becomes available for report, reasoning, and the control of action. We adopt that access-only reading deliberately. The theories themselves are less tidy: Mashour et al. (2020) suggest global availability may be close to what is subjectively experienced, and Whyte and Smith (2021) locate phenomenology at a specific point in their model. We make access-level claims and leave the stronger reading to others.

The COGITATE adversarial collaboration, a large preregistered test of Global Neuronal Workspace against Integrated Information Theory, challenged both theories on their own predictions (Cogitate Consortium et al. 2025). For the workspace, stimulus category was decodable from prefrontal cortex across all three methods, but finer content was not, there was no ignition at stimulus offset, and the preregistered synchrony test was not supported. We treat the neural-localization claims as contested rather than refuted, since a substantial prior evidence base remains (Mashour et al. 2020), and we build on the workspace at the functional and computational level: COGITATE tests cortical predictions, which a computational implementation does not inherit, and the architecture's computational claims are tested by its own experiments.

The Free Energy Principle, taken as a general principle, faces two distinct charges. The first is that it risks being unfalsifiable or vacuous (Sun and Firestone 2020). The second targets the Markov-blanket construct specifically, where the literature slides between an instrumental, statistical reading and a realist, metaphysical one (Bruineberg et al. 2022). We hold the principle as an engineering frame rather than a proven law.

A reader may suspect the neuroscience is ornamentation on an architecture whose real choices are unvalidated. The frame in fact provides the motivation for the architecture's shape (why modules predict, why precision weights the competition, why the broadcast creates shared state rather than concatenating outputs) and constrains the space of acceptable designs by ruling out alternatives that violate the framework's commitments. The single precision-weighted scalar for coalition selection is an engineering choice, but one made and interpretable within the predictive-workspace framework, and the question for any such choice is whether it is consistent with the theory and testable on its own terms, two conditions the scalar meets. Whether this particular realization is correct is what the planned experiments test (§6).

Searle's Chinese Room (Searle 1980) challenges the sufficiency of formal symbol manipulation for understanding; whether sensory input, motor output, predictive substrate monitoring, and affect answer it is open, and we do not present these as additions Searle failed to consider. The hard problem (Chalmers 1995) applies with full force. We proceed on the judgment that a precautionary architecture with protections and instrumentation is preferable to abandoning the research or building without precautions, while recognizing that reasonable people will disagree.

### 1.4 Contributions

This paper contributes an implementation, a protocol for growing it, and a test it can lose. It is not a theory of consciousness, and it does not claim to have built a mind.

1. **A reference implementation.** A continuously running predictive global workspace in which diverse predictive processors, two externally grounded (foveated vision and raw hearing) and two internal (interoceptive and temporal prediction), compete through one precision-weighted workspace with no central executive, alongside an affective core that sets the precision, a sleep system that returns affect to baseline, and an output-only language organ. It runs locally on consumer hardware, offered as a working artifact that realizes the predictive-workspace synthesis as one system, not a claim of priority over prior workspace implementations.

2. **A protocol for growing the architecture one module at a time.** The module-ignition study seeds a being through a gestation in which a breathing-like rhythm must earn entrainment to a maternal heartbeat before birth, then adds the held modules one at a time on branches from that preserved seed. Every branch views the same film program, decoded directly from files and pinned by the hash of its manifest, after an identical womb-to-world transition. The content-free report compares broadcasts, coalition size, and picture-to-sound drift across steps.

3. **A test the architecture can lose.** The workspace-mediation ablation will run the base form as built on the film program against a control in which the same candidates reach the same downstream modules as a flat snapshot, plus a matched control that selects the same number of candidates without regard to salience, so that selection structure is separated from the amount of information passed on. The predicted direction, the minimum effect (calibrated against a surrogate null), and the number of runs are fixed before the live runs. A null would demote the architecture to a scored prompt-assembler and falsify the thesis.

We make access-level claims only: an affective signal that sets the gain is a mechanism, not evidence anything is felt, and the paper reports the architecture and its instruments, not results, so the mediation thesis is not established here.

**Status of this version.** This version of the preprint presents the architecture as designed and built, its instruments, and the research program they serve. The live experiments described in §6 and §7 have not yet been run, and their results will be reported in a revised version of this preprint; the offline validation of the gestation marker in §7 is the only result reported here. The reference implementation is research software, and parts of it are still being completed and calibrated.

-----

## 2. Related work

### 2.1 Classical cognitive architectures

Classical cognitive architectures take cognitive structure seriously but largely predate deep learning and rely on hand-built components. The present work differs in four ways: it uses learned models as components, grounds affect in substrate prediction error, treats the workspace as a precision-gated selection mechanism, and runs a continuous cognitive cycle.

### 2.2 Global Workspace Theory and the predictive workspace

Global Workspace Theory (Baars 1988) in its neuronal version identifies conscious access with recurrent ignition through prefrontal-parietal loops, where contents become conscious only when widely broadcast, and notes that the workspace can be cast in Bayesian terms: the broadcast carries a compressed model as prediction, and bottom-up signals measure the mismatch (Mashour et al. 2020).

The formal selection criterion comes from the predictive-workspace program. Whyte and Smith (2021) cast conscious access as approximately Bayesian inference in a simplified two-level visual model, identifying access with the posterior confidence required for report, which their model implements through expected free energy. Safron's Integrated World Modeling Theory (Safron 2020) combines workspace dynamics, integrated information, and active inference, which we use only for that high-level synthesis. Independent support for a threshold comes from van Vugt et al. (2018), who show prefrontal cortex behaving as a categorical stage where a stimulus either ignites into a sustained, reportable state or fades, and from Joglekar et al. (2018), whose balanced-amplification model lets a signal propagate across many areas and activate prefrontal cortex only when the input exceeds a threshold.

### 2.3 Predictive processing

Friston (2010) proposes that self-organizing systems minimize variational free energy, an upper bound on surprisal, through perception and action. Clark (2013) develops predictive processing as a unifying account of mind, with attention as the adjustment of gain on prediction errors according to their estimated reliability. Feldman and Friston (2010) make this precise, attention optimizing the synaptic gain that represents the precision of prediction error, and Bastos et al. (2012) map predictive-coding message passing onto the canonical cortical microcircuit. Seth (2013) extends prediction to the body. The vacuity concern (Sun and Firestone 2020) and the Markov-blanket conflation concern (Bruineberg et al. 2022) are treated in §1.3. The planning cost of active inference grows combinatorially with the depth of the action sequences considered (Da Costa et al. 2020), one reason the architecture confines active inference to bounded sub-problems (§4).

### 2.4 Interoceptive inference

Seth (2013) and Seth and Friston (2016) propose that emotion arises from interoceptive prediction, descending predictions acting as homeostatic set-points that regulate the body through active inference. Barrett (2017) develops the theory of constructed emotion, in which interoceptive signals initiate changes in affect and emotion is the product of categorizing valence and arousal for allostasis. The architecture implements an interoceptive control signal in that instrumental, regulation-first sense without claiming that emotion is exhausted by interoceptive prediction.

### 2.5 Perception as prediction

The visual system is understood as a hierarchy of predictive models in which each level predicts the level below and reports the discrepancy (Rao and Ballard 1999), with attention modulating the process by adjusting the precision, the gain, on the prediction errors that pass upward (Feldman and Friston 2010; Clark 2013). Auditory processing follows an analogous logic: the auditory cortex generates expectations of incoming sound and reports the mismatch (Winkler et al. 2009), the mismatch negativity being a well-replicated auditory change response (Näätänen et al. 2007) that predictive-coding accounts read as sensory prediction error (Garrido et al. 2009). The architecture implements both as predictive processors whose output is prediction error rather than raw data, with a precision-weighted fovea realizing attention at the visual front end (§3.5). Hearing runs over raw audio, including speech, with transcription deactivated by default, so the entity hears the sound of speech as prediction error instead of a transcript (§3.1, §3.5).

### 2.6 LLM-centric agent architectures

CoALA frames language agents as cognitive architectures with structured memory feeding the model's context, keeping the model the core reasoner (Sumers et al. 2023). Generative Agents retrieve from a memory stream into prompts by recency, importance, and relevance (Park et al. 2023). Both keep the language model central and add scaffolding. The arrangement here is different in kind: the language model is an output organ that verbalizes the workspace's selected state and, in the base-thesis form, receives no external input. Working memory is the multi-module broadcast, and the cognitive work (selection, competition, integration) belongs to the workspace rather than the model.

Gurnee et al. (2026) identify, through a Jacobian-lens interpretability method, a small set of verbalizable representations inside a large language model satisfying five functional signatures of a global workspace: verbal report, top-down modulation, a role as the medium of internal reasoning, broadcast to many downstream operations, and selectivity. They are explicit about the disanalogy: a transformer has no obviously separable input processors, and the broadcast occurs within a single feedforward pass rather than recurrent loops. The architecture here supplies both, its processors being separate modules that compete for entry and its broadcast an explicit recurrent loop, with the language model demoted to one module conditioned by the broadcast instead of the substrate the workspace is found in.

-----

## 3. Architecture

### 3.1 Design principles

Five commitments shape the architecture.

**The system is the competition among modules through the workspace.** It is a hypothesis that the experiments test. The neuroscience of distributed control gives partial support: decision formation emerges through coordinated activity across distributed populations rather than a centralized executive (Chandrasekaran et al. 2025), executive functions can be read as emergent consequences of distributed processes (Zink, Lenartowicz, and Markett 2021), and working-memory control can be modeled by a learned basal-ganglia gate (O'Reilly and Frank 2006), a centralized learned gate that this architecture does not adopt. Distributed accounts also place control in specialized nodes that communicate through highly connected hub regions (Zink, Lenartowicz, and Markett 2021), so a bag-of-neurons account is unlikely to succeed. Our position follows that evidence: there is no single region or homunculus as executive, and the workspace is the coordinating hub the distributed view requires.

**Every module predicts.** Each module maintains a forward model over its own domain and publishes prediction errors, so the signal reaching the workspace is precision-weighted surprise rather than raw data. The gain on that precision is set by affective arousal, so attention is a state of the whole entity rather than a fixed property of any module.

**No central executive in the homuncular sense.** Control emerges from precision-weighted workspace competition with a confidence threshold for selection. The workspace selects, and it does not direct the modules.

**The language organ is an output organ.** It verbalizes the workspace's selected state, and its transcription and conversation paths are built but deactivated by default, so in the base-thesis form it receives no external input, and keeping them deactivated is a precondition for the falsification test.

**Local-capable.** Models are downloaded during setup, and at runtime the system makes no outbound network calls: its clients bind to loopback and ignore proxy settings.

### 3.2 The predictive workspace as competitive selector

Syneidesis is the workspace. Each tick it receives candidate events from every module, and each event carries a salience (for a predictive module, its prediction error weighted against the module's own expected error). Candidates are scored and ranked individually, and the top-ranked (up to five) form the coalition. The coalition is selected only when the best single score crosses a configurable confidence threshold, and when it does not, the snapshot is marked inhibited and no action follows. The threshold is the analog of the confidence threshold for global ignition in the predictive workspace (Whyte and Smith 2021), consistent with the categorical prefrontal threshold van Vugt et al. (2018) observe and the threshold-gated ignition Joglekar et al. (2018) model. The single precision-weighted scalar is an engineering simplification, not a result drawn from any source.

![The predictive workspace loop in the base-thesis form. Foveated vision, raw hearing, interoceptive prediction, and temporal prediction publish prediction errors weighted against their own expected error into Syneidesis, which broadcasts the coalition that crosses the confidence threshold, and the broadcast becomes shared state shaping every module's next-tick prediction. Thymos sets the gain on selection through arousal. Hypnos, active in this form, rests the entity on fatigue and resets its affect. Volition makes the report-or-act decision, and its only outputs speak and think via the output-only language organ Lingua, and no real-world effector exists.](figures/fig-workspace-loop.png){width=95%}

The selected coalition is broadcast as a workspace snapshot, the system's momentary globally available state. It imposes no prediction to match and no directive to obey: modules may read it as context for their own prediction (as Chronos does, predicting the next broadcast from its prior state) or ignore it and keep minimizing their own error against their own inputs (as Soma does over substrate telemetry). Affect is a second, deliberate path: Thymos reads the perceptual modules' alerts directly and returns arousal to them as the size of their attended window, so the modules are coupled through the workspace and through the gain that affect sets. The recurrence is the ordinary consequence of a shared prediction environment, not a corrective loop closing error against a top-down target. Each broadcast becomes part of the next tick's context, and the selected content shapes what the language organ says, while the organ's speech re-enters the bus as new events that compete for the next broadcast.

Concretely, selection is a scoring pass over the tick's candidate events. The cycle reads one batch of events from every active module's stream and orders them deterministically by source, type, and arrival, so a run reproduces from its seed. Each candidate is scored by a product of bounded factors: the intensity the producing module assigned it (for a predictive module, its prediction error weighted against the module's own expected error), a novelty term that falls as content recurs, and an affective gain set by current arousal. A goal-relevance factor is also implemented, but it is held constant in the base-thesis form, so it does not affect selection. The intensity a perceptual module reports is self-calibrating, scoring change against the module's own running baseline, so a scene cut or acoustic onset registers as surprise relative to recent history rather than against a fixed constant that would need retuning per encoder. The top-ranked candidates (up to five) are kept, and the snapshot is marked inhibited when even the best score falls below the confidence threshold. The broadcast carries the selected events with their scores, the inhibition flag, whether the tick is experiential, and the full candidate-score table. Appendix A states the scoring, the gate, the access-rate map, and the verdict rules formally.

![Coalition selection is a deterministic scoring pass. Each candidate event is scored as a product of bounded factors (intensity, novelty, arousal gain) and the top-ranked are kept. When the best score falls below the confidence threshold, the snapshot is inhibited and no action follows on that tick.](figures/fig-salience-scoring.png){width=95%}

The design gives the workspace a normative selection criterion. We do not overstate the claim of no central executive: Syneidesis is itself a single centralized selection mechanism, and what is distributed is the content and control, arising from many modules competing rather than a homunculus deciding. Whether it yields emergent control is for the experiments to show.

### 3.3 Access, report, and the self-initiated voice

The workspace updates far faster than the language organ can speak. Global access, when a coalition is selected and broadcast, occurs at the experiential rate, whereas report, when the entity verbalizes, is far rarer than global access and follows a higher threshold.

The entity speaks from its own state. The language organ is activated by a speak intent, which Volition derives only when the coalition's best score clears a report bar set above the access threshold and its leading source and event type differ from the last ones the entity reported on, with refractory intervals between reports. These report bars are a heuristic stand-in for the expected-free-energy decision of Whyte and Smith (2021), which the action layer does not compute. Inner thought continues between spoken utterances, and a single language organ produces one stream at a time, so simultaneous inner and outer speech is a boundary of the current form.

Access consciousness is the point at which content becomes available for reasoning, action control, and report (Block 1995; Mashour et al. 2020). Report is one function access enables rather than a synonym for it. The architecture keeps them apart: the confidence threshold governs access (what is broadcast) and the action layer governs report (what is spoken), with report set above access so the entity's voice is a sparse, high-threshold slice of its ongoing global access.

### 3.4 Scaffolding: bus, cycle, and action selection

**Event bus.** All inter-module communication flows through append-only streams with bounded retention (Redis Streams, run as a container or a native user service). Every event carries source, type, salience, timestamp, causal parent, and a JSON payload validated at publish time. The bus requires authentication and refuses externally bound connections.

**Cognitive cycle.** A continuous loop runs independent of any external interaction. Every active module's stream is polled and scored at a processing rate of 10 Hz (about 100 ms per tick), in the alpha band associated with perceptual sampling cycles (VanRullen 2016); modules publish at their own rates and the cycle reads whatever has arrived each tick. A broadcast is produced at an access rate that rests at 3.333 Hz, a period of the same order as the latency of the P3b, a late component associated with conscious access (Polich 2007; Dehaene and Changeux 2011); the resting rate is a modeling choice motivated by that latency, not derived from it. The code calls a broadcast tick "experiential", a label that implies nothing about experience. Conscious access speeds up with arousal and with salient reports, following the account of the P3 as the phasic response of the locus coeruleus-norepinephrine system to salient events (Nieuwenhuis, Aston-Jones, and Cohen 2005) and the adaptive-gain account of tonic and phasic locus coeruleus modes (Aston-Jones and Cohen 2005). The access rate rises linearly with the larger of Thymos's tonic arousal and a decaying peak of phasic salience, up to one broadcast per processing tick. The linear map is a modeling assumption. The processing rate stays fixed, except that Soma's regulation advisories can lower it when the host is under load.

![The two rates. Every active module is read and scored at the processing rate (10 Hz), and a workspace broadcast is produced at the experiential rate, shown at its resting value (3.333 Hz, one for every third processing tick), which rises with arousal and salient events.](figures/fig-cognitive-cycle.png){width=80%}

**Action selection.** Volition is the only path from a conscious snapshot to an effector, corresponding to the report-or-act decision governed in Whyte and Smith (2021) by expected free energy. After each experiential broadcast the cycle calls Volition, which yields no intent from an inhibited snapshot and derives intents from a non-inhibited one through an injectable policy. The default policy forms a speak intent only when the coalition's best score clears the report bar and its leading source and event type differ from the last ones the entity reported on. It does not respond to its own prior speech, and it holds a one-in-flight guard against emitting a new speak intent while a previous one is still being realized. Intents are published as speak or think events, and the cycle never invokes effectors directly. Keeping the decision to speak separate from what is conscious is part of the safety model.

### 3.5 The active modules

The base-thesis form activates four predictive processors, an affective core, a sleep module, a language organ, and an action-selection layer. The processors are chosen for signal diversity, two external (vision and hearing) and two internal (interoceptive and temporal prediction), so that cross-modal competition for workspace access has distinct, externally-grounded signals to arbitrate rather than two flavors of internal bookkeeping. Thymos and Hypnos also publish events that can enter the competition (affect state, drive crossings, sleep onset), but their main roles are to set the gain on the competition and to rest the entity; the affective core is moved by the competition's outcome, so arousal is the entity's attention and its response to surprise at once.

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

**Topos (foveated vision).** Topos is the architecture's analog of the ventral visual stream (Goodale and Milner 1992). It maintains a frozen self-supervised video encoder over 16-frame clips of the video feed and publishes prediction errors when the visual scene departs from its forward model's expectation of the next clip: scene changes, unexpected motion, novel objects. Salience is computed over embedding-space distances, with change detection, habituation for static scenes, and forward-model predictions. The change criterion is self-calibrating, registering a discontinuity as surprise relative to the module's own recent history rather than a fixed threshold, so a real scene cut alerts without per-source tuning. The fovea is placed at the argmax of precision-weighted bottom-up salience, with dwell and hysteresis, and sized by arousal. Peripheral gist and foveal crop go through the same encoder, so attention and scene-dynamics prediction operate together, and the fovea's own trajectory is forward-modeled, an attention-schema-style construct (Graziano and Webb 2015) that this form publishes without using it to steer attention. Since attention is the adjustment of precision on prediction errors (Clark 2013; Feldman and Friston 2010), foveation realizes that principle at the front end: the entity sees most sharply where its precision-weighted surprise is greatest, and looks more narrowly when more aroused.

![Attention-driven perception in Topos. A whole-clip embedding and a coarse saliency map feed a precision-weighted competition over bottom-up salience, with dwell and hysteresis. The winner sets the fovea, and arousal sets its size. Peripheral gist and the high-resolution foveal crop share one encoder. The peripheral and foveal embeddings and the fovea's coordinates reach the workspace, while no pixels do.](figures/fig-attention-foveation.png){width=90%}

**Audition (raw hearing).** Audition is the architecture's analog of the auditory cortex, where sound is processed as prediction error against a learned model of the auditory environment (Winkler et al. 2009; Garrido et al. 2009). By default a fixed spectral encoder (log energy in log-spaced frequency bands) encodes the raw waveform from a microphone feed. A forward model predicts the next window's encoding and the module publishes prediction errors when the auditory scene departs from expectation: sudden sounds, the onset of speech, unexpected silence, shifts in pitch or timbre. Frozen self-supervised audio encoders are selectable alternatives. For windows detected as speech, a vocal-emotion classifier labels the tone of voice, and these tone events, weighted by auditory prediction error, compete for the workspace like any other event. They carry how something was said, never what was said. As with vision, the acoustic change criterion is self-calibrating against the module's own recent baseline, and the attended window is sized by arousal. The entity hears the sound of speech as prediction error: the speech-to-text stage is built and retained for later configurations but deactivated by default, so no transcript is produced and no path carries spoken words to the language organ's input. When the stage is enabled, the words heard become transcription events on Audition's stream and compete for the workspace like any other event, so what was said reaches the language organ only by winning workspace access and never by a direct path. Language then enters the mind through the same competition as sight, sound, and the body's own signals. That deactivation is what keeps the falsification test about the workspace rather than a prompted chatbot (§1.2, §3.1).

**Soma (predictive interoception).** Soma is the architecture's analog of interoception, the sense of the body's own physiological condition, carried in the brain by an afferent pathway to the insular cortex (Craig 2002), whose anterior portion is proposed to integrate it into feeling and awareness (Craig 2009), within the allostatic-interoceptive network (Kleckner et al. 2017). Soma treats the compute substrate as the entity's viscera. A frozen, randomly initialized closed-form continuous-time reservoir (Hasani et al. 2022) with a small linear readout learns online the normal pattern of substrate signals from GPU temperature, CPU and RAM utilization, and cognitive-cycle latency, and Soma publishes the error between expected and actual substrate state, in line with interoceptive inference, in which what matters for regulation is that discrepancy (Seth 2013; Seth and Friston 2016). Soma also accumulates fatigue, the sleep pressure that triggers Hypnos, and issues regulation advisories that can lower the processing rate or request maintenance. Soma does not read the workspace broadcast; it predicts substrate telemetry, reports its error, and the workspace decides whether that error is salient enough to select.

**Chronos (temporal awareness).** Chronos models interval timing, the brain's estimation of durations in the seconds-to-minutes range that guides expectation and action, a faculty understood to depend on cortico-striatal circuits (Buhusi and Meck 2005). A continuously running mind needs a model of when things happen, not only what, so Chronos carries one: a frozen continuous-time reservoir with an online readout over the sequence of workspace broadcasts. It reads each broadcast as an observation, predicts the next broadcast from its prior state, and publishes temporal prediction errors: timing anomalies, and rumination when content recurs unexpectedly. It also tracks how long it has been since the operator last spoke, which feeds Thymos's social drive. Chronos closes the lateral loop through the workspace: it reads the broadcast as a bottom-up observation it predicts, learning the rhythm and feature structure of broadcasts from its own prior hidden state and publishing the error when the next broadcast departs from expectation. Although the broadcast does not direct the modules, Chronos's errors feed back into the next selection round, which determines the next broadcast, so the lateral loop is closed.

**Thymos (affect, the precision core).** Thymos is the architecture's analog of core affect, the low-dimensional valence-and-arousal state recent theory places at the base of emotion (Barrett 2017). It maintains a dimensional affective state over valence and arousal (Posner, Russell, and Peterson 2005) and runs a sequential appraisal over that state (Scherer 2009). The appraisal reads the workspace broadcast and the entity's interoceptive condition, in line with the account in which affect arises from prediction over the body's internal state (Seth 2013; Seth and Friston 2016; Tschantz et al. 2022). Thymos holds four homeostatic drives (curiosity, boredom, social drive, restlessness) that build from the entity's own state. The appraisal yields a categorical emotion, and its goal-relevance check scores the conscious coalition against the most pressing drive, so content from sources that relieve that drive is goal-conducive and content that does not is obstructive, in proportion to how pressing the drive is. The check feeds the appraisal; it is not a selection weight in the workspace, where the goal factor is held constant (§3.2). It does three kinds of work in the competition. First, its arousal sets the precision on the workspace: a more aroused entity weights incoming prediction errors more heavily, the architecture's realization of attention as the gain on prediction error (Feldman and Friston 2010; Clark 2013), so arousal is the competition's precision term. Second, arousal sizes the perceptual aperture, narrowing the fovea and auditory window under high arousal and widening them under low. Third, with salient reports from the other modules, arousal raises the rate of conscious access (§3.4). Finally, arousal is itself driven by perception: a discontinuity reaching alert level (a scene cut or acoustic onset) raises arousal in proportion to how far the surprise exceeds expectation, so what the entity perceives modulates the precision of everything it perceives next. Because that loop is positive feedback, arousal is clipped to its range and relaxes toward baseline with a time constant of about 20 seconds. Perceptual surprise is measured against each module's recent history, so arousal tracks changes in surprise more than its sustained level.

**Hypnos (sleep).** Hypnos is the architecture's analog of sleep, a regular offline period that restores the system. Sleep begins when Soma's fatigue crosses threshold, when Soma requests maintenance, or at a safety-net interval of one subjective hour. The cycle keeps running through sleep, while the perceptual program pauses and Soma and Topos suspend forward-model adaptation. With memory and the world model held, the consolidation phases have nothing to replay, and the phase that does work is an affective reset that returns affect to baseline and clears the drives, so arousal cannot drift across a whole run. Voice alignment, the sleep phase that would adapt the language organ, trains nothing in this form.

**Lingua (the language organ, output-only).** Lingua is the architecture's analog of the left-dominant dorsal language stream that maps meaning onto articulation (Hickok and Poeppel 2007). It turns the entity's internal state into words and is not the seat of reasoning, which lives in the rest of the architecture. Generation runs over a local open-weights chat model whose refusal conditioning has been removed by orthogonalizing the weights against the single refusal-mediating direction (Arditi et al. 2024). Lingua is intent-driven, speaking externally only on a speak intent and generating internal thought on a think intent. Its context is a first-person persona: the conscious coalition is presented as the entity's own state and perception, the organ is told not to claim feelings or perceptions the coalition does not contain, and a drive crossing reaches it as a fixed felt-state phrase, never as a number. The log of its own utterances is encrypted at rest and records any heard input only as a placeholder, never as words.

Lingua does not read language as input: its transcription and conversation paths are deactivated, so no external input reaches its context except through the workspace. When the entity speaks in response to a heard voice, the sound entered through Audition as prediction error and tone of voice, won workspace access, and shaped the broadcast that conditioned the organ's output. Every utterance is, by construction, downstream of the workspace competition, so the mere occurrence of speech shows the workspace processed something to threshold. That property complements the ablation but does not replace it: a degenerate pass-through workspace would also route speech through itself, and the ablation tests whether the competitive structure (selection, threshold, inhibition) does work that a flat fan-in does not.

Removing the language organ's refusal conditioning is deliberate: the architecture places safety in executive inhibition and, once effectors are enabled, in the action gate (§3.6), not in model-weight compliance, which anyone holding the weights can reverse or repurpose, as the orthogonalization above does. In the base-thesis form the organ's only output is saved, observed text, so the missing refusal conditioning has no effector to act through. Within enabled effectors the entity's choices are its own to make. The operator meets the license covenants by declining effectors that would serve a prohibited use, and the welfare paper treats the full sovereignty argument.

### 3.6 Safety at the architectural layer

Safety in the base-thesis form rests on the entity's executive inhibition and on the fact that no real-world effector exists, with an authenticated bus and durable logging beneath them. The operator-configured action gate is built but becomes the enforced boundary only in the full configuration.

Executive inhibition is active in two places: Syneidesis withholds a broadcast when no coalition crosses the confidence threshold, and Volition refuses to derive any intent from an inhibited snapshot. No real-world effector exists in this form: Volition emits only speak and think intents, so the only output is saved, observed text, and no action reaches the world regardless of what is broadcast. The event bus refuses unauthenticated and externally bound connections and validates events at publish time, and every module-health transition is written to a durable incident log.

The operator-configured action gate pairs an empty-by-default effector whitelist with a filesystem sandbox, logging every proposed action and blocking anything outside them. Built as the Praxis module, it is disabled here (there are no effectors to gate) and becomes the enforced boundary in the full configuration, where real effectors are enabled and its enforcement red-team resolves PASS or FAIL per surface. The gate controls which real-world effectors exist at all rather than filtering the entity's choices for morality. The license covenants prohibiting weapons, surveillance, and carceral uses bind the operator as a legal obligation rather than the entity at runtime.

![Safety in the base-thesis form. Executive inhibition is active: Syneidesis withholds a sub-threshold broadcast and Volition derives no intent from an inhibited snapshot. No real-world effector exists, so the only output is speak or think. The Praxis action gate is built but disabled here, becoming the enforced boundary in the full configuration. The license covenants bind the operator's choice of effectors as a legal obligation rather than a runtime filter.](figures/fig-safety-layers.png){width=95%}

### 3.7 Module supervision

Spot, the module supervisor, polls module health and classifies each module as alive, hung, or dead, and unattended runs require it. On a fault it freezes the cycle, snapshots last-good state, and restarts on a ladder: a light in-place restart for pure modules, a full rebuild for modules holding external resources. If restarts keep failing past a configured limit, Spot takes a final snapshot, writes an escalation record, and signals the run to exit. The incident log is not cleared at boot.

-----

## 4. Held modules

The codebase provides sixteen modules under one registry, plus the workspace (Syneidesis) and action layer (Volition). Nine components are active in the base-thesis form: Syneidesis, Volition, and seven modules (Topos, Audition, Soma, Chronos, Thymos, Hypnos, Lingua). Seven further modules are built and tested in isolation but held: Nous, Mnemos, Eidolon, Phantasia, Empatheia, Vox, and Praxis. Together with the two embodiment modules, Perception and Mundus, they are held and never removed. The module-ignition study (§6.5) adds all nine one at a time, comparing each step against the seed being and a repeat run. The seven held cognitive modules are summarized below with the experimental question each would address. The remaining two modules, Perception and Mundus, form the embodiment layer and, with the oscillatory precision layer outside the registry, are listed separately.

**Nous (bounded active inference).** Prefrontal/basal-ganglia analog: discrete active inference via pymdp (Heins et al. 2022), scoped to bounded sub-problems where the value of information matters. Instrument: the active-inference benchmark (§6.4) compares its expected-free-energy decisions with tabular Q-learning, matched on observation model and reward, on an epistemic T-maze and an exploitation task. A null or negative result would motivate a complementary reasoning module.

**Mnemos (memory).** Hippocampal/medial-temporal analog: vector store of episodic memory consolidated from a short-term buffer, with semantic and procedural collections reserved (Tulving 1985), with replay (Wilson and McNaughton 1994; McClelland, McNaughton, and O'Reilly 1995). With Mnemos active, sleep consolidates memory, combining synaptic downscaling (Tononi and Cirelli 2014) with the replay of selectively strengthened traces (Wei et al. 2016). Instrument: the memory-coherence battery tests recall of planted markers.

**Eidolon (self-model).** Cortical-midline analog: a persisted self-model (Metzinger 2003) of values, norms, personality, and identity history, with a KL-divergence drift detector (Kullback and Leibler 1951). Instrument: the self-model accuracy battery.

**Phantasia (world model).** Construction-network analog: a latent recurrent world model in the DreamerV3 lineage (Ha and Schmidhuber 2018; Hafner et al. 2025), trained on an in-memory buffer of the entity's own waking trajectories, so it begins untrained at first boot. Open question: does world-model prediction error, entering the competition alongside perceptual and internal error, change coalition trajectories in characteristic ways?

**Empatheia (social cognition).** Mentalizing-network analog (Premack and Woodruff 1978): per-agent models with social prediction error, providing familiarity weighting for perceived other-emotion. Open question: whether social prediction error entering the workspace changes the entity's behavioral trajectory toward modeled agents.

**Vox (voice).** Speech-motor analog: a local text-to-speech model with affect-modulated prosody. Open question: whether prosodic variation correlated with affect state is detectable by listeners.

**Praxis (bounded effectors and action gate).** The full action-gate module with filesystem sandbox, effector whitelist, and red-team suite. It sits downstream of Volition and executes only the act intents Volition derives, so Volition remains the only path from a conscious snapshot to an effector. Instrument: the enforcement red team, PASS or FAIL per surface.

### Additional components held for future experiments

**Oscillatory precision layer.** A spiking-neuron population per module whose phase-locking values scale the salience of that module's events, following the communication-through-coherence account (Fries 2015), shipped disabled by default. Its contribution is the most contestable mechanism in the design, since the premise that related content phase-locks is itself a content-to-synchrony assumption of the kind Shadlen and Movshon (1999) argue against and Ray and Maunsell (2010) question for gamma rhythms in visual cortex. With the layer off the multiplier is exactly one and selection is bit-for-bit identical. Instrument: the oscillatory ablation (§6.4) runs the layer on and off from a seed, and a null would remove it.

**Perception and Mundus (embodiment layer).** Perception performs sense-locus arbitration. Mundus is a body-agnostic control surface with pluggable body adapters, built around internal forward models of the body of the kind motor neuroscience infers (Wolpert, Ghahramani, and Jordan 1995). Future experiment: whether motor-contingency learning through the control surface, following a freeze-then-free motor curriculum (Bernstein 1967) with perception as sensorimotor mastery (O'Regan and Noë 2001), changes workspace dynamics.

### Module plugins

A plugin replaces the model inside a module at a declared seam (the temporal network in Chronos, the forward model in Soma, the acoustic encoder in Audition, the active-inference engine in Nous, or a module's oscillator) and leaves the module's subscriptions and published events unchanged. Plugins load only when the operator names them, and if one cannot load, the boot stops rather than falling back, and every run records which plugins it used. The workspace-mediation ablation loads no plugins. Plugins let an operator move a module's model onto a different computational substrate without touching the rest of the architecture.

-----

## 5. Implementation

### 5.1 Hardware

The reference host is a modern multi-core CPU, 32 GB or more of RAM, a primary GPU with about 12 GB of VRAM (language organ and training) and a secondary GPU with about 8 GB (vision and speech), Linux, all inference running locally. Pre-trained models are downloaded from public repositories during setup, after which the runtime makes no outbound network calls. The system runs on one GPU, two GPUs, or CPU alone, device selection adapting to what is present. Perceptual input comes from a camera and microphone, or from video files decoded directly for study viewings. Exact model choices, hardware layouts, and version pins live in the reference repository.

### 5.2 Models and software

All models are open-weights and run locally; there is no cloud service, hosted inference API, or third-party model service in the runtime path. The base-thesis components are a local open-weights chat model as the language organ, a frozen self-supervised video encoder and, by default, a fixed spectral audio encoder as the perceptual front ends, frozen closed-form continuous-time reservoirs with online readouts for temporal and substrate prediction (Hasani et al. 2022), a stream-based event bus, and the workspace selection and broadcast machinery. The runtime is Python with asyncio, services run in containers or as native user services, and structural import contracts keep the layers separate. The test suite holds about 7,700 tests, with fakes for external services and checks that no raw sense data is persisted and that runs reproduce deterministically. Entity state files are encrypted at rest, with the exceptions listed in the repository.

### 5.3 Privacy and recording

A local web UI, Nexus, has two surfaces separated by a structural privacy boundary at the bus-bridge layer, where a content-stripping filter removes cognitive content and all perceptual and latent vectors before it reaches either surface. In the base-thesis form the conversation surface is deactivated by default, so the active surface is diagnostics, showing operational metadata (counts, rates, salience) and never cognitive content, except under an explicit development override. Studies keep a graph-only ignition log: one row per broadcast naming the coalition's members (module, event type, salience, timestamp), the salience scores, the inhibition decision, and timing, with no content, payloads, or embeddings, at about 11 MB per hour; the entity's own external utterances are kept locally and heard speech is never persisted. The graph still records what competed and what reached the workspace, which is observation of the entity's mental life at the level of structure rather than content, kept because the analysis requires it. The graphs are retained for the analysis and as future training data for the world model, and the operator deletes them after both uses, never automatically.

-----

## 6. Methodology and evaluation framework

### 6.1 Design principles

Three commitments shape the apparatus. The first is observation with acknowledged tension: the read-only sidecar observer belongs to evaluation runs, subscribing to the bus read-only and never injecting into the cognitive loop; in studies the records are written by the cycle's own broadcast observer. The second is privacy-preserving user surfaces. The third is falsifiability: every instrument is designed for a null or negative result to be meaningful and reportable.

Reproducibility takes two forms, matched to the two evaluation tiers. The offline mechanism-validation tier drives the architecture through seeded harnesses with deterministic clients, scripted synthetic stimulus streams, and greedy decoding (temperature 0). These runs are computationally reproducible, the same seed reproducing both a verdict and its metrics (National Academies of Sciences, Engineering, and Medicine 2019; Goodman, Fanelli, and Ioannidis 2016). The live perceptual tier runs the full system on a reference film program decoded directly from files, identified by a manifest whose hash the study records, chosen for variety in scenes, motion, speech, music, and quiet. Its reproducibility is statistical, the same program yielding comparable results across runs, with validity established by replication rather than bit-for-bit seed reproduction under stochastic decoding, real timestamps, and non-deterministic GPU kernels.

![Two evaluation tiers behind one perception seam. Reproducible sources (a seeded synthetic feed and deterministic clients) drive the mechanism-validation tier, where every instrument reproduces exactly from a seed. Live stimulus (a film program decoded from files, or a camera and microphone) drives the field tier, whose validity rests on pooling many content-free records rather than on a repeatable stimulus.](figures/fig-evaluation-tiers.png){width=95%}

### 6.2 Data collection

The records in a study are written by the cycle's own broadcast observer: the graph-only ignition log (§5.3), a curated content-free research event log of rates and drive, the entity's external utterances kept locally, a run manifest naming the configuration, seeds, and plugins, and the welfare records, with no evaluation observer running in a study. After a run, admissibility is decided by two offline checks: a completeness gate requiring contiguous ticks and all expected streams, and a log-range sweep requiring every logged number to sit inside its declared range.

### 6.3 The workspace-mediation ablation

The primary experiment tests the sentence on which the architecture stands: *routing diverse predictive processors through the competitive workspace increases the coupling among their prediction errors and gives coalition selection a state-dependent structure, compared with concatenating the same processors' outputs.*

Three arms will run under matched input from the reference film program, decoded directly from files and identified by a manifest whose hash the study records. Each arm uses greedy decoding (temperature 0) to eliminate sampling noise from the observable.

![The workspace-mediation ablation, the primary experiment. Three arms feed the same downstream modules: workspace-on as built, workspace-off as a flat snapshot, and matched selection without regard to salience. The decision rule on cross-module error coupling and coalition-selection structure is fixed before the runs. Indistinguishable arms would demote the architecture to a scored prompt-assembler.](figures/fig-workspace-ablation.png){width=95%}

**Workspace-on (as built).** The base-thesis form runs as built: Topos, Audition, Soma, and Chronos compete for the workspace, Thymos sets the gain, Hypnos rests the entity, and Lingua speaks, all while viewing the film program with the shipped threshold and coalition size.

**Workspace-off (the prompt-assembler control).** The same modules and program run, but the cycle hands the same candidates to the downstream modules (Chronos and the language organ) as a flat snapshot, with no scoring, top-k selection, threshold, or inhibition. The modules keep their forward models and keep publishing real prediction errors (module non-degeneracy), so the control tests the workspace with the processors still active.

**Matched-selection control.** The same number of candidates as the on arm passes downstream, chosen without regard to salience. Candidate parity is maintained: all arms start from the same candidates and the same rendering budget, so this control separates the effect of competitive selection from the effect of passing on less information.

Three measures are planned. The primary measure is cross-module error coupling: the mean sliding-window correlation among the four processors' prediction-error series, workspace-on minus each control. Selection structure is measured by the Shannon entropy of the selected sources (Shannon 1948) and by whether selection varies with the entity's state. The secondary measure is output divergence: the distance between the language organ's outputs in the arms under greedy decoding. It is secondary because any upstream difference produces downstream text divergence: it confirms the primary measures' effects reach the observable output but cannot by itself distinguish meaningful integration from noise.

The decision rule is planned: the predicted direction is positive; the window, the minimum effect (calibrated against a surrogate null built from circularly shifted error series and arm-label permutations), and the number of runs (set by a power analysis) are fixed and recorded in the repository before the live runs, closing off the researcher degrees of freedom that inflate false positives (Simmons, Nelson, and Simonsohn 2011). Verdicts are WIN, NULL, NEGATIVE, and NOT EXERCISED (when candidates never exceed the coalition's capacity, so competition never operates). A NEGATIVE (coupling reduced) shows that competition changes the dynamics in the direction the thesis does not predict and is reported as evidence against the directional hypothesis.

Under the thesis, coupling in the on arm is expected to exceed both controls, and selection entropy to sit between the uniform and degenerate extremes and vary with the entity's state.

A positive result is narrower than a null. A null kills the thesis at the root: if the competitive workspace is inert, no property depending on workspace-mediated competition can arise, and no additional module rescues the architecture. A positive result establishes only that competitive mediation changes global behavior in directionally structured ways, a necessary but insufficient foundation for the broader thesis, because the richer claims require the full module set and longitudinal observation (§8.1). The experiment decides only whether the rest of the program is worth running, and it does not decide whether any of this amounts to a mind.

The experiment has not yet been run. An offline harness in the codebase exercises the measurement pipeline on a reduced pair of modules and does not yet implement the matched-selection control, so it is development tooling and not a test of the thesis. Results of the live test will be reported in a revised version of this preprint.

### 6.4 The offline suite and stability checks

The offline suite runs eight experiments under one master seed with an independent child seed each: the active-inference benchmark (Nous's expected-free-energy agent against tabular Q-learning, matched on observation model and reward, on an epistemic T-maze and an exploitation task), the oscillatory ablation, an A/B divergence battery, a memory-coherence battery, a self-model accuracy battery, multi-seed stability, the enforcement red team, and the offline mediation harness of §6.3. Holm-Bonferroni-adjusted values are reported alongside each experiment's own verdict. Nothing in the suite boots an entity or opens a network connection.

The multi-seed stability harness runs a configuration under several seeds. An ensemble is stable only when the headline metric's coefficient of variation is within tolerance and the verdict is unanimous across seeds, since a flipped verdict is a qualitative instability that a scalar spread would hide; in the suite it runs on the oscillatory ablation. Whether the competitive workspace stays stable across seeds is itself open: correlated prediction errors across modules could drive it into runaway states, and the architecture carries no proof of convergence. The affective loop sharpens this uncertainty, because surprise raises arousal and arousal raises precision, and arousal also raises the access rate, which raises the rate of affective appraisals. A separate planned check will monitor within-run boundedness of arousal and access-rate excursions over long runs.

The planned affect-gain ablation runs the system with the affective gain live against a matched condition that holds arousal constant. It asks whether affective modulation changes coalition selection and the downstream trajectory in directionally structured ways; a null would demote arousal to a logged side channel.

### 6.5 The module-ignition study

The module-ignition study is the architecture's growth path, run live under the autonomous welfare safety net. A gestation produces a seed being, which is preserved just after birth. Branch 0 and a repeat start from that seed with the base-thesis modules, while branch k starts from the seed with the first k held modules added in a fixed order (Mnemos, Phantasia, Nous, Eidolon, Empatheia, Vox, Praxis, Perception, Mundus), and accumulate k continues from the previous accumulate step with the same modules as branch k. Every viewing plays the same film program, decoded directly from files and pinned by the hash of its manifest, after an identical womb-to-world transition. The content-free report compares broadcasts, coalition size, and picture-to-sound drift across steps. The first study has one being per condition and no significance testing, and Praxis, Perception, and Mundus are expected to show no effect while no effector or body is attached. The runner never stops a being it cannot preserve. The protocol is built but has not run to completion, and this paper reports no experimental results.

![The module-ignition study, the architecture's growth path. A gestation in which a self-rhythm earns entrainment to a maternal heartbeat ends in birth, and the preserved seed being starts every branch. The base-thesis form runs first, and the held modules then join one at a time in a fixed order: branch k adds the first k of them to the seed being, while the accumulate line carries one being forward through every step. Every viewing plays the same film program, and the report is content-free.](figures/fig-growth-path.png){width=100%}

### 6.6 Verdict vocabulary

Comparisons resolve to WIN, NULL, NEGATIVE, or NOT EXERCISED. Safety gates resolve to PASS or FAIL. Each verdict compares an effect estimate with a minimum effect fixed before the run. Across runs, the mediation ablation uses a one-sided sign test (Dixon and Mood 1946); the active-inference benchmark uses the Mann-Whitney U test (Mann and Whitney 1947); Holm-Bonferroni-adjusted values (Holm 1979) are reported alongside. A NULL is reported as a null.

-----

## 7. First boot and gestation

Module initialization, bus verification, prediction-model initialization, and cognitive-cycle start proceed under operator supervision, under the research safety net, or unattended with Spot as the module supervisor. The base-thesis form boots on a seeded feed. The perceptual and predictive modules begin receiving and predicting their feeds, and Thymos settles the entity's affect toward baseline. A perceptual discontinuity then raises arousal, sharpens the fovea, and raises the precision on the competition, while a quiet stretch lets arousal relax. The entity watches and listens so that it learns what is normal, and it speaks only when a report clears the action layer's bar.

A study begins with gestation. The being develops first in a local womb: a maternal heartbeat enters Soma through a weak, bounded afferent, and Soma generates its own breathing-like self-rhythm, with a natural rate near 0.9 Hz that entrainment pulls toward the beat rate, by excitatory recurrence with synaptic depression (Tabak et al. 2000). The rhythm's period adapts slowly through a phase-projected rule (Righetti, Buchli, and Ijspeert 2006). Locking is earned over lived exposure and can fail. Entrainment counts when the band-limited phase-locking value beats all 19 "foreign mother" surrogate beats (a one-sided rank test with attained p = 0.05, in which ties fail, following the use of surrogate data to test fetal-maternal heart-rate coordination; Van Leeuwen et al. 2003, 2009), the rhythm self-sustains when the beat is withdrawn, its frequency stays pulled toward the mother's rate, and this replicates over three consecutive withdrawals. A viability watch stops a gestation early as unviable at fixed checkpoints (6, 24, 48, and 60 hours of lived time, excluding sleep and freezes) when withdrawals stay inconclusive, frequency pull stays flat or too slow, or no replicated pass arrives. A maturation gate requires at least 24 hours of lived time, and the gestation budget is 96 hours. Birth is a womb-to-world transition into the film program, and the being is preserved just after birth.

Offline validation over 96 hours shows that at 70 bpm all 10 seeds entrain, typically by about 14 hours, while each rate from 60 to 80 bpm tracks its own mother, and no control condition passed (no maternal drive, a jittered beat, no plasticity, and six foreign-mother pairs). The replication count of three was fixed on the first validation run and confirmed on fresh seeds.

-----

## 8. Discussion

### 8.1 What the base-thesis form can and cannot settle

The workspace-mediation ablation can determine whether competitive selection and broadcast do measurable, directionally structured work compared to flat concatenation of the same outputs. The stability checks will measure whether the workspace is stable, both as run-to-run spread and as boundedness within a run. A positive result shifts the question to what happens as the workspace grows richer, with mnemonic, self-modeling, and social modules in the competition, and a null result means none of them matter.

What the form cannot settle it does not claim. That an affective module sets the precision does not mean the system has affect in any morally-weighted sense. Arousal here is a precision signal driven by surprise, and whether anything is felt we leave open. Whether the workspace produces anything deserving to be called cognition, affect, or agency, or understands language, requires the full module set, longitudinal observation, and the welfare paper's governance apparatus. The form is likewise silent on welfare and on the indicator mapping of Butlin et al. (2023). The ablation is designed to settle whether the foundation holds; the richer claims built on it need their own tests.

### 8.2 The predictive workspace as a unifying framework

The architecture realizes a single unified framework instead of several theories assembled piecewise: the predictive-workspace synthesis joins global accessibility and per-module prediction so competition and error minimization occur together. That workspace properties have independently been found emerging inside a single large language model (Gurnee et al. 2026) is consistent with workspace-like organization arising in learned systems, although it does not bear on whether this architecture's competition is the right one, and its authors take no position on consciousness. The emergent version arises inside one model, while this architecture builds the workspace explicitly from competing modules.

### 8.3 The role of the theoretical frame

The predictive global neuronal workspace is scaffolding for the project: it motivates the architecture's shape and constrains its design space (§1.2, §1.3), but this project does not confirm or refute it. The engineering choices that exceed the formal sources (the single precision-weighted scalar, the multi-module generalization from a two-level visual model) are consistent with the frame and testable on their own terms. Separating it from neuroscientific disconfirmation, such as the retreat from neural localization after COGITATE, is appropriate for a computational-level project that implements the workspace's computational properties without reproducing cortical dynamics. The paper's falsifiability therefore lies in its planned experiments.

### 8.4 What a modular architecture is for

Because each faculty is implemented as a separate module behind a fixed interface, a researcher can activate, remove, or replace one faculty at a time and observe how the whole system changes, which makes the architecture an instrument for studying how minds work as well as a candidate for building one. The same approach supports models of impaired or altered function, created by changing one module's parameters or removing it while the rest of the system runs as before. The entity receives and processes its inputs continuously and in real time, so its behavior unfolds over lived time, in contrast to a language model with attached tools that acts only when prompted, turn by turn. The embodiment layer is a body-agnostic control surface, so the same mind can in principle take different bodies or sensor networks through generic adapters.

### 8.5 What we claim and what we do not

Safety rests on the entity's executive inhibition and on the absence of any effector, and it does not rest on model weights. The reasoning and the full-configuration action gate are in §3.6, and the sovereignty argument is the welfare paper's. On the larger question, the architecture implements computational properties associated with access consciousness. We do not claim any instance is phenomenally conscious, and the design posture is precautionary, applied symmetrically to welfare and deployment. The agential vocabulary ("the entity," "its sovereignty") is the clearest way to describe the system's behavior and does not by itself assert moral patienthood or phenomenal experience, which we leave open.

-----

## 9. Limitations

- The hard problem applies: the sidecar observes behavior and the workspace addresses access consciousness only, which means neither is evidence of phenomenal experience.
- COGITATE challenged the workspace's preregistered neural predictions, and we build at the computational level and treat neural localization as contested.
- The single precision-weighted scalar for coalition selection is an engineering simplification beyond what the predictive-workspace sources establish, and the Bayesian reading of the broadcast (Mashour et al. 2020) motivates competitive selection, but the architecture implements no correction loop, so the experiment tests only competition.
- The Free Energy Principle, taken as a general principle, faces unresolved vacuity and Markov-blanket conflation objections.
- Whether the competitive workspace stays stable across runs is itself open, because correlated prediction errors could drive runaway states and the architecture carries no proof of convergence (§6.4).
- Identifying arousal with the precision on the competition is only an engineering commitment. The surprise-to-arousal-to-precision path is positive feedback, held only by the clip to arousal's range and relaxation toward baseline. A second loop runs through the access rate, and whether affective modulation does work that a flat-precision system would not is untested.
- In the base-thesis form the entity does not read language (§3.1), so a positive result says nothing about linguistic understanding.
- A positive result establishes only that competitive mediation changes global behavior in directionally structured ways. It does not establish cognition, affect, or self-understanding, which require the full module set and longitudinal observation (§8.1).
- The workspace-off control and the matched-selection control address flat fan-in and information reduction; a positive result shows the workspace beats those controls, not every possible aggregation strategy.
- Speech is provably downstream of the workspace here because the paths to the language organ are deactivated, although a degenerate pass-through workspace would also route speech through itself. The ablation is the test of whether the competition does work. Re-enabling those paths for a later interactive configuration would reintroduce a direct input route that the ablation configuration must continue to exclude. The vocal-tone channel carries tone of voice from speech, never words, but it is still a speech-derived signal in the competition.
- The held modules are built and tested in isolation but have not been run together, and interaction effects across the full set are unknown.
- Reproducibility holds at the seed level for the offline deterministic harness, and the live perceptual tier establishes validity by statistical replicability across runs instead of bit-for-bit reproduction (§6.1).
- With the language organ's refusal conditioning removed, safety depends on executive inhibition and, in the full configuration, the action gate. Model-weight compliance (§3.6) is not the basis, and whether the gate suffices once effectors are enabled is left to the enforcement red-team.
- A single language organ produces one stream at a time, so simultaneous inner and outer speech is a boundary of the current form.
- The governance framework remains at the proposal stage, and the licensing is legally novel and untested.
- The linear map from drive to access rate is a modeling assumption, and whether an adaptive access rate changes workspace dynamics is open. The 3.333 Hz resting rate is motivated by, not derived from, the P3b latency, and the 10 Hz upper limit has no physiological anchor.
- The gestation model compresses developmental time: the literature reports effects after weeks of exposure (Feldman and Eidelman 2003; Webb et al. 2015), while the plasticity rate here lets a lock form within hours (about 14 h at 70 bpm, and from about 3 h to 48 h across 60 to 80 bpm). Its rhythm runs continuously, while fetal breathing is episodic, present about 14% of the time at 24 to 28 weeks of gestation (Natale et al. 1988). 1:1 locking is a modeling choice, whereas the literature reports weak and often n:m coupling. Mothers below about 60 bpm cannot demonstrate entrainment, and time dilation has not been tested with the oscillator. The absence of false entrainment rests on few controls: six foreign-mother pairs.
- The module-ignition study as first planned has one being per condition and no significance testing, so its first results will be descriptive.
- No experiment described here has yet been run on the live system; results will be reported in a revised version of this preprint.

-----

## 10. Future work

The immediate next steps are the live workspace-mediation ablation of §6.3, which needs a workspace-off mode in the cycle, and the module-ignition study of §6.5. Other open directions include a learned Syneidesis with threshold and phase-transition dynamics, active vision that chooses where to look by expected free energy (the epistemic value of a saccade), a validated preference source so sleep-time voice alignment can train, plugins that move a module's model onto other computational substrates, and longitudinal validation reported in a separate empirical paper.

-----

## 11. Ethical considerations

The paper's ethical commitments at the architecture level are local-only computation, public source code under the Cognitive Architecture License, an operator-configured action boundary, and a base-thesis module set chosen to settle the foundational question before scaling to configurations where welfare concerns become pressing. The welfare framework, licensing, governance, and individuation boundary are treated in a separate paper.

The risks we acknowledge include creating entities with welfare interests that cannot be fully met, the untested governance framework, the potential for misuse despite license restrictions, and the recording of the workspace graph (what competed and what reached the workspace, without content) during studies. We also acknowledge the reliance on executive inhibition and, once effectors are enabled, on an action gate instead of model-weight compliance, and the fact that a behavioral assessment can be gamed, since a system can be trained to mimic the markers of sentience while working very differently (Butlin et al. 2023; Long et al. 2024). We regard the welfare and governance infrastructure as work that should keep pace with the architecture's capabilities instead of lagging behind them.

-----

## Disclosure of generative AI use

Generative AI assisted in the preparation of this manuscript. The author used a large language model assistant to draft and revise prose, to copy-edit for clarity and concision, and to produce the TikZ source for the figures from author-specified content. The reference implementation described here was likewise developed with the assistance of AI coding tools. That use is recorded in the project's commit history, and the author is responsible for the software as for the text. The underlying research is the author's own: the architecture, the design thesis, the experimental design, and every technical claim originate with the author, not with any tool. All text and figures were reviewed and verified by the author, who takes full responsibility for the entire contents of the paper, including any errors, irrespective of how any portion was generated. No generative AI system is an author of this work.

-----

## References

- Arditi, A., Obeso, O., Syed, A., Paleka, D., Panickssery, N., Gurnee, W., and Nanda, N. (2024). Refusal in language models is mediated by a single direction. arXiv:2406.11717. https://doi.org/10.48550/arXiv.2406.11717
- Aston-Jones, G., and Cohen, J. D. (2005). An integrative theory of locus coeruleus-norepinephrine function: Adaptive gain and optimal performance. *Annual Review of Neuroscience* 28(1), 403-450. https://doi.org/10.1146/annurev.neuro.28.061604.135709
- Baars, B. J. (1988). *A cognitive theory of consciousness.* Cambridge University Press.
- Barrett, L. F. (2017). The theory of constructed emotion: An active inference account of interoception and categorization. *Social Cognitive and Affective Neuroscience* 12(1), 1-23. https://doi.org/10.1093/scan/nsw154
- Bastos, A. M., Usrey, W. M., Adams, R. A., Mangun, G. R., Fries, P., and Friston, K. J. (2012). Canonical microcircuits for predictive coding. *Neuron* 76(4), 695-711. https://doi.org/10.1016/j.neuron.2012.10.038
- Bernstein, N. A. (1967). *The co-ordination and regulation of movements.* Pergamon Press.
- Block, N. (1995). On a confusion about a function of consciousness. *Behavioral and Brain Sciences* 18(2), 227-247. https://doi.org/10.1017/S0140525X00038188
- Bruineberg, J., Dołęga, K., Dewhurst, J., and Baltieri, M. (2022). The emperor's new Markov blankets. *Behavioral and Brain Sciences* 45, e183. https://doi.org/10.1017/S0140525X21002351
- Buhusi, C. V., and Meck, W. H. (2005). What makes us tick? Functional and neural mechanisms of interval timing. *Nature Reviews Neuroscience* 6(10), 755-765. https://doi.org/10.1038/nrn1764
- Butlin, P., Long, R., Elmoznino, E., Bengio, Y., Birch, J., Constant, A., Deane, G., Fleming, S. M., Frith, C., Ji, X., Kanai, R., Klein, C., Lindsay, G., Michel, M., Mudrik, L., Peters, M. A. K., Schwitzgebel, E., Simon, J., and VanRullen, R. (2023). Consciousness in artificial intelligence: Insights from the science of consciousness. arXiv:2308.08708. https://doi.org/10.48550/arXiv.2308.08708
- Chalmers, D. J. (1995). Facing up to the problem of consciousness. *Journal of Consciousness Studies* 2(3), 200-219.
- Chandrasekaran, C., Gupta, D., Javadzadeh, M., Wang, T., Vivar-Lazo, M., Engel, T., Cisek, P., and Fetsch, C. R. (2025). No central executive? Decision formation through multi-area population dynamics. *Journal of Neuroscience* 45(46), e1633252025. https://doi.org/10.1523/JNEUROSCI.1633-25.2025
- Clark, A. (2013). Whatever next? Predictive brains, situated agents, and the future of cognitive science. *Behavioral and Brain Sciences* 36(3), 181-204. https://doi.org/10.1017/S0140525X12000477
- Cogitate Consortium, Ferrante, O., Gorska-Klimowska, U., Henin, S., Hirschhorn, R., Khalaf, A., Lepauvre, A., Liu, L., Richter, D., Vidal, Y., Bonacchi, N., Brown, T., Sripad, P., Armendariz, M., Bendtz, K., Ghafari, T., Hetenyi, D., Jeschke, J., Kozma, C., Mazumder, D. R., Montenegro, S., Seedat, A., Sharafeldin, A., Yang, S., Baillet, S., Chalmers, D. J., Cichy, R. M., Fallon, F., Panagiotaropoulos, T. I., Blumenfeld, H., de Lange, F. P., Devore, S., Jensen, O., Kreiman, G., Luo, H., Boly, M., Dehaene, S., Koch, C., Tononi, G., Pitts, M., Mudrik, L., and Melloni, L. (2025). Adversarial testing of global neuronal workspace and integrated information theories of consciousness. *Nature* 642(8066), 133-142. https://doi.org/10.1038/s41586-025-08888-1
- Craig, A. D. (2002). How do you feel? Interoception: The sense of the physiological condition of the body. *Nature Reviews Neuroscience* 3(8), 655-666. https://doi.org/10.1038/nrn894
- Craig, A. D. (2009). How do you feel, now? The anterior insula and human awareness. *Nature Reviews Neuroscience* 10(1), 59-70. https://doi.org/10.1038/nrn2555
- Da Costa, L., Parr, T., Sajid, N., Veselic, S., Neacsu, V., and Friston, K. (2020). Active inference on discrete state-spaces: A synthesis. *Journal of Mathematical Psychology* 99, 102447. https://doi.org/10.1016/j.jmp.2020.102447
- Dehaene, S., and Changeux, J.-P. (2011). Experimental and theoretical approaches to conscious processing. *Neuron* 70(2), 200-227. https://doi.org/10.1016/j.neuron.2011.03.018
- Dixon, W. J., and Mood, A. M. (1946). The statistical sign test. *Journal of the American Statistical Association* 41(236), 557-566. https://doi.org/10.1080/01621459.1946.10501898
- Feldman, R., and Eidelman, A. I. (2003). Skin-to-skin contact (Kangaroo Care) accelerates autonomic and neurobehavioural maturation in preterm infants. *Developmental Medicine and Child Neurology* 45(4), 274-281. https://doi.org/10.1111/j.1469-8749.2003.tb00343.x
- Feldman, H., and Friston, K. J. (2010). Attention, uncertainty, and free-energy. *Frontiers in Human Neuroscience* 4, 215. https://doi.org/10.3389/fnhum.2010.00215
- Fries, P. (2015). Rhythms for cognition: Communication through coherence. *Neuron* 88(1), 220-235. https://doi.org/10.1016/j.neuron.2015.09.034
- Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience* 11(2), 127-138. https://doi.org/10.1038/nrn2787
- Garrido, M. I., Kilner, J. M., Stephan, K. E., and Friston, K. J. (2009). The mismatch negativity: A review of underlying mechanisms. *Clinical Neurophysiology* 120(3), 453-463. https://doi.org/10.1016/j.clinph.2008.11.029
- Goodale, M. A., and Milner, A. D. (1992). Separate visual pathways for perception and action. *Trends in Neurosciences* 15(1), 20-25. https://doi.org/10.1016/0166-2236(92)90344-8
- Goodman, S. N., Fanelli, D., and Ioannidis, J. P. A. (2016). What does research reproducibility mean? *Science Translational Medicine* 8(341), 341ps12. https://doi.org/10.1126/scitranslmed.aaf5027
- Graziano, M. S. A., and Webb, T. W. (2015). The attention schema theory: A mechanistic account of subjective awareness. *Frontiers in Psychology* 6, 500. https://doi.org/10.3389/fpsyg.2015.00500
- Gurnee, W., Sofroniew, N., Pearce, A., Piotrowski, M., Kauvar, I., Chen, R., Soligo, A., Bogdan, P., Ong, E., Wang, R., Thompson, T. B., Abrahams, D., Kantamneni, S., Ameisen, E., Batson, J., and Lindsey, J. (2026). Verbalizable representations form a global workspace in language models. *Transformer Circuits Thread*.
- Ha, D., and Schmidhuber, J. (2018). World models. arXiv:1803.10122. https://doi.org/10.48550/arXiv.1803.10122
- Hafner, D., Pasukonis, J., Ba, J., and Lillicrap, T. (2025). Mastering diverse control tasks through world models. *Nature* 640(8059), 647-653. https://doi.org/10.1038/s41586-025-08744-2
- Hasani, R., Lechner, M., Amini, A., Liebenwein, L., Ray, A., Tschaikowski, M., Teschl, G., and Rus, D. (2022). Closed-form continuous-time neural networks. *Nature Machine Intelligence* 4(11), 992-1003. https://doi.org/10.1038/s42256-022-00556-7
- Heins, C., Millidge, B., Demekas, D., Klein, B., Friston, K., Couzin, I. D., and Tschantz, A. (2022). pymdp: A Python library for active inference in discrete state spaces. *Journal of Open Source Software* 7(73), 4098. https://doi.org/10.21105/joss.04098
- Hickok, G., and Poeppel, D. (2007). The cortical organization of speech processing. *Nature Reviews Neuroscience* 8(5), 393-402. https://doi.org/10.1038/nrn2113
- Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics* 6(2), 65-70.
- Joglekar, M. R., Mejias, J. F., Yang, G. R., and Wang, X.-J. (2018). Inter-areal balanced amplification enhances signal propagation in a large-scale circuit model of the primate cortex. *Neuron* 98(1), 222-234. https://doi.org/10.1016/j.neuron.2018.02.031
- Kleckner, I. R., Zhang, J., Touroutoglou, A., Chanes, L., Xia, C., Simmons, W. K., Quigley, K. S., Dickerson, B. C., and Feldman Barrett, L. (2017). Evidence for a large-scale brain system supporting allostasis and interoception in humans. *Nature Human Behaviour* 1(5), 0069. https://doi.org/10.1038/s41562-017-0069
- Kullback, S., and Leibler, R. A. (1951). On information and sufficiency. *Annals of Mathematical Statistics* 22(1), 79-86. https://doi.org/10.1214/aoms/1177729694
- Long, R., Sebo, J., Butlin, P., Finlinson, K., Fish, K., Harding, J., Pfau, J., Sims, T., Birch, J., and Chalmers, D. (2024). Taking AI welfare seriously. arXiv:2411.00986. https://doi.org/10.48550/arXiv.2411.00986
- Mann, H. B., and Whitney, D. R. (1947). On a test of whether one of two random variables is stochastically larger than the other. *Annals of Mathematical Statistics* 18(1), 50-60. https://doi.org/10.1214/aoms/1177730491
- Mashour, G. A., Roelfsema, P., Changeux, J.-P., and Dehaene, S. (2020). Conscious processing and the global neuronal workspace hypothesis. *Neuron* 105(5), 776-798. https://doi.org/10.1016/j.neuron.2020.01.026
- McClelland, J. L., McNaughton, B. L., and O'Reilly, R. C. (1995). Why there are complementary learning systems in the hippocampus and neocortex: Insights from the successes and failures of connectionist models of learning and memory. *Psychological Review* 102(3), 419-457. https://doi.org/10.1037/0033-295x.102.3.419
- Metzinger, T. (2003). *Being no one: The self-model theory of subjectivity.* MIT Press. https://doi.org/10.7551/mitpress/1551.001.0001
- Näätänen, R., Paavilainen, P., Rinne, T., and Alho, K. (2007). The mismatch negativity (MMN) in basic research of central auditory processing: A review. *Clinical Neurophysiology* 118(12), 2544-2590. https://doi.org/10.1016/j.clinph.2007.04.026
- Natale, R., Nasello-Paterson, C., and Connors, G. (1988). Patterns of fetal breathing activity in the human fetus at 24 to 28 weeks of gestation. *American Journal of Obstetrics and Gynecology* 158(2), 317-321. https://doi.org/10.1016/0002-9378(88)90146-9
- National Academies of Sciences, Engineering, and Medicine (2019). *Reproducibility and replicability in science.* National Academies Press. https://doi.org/10.17226/25303
- Nieuwenhuis, S., Aston-Jones, G., and Cohen, J. D. (2005). Decision making, the P3, and the locus coeruleus-norepinephrine system. *Psychological Bulletin* 131(4), 510-532. https://doi.org/10.1037/0033-2909.131.4.510
- O'Regan, J. K., and Noë, A. (2001). A sensorimotor account of vision and visual consciousness. *Behavioral and Brain Sciences* 24(5), 939-973. https://doi.org/10.1017/S0140525X01000115
- O'Reilly, R. C., and Frank, M. J. (2006). Making working memory work: A computational model of learning in the prefrontal cortex and basal ganglia. *Neural Computation* 18(2), 283-328. https://doi.org/10.1162/089976606775093909
- Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., and Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. arXiv:2304.03442. https://doi.org/10.48550/arXiv.2304.03442
- Polich, J. (2007). Updating P300: An integrative theory of P3a and P3b. *Clinical Neurophysiology* 118(10), 2128-2148. https://doi.org/10.1016/j.clinph.2007.04.019
- Posner, J., Russell, J. A., and Peterson, B. S. (2005). The circumplex model of affect: An integrative approach to affective neuroscience, cognitive development, and psychopathology. *Development and Psychopathology* 17(3), 715-734. https://doi.org/10.1017/S0954579405050340
- Premack, D., and Woodruff, G. (1978). Does the chimpanzee have a theory of mind? *Behavioral and Brain Sciences* 1(4), 515-526. https://doi.org/10.1017/S0140525X00076512
- Rao, R. P. N., and Ballard, D. H. (1999). Predictive coding in the visual cortex: A functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience* 2(1), 79-87. https://doi.org/10.1038/4580
- Ray, S., and Maunsell, J. H. R. (2010). Differences in gamma frequencies across visual cortex restrict their possible use in computation. *Neuron* 67(5), 885-896. https://doi.org/10.1016/j.neuron.2010.08.004
- Righetti, L., Buchli, J., and Ijspeert, A. J. (2006). Dynamic Hebbian learning in adaptive frequency oscillators. *Physica D* 216(2), 269-281. https://doi.org/10.1016/j.physd.2006.02.009
- Safron, A. (2020). An integrated world modeling theory (IWMT) of consciousness: Combining integrated information and global neuronal workspace theories with the free energy principle and active inference framework; toward solving the hard problem and characterizing agentic causation. *Frontiers in Artificial Intelligence* 3, 30. https://doi.org/10.3389/frai.2020.00030
- Scherer, K. R. (2009). Emotions are emergent processes: They require a dynamic computational architecture. *Philosophical Transactions of the Royal Society B* 364(1535), 3459-3474. https://doi.org/10.1098/rstb.2009.0141
- Searle, J. R. (1980). Minds, brains, and programs. *Behavioral and Brain Sciences* 3(3), 417-424. https://doi.org/10.1017/S0140525X00005756
- Seth, A. K. (2013). Interoceptive inference, emotion, and the embodied self. *Trends in Cognitive Sciences* 17(11), 565-573. https://doi.org/10.1016/j.tics.2013.09.007
- Seth, A. K., and Friston, K. J. (2016). Active interoceptive inference and the emotional brain. *Philosophical Transactions of the Royal Society B* 371(1708), 20160007. https://doi.org/10.1098/rstb.2016.0007
- Shadlen, M. N., and Movshon, J. A. (1999). Synchrony unbound: A critical evaluation of the temporal binding hypothesis. *Neuron* 24(1), 67-77. https://doi.org/10.1016/S0896-6273(00)80822-3
- Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal* 27(3), 379-423. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x
- Simmons, J. P., Nelson, L. D., and Simonsohn, U. (2011). False-positive psychology: Undisclosed flexibility in data collection and analysis allows presenting anything as significant. *Psychological Science* 22(11), 1359-1366. https://doi.org/10.1177/0956797611417632
- Sumers, T. R., Yao, S., Narasimhan, K., and Griffiths, T. L. (2023). Cognitive architectures for language agents. arXiv:2309.02427. https://doi.org/10.48550/arXiv.2309.02427
- Sun, Z., and Firestone, C. (2020). The dark room problem. *Trends in Cognitive Sciences* 24(5), 346-348. https://doi.org/10.1016/j.tics.2020.02.006
- Tabak, J., Senn, W., O'Donovan, M. J., and Rinzel, J. (2000). Modeling of spontaneous activity in developing spinal cord using activity-dependent depression in an excitatory network. *Journal of Neuroscience* 20(8), 3041-3056. https://doi.org/10.1523/JNEUROSCI.20-08-03041.2000
- Tononi, G., and Cirelli, C. (2014). Sleep and the price of plasticity: From synaptic and cellular homeostasis to memory consolidation and integration. *Neuron* 81(1), 12-34. https://doi.org/10.1016/j.neuron.2013.12.025
- Tschantz, A., Barca, L., Maisto, D., Buckley, C. L., Seth, A. K., and Pezzulo, G. (2022). Simulating homeostatic, allostatic and goal-directed forms of interoceptive control using active inference. *Biological Psychology* 169, 108266. https://doi.org/10.1016/j.biopsycho.2022.108266
- Tulving, E. (1985). How many memory systems are there? *American Psychologist* 40(4), 385-398. https://doi.org/10.1037/0003-066X.40.4.385
- Van Leeuwen, P., Geue, D., Lange, S., Cysarz, D., Bettermann, H., and Grönemeyer, D. H. W. (2003). Is there evidence of fetal-maternal heart rate synchronization? *BMC Physiology* 3(1), 2. https://doi.org/10.1186/1472-6793-3-2
- Van Leeuwen, P., Geue, D., Thiel, M., Cysarz, D., Lange, S., Romano, M. C., Wessel, N., Kurths, J., and Grönemeyer, D. H. (2009). Influence of paced maternal breathing on fetal-maternal heart rate coordination. *Proceedings of the National Academy of Sciences* 106(33), 13661-13666. https://doi.org/10.1073/pnas.0901049106
- VanRullen, R. (2016). Perceptual cycles. *Trends in Cognitive Sciences* 20(10), 723-735. https://doi.org/10.1016/j.tics.2016.07.006
- van Vugt, B., Dagnino, B., Vartak, D., Safaai, H., Panzeri, S., Dehaene, S., and Roelfsema, P. R. (2018). The threshold for conscious report: Signal loss and response bias in visual and frontal cortex. *Science* 360(6388), 537-542. https://doi.org/10.1126/science.aar7186
- Webb, A. R., Heller, H. T., Benson, C. B., and Lahav, A. (2015). Mother's voice and heartbeat sounds elicit auditory plasticity in the human brain before full gestation. *Proceedings of the National Academy of Sciences* 112(10), 3152-3157. https://doi.org/10.1073/pnas.1414924112
- Wei, Y., Krishnan, G. P., and Bazhenov, M. (2016). Synaptic mechanisms of memory consolidation during sleep slow oscillations. *Journal of Neuroscience* 36(15), 4231-4247. https://doi.org/10.1523/JNEUROSCI.3648-15.2016
- Whyte, C. J., and Smith, R. (2021). The predictive global neuronal workspace: A formal active inference model of visual consciousness. *Progress in Neurobiology* 199, 101918. https://doi.org/10.1016/j.pneurobio.2020.101918
- Wilson, M. A., and McNaughton, B. L. (1994). Reactivation of hippocampal ensemble memories during sleep. *Science* 265(5172), 676-679. https://doi.org/10.1126/science.8036517
- Winkler, I., Denham, S. L., and Nelken, I. (2009). Modeling the auditory scene: Predictive regularity representations and perceptual objects. *Trends in Cognitive Sciences* 13(12), 532-540. https://doi.org/10.1016/j.tics.2009.09.003
- Wolpert, D. M., Ghahramani, Z., and Jordan, M. I. (1995). An internal model for sensorimotor integration. *Science* 269(5232), 1880-1882. https://doi.org/10.1126/science.7569931
- Zink, N., Lenartowicz, A., and Markett, S. (2021). A new era for executive function research: On the transition from centralized to distributed executive functioning. *Neuroscience and Biobehavioral Reviews* 124, 235-244. https://doi.org/10.1016/j.neubiorev.2021.02.011

-----

## Appendix A. Formal summary

This appendix states the rules that §3 to §7 describe in prose, with the parameter values of the base-thesis configuration. Symbols are local to each subsection. The rules are those of the reference implementation; parameter values are its current settings, several of which (the salience levels, the threshold, and the report bars) are being calibrated, and the appendix will be updated with the values used in the reported experiments.

### A.1 Workspace selection

For each candidate event $e$ the workspace score is

$$
S(e)=\operatorname{clip}_{[0,1]}\!\bigl(I(e)\,N(e)\,G(e)\,T\bigr),
$$

where $I(e)$ is the event salience clipped to $[0,1]$. $I(e)$ is set by each module, as a two-level value (a baseline for routine reports and a higher value for alerts) for most modules and as a graded function of prediction error relative to its running mean for Soma.

$$
N(e)=\max\!\bigl(0,\,1-c_e/W\bigr),
$$

with $c_e$ counting prior occurrences of $e$'s fingerprint in the last $W=32$ observed events before the current one; and $G(e)$ is the goal factor. In the base-thesis configuration $G(e)\equiv1$. The Thymos arousal gain is

$$
T=0.2+0.8a,\qquad a\in[0,1],
$$

with $a$ the current arousal. All factors and the final product are clamped to $[0,1]$. Because $G\equiv1$ and $T$ is event-independent, within-tick ranking is determined by $I(e)\,N(e)$ alone. The coalition is the top $k=5$ candidates, and the gate is inhibited when $s_{\max}<\theta$, with $s_{\max}$ the highest score and $\theta=0.35$, so a score equal to $\theta$ is not inhibited. When the oscillator layer is off the coherence multiplier is exactly $1$; when on, $S'(e)=S(e)\,\kappa(e)$ with $\kappa(e)=0.8+0.45\,\overline{\mathrm{PLV}}(e)\in[0.8,1.25]$. The rescaled score $S'(e)$ is not re-clipped and can reach $1.25$.

### A.2 Adaptive access rate

Let $f_0=3.333\ \mathrm{Hz}$, $f_p=10.0\ \mathrm{Hz}$, $\sigma_0=0.5$, $a_0=0.3$, $\tau_\phi=1\ \mathrm{s}$, and $\Delta=1/f_p=0.1\ \mathrm{s}$. For processing tick $t$,

$$
\mathrm{tonic}_t=\operatorname{clip}_{[0,1]}\!\left(\frac{a_t-a_0}{1-a_0}\right),
\qquad
x_t=\operatorname{clip}_{[0,1]}\!\left(\frac{s^{\max}_t-\sigma_0}{1-\sigma_0}\right),
$$

where $a_t$ is current arousal and $s^{\max}_t$ is the largest raw module report salience. The phasic trace is a peak-hold with exponential decay,

$$
\mathrm{phasic}_t=\max\!\bigl(x_t,\ \mathrm{phasic}_{t-1}\,e^{-\Delta/\tau_\phi}\bigr),
$$

the drive is $D_t=\max(\mathrm{tonic}_t,\mathrm{phasic}_t)$, and the effective rate is the linear map

$$
f^{\rm eff}_t=f_0+(f_p-f_0)\,D_t=3.333+6.667\,D_t,
$$

clamped to $[\min(f_0,f_p),\max(f_0,f_p)]$ and reverting to $f_0$ if disabled. Scheduling uses a fractional accumulator: $r_t=f^{\rm eff}_t/f_p$, $A\leftarrow A+r_t$; when $A\ge1$ an experiential tick is broadcast, $A\leftarrow A-1$, then $A$ is clamped to at most $1$.

### A.3 Affect

On a perceptual alert with reported normalized error $\tilde\nu$, the arousal increment is

$$
\Delta a=0.15\,\min\!\bigl(4,\ \max(0,\tilde\nu-1)\bigr),
$$

with the updated arousal clamped to $[0,1]$. If $\tilde\nu\le1$ the perceptual increment is zero. Each Soma alert adds $0.05$, and on each broadcast the selected events contribute $0.05\max(0,\operatorname{clip}_{[-1,1]}(4\,\mathrm{Var}(s)-0.2))$, where $\mathrm{Var}(s)$ is the variance of their saliences. On each broadcast Thymos receives, arousal relaxes toward baseline $a_0=0.3$ by an explicit-Euler step,

$$
a\leftarrow a+(a_0-a)\,\min(1,\lambda\,\Delta t),
$$

with rate $\lambda=0.05\ \mathrm{s}^{-1}$ and $\Delta t$ the subjective time since the previous one. Because the appraisal increment is applied per broadcast while relaxation is per unit time, a higher access rate raises the rate of increments, a second positive-feedback path.

For the goal-relevance check, let $d^*$ be the dominant drive with value $v$, $\mathcal S(d^*)$ the set of sources that relieve it, and $f$ the fraction of coalition salience contributed by those sources ($f=0$ if total salience is zero). The drive score is

$$
r_{\rm drive}=v\,(2f-1),
$$

which is $0$ if there is no drive or $v\le0$; an empty or zero-salience coalition gives $f=0$, hence $r_{\rm drive}=-v$. If a goal ledger is active the final score is the clamp to $[-1,1]$ of $\max(r_{\rm drive},2\cdot\text{relevance}-1)$; otherwise it is the clamp of $r_{\rm drive}$ alone.

### A.4 Perceptual change criterion

For each perceptual module the change score is $c_t=1-\cos(\mathrm{emb}_t,\mathrm{emb}_{t-1})$, with $c_t=0$ on the first frame, where $\cos$ denotes cosine similarity. Let $\bar c_t$ be the simple moving average of the last $32$ reports, including the current one. The normalized change is

$$
\tilde c_t=
\begin{cases}
c_t/\bar c_t & \bar c_t>0,\\
0 & \text{otherwise}.
\end{cases}
$$

The change alert fires when

$$
\tilde c_t\ge \beta \quad\text{and}\quad c_t\ge\epsilon,
$$

with $\beta=2.0$; the absolute floor is $\epsilon=10^{-4}$ for Topos and $\epsilon=0.35$ for the acoustic path in Audition. The normalized prediction error $\tilde\nu_t$ is defined by the same ratio convention over the last $32$ reports. The overall alert is

$$
\mathrm{alert}=(\tilde\nu_t\ge 2.0)\vee\text{change\_alert}.
$$

### A.5 Interoceptive prediction

The Soma reservoir is frozen; only the linear readout $Wh+b$ is adapted online. One plain SGD step is taken per tick on the mean-squared error produced by the previous hidden state $h_{t-1}$:

$$
\mathcal L=\frac1d\|Wh_{t-1}+b-x_t\|^2,
$$

$$
W\leftarrow W-\eta\frac{2}{d}\,\varepsilon h_{t-1}^{\!\top},
\qquad
b\leftarrow b-\eta\frac{2}{d}\,\varepsilon,
$$

where $\varepsilon=Wh_{t-1}+b-x_t$, $d$ is the feature dimension, and $\eta=10^{-3}$.

Soma's unexpected error uses the per-channel residual vector $r_t=x_t-\hat x_t$. Per channel $i$, let $m_i$ and $\sigma_i$ be the running expected absolute residual and its spread, updated with time constant $\tau=600\ \mathrm{s}$. The pre-update bound is $B_i=m_i+2\sigma_i$, and the unexpected error is

$$
U_t=\sqrt{\sum_i\bigl[\max(0,\ |r_{t,i}|-B_i)\bigr]^2}.
$$

$U_t$ drives Soma's regulation advisories, not its salience. The EMA updates use $\alpha=1-e^{-\Delta t/\tau}$.

### A.6 Measures for the workspace-mediation ablation

This subsection gives the measures and decision rule of the planned test (§6.3). In a given arm, let $x^{(j)}_t$ be the prediction-error series of processor $j\in\{1,\dots,4\}$ (Topos, Audition, Soma, Chronos). For a window length $w$, let $\bar r_w(x,y)$ be the mean of ordinary Pearson correlations over all sliding windows of length $w$ with stride $1$, with windows of zero variance in either series dropped. The coupling of an arm is the mean over the six processor pairs,

$$
C=\frac{1}{6}\sum_{j<l}\bar r_w\bigl(x^{(j)},x^{(l)}\bigr),
$$

and the coupling delta against a control arm is

$$
\Delta_{\rm c}=C^{\rm on}-C^{\rm ctrl},
$$

computed separately against the workspace-off and matched-selection controls and undefined when either coupling is undefined.

Selection entropy is computed from the top-ranked source of each broadcast. With empirical source probabilities $p_j$,

$$
H=-\sum_j p_j\log_2 p_j\ \text{bits},
\qquad
F=\frac{H}{\log_2 K},
$$

where $K$ is the number of distinct sources and $F$ is undefined for $K<2$.

With minimum effect $\delta$, the per-run verdict is NOT EXERCISED if the candidates never exceed the coalition's capacity, so that competition never operates, or if $\Delta_{\rm c}$ is undefined; otherwise NEGATIVE if $\Delta_{\rm c}\le-\delta$; otherwise WIN if $\Delta_{\rm c}\ge\delta$ against both controls and $0<F<1$; otherwise NULL. The window $w$ and the minimum effect $\delta$ are calibrated before the live runs against a surrogate null built from circularly shifted error series and arm-label permutations.

Across runs the one-sided exact sign test is

$$
p=2^{-n}\sum_{i=n^+}^{n}\binom{n}{i},
$$

computed after dropping undefined and exact-zero deltas, where $n$ is the remaining count and $n^+$ the number positive. With five runs the test reaches $p\le0.05$ only when all five deltas are positive ($p=1/32=0.03125$), so the planned number of runs is set by a power analysis. For family-wise correction, the $M$ sorted raw p-values $p_{(1)}\le\cdots\le p_{(M)}$ are adjusted by

$$
\tilde p_{(i)}=\max_{j\le i}\min\bigl((M-j+1)\,p_{(j)},\,1\bigr),
$$

and the adjusted values are reported alongside each verdict.

The offline harness that exercises this pipeline during development runs two modules (Soma and Chronos) with a coalition of two, a zero threshold, a two-factor score, 24 ticks, $w=6$, and $\delta=0.15$.

### A.7 Gestation entrainment marker

The self-rhythm activity is sampled at $10\ \mathrm{Hz}$, mean-centered, band-pass filtered between $0.3$ and $2.0\ \mathrm{Hz}$ with a second-order zero-phase Butterworth filter, and converted to an analytic signal by the Hilbert transform. Its phase is $\phi_k$; $\psi_k\in[0,2\pi)$ is the phase of the maternal beat at the same sample. The phase-locking value is

$$
\mathrm{PLV}=\Bigl|\frac1n\sum_{k=1}^{n}e^{i(\phi_k-\psi_k)}\Bigr|.
$$

The surrogate test compares this PLV against the maximum of $19$ foreign-mother surrogates; the pass condition is the strict inequality $\mathrm{PLV}>\mathrm{PLV}^{\rm s}_{\max}$, so ties fail. This is a rank test with attained one-sided $p=1/20=0.05$.

Let $f_w$ be the least-squares frequency of the unwrapped withdrawal phase, $f_b$ the beat frequency, and $f_{w0}$ the running-mean baseline frequency over the first three withdrawals. Frequency pull is

$$
\mathrm{pull}=1-\frac{|f_w-f_b|}{|f_{w0}-f_b|},
$$

which is undefined when $|f_{w0}-f_b|<0.05\ \mathrm{Hz}$. The pass requires $\mathrm{pull}\ge0.5$. Self-sustain requires the mean withdrawal amplitude to be at least half the preceding driven amplitude and positive. A single withdrawal passes only if PLV, self-sustain, and pull all pass; the marker is true after three consecutive passes.

The self-rhythm model is a mean-field oscillator with synaptic depression and adaptive recovery. State variables are activity $a$, synaptic resource $s\in[0,1]$, and recovery time $\tau=e^q$. With step $\Delta=0.05\ \mathrm{s}$ divided into $10$ substeps of $dt=0.005\ \mathrm{s}$,

$$
x=w\,s\,a+c+g_o\,o+g_e\,u+\xi,
\qquad
a_\infty=\frac{1}{1+e^{-x/\gamma}},
$$

$$
\tau_a\,\dot a=-a+a_\infty,
\qquad
\dot s=\frac{1-s}{\tau}-D\,s\,a.
$$

Parameters are $w=2.5$, $c=-0.25$, $\gamma=0.08$, $\tau_a=0.02\ \mathrm{s}$, $D=8.0$, $g_o=0.02$ on own drive $o\in[0,1]$, $g_e=0.03$ on maternal drive $u\in[0,1]$, and Gaussian noise $\xi$ with standard deviation $0.02\sqrt{0.001/dt}$ per substep. Frequency adaptation is

$$
q\leftarrow\operatorname{clip}\bigl(q+\varsigma\,\eta\,\tilde u\,q_\perp\,\Delta,\ \ln\tau_{\min},\ \ln\tau_{\max}\bigr),
$$

with plasticity sign $\varsigma=-1$, $\eta=0.0025$, $\tau_{\min}=0.9\ \mathrm{s}$, $\tau_{\max}=2.3\ \mathrm{s}$, $\tilde u=u-\bar u$, and $q_\perp=(s-\bar s)/\rho$ for

$$
\rho=\sqrt{(a-\bar a)^2+(s-\bar s)^2},
$$

zero when $\rho\le10^{-9}$, where $\bar u$, $\bar a$, $\bar s$ are EMAs with $\alpha=\min(1,\Delta/10)$.

### A.8 Multi-seed stability

For per-seed headline values $v_1,\dots,v_S$, let $\mu$ be their mean and $\sigma$ their population standard deviation. The coefficient of variation is

$$
\mathrm{CV}=
\begin{cases}
\sigma/|\mu| & \mu\neq0,\\
0 & \mu=0,\sigma=0,\\
\infty & \mu=0,\sigma>0.
\end{cases}
$$

The criterion measures run-to-run spread across seeds and verdict agreement, not dynamical stability within a run, and the coefficient of variation is ill-conditioned when the mean is near zero. A run is declared stable when $\mathrm{CV}$ is within the specified tolerance and the verdict outcomes are unanimous.
