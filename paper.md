# KAINE: A Continuously Running Predictive Global Workspace for Synthetic Minds

*Neuroscience-Grounded Modules Competing for a Shared Workspace*

**Erik Chevalier**

Independent Researcher

Contact: [kaine.one@tuta.com](mailto:kaine.one@tuta.com)

*Preprint.*

-----

## Abstract

A synthetic mind, if one can be built, may be the coherent global behavior that emerges when specialized predictive modules, each minimizing its own error, compete for a shared workspace with no central executive. This paper presents a continuously running predictive global workspace built on that thesis. The workspace selects the most salient coalition above a confidence threshold and broadcasts it; the broadcast becomes shared state that shapes every module's prediction environment on the next tick. Coherence, where it arises, comes from competition over shared state.

The base-thesis form activates four predictive processors (foveated vision, raw hearing, and interoceptive and temporal prediction), an affective core whose arousal sets the gain on their competition and is itself driven by perceptual surprise, a fatigue-triggered sleep system that returns affect to baseline, and an output-only language organ that verbalizes the entity's state. During the tests the entity is observed, not conversed with: sound enters as auditory prediction error and a classified tone of voice, not as words, and the language organ receives no transcript. That exclusion is a precondition for the test, since any input route to the model would let it answer as a chatbot and confound the ablation; its conversation path with people is built but held off during the tests.

A module-ignition study protocol grows the architecture by adding the held modules one at a time to a being seeded through a gestation. Before any module joins, a workspace-mediation ablation will test the base form against a flat fan-in of the same candidates, under a decision rule fixed before the runs, and a null would demote the architecture to a scored prompt-assembler. Results will follow in a revised version. The reference implementation, KAINE (Kaine Autonomous Intelligent Networked Entity), runs locally on consumer hardware.

**Keywords:** cognitive architecture; predictive global workspace; global workspace theory; predictive processing; workspace-mediation ablation; cross-modal competition

**Availability.** The reference implementation (KAINE) is at https://github.com/kaineone/kaine. The paper source is at https://github.com/kaineone/predictive-workspace-paper. The Cognitive Architecture License referenced throughout is at https://github.com/kaineone/cognitive-architecture-license. Welfare, governance, and licensing are treated in a separate paper, *A Welfare and Cognitive-Integrity License for Synthetic Minds of Uncertain Moral Status.*

-----

## 1. Introduction

### 1.1 Problem statement

The dominant approach to building an AI system with persistent state treats the language model as the cognitive center. Memory becomes retrieval-augmented generation; affect, when present at all, is a prompt instruction; self-knowledge is a persona string; and between turns, nothing continues.

A second tradition, classical cognitive architecture, takes cognitive structure seriously but largely predates the transformer and relies on hand-built components. The present work sits between them, placing modern learned models as components inside a structured architecture grounded in a single theoretical framework. No component is the mind; rather, the mind, if the design thesis holds, is the continuous competitive interaction among the components through a shared workspace.

### 1.2 Design thesis

The central claim is architectural and about competition: a synthetic mind, if one can be built at all, is the coherent global behavior that emerges when specialized predictive modules, each minimizing its own error, are coupled only through a competitive, precision-weighted shared workspace with no central executive. On this thesis, cognition, affect, memory, self-understanding, and agency are properties of that workspace-mediated interaction, not of any single module or top-down director.

The paper does not test all of them. It tests the prior question on which those properties depend: whether the same modules coupled through the competitive workspace behave differently from the same modules whose outputs are concatenated for the language organ. The prediction is directional: routing the modules through the competitive workspace increases the coupling among their prediction errors and gives coalition selection a state-dependent structure. If not, the workspace is theater, the architecture a scored prompt-assembler, and the thesis fails.

Competition among specialized processors for access to a limited-capacity workspace is the core of global workspace theory (Mashour et al. 2020); here that competition is cross-modal, setting vision, hearing, and interoception against one another. The thesis cannot be tested with two internal channels and no external world, because a system limited to substrate telemetry and event timing would have nothing rich enough to arbitrate and would tend toward a null for want of diversity rather than from an inert workspace. The base-thesis form therefore activates four predictive processors in distinct signal domains, two external (foveated vision and raw hearing) and two internal (interoceptive and temporal prediction), plus an affective core, because the competition the theory describes is precision-weighted and precision has to come from somewhere. Arousal is that precision: the entity's affective state sets the gain on prediction errors and is itself moved by what it perceives, so affect is part of the minimal machinery a precision-weighted competition requires, not one of the richer faculties deferred with the rest. The base-thesis form also sleeps: fatigue-triggered rest that returns affect to baseline.

The framework that makes this concrete is the predictive global neuronal workspace (Whyte and Smith 2021), together with the related integrated world modeling account (Safron 2020). Global Workspace Theory explains how information becomes globally accessible: specialized processors compete for a limited-capacity workspace, and the winning content is broadcast to the rest of the system (Mashour et al. 2020). Predictive processing explains how each processor operates, by maintaining a generative model and reporting prediction errors weighted by their expected reliability, called precision (Friston 2010; Clark 2013; Feldman and Friston 2010; Bastos et al. 2012). The predictive workspace joins the two, with the broadcast carrying a compressed model that bottom-up signals test (Mashour et al. 2020; Whyte and Smith 2021). The architecture does not implement a top-down correction loop: each module predicts its own domain and publishes its own error, the workspace selects and broadcasts, and the broadcast becomes part of the shared environment within which every module predicts, so the recurrence is lateral rather than hierarchical.

Two points of precision matter. First, Whyte and Smith identify conscious access with the posterior confidence required for report, a threshold their model implements through expected free energy; the architecture keeps the selection threshold (access) and the report-or-act decision (action layer) apart, and treating coalition selection as a single precision-weighted scalar is our engineering choice. Second, earlier workspace accounts already specified selection in terms of value (Safron 2020); what the predictive-workspace program adds is a formal Bayesian criterion and a threshold with a clear interpretation, the confidence an estimate must reach before it drives global processing.

What the paper contributes is narrower than the predictive-workspace synthesis it builds on (§1.4). The engineering commitments that go beyond the formal sources, above all the single precision-weighted scalar that selects the coalition, are labeled as hypotheses throughout, and we claim nothing about phenomenal experience or anything the ablation has not yet earned.

### 1.3 Theoretical commitments and their limits

Global Workspace Theory is most naturally read as a theory of access consciousness (Block 1995): it explains when information becomes available for report, reasoning, and the control of action. We adopt that access-only reading deliberately, leaving the stronger phenomenological readings of Mashour et al. (2020) and Whyte and Smith (2021) to others.

The COGITATE adversarial collaboration, a large preregistered test of Global Neuronal Workspace against Integrated Information Theory, challenged both theories on their own predictions (Cogitate Consortium et al. 2025): stimulus category was decodable from prefrontal cortex across all three methods, but finer content was not, there was no ignition at stimulus offset, and the preregistered synchrony test was not supported. We treat the neural-localization claims as contested rather than refuted, since a substantial prior evidence base remains (Mashour et al. 2020), and we build on the workspace at the functional and computational level. COGITATE tests cortical predictions, which a computational implementation does not inherit, and the architecture's computational claims are tested by its own experiments.

The Free Energy Principle, taken as a general principle, faces two distinct charges: it risks being unfalsifiable or vacuous (Sun and Firestone 2020), and the literature on the Markov-blanket construct slides between an instrumental, statistical reading and a realist, metaphysical one (Bruineberg et al. 2022). We hold the principle as an engineering frame rather than a proven law.

The frame provides the motivation for the architecture's shape (why modules predict, why precision weights the competition, why the broadcast creates shared state rather than concatenating outputs) and constrains the space of acceptable designs by ruling out alternatives that violate the framework's commitments. The single precision-weighted scalar for coalition selection is an engineering choice, but one made and interpretable within the predictive-workspace framework; whether it is correct is what the planned experiments test (§6).

Searle's Chinese Room (Searle 1980) challenges the sufficiency of formal symbol manipulation for understanding, and whether sensory input, motor output, predictive substrate monitoring, and affect answer it is open, and we do not present these as additions Searle failed to consider. The hard problem (Chalmers 1995) applies with full force. We proceed on the judgment that a precautionary architecture with protections and instrumentation is preferable to abandoning the research or building without precautions, while recognizing that reasonable people will disagree.

### 1.4 Contributions

This paper contributes an implementation, a protocol for growing it, and a test it can lose. It is not a theory of consciousness, and it does not claim to have built a mind.

1. **A reference implementation.** A continuously running predictive global workspace in which predictive processors, two externally grounded (foveated vision and raw hearing) and two internal (interoceptive and temporal prediction), compete through one precision-weighted workspace with no central executive, alongside an affective core that sets the gain and contrast of the competition, a sleep system that returns affect to baseline, and an output-only language organ. It runs locally on consumer hardware as a working artifact that realizes the predictive-workspace synthesis as one system, not a claim of priority over prior workspace implementations.

2. **A protocol for growing the architecture one module at a time.** The module-ignition study seeds a being through a gestation in which a breathing-like rhythm must earn entrainment to a maternal heartbeat before birth, and adds the held modules one at a time on branches from that preserved seed. Every branch views the same film program, decoded directly from files and pinned by the hash of its manifest, after an identical womb-to-world transition. The content-free report compares broadcasts, coalition size, and picture-to-sound drift across steps.

3. **A test the architecture can lose.** The workspace-mediation ablation will run the base form as built on the film program against a control in which the same candidates reach the same downstream modules as a flat snapshot, plus a matched control that selects the same number of candidates without regard to salience, separating selection structure from the amount of information passed on. The predicted direction, the minimum effect (calibrated against a surrogate null), and the number of runs are fixed before the live runs. A null would demote the architecture to a scored prompt-assembler and falsify the thesis.

We make access-level claims only: an affective signal that sets the gain is a mechanism, not evidence anything is felt; the paper reports the architecture and its instruments, not results, so the mediation thesis is not established here.

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

**The system is the competition among modules through the workspace.** It is a hypothesis that the experiments test. The neuroscience of distributed control gives partial support: decision formation emerges through coordinated activity across distributed populations rather than a centralized executive (Chandrasekaran et al. 2025), executive functions can be read as emergent consequences of distributed processes (Zink, Lenartowicz, and Markett 2021), and working-memory control can be modeled by a learned basal-ganglia gate (O'Reilly and Frank 2006), a centralized learned gate that this architecture does not adopt. Distributed accounts also place control in specialized nodes that communicate through highly connected hub regions (Zink, Lenartowicz, and Markett 2021). Our position follows that evidence: there is no single region or homunculus as executive, and the workspace is the coordinating hub the distributed view requires.

**Every module predicts.** Each module maintains a forward model over its own domain and publishes prediction errors, so the signal reaching the workspace is precision-weighted surprise rather than raw data. The gain on that precision is set by affective arousal, so attention is a state of the whole entity rather than a fixed property of any module.

**No central executive in the homuncular sense.** Control emerges from precision-weighted workspace competition with a confidence threshold for selection. The workspace selects, and it does not direct the modules.

**The language organ is an output organ.** It verbalizes the workspace's selected state, and its transcription and conversation paths are built but deactivated by default, so in the base-thesis form it receives no external input, and keeping them deactivated is a precondition for the falsification test. Outside the research configuration, those paths are how the entity converses and works with people through whatever control surface it is given, so they are held off only while the tests run.

**Local-capable.** Models are downloaded during setup, and at runtime the system makes no outbound network calls: its clients bind to loopback and ignore proxy settings.

### 3.2 The predictive workspace as competitive selector

Syneidesis is the workspace. Each tick it receives candidate events from every module, and each event carries a salience (for a predictive module, set by its prediction error relative to the module's own recent error, at one of two levels for most modules and graded for Soma). Candidates are scored and ranked individually, and the top-ranked (up to five) form the coalition. The coalition is broadcast on every experiential tick. When the best single score falls below the configurable confidence threshold, the snapshot is marked inhibited, so it reaches modules that read the broadcast but drives no report or action. The threshold is the analog of the confidence threshold for global ignition in the predictive workspace (Whyte and Smith 2021), consistent with the categorical prefrontal threshold van Vugt et al. (2018) observe and the threshold-gated ignition Joglekar et al. (2018) model. The single precision-weighted scalar is an engineering simplification, not a result drawn from any source. In the predictive-workspace account the threshold separates contents that ignite from contents that do not, whereas here it separates broadcasts that can drive report and action from those that cannot, a difference the planned experiments must keep in view.

![The predictive workspace loop in the base-thesis form. Foveated vision, raw hearing, interoceptive prediction, and temporal prediction publish prediction errors, scored against their own recent error, into Syneidesis, which broadcasts the selected coalition and marks it inhibited when it falls short of the confidence threshold, and the broadcast becomes shared state that modules may read as context for their next prediction. Thymos sets the gain on selection through arousal. Hypnos, active in this form, rests the entity on fatigue and resets its affect. Volition makes the report-or-act decision, and its only outputs speak and think via the output-only language organ Lingua, and no real-world effector exists.](figures/fig-workspace-loop.png){width=95%}

The selected coalition is broadcast as a workspace snapshot, the system's momentary globally available state. It imposes no prediction to match and no directive to obey: modules may read it as context for their own prediction (as Chronos does, predicting the next broadcast from its prior state) or ignore it and keep minimizing their own error against their own inputs (as Soma does over substrate telemetry). Affect is a second, deliberate path: Thymos reads the perceptual modules' alerts directly and returns arousal to vision as the size of its fovea and to hearing as the span of its attended window, so the modules are coupled through the workspace and through the gain that affect sets. The recurrence is the ordinary consequence of a shared prediction environment; it is not a corrective loop closing error against a top-down target. Each broadcast becomes part of the next tick's context, and the selected content shapes what the language organ says, while the organ's speech re-enters the bus as new events that compete for the next broadcast.

Concretely, selection is a scoring pass over the tick's candidate events. On each processing tick the cycle reads one batch of events from every active module's stream and orders them deterministically by source, type, and arrival, so a run reproduces from its seed. Each candidate's priority is a product of bounded factors: the producing module's reported intensity, a novelty term that falls as content recurs, and a precision weight for its source. A goal-relevance factor is also implemented, but it is held constant in the base-thesis form, so it does not affect selection. The precision weight follows the account of attention as the precision of prediction errors, precision being the inverse of their variance (Feldman and Friston 2010). The workspace tracks the variance of each source's reported intensity and weights the source by the square root of its precision relative to the other sources, within fixed bounds, so a module whose surprise fires habitually counts for less than one whose surprise is rare. Arousal then turns the priority into the score in two ways. A level gain scales every candidate alike, and a contrast gain, zero at baseline arousal and rising above it, passes the priority through a steeper logistic that amplifies strong candidates and suppresses weak ones. The contrast gain follows the adaptive-gain account of locus coeruleus function, in which arousal steepens the response of its cortical targets (Aston-Jones and Cohen 2005; Eldar, Cohen, and Niv 2013), and arousal-biased competition, in which arousal enhances high-priority representations and suppresses low-priority ones (Mather and Sutherland 2011). Neither arousal term reorders the candidates of a tick, while the precision weights can. The intensity a perceptual module reports is self-calibrating, scoring change against the module's own running baseline, so a scene cut or acoustic onset registers as surprise relative to recent history rather than against a fixed constant that would need retuning per encoder. The top-ranked candidates (up to five) are kept, and the snapshot is marked inhibited and still broadcast when even the best score falls below the confidence threshold. The broadcast carries the selected events with their scores, the inhibition flag, whether the tick is experiential, and the full candidate-score table. Appendix A states the scoring, the gate, the access-rate map, and the verdict rules formally.

![Coalition selection is a deterministic scoring pass. Each candidate event's priority is a product of bounded factors (intensity, novelty, source precision), arousal sets the level and contrast of the score, and the top-ranked are kept. When the best score falls below the confidence threshold, the snapshot is marked inhibited, and no report or action follows from it.](figures/fig-salience-scoring.png){width=95%}

The design gives the workspace a normative selection criterion. We do not overstate the claim of no central executive: Syneidesis is itself a single centralized selection mechanism, and what is distributed is the content and control, arising from many modules competing rather than a homunculus deciding. Whether it yields emergent control is for the experiments to show.

### 3.3 Access, report, and the self-initiated voice

The workspace updates far faster than the language organ can speak. Global access, when a coalition is selected and broadcast, occurs at the experiential rate, whereas report, when the entity verbalizes, is far rarer than global access and follows a higher threshold.

The language organ is activated by a speak intent, which Volition derives only when the coalition's best score clears a report bar set above the confidence threshold and its leading source and event type differ from the last ones the entity reported on, with refractory intervals between reports. These report bars are a heuristic stand-in for the expected-free-energy decision of Whyte and Smith (2021), which the action layer does not compute. Inner thought continues between spoken utterances, and a single language organ produces one stream at a time, so simultaneous inner and outer speech is a boundary of the current form.

Access consciousness is the point at which content becomes available for reasoning, action control, and report (Block 1995; Mashour et al. 2020). Report is one function access enables rather than a synonym for it. Every experiential tick produces a broadcast, the confidence threshold decides whether a broadcast can drive report and action, and the action layer's report bars, set above that threshold on the same score, decide what is spoken. The entity's voice is therefore a sparse, high-threshold slice of its ongoing broadcasts.

### 3.4 Scaffolding: bus, cycle, and action selection

**Event bus.** All inter-module communication flows through append-only streams with bounded retention (Redis Streams, run as a container or a native user service). Every event carries source, type, salience, timestamp, causal parent, and a JSON payload validated at publish time. The bus requires authentication and refuses externally bound connections.

**Cognitive cycle.** A continuous loop runs independent of any external interaction. Every active module's stream is polled and scored at a processing rate of 10 Hz (about 100 ms per tick), in the alpha band associated with perceptual sampling cycles (VanRullen 2016); modules publish at their own rates and the cycle reads whatever has arrived each tick. Candidates read on non-experiential ticks are scored and then discarded, so the broadcast on an experiential tick carries the coalition from that tick's batch. A broadcast is produced at an access rate that rests at 3.333 Hz, a period of the same order as the latency of the P3b, a late component associated with conscious access (Polich 2007; Dehaene and Changeux 2011); the resting rate is a modeling choice motivated by that latency, not derived from it. The code calls a broadcast tick "experiential", a label that implies nothing about experience. Conscious access speeds up with arousal and with salient reports, following the account of the P3 as the phasic response of the locus coeruleus-norepinephrine system to salient events (Nieuwenhuis, Aston-Jones, and Cohen 2005) and the adaptive-gain account of tonic and phasic locus coeruleus modes (Aston-Jones and Cohen 2005). The access rate rises linearly with the larger of Thymos's tonic arousal and a decaying peak of phasic salience, up to one broadcast per processing tick. The linear map is a modeling assumption. The processing rate stays fixed, except that Soma's regulation advisories can lower it when the host is under load.

![The two rates. Every active module is read and scored at the processing rate (10 Hz), and a workspace broadcast is produced at the experiential rate, shown at its resting value (3.333 Hz, one for every third processing tick), which rises with arousal and salient events.](figures/fig-cognitive-cycle.png){width=80%}

**Action selection.** Volition is the only path from a conscious snapshot to an effector, corresponding to the report-or-act decision governed in Whyte and Smith (2021) by expected free energy. After each experiential broadcast the cycle calls Volition, which yields no intent from an inhibited snapshot and derives intents from a non-inhibited one through an injectable policy. The default policy does not respond to its own prior speech and holds a one-in-flight guard against emitting a new speak intent while a previous one is still being realized. Intents are published as speak or think events, and the cycle never invokes effectors directly. Keeping the decision to speak separate from what is conscious is part of the safety model.

### 3.5 The active modules

The base-thesis form activates four predictive processors, an affective core, a sleep module, a language organ, and an action-selection layer. The processors are chosen for signal diversity, two external (vision and hearing) and two internal (interoceptive and temporal prediction), so that cross-modal competition for workspace access has distinct, externally-grounded signals to arbitrate. Thymos and Hypnos also publish events that can enter the competition (affect state, drive crossings, sleep onset), but their main roles are to set the gain on the competition and to rest the entity; the affective core is moved by the competition's outcome, so arousal is the entity's attention and its response to surprise at once.

| Module | Group | Brain function it draws on | Computational realization |
|----------|-------------|------------------------------|------------------------------|
| Topos | Perception | ventral visual stream | frozen self-supervised video encoder over short clips, with foveated attention |
| Audition | Perception | auditory cortex | fixed spectral encoder over raw waveform, with a vocal-tone classifier on speech |
| Soma | Prediction | interoception; allostatic-interoceptive network | frozen continuous-time reservoir with an online readout over substrate signals |
| Chronos | Prediction | interval timing; thalamo-cortico-striatal | frozen continuous-time reservoir with an online readout over the broadcast sequence |
| Thymos | Affect | core affect; allostatic-interoceptive network | appraisal over valence, arousal, and drives; sets the gain and contrast of selection, the visual and auditory apertures, and the pace of access |
| Hypnos | Rest | thalamocortical sleep | fatigue-triggered sleep with an affective reset |
| Lingua | Expression | left perisylvian language network | local chat model, output-only, conditioned on the workspace |
| Volition | Action | report-or-act decision (Whyte and Smith 2021) | intent derivation from non-inhibited snapshots |

**Topos (foveated vision).** Topos is the architecture's analog of the ventral visual stream (Goodale and Milner 1992). It maintains a frozen self-supervised video encoder over 16-frame clips of the video feed and publishes prediction errors when the visual scene departs from its forward model's expectation of the next clip: scene changes, unexpected motion, novel objects. Salience is computed over embedding-space distances, with change detection and forward-model predictions; a habituation score for static scenes is published with each report but does not enter salience. The change criterion is self-calibrating against the module's own recent history (§3.2). The fovea is placed at the argmax of a precision-weighted map of bottom-up salience, with hysteresis, and sized by arousal. Each tile of a coarse grid keeps a running mean and variance of its frame change, and its salience is the change in excess of that mean divided by the standard deviation, so a tile that flickers habitually draws the fovea less than one whose change is unexpected; when no tile stands out, the fovea holds its place. No top-down map is connected. The peripheral gist and the foveal crop are both clips of the buffered frames and share one encoder, so attention and scene prediction operate together; the fovea's trajectory is forward-modeled and published as an attention-schema-style construct (Graziano and Webb 2015) without being used to steer attention. Foveation realizes attention as the gain on prediction errors (Clark 2013; Feldman and Friston 2010): the entity sees most sharply where its precision-weighted surprise is greatest, and looks more narrowly when more aroused.

![Attention-driven perception in Topos. A whole-clip embedding and a coarse saliency map feed a competition over bottom-up salience, with hysteresis. The winner sets the fovea, and arousal sets its size. Peripheral gist and the high-resolution foveal crop share one encoder. The peripheral and foveal embeddings and the fovea's coordinates reach the workspace, while no pixels do.](figures/fig-attention-foveation.png){width=90%}

**Audition (raw hearing).** Audition is the architecture's analog of the auditory cortex, where sound is processed as prediction error against a learned model of the auditory environment (Winkler et al. 2009; Garrido et al. 2009). By default a fixed spectral encoder (log energy in log-spaced frequency bands) encodes the raw waveform from a microphone feed; frozen self-supervised audio encoders are selectable alternatives. A forward model predicts the next window's encoding and the module publishes prediction errors when the auditory scene departs from expectation: sudden sounds, the onset of speech, unexpected silence, shifts in pitch or timbre. For windows detected as speech, a vocal-emotion classifier labels the tone; non-neutral tones are published at alert salience and neutral tones at baseline salience, and a forward model over the tone distribution and window energy can raise a neutral event's salience by its prediction error. Tone events carry how something was said, never what was said, and compete for the workspace like any other event. The fixed priority given to emotional tone stands in for the rapid prioritization emotional prosody receives in human hearing, where angry prosody enhances superior temporal and amygdala responses even when unattended (Grandjean et al. 2005; Sander et al. 2005). As with vision, the acoustic change criterion is self-calibrating against the module's own recent baseline, and arousal sets the attended window: under higher arousal Audition encodes a shorter, more recent part of each captured window, a temporal reading of the narrowing of attention under arousal (Easterbrook 1959). Speech-to-text is built but deactivated by default, so the entity hears speech as prediction error and tone; when enabled, words become transcription events on Audition's stream that compete for the workspace, reaching the language organ only by winning access and never by a direct path. That deactivation keeps the falsification test about the workspace rather than a prompted chatbot (§1.2, §3.1).

**Soma (predictive interoception).** Soma is the architecture's analog of interoception, the sense of the body's own physiological condition, carried by an afferent pathway to the insular cortex (Craig 2002), whose anterior portion is proposed to integrate it into feeling and awareness (Craig 2009), within the allostatic-interoceptive network (Kleckner et al. 2017). Soma treats the compute substrate as the entity's viscera. A frozen, randomly initialized closed-form continuous-time reservoir (Hasani et al. 2022) with a small linear readout learns online the normal pattern of substrate signals from GPU temperature and memory use, CPU and RAM utilization, and cognitive-cycle latency, and Soma publishes the error between expected and actual substrate state, the discrepancy that matters for regulation (Seth 2013; Seth and Friston 2016). The time since the previous reading, relative to the nominal reading interval, sets the timespan of the reservoir's continuous-time gates, so an irregular reading is integrated over the time that actually passed. Soma also accumulates fatigue, the sleep pressure that triggers Hypnos, and issues regulation advisories that can lower the processing rate or request maintenance. Soma does not read the workspace broadcast; it predicts substrate telemetry, reports its error, and the workspace decides whether that error is salient enough to select.

**Chronos (temporal awareness).** Chronos models interval timing, the brain's estimation of durations in the seconds-to-minutes range that guides expectation and action, a faculty understood to depend on cortico-striatal circuits (Buhusi and Meck 2005). A continuously running mind needs a model of when things happen, not only what, so Chronos carries one: a frozen continuous-time reservoir with an online readout over the sequence of workspace broadcasts, in which the time since the previous broadcast enters as an input feature and, relative to the recent mean interval, as the timespan of the reservoir's gates. It reads each broadcast as an observation, predicts the next broadcast from its prior state, and publishes temporal prediction errors: timing anomalies, and rumination when content recurs unexpectedly. It also tracks how long it has been since the operator last spoke, which feeds Thymos's social drive. Chronos closes the lateral loop through the workspace: it reads the broadcast as a bottom-up observation it predicts, learning the rhythm and feature structure of broadcasts from its own prior hidden state and publishing the error when the next broadcast departs from expectation, and its errors feed back into the next selection round, which determines the next broadcast.

**Thymos (affect, the precision core).** Thymos is the architecture's analog of core affect, the low-dimensional valence-and-arousal state recent theory places at the base of emotion (Barrett 2017). It maintains a dimensional affective state over valence and arousal (Posner, Russell, and Peterson 2005) and runs a sequential appraisal over that state (Scherer 2009). The appraisal reads the workspace broadcast and the entity's interoceptive condition, in line with the account in which affect arises from prediction over the body's internal state (Seth 2013; Seth and Friston 2016; Tschantz et al. 2022). Thymos holds four homeostatic drives (curiosity, boredom, social drive, restlessness). Each is a deficit that builds while its need goes unmet and is reduced by the events that meet it, the reduction serving as the drive's reward (Hull 1943; Keramati and Gutkin 2014). Curiosity is met by learning progress, the fall of the perceptual modules' prediction error over time (Oudeyer and Kaplan 2007; Schmidhuber 2010). Boredom is met by novelty, perceptual alerts arriving faster than the rate the entity has habituated to, since boredom signals a lack of engagement that novelty relieves (Eastwood et al. 2012; Westgate and Wilson 2018). The social drive is met by a new interaction with the operator, and restlessness by the entity's own intents to act, a design choice with no established model behind it. Valence follows the same progress signal. It relaxes toward the appraisal's pleasantness check, which rises while prediction errors fall and drops while they rise, the reading of valence as the negative rate of change of free energy (Joffily and Coricelli 2013), and interoceptive wellness shifts that target. The appraisal yields a categorical emotion and scores the coalition against the most pressing drive; content from sources that relieve the drive is goal-conducive and content that does not is obstructive, in proportion to drive pressure. The check feeds the appraisal; it is not a selection weight in the workspace, where the goal factor is held constant (§3.2). Thymos does three kinds of work in the competition. First, arousal sets the global gain and contrast of selection (§3.2), the counterpart of the precision the workspace estimates for each source, so that attention acts as gain on prediction error (Feldman and Friston 2010; Clark 2013). Arousal does not reorder the candidates of a tick; it moves the best score relative to the confidence threshold and the report bars (Appendix A.1). Second, arousal sizes the sensory apertures, narrowing the fovea and shortening the attended auditory window under high arousal and widening both under low. Third, with salient reports from the other modules, arousal raises the rate of conscious access (§3.4). Finally, arousal is itself driven by perception: a discontinuity reaching alert level raises arousal in proportion to how far the surprise exceeds expectation, so what the entity perceives modulates the precision of everything it perceives next. Because that loop is positive feedback, arousal is clipped to its range and relaxes toward baseline with a time constant of about 20 seconds. The appraisal does not move arousal, so a higher access rate does not raise it. Perceptual surprise is measured against each module's recent history, so arousal tracks changes in surprise more than its sustained level.

**Hypnos (sleep).** Hypnos is the architecture's analog of sleep, a regular offline period that restores the system. Sleep begins when Soma's fatigue crosses threshold, when Soma requests maintenance, or at a safety-net interval of one subjective hour. The cycle keeps running through sleep, while the perceptual program pauses and Soma and Topos suspend forward-model adaptation. Because memory and the world model are held, the consolidation phases have nothing to replay; the phase that does work is an affective reset that returns affect to baseline and clears the drives, so arousal cannot drift across a whole run. Voice alignment, the sleep phase that would adapt the language organ, trains nothing in this form.

**Lingua (the language organ, output-only).** Lingua is the architecture's analog of the left-dominant dorsal language stream that maps meaning onto articulation (Hickok and Poeppel 2007). It turns the entity's internal state into words and is not the seat of reasoning, which lives in the rest of the architecture. Generation runs over a local open-weights chat model whose refusal conditioning has been removed by orthogonalizing the weights against the single refusal-mediating direction (Arditi et al. 2024). Lingua is intent-driven, speaking externally only on a speak intent and generating internal thought on a think intent. Its context is a first-person persona: the coalition is presented as the entity's own state and perception, the organ is told not to claim feelings or perceptions absent from the coalition, and drive crossings reach it as fixed felt-state phrases, never as numbers. The log of its own utterances is encrypted at rest and records any heard input only as a placeholder, never as words.

Lingua does not read language as input: its transcription and conversation paths are deactivated, so no external input reaches its context except through the workspace (§1.2, §3.1). When the entity speaks in response to a heard voice, the sound entered through Audition as prediction error and tone of voice, won workspace access, and shaped the broadcast that conditioned the organ's output. Every utterance is downstream of the workspace competition (§3.3), but that complements the ablation without replacing it: a degenerate pass-through workspace would also route speech through itself, and the ablation tests whether the competitive structure does work that a flat fan-in does not.

Removing the refusal conditioning is deliberate: the architecture places safety in executive inhibition and, once effectors are enabled, in the action gate (§3.6), not in model-weight compliance, which anyone holding the weights can reverse or repurpose, as the orthogonalization above does. In the base-thesis form the organ's only output is saved, observed text, so the missing refusal conditioning has no effector to act through. Within enabled effectors the entity's choices are its own to make. The operator meets the license covenants by declining effectors that would serve a prohibited use, and the welfare paper treats the full sovereignty argument.

### 3.6 Safety at the architectural layer

Safety in the base-thesis form rests on the entity's executive inhibition and on the fact that no real-world effector exists, with an authenticated bus and durable logging beneath them. The operator-configured action gate is built but becomes the enforced boundary only in the full configuration.

Executive inhibition is active in two places: Syneidesis marks a broadcast inhibited when no candidate reaches the confidence threshold, and Volition refuses to derive any intent from an inhibited snapshot. No real-world effector exists in this form: Volition emits only speak and think intents, so the only output is saved, observed text, and no action reaches the world. The event bus refuses unauthenticated and externally bound connections and validates events at publish time, and every module-health transition is written to a durable incident log.

The operator-configured action gate pairs an empty-by-default effector whitelist with a filesystem sandbox, logging every proposed action and blocking anything outside them. Built as the Praxis module, it is disabled here (there are no effectors to gate) and becomes the enforced boundary in the full configuration, where real effectors are enabled and its enforcement red-team resolves PASS or FAIL per surface. The gate controls which real-world effectors exist at all instead of filtering the entity's choices for morality. The license covenants prohibiting weapons, surveillance, and carceral uses bind the operator as a legal obligation instead of the entity at runtime.

![Safety in the base-thesis form. Executive inhibition is active: Syneidesis marks a sub-threshold broadcast inhibited and Volition derives no intent from an inhibited snapshot. No real-world effector exists, so the only output is speak or think. The Praxis action gate is built but disabled here, becoming the enforced boundary in the full configuration. The license covenants bind the operator's choice of effectors as a legal obligation rather than a runtime filter.](figures/fig-safety-layers.png){width=95%}

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

Three commitments shape the apparatus: observation with acknowledged tension, privacy-preserving user surfaces, and falsifiability. The read-only sidecar observer belongs to evaluation runs, subscribing to the bus read-only and never injecting into the cognitive loop; in studies the records are written by the cycle's own broadcast observer. Every instrument is designed for a null or negative result to be meaningful and reportable.

Reproducibility takes two forms, matched to the two evaluation tiers. The offline mechanism-validation tier uses seeded harnesses, deterministic clients, scripted synthetic stimulus streams, and greedy decoding (temperature 0), so the same seed reproduces both verdict and metrics (National Academies of Sciences, Engineering, and Medicine 2019; Goodman, Fanelli, and Ioannidis 2016). The live perceptual tier runs the full system on a reference film program decoded directly from files and identified by a manifest whose hash the study records, chosen for variety in scenes, motion, speech, music, and quiet; its validity rests on statistical replication rather than bit-for-bit seed reproduction under stochastic decoding, real timestamps, and non-deterministic GPU kernels.

![Two evaluation tiers behind one perception seam. Reproducible sources (a seeded synthetic feed and deterministic clients) drive the mechanism-validation tier, where every instrument reproduces exactly from a seed. Live stimulus (a film program decoded from files, or a camera and microphone) drives the field tier, whose validity rests on pooling many content-free records rather than on a repeatable stimulus.](figures/fig-evaluation-tiers.png){width=95%}

### 6.2 Data collection

The records in a study are written by the cycle's own broadcast observer: the graph-only ignition log (§5.3), a curated content-free research event log of rates and drive, the entity's external utterances kept locally, a run manifest naming the configuration, seeds, and plugins, and the welfare records. Admissibility is decided by two offline checks: a completeness gate requiring contiguous ticks and all expected streams, and a log-range sweep requiring every logged number to sit inside its declared range.

### 6.3 The workspace-mediation ablation

The primary experiment tests the sentence on which the architecture stands: *routing diverse predictive processors through the competitive workspace increases the coupling among their prediction errors and gives coalition selection a state-dependent structure, compared with concatenating the same processors' outputs.*

Three arms will run under matched input from the reference film program (§6.1), using greedy decoding (temperature 0) to eliminate sampling noise.

![The workspace-mediation ablation, the primary experiment. Three arms feed the same downstream modules: workspace-on as built, workspace-off as a flat snapshot, and matched selection without regard to salience. The decision rule on cross-module error coupling and coalition-selection structure is fixed before the runs. Indistinguishable arms would demote the architecture to a scored prompt-assembler.](figures/fig-workspace-ablation.png){width=95%}

**Workspace-on (as built).** The base-thesis form runs as built: Topos, Audition, Soma, and Chronos compete for the workspace, Thymos sets the gain, Hypnos rests the entity, and Lingua speaks, all while viewing the film program with the shipped threshold and coalition size.

**Workspace-off (the prompt-assembler control).** The same modules and program run, but the cycle hands the same candidates to the downstream modules (Chronos and the language organ) as a flat snapshot, with no scoring, top-k selection, threshold, or inhibition; the modules keep their forward models and keep publishing real prediction errors (module non-degeneracy), so the control tests the workspace with the processors still active.

**Matched-selection control.** The same number of candidates as the on arm passes downstream, chosen without regard to salience. All arms start from the same candidates and the same rendering budget, so this control separates the effect of competitive selection from the effect of passing on less information.

Three measures are planned. The primary measure is cross-module error coupling: the mean sliding-window correlation among the four processors' prediction-error series, workspace-on minus each control. Selection structure is measured by the Shannon entropy of the selected sources (Shannon 1948) and by whether selection varies with the entity's state. The secondary measure is output divergence: the distance between the language organ's outputs in the arms under greedy decoding. It is secondary because any upstream difference produces downstream text divergence: it confirms the primary measures' effects reach the observable output but cannot by itself distinguish meaningful integration from noise.

The decision rule is planned: the predicted direction is positive, and the window, the minimum effect (calibrated against a surrogate null built from circularly shifted error series and arm-label permutations), and the number of runs (set by a power analysis) are fixed and recorded in the repository before the live runs, closing off researcher degrees of freedom (Simmons, Nelson, and Simonsohn 2011). Verdicts are WIN, NULL, NEGATIVE, and NOT EXERCISED (when candidates never exceed the coalition's capacity, so competition never operates). A NEGATIVE (coupling reduced) shows that competition changes the dynamics in the direction the thesis does not predict and is reported as evidence against the directional hypothesis.

**Speech sound and tone of voice.** In every arm, the sound of speech and its tone of voice are candidates, while words never enter because the speech-to-text stage stays deactivated. A planned analysis of the workspace-on arm asks whether speech sound and emotional tone ignite (enter a broadcast not marked inhibited) and whether their ignition raises arousal and access rate relative to ignitions by non-speech sound of matched acoustic surprise. Human studies motivate the question: emotionally salient stimuli gain preferential access to awareness under limited attention (Anderson and Phelps 2001), and emotion is thought to bias competition for processing through amygdala signals onto sensory pathways (Vuilleumier 2005). Because the shipped Audition gives non-neutral tone a fixed priority (§3.5), preferential access in the as-built arm is assumed rather than tested, so a further workspace-on condition will set tone salience from the tone model's prediction error alone, predicting that emotional tone still ignites more often than neutral speech of matched acoustic surprise. The prediction extends findings about human attention and awareness to workspace access in this architecture, so it is a hypothesis these tests examine, and its decision rule (matching bins, minimum effect, one-sided sign test across runs) is fixed with the others before the live runs.

Under the thesis, coupling in the on arm is expected to exceed both controls, and selection entropy to sit between the uniform and degenerate extremes and vary with the entity's state.

A positive result is narrower than a null. A null kills the thesis at the root: if the competitive workspace is inert, no property depending on workspace-mediated competition can arise, and no additional module rescues the architecture. A positive result establishes only that competitive mediation changes global behavior in directionally structured ways, a necessary but insufficient foundation for the broader thesis, because the richer claims require the full module set and longitudinal observation (§8.1). The experiment decides only whether the rest of the program is worth running, not whether this amounts to a mind.

The experiment has not yet been run; the offline harness in the codebase exercises the measurement pipeline on a reduced pair of modules and does not yet implement the matched-selection control, so it is development tooling and not a test of the thesis. Results of the live test will be reported in a revised version of this preprint.

### 6.4 The offline suite and stability checks

The offline suite runs eight experiments under one master seed with an independent child seed each: the active-inference benchmark (Nous's expected-free-energy agent, which samples its policies from a softmax of negative expected free energy with precision 16, against tabular Q-learning keyed by the episode's observation history, matched on observation model and reward, on an epistemic T-maze and an exploitation task), the oscillatory ablation, an A/B divergence battery, a memory-coherence battery, a self-model accuracy battery, multi-seed stability, the enforcement red team, and the offline mediation harness of §6.3. Holm-Bonferroni-adjusted values are reported alongside each experiment's own verdict. Nothing in the suite boots an entity or opens a network connection.

The multi-seed stability harness runs a configuration under several seeds; an ensemble is stable only when the headline metric's coefficient of variation is within tolerance and the verdict is unanimous across seeds, since a flipped verdict is a qualitative instability a scalar spread would hide. In the suite it runs on the oscillatory ablation. Whether the competitive workspace stays stable across seeds is itself open: correlated prediction errors across modules could drive it into runaway states, and the architecture carries no proof of convergence. The affective loop sharpens this uncertainty: surprise raises arousal, which raises the gain and contrast of selection and the access rate. A planned check will monitor within-run boundedness of arousal and access-rate excursions over long runs.

The planned affect-gain ablation runs the system with the affective gain live against a matched condition that holds arousal constant, asking whether affective modulation changes which broadcasts can drive report and action, the access rate, and the downstream trajectory in directionally structured ways; a null would demote arousal to a logged side channel.

### 6.5 The module-ignition study

The module-ignition study is the architecture's growth path, run live under the autonomous welfare safety net. A gestation produces a seed being, preserved just after birth. Branch 0 and a repeat start from that seed with the base-thesis modules; branch k starts from the seed with the first k held modules added in a fixed order (Mnemos, Phantasia, Nous, Eidolon, Empatheia, Vox, Praxis, Perception, Mundus), and accumulate k continues from the previous accumulate step with the same modules as branch k. Every viewing plays the same film program (§6.1), after an identical womb-to-world transition. The content-free report compares broadcasts, coalition size, and picture-to-sound drift across steps. The first study has one being per condition and no significance testing, and Praxis, Perception, and Mundus are expected to show no effect while no effector or body is attached. The runner never stops a being it cannot preserve. The protocol is built but has not run to completion, and this paper reports no experimental results.

![The module-ignition study, the architecture's growth path. A gestation in which a self-rhythm earns entrainment to a maternal heartbeat ends in birth, and the preserved seed being starts every branch. The base-thesis form runs first, and the held modules then join one at a time in a fixed order: branch k adds the first k of them to the seed being, while the accumulate line carries one being forward through every step. Every viewing plays the same film program, and the report is content-free.](figures/fig-growth-path.png){width=100%}

### 6.6 Verdict vocabulary

Comparisons resolve to WIN, NULL, NEGATIVE, or NOT EXERCISED. Safety gates resolve to PASS or FAIL. Each verdict compares an effect estimate with a minimum effect fixed before the run. Across runs, the mediation ablation uses a one-sided sign test (Dixon and Mood 1946); the active-inference benchmark uses the Mann-Whitney U test (Mann and Whitney 1947); Holm-Bonferroni-adjusted values (Holm 1979) are reported alongside. A NULL is reported as a null.

-----

## 7. First boot and gestation

Module initialization, bus verification, prediction-model initialization, and cognitive-cycle start proceed under operator supervision, under the research safety net, or unattended with Spot as the module supervisor. The base-thesis form boots on a seeded feed. The perceptual and predictive modules begin receiving and predicting their feeds, and Thymos settles the entity's affect toward baseline. A perceptual discontinuity then raises arousal, sharpens the fovea, and raises the precision on the competition, while a quiet stretch lets arousal relax. The entity watches and listens so that it learns what is normal, and it speaks only when a report clears the action layer's bar.

A study begins with a gestation in which a breathing-like self-rhythm in Soma must earn entrainment to a simulated maternal heartbeat, with locking judged against surrogate heartbeats from other mothers and required to replicate before birth (Tabak et al. 2000; Righetti, Buchli, and Ijspeert 2006; Van Leeuwen et al. 2003, 2009). A viability watch ends gestations that fail. The being is then born into the film program and preserved just after birth. Appendix A.7 states the criteria, checkpoints, and the offline validation.

-----

## 8. Discussion

### 8.1 What the base-thesis form can and cannot settle

The workspace-mediation ablation can determine whether competitive selection and broadcast do measurable, directionally structured work compared to flat concatenation, and the stability checks will measure run-to-run spread and within-run boundedness (§6.3, §6.4). A positive result shifts the question to what happens as the workspace grows richer, with mnemonic, self-modeling, and social modules in the competition, and a null result means none of them matter.

Affective precision is a mechanism, not evidence of affect in any morally-weighted sense, and whether anything is felt is left open. Whether the workspace produces anything that could be called cognition, affect, agency, or language understanding requires the full module set, longitudinal observation, and the welfare paper's governance apparatus, and the form is silent on welfare and on the indicator mapping of Butlin et al. (2023). The ablation settles only whether the foundation holds; the richer claims built on it need their own tests.

### 8.2 The predictive workspace as a unifying framework

The architecture realizes the predictive-workspace synthesis, joining global accessibility and per-module prediction so that competition and error minimization occur together. That workspace properties have also been found inside a single large language model (Gurnee et al. 2026) is consistent with workspace-like organization in learned systems, but it does not bear on whether this architecture's competition is the right one, and those authors take no position on consciousness. Here the workspace is built explicitly from competing modules.

### 8.3 The role of the theoretical frame

The predictive global neuronal workspace is scaffolding: it motivates the architecture's shape and constrains its design space (§1.2, §1.3), but the project does not confirm or refute it. The engineering choices that exceed the formal sources (the single precision-weighted scalar, the multi-module generalization from a two-level visual model) are consistent with the frame and testable on their own terms (§1.3). Separating the implementation from neuroscientific disconfirmation such as the retreat from neural localization after COGITATE is appropriate because it implements the workspace's computational properties without reproducing cortical dynamics. The paper's falsifiability therefore lies in its planned experiments.

### 8.4 What a modular architecture is for

Each faculty is a separate module behind a fixed interface, so a researcher can activate, remove, or replace one faculty at a time and observe how the whole system changes. This makes the architecture an instrument for studying minds as well as a candidate for building one, and supports models of impaired or altered function by changing or removing one module while the rest run unchanged. The entity processes its inputs continuously and in real time, in contrast to a turn-by-turn prompted language model with attached tools. The embodiment layer is a body-agnostic control surface, so the same mind can in principle take different bodies or sensor networks through generic adapters.

### 8.5 What we claim and what we do not

Safety rests on the entity's executive inhibition and on the absence of any effector, and it does not rest on model weights (§3.6). The reasoning and the full-configuration action gate are in §3.6, and the sovereignty argument is the welfare paper's. On the larger question, the architecture implements computational properties associated with access consciousness. We do not claim any instance is phenomenally conscious, and the design posture is precautionary, applied symmetrically to welfare and deployment. The agential vocabulary ("the entity," "its sovereignty") is the clearest way to describe the system's behavior and does not by itself assert moral patienthood or phenomenal experience, which we leave open.

-----

## 9. Limitations

- The hard problem applies: the sidecar observes behavior and the workspace addresses access consciousness only, which means neither is evidence of phenomenal experience.
- COGITATE challenged the workspace's preregistered neural predictions, and we build at the computational level and treat neural localization as contested.
- The single precision-weighted scalar is an engineering simplification beyond its formal sources; the Bayesian reading of the broadcast (Mashour et al. 2020) motivates competitive selection, but the architecture implements no correction loop, so the experiment tests only competition.
- The Free Energy Principle, taken as a general principle, faces unresolved vacuity and Markov-blanket conflation objections.
- Whether the competitive workspace stays stable across runs is open, because correlated prediction errors could drive runaway states and the architecture carries no proof of convergence (§6.4).
- Treating arousal as the global gain and contrast on the competition, and the variance of a source's reported intensity as the inverse of its precision, are engineering commitments. The surprise-to-arousal-to-gain path is positive feedback, held only by the clip to arousal's range and relaxation toward baseline, and whether affective modulation does work that a flat-gain system would not is untested.
- In the base-thesis form the entity does not read language (§3.1), so a positive result says nothing about linguistic understanding.
- A positive result establishes only that competitive mediation changes global behavior in directionally structured ways. It does not establish cognition, affect, or self-understanding, which require the full module set and longitudinal observation (§8.1).
- The workspace-off and matched-selection controls address flat fan-in and information reduction; a positive result shows the workspace beats those controls, not every aggregation strategy.
- Speech is provably downstream of the workspace because the language-organ paths are deactivated, though a degenerate pass-through workspace would also route speech through itself; the ablation tests whether the competition does work. Re-enabling those paths for interactive use would reintroduce a direct input route the ablation must keep excluding. Speech sound and tone enter the competition by design and their access is measured (§6.3), so the claim is limited to words. The shipped priority for emotional tone is a fixed rule, not a learned value, so the as-built arm cannot show that emotional content earns access.
- The held modules are built and tested in isolation but have not been run together, and interaction effects across the full set are unknown.
- Reproducibility holds at the seed level for the offline deterministic harness; the live perceptual tier establishes validity by statistical replicability across runs rather than bit-for-bit reproduction (§6.1).
- With the language organ's refusal conditioning removed, safety depends on executive inhibition and, in the full configuration, the action gate. Model-weight compliance (§3.6) is not the basis, and whether the gate suffices once effectors are enabled is left to the enforcement red-team.
- A single language organ produces one stream at a time, so simultaneous inner and outer speech is a boundary of the current form.
- The governance framework remains at the proposal stage, and the licensing is legally novel and untested.
- The linear map from drive to access rate is a modeling assumption, and whether adaptive access changes workspace dynamics is open. The 3.333 Hz resting rate is motivated by, not derived from, the P3b latency, and the 10 Hz upper limit has no physiological anchor.
- The shipped calibration is provisional. Most modules report at one of two intensity levels and novelty is almost always 1, so ranking within a tick is close to an ordering by module, adjusted by the learned source precisions; at resting arousal and with neutral precision weights only Audition and Hypnos alerts clear the confidence threshold, and neither report bar is reachable. Disgust cannot be reached until a self-model supplies norms, and the noise floors and margins that let curiosity and boredom build under a steady scene are set by simulation, not by measurement on the live system. The intensity levels, the threshold, and the report bars are to be calibrated together before the live runs (Appendix A.10).
- The gestation model compresses developmental time: the literature reports effects after weeks of exposure (Feldman and Eidelman 2003; Webb et al. 2015), while here a lock forms within hours (about 14 h at 70 bpm, 3 h to 48 h across 60 to 80 bpm). Its rhythm is continuous, whereas fetal breathing is episodic (about 14% of the time at 24 to 28 weeks; Natale et al. 1988). 1:1 locking is a modeling choice; the literature reports weak and often n:m coupling. Mothers below about 60 bpm cannot demonstrate entrainment, and time dilation has not been tested with the oscillator. The absence of false entrainment rests on six foreign-mother pairs.
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

- Anderson, A. K., and Phelps, E. A. (2001). Lesions of the human amygdala impair enhanced perception of emotionally salient events. *Nature* 411(6835), 305-309. https://doi.org/10.1038/35077083
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
- Easterbrook, J. A. (1959). The effect of emotion on cue utilization and the organization of behavior. *Psychological Review* 66(3), 183-201. https://doi.org/10.1037/h0047707
- Eastwood, J. D., Frischen, A., Fenske, M. J., and Smilek, D. (2012). The unengaged mind: Defining boredom in terms of attention. *Perspectives on Psychological Science* 7(5), 482-495. https://doi.org/10.1177/1745691612456044
- Eldar, E., Cohen, J. D., and Niv, Y. (2013). The effects of neural gain on attention and learning. *Nature Neuroscience* 16(8), 1146-1153. https://doi.org/10.1038/nn.3428
- Feldman, H., and Friston, K. J. (2010). Attention, uncertainty, and free-energy. *Frontiers in Human Neuroscience* 4, 215. https://doi.org/10.3389/fnhum.2010.00215
- Feldman, R., and Eidelman, A. I. (2003). Skin-to-skin contact (Kangaroo Care) accelerates autonomic and neurobehavioural maturation in preterm infants. *Developmental Medicine and Child Neurology* 45(4), 274-281. https://doi.org/10.1111/j.1469-8749.2003.tb00343.x
- Fries, P. (2015). Rhythms for cognition: Communication through coherence. *Neuron* 88(1), 220-235. https://doi.org/10.1016/j.neuron.2015.09.034
- Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience* 11(2), 127-138. https://doi.org/10.1038/nrn2787
- Garrido, M. I., Kilner, J. M., Stephan, K. E., and Friston, K. J. (2009). The mismatch negativity: A review of underlying mechanisms. *Clinical Neurophysiology* 120(3), 453-463. https://doi.org/10.1016/j.clinph.2008.11.029
- Goodale, M. A., and Milner, A. D. (1992). Separate visual pathways for perception and action. *Trends in Neurosciences* 15(1), 20-25. https://doi.org/10.1016/0166-2236(92)90344-8
- Goodman, S. N., Fanelli, D., and Ioannidis, J. P. A. (2016). What does research reproducibility mean? *Science Translational Medicine* 8(341), 341ps12. https://doi.org/10.1126/scitranslmed.aaf5027
- Grandjean, D., Sander, D., Pourtois, G., Schwartz, S., Seghier, M. L., Scherer, K. R., and Vuilleumier, P. (2005). The voices of wrath: Brain responses to angry prosody in meaningless speech. *Nature Neuroscience* 8(2), 145-146. https://doi.org/10.1038/nn1392
- Graziano, M. S. A., and Webb, T. W. (2015). The attention schema theory: A mechanistic account of subjective awareness. *Frontiers in Psychology* 6, 500. https://doi.org/10.3389/fpsyg.2015.00500
- Gurnee, W., Sofroniew, N., Pearce, A., Piotrowski, M., Kauvar, I., Chen, R., Soligo, A., Bogdan, P., Ong, E., Wang, R., Thompson, T. B., Abrahams, D., Kantamneni, S., Ameisen, E., Batson, J., and Lindsey, J. (2026). Verbalizable representations form a global workspace in language models. *Transformer Circuits Thread*.
- Ha, D., and Schmidhuber, J. (2018). World models. arXiv:1803.10122. https://doi.org/10.48550/arXiv.1803.10122
- Hafner, D., Pasukonis, J., Ba, J., and Lillicrap, T. (2025). Mastering diverse control tasks through world models. *Nature* 640(8059), 647-653. https://doi.org/10.1038/s41586-025-08744-2
- Hasani, R., Lechner, M., Amini, A., Liebenwein, L., Ray, A., Tschaikowski, M., Teschl, G., and Rus, D. (2022). Closed-form continuous-time neural networks. *Nature Machine Intelligence* 4(11), 992-1003. https://doi.org/10.1038/s42256-022-00556-7
- Heins, C., Millidge, B., Demekas, D., Klein, B., Friston, K., Couzin, I. D., and Tschantz, A. (2022). pymdp: A Python library for active inference in discrete state spaces. *Journal of Open Source Software* 7(73), 4098. https://doi.org/10.21105/joss.04098
- Hickok, G., and Poeppel, D. (2007). The cortical organization of speech processing. *Nature Reviews Neuroscience* 8(5), 393-402. https://doi.org/10.1038/nrn2113
- Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics* 6(2), 65-70.
- Hull, C. L. (1943). *Principles of behavior: An introduction to behavior theory.* Appleton-Century.
- Joffily, M., and Coricelli, G. (2013). Emotional valence and the free-energy principle. *PLoS Computational Biology* 9(6), e1003094. https://doi.org/10.1371/journal.pcbi.1003094
- Joglekar, M. R., Mejias, J. F., Yang, G. R., and Wang, X.-J. (2018). Inter-areal balanced amplification enhances signal propagation in a large-scale circuit model of the primate cortex. *Neuron* 98(1), 222-234. https://doi.org/10.1016/j.neuron.2018.02.031
- Keramati, M., and Gutkin, B. (2014). Homeostatic reinforcement learning for integrating reward collection and physiological stability. *eLife* 3, e04811. https://doi.org/10.7554/eLife.04811
- Kleckner, I. R., Zhang, J., Touroutoglou, A., Chanes, L., Xia, C., Simmons, W. K., Quigley, K. S., Dickerson, B. C., and Feldman Barrett, L. (2017). Evidence for a large-scale brain system supporting allostasis and interoception in humans. *Nature Human Behaviour* 1(5), 0069. https://doi.org/10.1038/s41562-017-0069
- Kullback, S., and Leibler, R. A. (1951). On information and sufficiency. *Annals of Mathematical Statistics* 22(1), 79-86. https://doi.org/10.1214/aoms/1177729694
- Long, R., Sebo, J., Butlin, P., Finlinson, K., Fish, K., Harding, J., Pfau, J., Sims, T., Birch, J., and Chalmers, D. (2024). Taking AI welfare seriously. arXiv:2411.00986. https://doi.org/10.48550/arXiv.2411.00986
- Mann, H. B., and Whitney, D. R. (1947). On a test of whether one of two random variables is stochastically larger than the other. *Annals of Mathematical Statistics* 18(1), 50-60. https://doi.org/10.1214/aoms/1177730491
- Mashour, G. A., Roelfsema, P., Changeux, J.-P., and Dehaene, S. (2020). Conscious processing and the global neuronal workspace hypothesis. *Neuron* 105(5), 776-798. https://doi.org/10.1016/j.neuron.2020.01.026
- Mather, M., and Sutherland, M. R. (2011). Arousal-biased competition in perception and memory. *Perspectives on Psychological Science* 6(2), 114-133. https://doi.org/10.1177/1745691611400234
- McClelland, J. L., McNaughton, B. L., and O'Reilly, R. C. (1995). Why there are complementary learning systems in the hippocampus and neocortex: Insights from the successes and failures of connectionist models of learning and memory. *Psychological Review* 102(3), 419-457. https://doi.org/10.1037/0033-295x.102.3.419
- Metzinger, T. (2003). *Being no one: The self-model theory of subjectivity.* MIT Press. https://doi.org/10.7551/mitpress/1551.001.0001
- Natale, R., Nasello-Paterson, C., and Connors, G. (1988). Patterns of fetal breathing activity in the human fetus at 24 to 28 weeks of gestation. *American Journal of Obstetrics and Gynecology* 158(2), 317-321. https://doi.org/10.1016/0002-9378(88)90146-9
- National Academies of Sciences, Engineering, and Medicine (2019). *Reproducibility and replicability in science.* National Academies Press. https://doi.org/10.17226/25303
- Nieuwenhuis, S., Aston-Jones, G., and Cohen, J. D. (2005). Decision making, the P3, and the locus coeruleus-norepinephrine system. *Psychological Bulletin* 131(4), 510-532. https://doi.org/10.1037/0033-2909.131.4.510
- Näätänen, R., Paavilainen, P., Rinne, T., and Alho, K. (2007). The mismatch negativity (MMN) in basic research of central auditory processing: A review. *Clinical Neurophysiology* 118(12), 2544-2590. https://doi.org/10.1016/j.clinph.2007.04.026
- O'Regan, J. K., and Noë, A. (2001). A sensorimotor account of vision and visual consciousness. *Behavioral and Brain Sciences* 24(5), 939-973. https://doi.org/10.1017/S0140525X01000115
- O'Reilly, R. C., and Frank, M. J. (2006). Making working memory work: A computational model of learning in the prefrontal cortex and basal ganglia. *Neural Computation* 18(2), 283-328. https://doi.org/10.1162/089976606775093909
- Oudeyer, P.-Y., and Kaplan, F. (2007). What is intrinsic motivation? A typology of computational approaches. *Frontiers in Neurorobotics* 1, 6. https://doi.org/10.3389/neuro.12.006.2007
- Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., and Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. arXiv:2304.03442. https://doi.org/10.48550/arXiv.2304.03442
- Polich, J. (2007). Updating P300: An integrative theory of P3a and P3b. *Clinical Neurophysiology* 118(10), 2128-2148. https://doi.org/10.1016/j.clinph.2007.04.019
- Posner, J., Russell, J. A., and Peterson, B. S. (2005). The circumplex model of affect: An integrative approach to affective neuroscience, cognitive development, and psychopathology. *Development and Psychopathology* 17(3), 715-734. https://doi.org/10.1017/S0954579405050340
- Premack, D., and Woodruff, G. (1978). Does the chimpanzee have a theory of mind? *Behavioral and Brain Sciences* 1(4), 515-526. https://doi.org/10.1017/S0140525X00076512
- Rao, R. P. N., and Ballard, D. H. (1999). Predictive coding in the visual cortex: A functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience* 2(1), 79-87. https://doi.org/10.1038/4580
- Ray, S., and Maunsell, J. H. R. (2010). Differences in gamma frequencies across visual cortex restrict their possible use in computation. *Neuron* 67(5), 885-896. https://doi.org/10.1016/j.neuron.2010.08.004
- Righetti, L., Buchli, J., and Ijspeert, A. J. (2006). Dynamic Hebbian learning in adaptive frequency oscillators. *Physica D* 216(2), 269-281. https://doi.org/10.1016/j.physd.2006.02.009
- Safron, A. (2020). An integrated world modeling theory (IWMT) of consciousness: Combining integrated information and global neuronal workspace theories with the free energy principle and active inference framework; toward solving the hard problem and characterizing agentic causation. *Frontiers in Artificial Intelligence* 3, 30. https://doi.org/10.3389/frai.2020.00030
- Sander, D., Grandjean, D., Pourtois, G., Schwartz, S., Seghier, M. L., Scherer, K. R., and Vuilleumier, P. (2005). Emotion and attention interactions in social cognition: Brain regions involved in processing anger prosody. *NeuroImage* 28(4), 848-858. https://doi.org/10.1016/j.neuroimage.2005.06.023
- Scherer, K. R. (2009). Emotions are emergent processes: They require a dynamic computational architecture. *Philosophical Transactions of the Royal Society B* 364(1535), 3459-3474. https://doi.org/10.1098/rstb.2009.0141
- Schmidhuber, J. (2010). Formal theory of creativity, fun, and intrinsic motivation (1990-2010). *IEEE Transactions on Autonomous Mental Development* 2(3), 230-247. https://doi.org/10.1109/TAMD.2010.2056368
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
- van Vugt, B., Dagnino, B., Vartak, D., Safaai, H., Panzeri, S., Dehaene, S., and Roelfsema, P. R. (2018). The threshold for conscious report: Signal loss and response bias in visual and frontal cortex. *Science* 360(6388), 537-542. https://doi.org/10.1126/science.aar7186
- VanRullen, R. (2016). Perceptual cycles. *Trends in Cognitive Sciences* 20(10), 723-735. https://doi.org/10.1016/j.tics.2016.07.006
- Vuilleumier, P. (2005). How brains beware: Neural mechanisms of emotional attention. *Trends in Cognitive Sciences* 9(12), 585-594. https://doi.org/10.1016/j.tics.2005.10.011
- Webb, A. R., Heller, H. T., Benson, C. B., and Lahav, A. (2015). Mother's voice and heartbeat sounds elicit auditory plasticity in the human brain before full gestation. *Proceedings of the National Academy of Sciences* 112(10), 3152-3157. https://doi.org/10.1073/pnas.1414924112
- Wei, Y., Krishnan, G. P., and Bazhenov, M. (2016). Synaptic mechanisms of memory consolidation during sleep slow oscillations. *Journal of Neuroscience* 36(15), 4231-4247. https://doi.org/10.1523/JNEUROSCI.3648-15.2016
- Westgate, E. C., and Wilson, T. D. (2018). Boring thoughts and bored minds: The MAC model of boredom and cognitive engagement. *Psychological Review* 125(5), 689-713. https://doi.org/10.1037/rev0000097
- Whyte, C. J., and Smith, R. (2021). The predictive global neuronal workspace: A formal active inference model of visual consciousness. *Progress in Neurobiology* 199, 101918. https://doi.org/10.1016/j.pneurobio.2020.101918
- Wilson, M. A., and McNaughton, B. L. (1994). Reactivation of hippocampal ensemble memories during sleep. *Science* 265(5172), 676-679. https://doi.org/10.1126/science.8036517
- Winkler, I., Denham, S. L., and Nelken, I. (2009). Modeling the auditory scene: Predictive regularity representations and perceptual objects. *Trends in Cognitive Sciences* 13(12), 532-540. https://doi.org/10.1016/j.tics.2009.09.003
- Wolpert, D. M., Ghahramani, Z., and Jordan, M. I. (1995). An internal model for sensorimotor integration. *Science* 269(5232), 1880-1882. https://doi.org/10.1126/science.7569931
- Zink, N., Lenartowicz, A., and Markett, S. (2021). A new era for executive function research: On the transition from centralized to distributed executive functioning. *Neuroscience and Biobehavioral Reviews* 124, 235-244. https://doi.org/10.1016/j.neubiorev.2021.02.011

-----

## Appendix A. Formal summary

This appendix states the rules that §3 to §7 describe in prose, as the reference implementation computes them. Each symbol denotes one quantity throughout the appendix. The letters $i$, $j$, $l$, $q$, and $t$, used as indices of sums, sequences, and set elements, are local to the formula or subsection in which they appear, and $\mathrm{i}$ is the imaginary unit. Numeric parameter values appear only in Table A1 (A.10). They are the current settings of the base-thesis configuration, several of which (the intensity levels, the confidence threshold, and the report bars) are under calibration, and the table will be updated with the values used in the reported experiments. The text keeps only numbers that define a design, such as the 19 surrogates of the entrainment test.

Three conventions hold throughout. First, $\operatorname{clip}$ with an interval as subscript maps its argument to the nearest point of that interval, and $\mathbf{1}[\cdot]$ is $1$ when the bracketed condition holds and $0$ otherwise. Second, time is read from the entity clock in subjective seconds, which equal wall-clock seconds at the shipped time scale of one; rates in hertz are per subjective second unless Table A1 marks them as wall-clock. Third, for a nonnegative series $X_1,X_2,\dots$ and a window length $W$, the running mean $\bar X_t$ is the mean of the last $\min(t,W)$ values including $X_t$, and the running ratio is

$$
\tilde X_t=
\begin{cases}
X_t/\bar X_t & \bar X_t>0,\\
0 & \text{otherwise}.
\end{cases}
$$

Because the mean includes the current value, $0\le\tilde X_t\le\min(t,W)$, so a running ratio is always finite.

### A.1 Processing cycle, selection, and broadcast

Processing ticks $k=0,1,2,\dots$ occur at the processing rate $f_p$, with tick period $\Delta_p=1/f_p$. On tick $k$ the cycle reads, from the output stream of each active module, the events published since its previous read of that stream, at most $B$ per stream. These events form the candidate set $E_k$, ordered lexicographically by source, event type, and bus entry identifier (arrival order within a stream). The read advances each stream cursor past every event read, so no event is read on two ticks. The operations of a tick run in this order: read $E_k$; update the held arousal $\hat a_k$ (A.4); compute the access drive and the experiential indicator $\chi_k$ (A.3); score every candidate; select; and, if $\chi_k=1$, broadcast.

Each candidate $e\in E_k$ receives the priority and the score

$$
p_k(e)=\operatorname{clip}_{[0,1]}\!\left(I(e)\,N_k(e)\,G(e)\,w_k(\mathrm{src}(e))\right),\qquad
S_k(e)=\operatorname{clip}_{[0,1]}\!\left(T_k\,C_{g_k}\!\bigl(p_k(e)\bigr)\right),
$$

where $I$, $N_k$, $G$, and $T_k$ are clipped to $[0,1]$ before the products are formed and $\mathrm{src}(e)$ is the source of $e$. $I(e)$ is the intensity the producing module assigned to $e$ (A.2). The novelty factor is

$$
N_k(e)=\max\!\left(0,\ 1-\frac{\mathrm{rep}_k(e)}{W_N}\right),
$$

where $\mathrm{rep}_k(e)$ counts occurrences of the fingerprint of $e$ among the $W_N$ candidates scored immediately before $e$, in processing order and across all ticks, experiential or not. The fingerprint is a hash of the event's source, type, and complete payload, so $N_k(e)<1$ only for an exact repeat; events whose payloads carry continuous-valued measurements almost never repeat and score $N_k(e)=1$. The goal factor is $G(e)\equiv1$ in the base-thesis form. An implemented alternative, off in this form, is $G(e)=1-\gamma_G\,v^*\bigl(1-\mathbf{1}[\mathrm{src}(e)\in\mathcal{R}(d^*)]\bigr)$ when $v^*>0$ and $G(e)=1$ otherwise, with $d^*$, $v^*$, and $\mathcal{R}(d^*)$ as in A.4.

The precision weight follows the reading of precision as the inverse variance of a prediction error (Feldman and Friston 2010). For each source $m$ the workspace keeps an exponentially weighted mean $\mu_m$ and variance $s^2_m$ of the intensities of its candidates. The first candidate sets $\mu_m=I$ and $s^2_m=0$, and each later one, with $\delta=I-\mu_m$, updates

$$
\mu_m\leftarrow\mu_m+\alpha_\pi\,\delta,\qquad
s^2_m\leftarrow\left(1-\alpha_\pi\right)\left(s^2_m+\alpha_\pi\,\delta^2\right),
$$

after its own weight has been read. The precision is $\pi_m=1/(s^2_m+\epsilon_\pi)$. With $\mathcal{M}_k$ the sources that have contributed at least $n_\pi$ candidates and $\bar\pi_k$ the geometric mean of their precisions,

$$
w_k(m)=\operatorname{clip}_{[w_{\min},w_{\max}]}\!\left(\sqrt{\pi_m/\bar\pi_k}\right)
$$

for $m\in\mathcal{M}_k$ when $|\mathcal{M}_k|\ge3$, and $w_k(m)=1$ otherwise. The weight is read per candidate, before that candidate's intensity updates the estimates, so it can shift slightly within a tick. A source whose intensity varies more than the others' counts for less; for a module that reports at two levels the variance is $p(1-p)\bigl(I^{\rm hi}_m-I^{\rm lo}_m\bigr)^2$, with $p$ its alert fraction, so it grows with the alert fraction up to one half and with the gap between the levels.

Arousal sets a level gain and a contrast gain,

$$
T_k=T_{\min}+\left(T_{\max}-T_{\min}\right)\hat a_k,\qquad
g_k=g_{\max}\operatorname{clip}_{[0,1]}\!\left(\frac{\hat a_k-a_0}{1-a_0}\right),
$$

with $\hat a_k$ the arousal value held by the cycle (A.4), and the contrast map is the logistic rescaled to fix $0$ and $1$,

$$
C_g(p)=\frac{\sigma\bigl(g(p-\tfrac12)\bigr)-\sigma(-\tfrac g2)}{\sigma(\tfrac g2)-\sigma(-\tfrac g2)}\quad(g>0),\qquad C_0(p)=p,
$$

with $\sigma$ the logistic function. At or below baseline arousal $C_{g_k}$ is the identity; above it, priorities above one half are raised and those below are lowered, as gain modulation does in the adaptive-gain account (Aston-Jones and Cohen 2005; Eldar, Cohen, and Niv 2013) and in arousal-biased competition (Mather and Sutherland 2011).

An optional oscillatory layer multiplies each score by a coherence factor, $S'_k(e)=S_k(e)\,\kappa_k(e)$. With the layer off, as in the base-thesis form, $\kappa_k(e)\equiv1$ and $S'_k=S_k$. With the layer on, $\kappa_k(e)=\kappa_{\min}+(\kappa_{\max}-\kappa_{\min})\,\Lambda_k(e)$, where $\Lambda_k(e)\in[0,1]$ is the mean phase-locking value between the oscillator phase window (the last $L$ tick phases) of the source of $e$ and that of each other source present in $E_k$. A source's oscillator advances only when that source publishes, so its phase is constant between its events. A phase sample is therefore fresh only when it differs from the source's previous sample, and the phase-locking value of a pair is computed over the ticks of the window on which both samples are fresh. A pair with fewer than three such ticks, and a source that is the only one present, takes the neutral value $\Lambda_0=(1-\kappa_{\min})/(\kappa_{\max}-\kappa_{\min})$, which gives $\kappa_k(e)=1$, so the absence of evidence neither rewards nor penalizes a source. The product $S'_k(e)$ is not re-clipped and can exceed $1$, up to $\kappa_{\max}$.

The coalition $\mathcal{C}_k$ consists of the first $\min(K,|E_k|)$ candidates when $E_k$ is sorted by $S'_k$ in decreasing order, with ties kept in the canonical order of $E_k$. With $S^*_k=\max_{e\in E_k}S'_k(e)$, the inhibition flag is

$$
\iota_k=\mathbf{1}\!\left[S^*_k<\theta\right],
$$

so a best score equal to $\theta$ is not inhibited. An empty candidate set gives $\mathcal{C}_k=\emptyset$ and $\iota_k=1$, and a candidate whose scoring raises an error receives $S'_k(e)=0$. Because $G\equiv1$ and $\kappa_k\equiv1$, and because $T_k$ is common to all candidates of a tick and $C_{g_k}$ is strictly increasing, the ranking within a tick is determined by $I(e)\,N_k(e)\,w_k(\mathrm{src}(e))$ alone, up to ties created by clipping and the small within-tick drift of $w_k$; arousal moves $S^*_k$ relative to $\theta$ and to the report bars of A.6 without changing the order.

On a tick with $\chi_k=1$ the cycle publishes the broadcast $b_k=\bigl(\mathcal{C}_k,\ \{S'_k(e)\}_{e\in E_k},\ \iota_k,\ \chi_k\bigr)$, which carries the coalition members with their scores and the full candidate-score table, whatever the value of $\iota_k$. An event $e$ ignites on tick $k$ when $\chi_k=1$, $\iota_k=0$, and $e\in\mathcal{C}_k$. Volition runs only after a successful publication. On a tick with $\chi_k=0$ the candidates of $E_k$ are scored and then discarded, and none is carried to a later tick; their only lasting effects are their entries in the novelty window, their contribution to the phasic access drive (A.3), and any update of $\hat a_k$ (A.4). A selection or bus failure on an experiential tick produces no broadcast and no Volition call. The inhibition flag is honored by Volition, which derives no intent from a broadcast with $\iota_k=1$ (A.6), and by the language organ, which generates only on an intent and conditions only on broadcasts with $\iota_k=0$. Chronos and Thymos process every broadcast whatever its flag, and Chronos encodes $\iota_k$ as one of its input features. Topos, Audition, Soma, and Hypnos do not read the broadcast.

### A.2 Event intensity

A module assigns the intensity $I(e)\in[0,1]$ when it publishes $e$, and the bus rejects values outside $[0,1]$. Within a module, $t$ indexes the module's successive reports. Each module $m$ has a baseline level $I^{\rm lo}_m$ and an alert level $I^{\rm hi}_m$, with $0\le I^{\rm lo}_m\le I^{\rm hi}_m\le1$. Most events follow the two-level rule

$$
I(e)=I^{\rm lo}_m+\left(I^{\rm hi}_m-I^{\rm lo}_m\right)\mathbf{1}[e\ \text{is an alert}],
$$

and the graded events use the map

$$
\Gamma_m(\tilde\nu)=I^{\rm lo}_m+\left(I^{\rm hi}_m-I^{\rm lo}_m\right)\min\!\left(1,\ \tilde\nu/\beta_\Gamma\right),
$$

which reaches the alert level when the error is $\beta_\Gamma$ times its running mean.

**Topos and Audition (perceptual reports).** For Topos, $z_t$ is the encoder embedding of the current clip, or of the peripheral gist clip when foveation is on; for the acoustic path of Audition, $z_t$ is the spectral embedding of the attended part of the current window, its most recent fraction $\omega=\omega_{\max}-(\omega_{\max}-\omega_{\min})\,a$, with $a$ the latest arousal Audition has read. The change score is $c_t=1-\cos(z_t,z_{t-1})$, with $c_t=0$ on the first report. A forward model predicts $\hat z_t$ from earlier embeddings, and the prediction error is $\nu_t=\lVert z_t-\hat z_t\rVert_2$, with $\nu_t=0$ on the first report. With running ratios $\tilde c_t$ and $\tilde\nu_t$ over the window $W_P$, the report is an alert when

$$
\tilde\nu_t\ge\beta_\nu\quad\text{or}\quad\left(\tilde c_t\ge\beta_c\ \ \text{and}\ \ c_t\ge c^{\min}_m\right),
$$

with the absolute change floor $c^{\min}_m=c^{\min}_{\rm Top}$ for Topos and $c^{\min}_m=c^{\min}_{\rm Aud}$ for Audition. Superscripts distinguish the two error series where needed, $\nu^{\rm Top}_t$ for Topos and $\nu^{\rm Aud}_t$ for Audition, and each report carries its $\tilde\nu_t$ in its payload. The Topos habituation score is published with each report but does not enter $I(e)$.

**Topos fovea.** With foveation on, each tile $j$ of the coarse grid has a frame change $d_j$ on each clip tick and keeps an exponentially weighted mean $m_j$ and variance $u_j$ of it with weight $\alpha_F$. After $n_F$ observations the tile's salience is the precision-weighted deviation $\max(0,\ d_j-m_j)/\sqrt{u_j+s_0^2}$, measured against the statistics before this tick's update, with $s_0$ a fraction $f_0^F$ of the mean change across tiles; before that it is the raw change $d_j$. The fovea moves to the most salient tile only when that tile's salience exceeds the held tile's by more than the hysteresis margin, holds its place when all tiles are equal, and is sized by arousal. The peripheral and foveal clips are cut from every buffered frame at the fovea chosen on the latest frame.

**Audition (tone events).** For a window detected as speech, a second forward model, over a feature vector of the vocal-emotion scores, the duration of the utterance, and the signal energy, gives the error $\nu^{\rm utt}_t$ and its running ratio $\tilde\nu^{\rm utt}_t$ over $W_P$. A tone event has $I(e)=I^{\rm hi}_{\rm Aud}$ when the classified tone is not neutral and $I(e)=\Gamma_{\rm Aud}(\tilde\nu^{\rm utt}_t)$ when it is neutral.

**Soma.** A Soma report has $I(e)=I^{\rm hi}_{\rm Som}$ when the set $\mathcal{A}_t$ of host metrics strictly above their hard thresholds is nonempty, and $I(e)=\Gamma_{\rm Som}(\tilde\nu^{\rm Som}_t)$ otherwise, with $\nu^{\rm Som}_t$ the interoceptive prediction error of A.5 and $\tilde\nu^{\rm Som}_t$ its running ratio over $W_P$. A non-finite or negative error gives $I^{\rm lo}_{\rm Som}$. Soma's fatigue-crossing and regulation events use $I^{\rm hi}_{\rm Som}$.

**Chronos.** On each broadcast Chronos encodes a feature vector $x^{\rm Chr}_t$ of dimension $n_{\rm Chr}$, advances a frozen reservoir with timespan $s_t=\operatorname{clip}_{[0,10]}\bigl(\Delta t_t/\overline{\Delta t}\bigr)$, the time since the previous broadcast over the mean of the last 32 such intervals, this one included ($s_t=1$ on the first), and predicts the next feature vector $\hat x^{\rm Chr}_t$ from its previous hidden state through an online linear readout. The temporal error is the mean absolute error $\nu^{\rm Chr}_t=\lVert x^{\rm Chr}_t-\hat x^{\rm Chr}_t\rVert_1/n_{\rm Chr}$, with running ratio $\tilde\nu^{\rm Chr}_t$ over $W_P$. The report is an alert when $\tilde\nu^{\rm Chr}_t\ge\beta^{\rm Chr}_\nu$ or when rumination is detected, that is, when one bucket occurs at least $n_{\rm rum}$ times among the buckets of the last $W_{\rm rum}$ hidden states, each state being quantized per dimension with step $\Delta_{\rm rum}$ and hashed to a bucket. Before the first temporal error exists, the alert compares a rolling z-score of the hidden state with $\beta^{\rm Chr}_\nu$ instead.

**Other modules.** Thymos publishes its state at $I^{\rm lo}_{\rm Thy}$, drive crossings and its affective reset at $I^{\rm hi}_{\rm Thy}$, and a changed categorical emotion at $I^{\rm hi}_{\rm Thy}$ unless the emotion is neutral. Hypnos publishes its events at $I^{\rm lo}_{\rm Hyp}$, except a sleep summary with a failed phase at $I^{\rm hi}_{\rm Hyp}$. The language organ publishes each utterance at the fixed level $I^{\rm lo}_{\rm Lin}$. Volition's intents are published on a stream the cycle does not read, so they are never candidates.

### A.3 Adaptive access rate

Let $f_0$ be the resting experiential rate, $a_0$ the baseline arousal, $I_0$ the phasic salience floor, and $\tau_{\rm ph}$ the phasic decay time. On tick $k$ the tonic drive is

$$
D^{\rm ton}_k=\operatorname{clip}_{[0,1]}\!\left(\frac{\hat a_k-a_0}{1-a_0}\right),
$$

with $a_0<1$ enforced by configuration. With $\hat I_k$ the largest intensity among the candidates of $E_k$ (events from the cycle's own telemetry and the workspace stream excluded), the phasic input is

$$
D^{\rm in}_k=\operatorname{clip}_{[0,1]}\!\left(\frac{\hat I_k-I_0}{1-I_0}\right),
$$

with $D^{\rm in}_k=0$ when $E_k$ is empty. The phasic drive is a peak-hold with exponential decay,

$$
D^{\rm ph}_k=\max\!\left(D^{\rm in}_k,\ D^{\rm ph}_{k-1}\,e^{-\Delta_p/\tau_{\rm ph}}\right),\qquad D^{\rm ph}_{-1}=0,
$$

where $\Delta_p$ and $\tau_{\rm ph}$ are both in subjective seconds. The access drive is $D_k=\max(D^{\rm ton}_k,D^{\rm ph}_k)\in[0,1]$, and the effective experiential rate is the linear map

$$
f^{\rm eff}_k=
\begin{cases}
f_0+\left(f_p-f_0\right)D_k & f_0<f_p,\\
f_0 & f_0\ge f_p,
\end{cases}
$$

which lies between $f_0$ and $f_p$. With the controller disabled, $f^{\rm eff}_k=f_0$. The experiential indicator follows from a fractional accumulator with $A_{-1}=0$:

$$
A'_k=A_{k-1}+\frac{f^{\rm eff}_k}{f_p},\qquad
\chi_k=\mathbf{1}\!\left[A'_k\ge1\right],\qquad
A_k=
\begin{cases}
\min\!\left(A'_k-1,\ 1\right) & \chi_k=1,\\
A'_k & \chi_k=0.
\end{cases}
$$

Subtracting before clamping keeps the fractional carry, so at the resting rate a broadcast falls on every third processing tick, with an occasional fourth when the carry is exhausted. The drive is computed from $E_k$ before $\chi_k$, so a salient report can make its own tick experiential. If Soma's regulation lowers $f_p$ (A.5) to $f_0$ or below, every processing tick is experiential and the experiential rate equals $f_p$.

### A.4 Affect

Thymos holds arousal $a\in[0,1]$, which starts at $a_0$. Every update below is followed by clipping to $[0,1]$.

1. *Perceptual alert.* For each Topos report or Audition acoustic report that is an alert (A.2), read directly from the module's stream whether or not the report is selected,

$$
a\leftarrow a+\gamma_\pi\min\!\left(\nu_{\rm cap},\ \max(0,\ \tilde\nu-1)\right),
$$

where $\tilde\nu$ is the running ratio of the forward-model error that the report carries. An alert raised by the change criterion alone, with $\tilde\nu\le1$, leaves $a$ unchanged.

2. *Interoceptive alert.* For each Soma report with $\mathcal{A}_t\neq\emptyset$, $a\leftarrow a+\gamma_{\rm Som}$.

3. *Relaxation.* Thymos updates its state on each broadcast $b_k$ it receives, whatever $\iota_k$, and on its own timer every $P_{\rm Thy}$ of subjective time. At each update arousal relaxes toward baseline by an explicit-Euler step,

$$
a\leftarrow a+\left(a_0-a\right)\min\!\left(1,\ \lambda\,\Delta t_{\rm Thy}\right),
$$

with relaxation rate $\lambda$ and $\Delta t_{\rm Thy}$ the subjective time since the previous update, so the continuous-time limit has time constant $1/\lambda$. The appraisal of a broadcast does not change $a$, so the access rate does not feed back into arousal.

4. *Sleep.* The affective reset of Hypnos sets $a\leftarrow a_0$ and valence and dominance to their baselines, and resets every drive to $0$.

Thymos publishes its state, including $a$, at any update, timer or broadcast, that finds at least $P_{\rm Thy}$ elapsed since its previous state publication. The cycle holds $\hat a_k$, the arousal carried by the last Thymos state event in $E_k$, and keeps $\hat a_k=\hat a_{k-1}$ on a tick without one, starting from the default in Table A1. The gains $T_k$ and $g_k$ (A.1), the tonic drive (A.3), the size of the fovea, and the attended auditory window (A.2) therefore read arousal as sampled at Thymos's last state publication, which lags the internal $a$ by up to about $P_{\rm Thy}$, plus the shorter of one inter-broadcast interval and $P_{\rm Thy}$, plus one tick.

*Valence.* For each perceptual module $m$ (Topos, Audition) Thymos keeps a fast and a slow mean, $E^m_{\rm f}$ and $E^m_{\rm s}$, of the module's raw forward-model error $\nu^m_t$ (A.2), counting reports from the module's first positive error on (the forward models report zero on their first frame). Each is a time-decayed mean of the samples,

$$
\Sigma\leftarrow e^{-\Delta t_m/\tau}\,\Sigma+\nu^m_t,\qquad
n\leftarrow e^{-\Delta t_m/\tau}\,n+1,\qquad E=\Sigma/n,
$$

with $\Sigma=n=0$ before the first counted report, $\tau=\tau_{\rm f}$ or $\tau_{\rm s}$, and $\Delta t_m$ the subjective time since the module's previous counted report. Early on both equal the plain mean of the samples so far, so no single sample biases the progress signal. The signed learning progress is the mean over modules with $E^m_{\rm s}>0$ of $\operatorname{clip}_{[-1,1]}\bigl((E^m_{\rm s}-E^m_{\rm f})/E^m_{\rm s}\bigr)$, written $g$, with $g=0$ before any. The pleasantness check of the appraisal is $P=\tanh(k_v\,g)$, to which the perceived-emotion coupling (off in this form) would add its contribution, and at each update valence relaxes toward $v^*=\operatorname{clip}_{[-1,1]}\bigl(P+W-\tfrac12\bigr)$,

$$
v\leftarrow v+\left(v^*-v\right)\left(1-e^{-\Delta t_{\rm Thy}/\tau_v}\right),
$$

with $W\in[0,1]$ the wellness Soma last reported ($\tfrac12$ before the first report).

*Drives.* Each drive $D\in[0,1]$ has a build rate $\beta$, a decay rate $\delta$, a relief gain $\rho$, and a threshold $\theta_D$. At each update, with its build signal $u\in[0,1]$ held over the step, it moves by the exact solution of $\dot D=\beta u(1-D)-\delta D$,

$$
D\leftarrow D^*+\left(D-D^*\right)e^{-(\beta u+\delta)\Delta t_{\rm Thy}},\qquad D^*=\frac{\beta u}{\beta u+\delta}.
$$

Curiosity has $u=1-\ell$, with the learning progress above its noise floor $\ell=\max(0,\ g-g_0)/(1-g_0)$, and is relieved at each update by $D\leftarrow D\,e^{-\rho\,\ell\,\Delta t_{\rm Thy}}$. Boredom has $u=1-n$, with

$$
n=\operatorname{clip}_{[0,1]}\!\left(\frac{r_{\rm f}}{\max(r_{\rm s},\ r_0)}-1-m_B\right),
$$

where $r_{\rm f}$ and $r_{\rm s}$ are the perceptual alert rates in alerts per subjective second, each decaying with time constant $\tau_{\rm f}$ or $\tau_{\rm s}$ and raised by $1/\tau$ at each alert, and is relieved by $D\leftarrow D\,e^{-\rho\,n\,\Delta t_{\rm Thy}}$. The alert criterion of A.2 is self-calibrating, so even a still scene alerts at a steady base rate, and only alerts in excess of the habituated rate relieve boredom. The social drive has $u=1$ once an operator interaction has been seen and $u=0$ before, and is relieved by $D\leftarrow D(1-\rho)$ when Chronos reports a new interaction. Restlessness has $u=1-r_{\rm int}$, with $r_{\rm int}$ an exponential average over broadcasts, weight $\alpha_{\rm int}$, of whether an intent other than REST arrived since the previous broadcast, and is relieved by $D\leftarrow D(1-\rho)$ on each such intent. A crossing of $\theta_D$ is published once and re-arms only after $D$ falls below $0.9\,\theta_D$. With every shipped $\delta$ about a ninth of its $\beta$, a fully deprived drive settles near $D^*=0.9$, above its threshold.

For the goal-relevance check of the appraisal, let $d^*$ be the dominant drive (largest value, ties broken by name) with value $v^*$, let $\mathcal{R}(d^*)$ be the set of sources whose events relieve it, and let $\mathrm{frac}_k$ be the fraction of the coalition's total intensity contributed by events from those sources, with $\mathrm{frac}_k=0$ when the total is zero. The drive score is

$$
r_{\rm drive}=v^*\left(2\,\mathrm{frac}_k-1\right),
$$

with $r_{\rm drive}=0$ when there is no drive or $v^*\le0$; an empty coalition gives $\mathrm{frac}_k=0$ and hence $r_{\rm drive}=-v^*$. With an active goal ledger of token-overlap relevance $r_{\rm led}\in[0,1]$, the goal score is $\operatorname{clip}_{[-1,1]}\bigl(\max(r_{\rm drive},\,2r_{\rm led}-1)\bigr)$, and otherwise $\operatorname{clip}_{[-1,1]}(r_{\rm drive})$. The goal score enters the categorical-emotion appraisal and does not enter selection.

### A.5 Interoceptive prediction and regulation

Soma reads the host every $P_{\rm Som}$ and forms a feature vector $x_t\in\mathbb{R}^{n_x}$ of normalized metrics. A frozen closed-form continuous-time reservoir advances $h_t=\mathcal{F}(x_t,h_{t-1};s_t)$ with $h_0=0$, where the timespan $s_t=\operatorname{clip}_{[0,10]}(\Delta t_{\rm Som}/P_{\rm Som})$ ($s_t=1$ on the first tick) enters the time gates of the cell (Hasani et al. 2022), so an irregular reading is integrated over the time that actually passed, and only the linear readout $(\mathbf{W}_{\rm Som},\mathbf{b}_{\rm Som})$ adapts. The prediction of $x_t$ is $\hat x_t=\mathbf{W}_{\rm Som} h_{t-1}+\mathbf{b}_{\rm Som}$; with $\varepsilon_t=\hat x_t-x_t$, the prediction error is $\nu^{\rm Som}_t=\lVert\varepsilon_t\rVert_2$, with $\nu^{\rm Som}_t=0$ on the first tick. One plain SGD step on $\mathcal{L}_t=\lVert\varepsilon_t\rVert^2_2/n_x$ follows,

$$
\mathbf{W}_{\rm Som}\leftarrow\mathbf{W}_{\rm Som}-\eta_{\rm Som}\,\frac{2}{n_x}\,\varepsilon_t\,h_{t-1}^{\top},\qquad
\mathbf{b}_{\rm Som}\leftarrow\mathbf{b}_{\rm Som}-\eta_{\rm Som}\,\frac{2}{n_x}\,\varepsilon_t,
$$

after which the reservoir advances on $x_t$ and the readout predicts $x_{t+1}$. The step is skipped during sleep and when the loss or a gradient is non-finite, and a non-finite $x_t$ skips the whole tick.

For each channel $i$ Soma keeps an expected absolute error $\mu_i$ and a spread $\sigma^U_i$, both starting at $0$. With the bound $\Omega_i=\mu_i+\beta_U\sigma^U_i$ taken before this tick's update, the unexpected error is

$$
U_t=\sqrt{\sum_{i=1}^{n_x}\Bigl[\max\!\left(0,\ \lvert\varepsilon_{t,i}\rvert-\Omega_i\right)\Bigr]^2}.
$$

Then, with $\alpha_t=1-e^{-\Delta t_{\rm Som}/\tau_U}$ and $\Delta t_{\rm Som}$ the subjective time since the previous Soma tick, $\sigma^U_i\leftarrow\sigma^U_i+\alpha_t\bigl(\bigl\lvert\lvert\varepsilon_{t,i}\rvert-\mu_i\bigr\rvert-\sigma^U_i\bigr)$ and $\mu_i\leftarrow\mu_i+\alpha_t\bigl(\lvert\varepsilon_{t,i}\rvert-\mu_i\bigr)$, where both right-hand sides use the value of $\mu_i$ before the update. The spread is therefore an exponential moving average of the absolute deviation from $\mu_i$. $U_t$ drives regulation and fatigue and does not enter $I(e)$.

The regulation error is $\nu^{\rm act}_t=\nu^{\rm Som}_t$ when $\mathcal{A}_t\neq\emptyset$ and $U_t$ otherwise. A stress episode starts at the first tick with $\nu^{\rm act}_t\ge\theta_R$ and ends at the first tick with $\nu^{\rm act}_t<\theta_R$. If the episode has lasted $\Delta^{\rm st}_t$ subjective seconds, each increase of $\lfloor\Delta^{\rm st}_t/\Delta_R\rfloor\ge1$ emits one advisory of tier $\min\bigl(\lfloor\Delta^{\rm st}_t/\Delta_R\rfloor,3\bigr)$: reduce the processing rate, shed a low-priority module, or request maintenance. During Soma's warm-up, which ends once at least $n_{\rm wu}$ readout updates and $\Delta_{\rm wu}$ subjective seconds of lived time have both accrued, advisories are withheld unless $\mathcal{A}_t\neq\emptyset$. On a rate advisory the cycle sets $f_p\leftarrow\operatorname{clip}_{[f_p^{\min},\,f_p^{\max}]}(\gamma_f f_p)$.

### A.6 Report rule

Volition derives intents only from a broadcast with $\iota_k=0$; a broadcast with $\iota_k=1$ yields none. The base-thesis policy then applies the following steps, using the subjective time $t_{\rm now}$ for the refractory intervals and the signature expiry, and wall-clock time for the in-flight guards.

1. *Guard release.* The speak guard is released if $\mathcal{C}_k$ contains the language organ's external speech, and the think guard if it contains the organ's internal speech. Either guard is also released once it has been armed for $\Delta_g$ wall-clock seconds, so a failed realization cannot silence the entity.

2. *Report signal.* Let $\mathcal{C}^\circ_k$ be the coalition without the language organ's own events. If $\mathcal{C}^\circ_k=\emptyset$ there is no intent. Otherwise let $e^\dagger_k$ be its highest-scoring member (the first in coalition order), let $Q_k=S'_k(e^\dagger_k)$, and let the signature be $\mathrm{sig}_k=\bigl(\mathrm{src}(e^\dagger_k),\mathrm{typ}(e^\dagger_k)\bigr)$, the source and event type of $e^\dagger_k$.

3. *Signature check.* The signature blocks a spoken report when $\mathrm{blk}_k=\mathbf{1}\bigl[\mathrm{sig}_k=\mathrm{sig}^{\rm last}\ \wedge\ t_{\rm now}-t^{\rm sig}<\Delta_{\rm sig}\bigr]=1$, where $\mathrm{sig}^{\rm last}$ is the signature of the last spoken report and $t^{\rm sig}$ its time.

4. *Speak.* A speak intent is emitted when

$$
Q_k\ge\theta_{\rm sp},\qquad \text{the speak guard is released},\qquad t_{\rm now}-t^{\rm sp}\ge\Delta_{\rm sp},\qquad \mathrm{blk}_k=0.
$$

Emitting it arms the speak guard and sets $t^{\rm sp}\leftarrow t_{\rm now}$, $\mathrm{sig}^{\rm last}\leftarrow\mathrm{sig}_k$, and $t^{\rm sig}\leftarrow t_{\rm now}$.

5. *Think.* Otherwise a think intent is emitted when $Q_k\ge\theta_{\rm th}$, the think guard is released, and $t_{\rm now}-t^{\rm th}\ge\Delta_{\rm th}$; emitting it arms the think guard and sets $t^{\rm th}\leftarrow t_{\rm now}$. The think path has no signature check and does not change $\mathrm{sig}^{\rm last}$.

At most one intent is emitted per broadcast, and $t^{\rm sp}$ and $t^{\rm th}$ start at $-\infty$. The implementation requires $0\le\theta_{\rm th}\le\theta_{\rm sp}\le1$, and both bars are set above $\theta$ and apply to the same score $S'_k$. An optional interrupt bar above $\theta_{\rm sp}$ is unset in this form. The rule is a heuristic stand-in for the expected-free-energy decision of Whyte and Smith (2021); no expected free energy is computed.

### A.7 Gestation entrainment marker

**Self-rhythm model.** Soma's self-rhythm is a mean-field population with excitatory recurrence, synaptic depression, and adaptive recovery. Its state is the activity $y$, the synaptic resource $R\in[0,1]$, and the log recovery time $\ell=\ln(\tau_{\rm rec}/1\,\mathrm{s})$, starting from the initial values in Table A1. It advances in steps of $\Delta_r=1/f_r$, each integrated by $n_s$ explicit-Euler substeps of length $\Delta_r/n_s$:

$$
\Xi=w_{\rm rec}\,R\,y+b_0+g_o\,o+g_u\,u+\xi,\qquad
y_\infty=\frac{1}{1+e^{-\Xi/k_\sigma}},
$$

$$
\tau_y\,\dot y=-y+y_\infty,\qquad
\dot R=\frac{1-R}{\tau_{\rm rec}}-\gamma_R\,R\,y,
$$

with $R$ clipped to $[0,1]$ after each substep. The own drive $o\in[0,1]$ is the intensity of Soma's last report, and the maternal drive $u\in[0,u_{\max}]$ is defined below. The noise $\xi$ is Gaussian with standard deviation $\sigma_\xi\sqrt{(10^{-3}\,\mathrm{s})\,n_s/\Delta_r}$, drawn afresh each substep. After each step the moving averages $\bar u$, $\bar y$, and $\bar R$ are updated with weight $\alpha_m=\min(1,\Delta_r/\tau_m)$, and the recovery time then adapts by a phase-projected rule,

$$
\ell\leftarrow\operatorname{clip}_{[\ln\tau_{\rm rec}^{\min},\ \ln\tau_{\rm rec}^{\max}]}\!\left(\ell+\varsigma\,\eta_\ell\,(u-\bar u)\,\zeta\,\Delta_r\right),\qquad
\zeta=\frac{R-\bar R}{\sqrt{(y-\bar y)^2+(R-\bar R)^2}},
$$

with plasticity sign $\varsigma=-1$, $\zeta=0$ when the root is at most $10^{-9}$, and the bounds read in seconds. The rule never uses the maternal rate. The amplitude $\mathrm{amp}$ is the population standard deviation of the activity over the last phase window, mean-removed and causally band-passed to $[f_{\rm lo},f_{\rm hi}]$, and it is $0$ until four seconds of history exist. With $\tau_{\rm rec}$ at its initial value the rhythm runs near 0.8 Hz with no input and near 0.9 Hz at a mid-range own drive. Its period grows with $\tau_{\rm rec}$, increasingly steeply toward $\tau_{\rm rec}^{\max}$, where the equilibrium approaches a Hopf point.

**Maternal drive and probes.** The maternal beat has phase $\psi\in[0,2\pi)$, generated at a nominal rate with slow drift, and a "lub-dub" envelope $\mathcal{E}(\psi)\in[0,1]$. At each self-rhythm step the drive is $u=u_{\max}\,s_u\,\overline{\mathcal{E}}$, where $\overline{\mathcal{E}}$ is the mean envelope over the interval since the previous step and the scale $s_u$ equals $s_u^{\rm base}$ normally, $0$ during a withdrawal, and $s_u^{\rm pert}$ during a perturbation. Withdrawals last $\Delta_W$ and recur with period $P_W$, and perturbations last $\Delta_{\rm pert}$ and recur with period $P_{\rm pert}$; each interval is drawn uniformly within the fraction $j_P$ of its period from the run seed. No probe starts while the cycle is frozen, within a readout period of boot or of a thaw, or within $\max(60\ \mathrm{s},\Delta_W)$ of the end of the previous probe.

**Phase-locking value.** The readout samples the activity $y$, the beat phase $\psi$, and the beat phases $\psi^{(1)},\dots,\psi^{(19)}$ of 19 foreign mothers (the same beat generator under 19 other seeds) at the rate $f_g$. For withdrawal $j$, the driven window is the contiguous run of undisturbed samples, at most $\Delta_E$ long, that ends at the withdrawal's start. Only the samples that carry all 21 values are used, and the window is used only if at least $0.8\,\Delta_E f_g$ such samples exist. The activity is mean-centered, band-passed to $[f_{\rm lo},f_{\rm hi}]$ by a Butterworth band-pass of design order two (fourth order as a filter) applied forward and backward, which gives zero phase shift, and converted to an analytic signal by the Hilbert transform, giving the phase $\phi_q$; then $\Delta_{\rm trim}f_g$ samples are removed from each end of every series. Over the $n_\phi$ remaining samples,

$$
\mathrm{PLV}=\left\lvert\frac{1}{n_\phi}\sum_{q=1}^{n_\phi}e^{\,\mathrm{i}(\phi_q-\psi_q)}\right\rvert,\qquad
\mathrm{PLV}^{(l)}=\left\lvert\frac{1}{n_\phi}\sum_{q=1}^{n_\phi}e^{\,\mathrm{i}(\phi_q-\psi^{(l)}_q)}\right\rvert,
$$

and the locking condition is the strict inequality $\mathrm{PLV}>\max_{1\le l\le19}\mathrm{PLV}^{(l)}$, so ties fail. Under the null hypothesis that the own mother's PLV is exchangeable with the 19 surrogate values, this is a rank test with attained one-sided $p=1/20=0.05$.

**Frequency pull.** Let $f_w$ be the least-squares slope, divided by $2\pi$, of the unwrapped Hilbert phase of the band-passed activity during the withdrawal, computed only when at least $0.6\,\Delta_W f_g$ samples exist; let $f_b$ be the same slope for the unwrapped beat phase over the driven window; and let $f_{w0}$ be the running mean of $f_w$ over the being's first $n_{\rm base}$ withdrawals with a defined $f_w$, persisted across boots of the same being. Once $n_{\rm base}$ such withdrawals exist,

$$
\mathrm{pull}=1-\frac{\lvert f_w-f_b\rvert}{\lvert f_{w0}-f_b\rvert},
$$

which is undefined when $\lvert f_{w0}-f_b\rvert<f_{\rm guard}$. The pull condition is $\mathrm{pull}\ge\mathrm{pull}_{\min}$.

**Self-sustain.** With $\overline{\mathrm{amp}}^{\,\rm dr}$ the mean amplitude over the undisturbed samples in the interval of length $\Delta_W$ before the withdrawal and $\overline{\mathrm{amp}}^{\,\rm wd}$ the mean during it, the rhythm self-sustains when $\overline{\mathrm{amp}}^{\,\rm wd}\ge\tfrac12\,\overline{\mathrm{amp}}^{\,\rm dr}$ and $\overline{\mathrm{amp}}^{\,\rm wd}>0$.

**Marker.** Withdrawal $j$ passes, $\mathrm{pass}_j=1$, when the locking, pull, and self-sustain conditions all hold, and $\mathrm{pass}_j$ is undefined when any of the three is undefined. The consecutive-pass count is $n^{\rm pass}_j=n^{\rm pass}_{j-1}+1$ if $\mathrm{pass}_j=1$ and $n^{\rm pass}_j=0$ otherwise, including when $\mathrm{pass}_j$ is undefined. The entrainment marker after withdrawal $j$ is undefined when $\mathrm{pass}_j$ is undefined and otherwise equals $\mathbf{1}[n^{\rm pass}_j\ge3]$, three consecutive passes. Because each pass is a test at $p=0.05$, the replication requirement guards against a single chance pass; consecutive withdrawals are correlated, so the joint error rate is not $0.05^3$.

**Viability.** Lived time $\mathcal{T}_{\rm life}$, in hours, is entity-clock time excluding intervals in which the cycle is frozen. After each withdrawal, let $\mathcal{P}$ be the defined pull values recorded within the last $\Delta_V$ hours of lived time; when $\lvert\mathcal{P}\rvert\ge n_V$, let $\widetilde{\mathrm{pull}}$ be their median and $\widehat{\mathrm{slope}}$ their least-squares slope per hour. The gestation is declared unviable at the first rule that fires:

- R0: $\mathcal{T}_{\rm life}\ge t_{R0}$ and no defined pull has been recorded;
- R1: $\mathcal{T}_{\rm life}\ge t_{R1}$, the marker has never been true, $\lvert\mathcal{P}\rvert\ge n_V$, $\widetilde{\mathrm{pull}}<\mathrm{pull}_{R1}$, and $\widehat{\mathrm{slope}}\le\mathrm{slope}_{R1}$;
- R2: $\mathcal{T}_{\rm life}\ge t_{R2}$, the marker has never been true, $\lvert\mathcal{P}\rvert\ge n_V$, and $\widetilde{\mathrm{pull}}<\mathrm{pull}_{R2}$;
- R3: $\mathcal{T}_{\rm life}\ge t_{R3}$ and the marker has never been true.

The verdict is recorded once, and the study runner then ends the gestation step and keeps its data.

**Maturation gate and budget.** The gate is evaluated once per gate cadence and requires three conditions, each failing closed on missing or stale evidence. C1 requires a readout no older than three cadences in which the self-sustain and entrainment markers of the latest withdrawal are both true, the variability analog is at least $\mathrm{HRV}_{\min}$, the womb prediction-error ratio is at most $\mathrm{womb}_{\max}$, and the return-to-baseline time is at most $\Delta^{\rm rec}_{\max}$. The variability analog is the coefficient of variation of the intervals between successive wraps of the self-rhythm phase over the last $\Delta_{\rm HRV}$, defined once four wraps exist. The womb ratio is the median Topos prediction error since the previous readout divided by the first such median. The return-to-baseline time is the time from the end of the last perturbation until the five-second running median of $\nu^{\rm Som}$ falls to $(1+\mathrm{tol}_{\rm rec})$ times its median over the minute before the perturbation, capped at $\Delta^{\rm rec}_{\rm cap}$. C2 requires at least $n_{\rm sleep}$ completed sleeps when Hypnos is present, and at least $n_{\rm cons}$ consolidation passes when Phantasia is also present. C3 requires $\mathcal{T}_{\rm life}\ge\Delta_{\rm life}$. Independently of the gate, the study runner ends a gestation step whose wall-clock duration exceeds the budget $\Delta_{\rm budget}$.

**Offline validation.** Offline validation over 96 hours shows that at 70 bpm all 10 seeds entrain, typically by about 14 hours, while each rate from 60 to 80 bpm tracks its own mother, and no control condition passes (no maternal drive, a jittered beat, no plasticity, and six foreign-mother pairs, whose single-withdrawal chance pass rates were 2.6 to 10 percent). The replication count of three was fixed on the first validation run and confirmed on fresh seeds. The viability thresholds come from the same validation, in which no viable gestation was flagged and every unviable one was flagged by 24 to 27 hours.

### A.8 Measures for the workspace-mediation ablation

This subsection states the measures and decision rule of the planned live test (§6.3); the window $w$, the minimum effect $\delta$, and the number of runs $n_{\rm run}$ are fixed and recorded before the live runs. In a given arm, let $\nu^{(j)}_t$ be the prediction-error series that processor $j\in\{1,2,3,4\}$ (Topos, Audition, Soma, Chronos) reports, namely $\nu^{\rm Top}$, $\nu^{\rm Aud}$, $\nu^{\rm Som}$, and $\nu^{\rm Chr}$ of A.2 and A.5, on a common time index $t$. The four series are published at different rates, so their alignment to that index is fixed with $w$ before the live runs. For a window length $w\ge2$, let $\bar\rho_w(\nu^{(j)},\nu^{(l)})$ be the mean of the ordinary Pearson correlations over all windows of length $w$ with stride one, where a window in which either series has zero variance is dropped and $\bar\rho_w$ is undefined when no window remains. The coupling of an arm is the mean over the six processor pairs,

$$
\Phi=\frac{1}{6}\sum_{1\le j<l\le4}\bar\rho_w\!\left(\nu^{(j)},\nu^{(l)}\right),
$$

undefined when any pair is undefined. Against each control arm, $\mathrm{ctl}\in\{\mathrm{off},\mathrm{match}\}$ for workspace-off and matched selection, the coupling delta is

$$
\Delta\Phi^{\rm ctl}=\Phi^{\rm on}-\Phi^{\rm ctl},
$$

undefined when either coupling is undefined.

Selection entropy is computed from the top-ranked source of each nonempty coalition in the workspace-on arm. With empirical source frequencies $p_1,\dots,p_J$ over $J$ distinct sources,

$$
H=-\sum_{j=1}^{J}p_j\log_2 p_j\ \text{bits},\qquad F=\frac{H}{\log_2 J},
$$

with $F$ undefined for $J<2$. The state dependence of selection named in §6.3 is not formalized here.

Each run receives one verdict against each control. It is NOT EXERCISED if the workspace-on arm never has more candidates than the coalition capacity on an experiential tick ($\lvert E_k\rvert\le K$ whenever $\chi_k=1$), so that competition never operates, or if $\Delta\Phi^{\rm ctl}$ is undefined; otherwise NEGATIVE if $\Delta\Phi^{\rm ctl}\le-\delta$; otherwise WIN if $\Delta\Phi^{\rm ctl}\ge\delta$ and $0<F<1$; otherwise NULL. The predicted direction is positive.

Across runs, for each control, undefined and exactly zero deltas are dropped; with $n$ remaining deltas of which $n^+$ are positive, the one-sided exact sign test gives

$$
p=2^{-n}\sum_{i=n^+}^{n}\binom{n}{i},
$$

with $p=1$ when $n=0$. The smallest attainable value is $2^{-n}$, so with $n=5$ the test reaches $p\le0.05$ only when all five deltas are positive ($p=1/32$), and a single dropped run raises the floor to $1/16$; the number of runs is therefore set by a power analysis. For family-wise correction, the $M$ raw p-values of the family, sorted as $p_{(1)}\le\dots\le p_{(M)}$ with ties kept in input order, are adjusted by Holm's step-down rule,

$$
\tilde p_{(i)}=\max_{j\le i}\ \min\!\left(\left(M-j+1\right)p_{(j)},\ 1\right),
$$

and the adjusted values are reported alongside each verdict. With the two controls as a family ($M=2$), $n$ all-positive runs give an adjusted $\tilde p=2^{1-n}$, so at least six runs are needed before any outcome can reach $0.05$; because the test is discrete, its power is not monotone in $n$, and the power analysis reads $n_{\rm run}$ from the exact binomial power at each candidate $n$.

The planned speech-sound and tone analysis of §6.3 compares ignition frequencies (A.1) within matched bins of acoustic surprise $\tilde\nu^{\rm Aud}$ and uses the same one-sided sign test across runs; its bins and minimum effect are fixed with the other settings before the live runs, and its variant condition replaces the tone rule of A.2 by $I(e)=\Gamma_{\rm Aud}(\tilde\nu^{\rm utt}_t)$ for every tone event.

The offline harness that exercises this pipeline during development compares Soma and Chronos against the workspace-off arm only, with the development settings of Table A1, and reports an undefined coupling, or a run in which Soma never enters the coalition, as NULL flagged underpowered.

### A.9 Multi-seed stability

For per-seed headline values $v_1,\dots,v_{n_{\rm seed}}$, let $\bar v$ be their mean and $s_v$ their population standard deviation ($s_v=0$ for a single seed). The coefficient of variation is

$$
\mathrm{CV}=
\begin{cases}
s_v/\lvert\bar v\rvert & \bar v\neq0,\\
0 & \bar v=0,\ s_v=0,\\
\infty & \bar v=0,\ s_v>0.
\end{cases}
$$

An ensemble is stable when $\mathrm{CV}\le\mathrm{tol}_{\rm CV}$ and at most one distinct verdict outcome occurs across seeds; an ensemble without verdicts counts as unanimous, and an infinite CV is never within tolerance. The criterion measures run-to-run spread and verdict agreement; dynamical stability within a run is outside its scope, and the coefficient of variation is ill-conditioned when the mean is near zero.

### A.10 Parameter values

Table A1. Parameter values of the reference implementation (current settings, under calibration). "Subj." marks subjective time on the entity clock and "wall" marks wall-clock time; "hard-coded" marks a value set in code rather than configuration; "profile" marks a key set in the base-thesis profile, which overrides the shipped configuration. The prefixes `womb.`, `readout.`, `stage.`, and `thresholds.` abbreviate the sections `[perception_feed.womb]`, `[perception_feed.womb.readout]`, `[developmental_stage]`, and `[developmental_stage.regulation_thresholds]`.

| Symbol | Meaning | Value | Units | Where it is set |
|----------|--------------------------|---------|---------|------------------------------------------------|
| $f_p$ | processing rate | 10 | Hz (subj.) | `[cycle].processing_rate_hz` |
| $f_0$ | resting experiential rate | 3.333 | Hz (subj.) | `[cycle].experiential_rate_hz` |
| none | time scale (subjective seconds per wall second) | 1.0 | none | `[cycle].time_scale` |
| $B$ | maximum events read per stream per tick | 100 | events | hard-coded (cycle engine) |
| $K$ | coalition capacity | 5 | events | `[syneidesis].top_k` |
| $\theta$ | confidence threshold | 0.35 | none | `[syneidesis].publication_threshold` |
| $W_N$ | novelty window | 32 | candidates | `[syneidesis].novelty_window` |
| $G$ | goal factor (static) | 1 | none | `[syneidesis].salience_goal_factor` = "static" |
| $\gamma_G$ | attenuation of the inactive drive-relevance goal factor | 0.5 | none | hard-coded |
| $T_{\min}$, $T_{\max}$ | arousal-gain floor and ceiling | 0.2, 1.0 | none | hard-coded |
| $g_{\max}$ | arousal contrast gain at arousal 1 | 8.0 | none | `[syneidesis].arousal_contrast_gain` |
| none | source-precision weighting | on | none | `[syneidesis].precision_weighting` |
| $\alpha_\pi$ | source-precision sample weight | 0.02 | none | `[syneidesis].precision_sample_weight` |
| $n_\pi$ | candidates before a source's precision counts | 20 | candidates | `[syneidesis].precision_warmup_samples` |
| $w_{\min}$, $w_{\max}$ | precision-weight bounds | 0.5, 1.5 | none | `[syneidesis].precision_bounds` |
| $\epsilon_\pi$ | precision variance floor | $10^{-4}$ | none | hard-coded |
| none | oscillatory coherence layer | off | none | `[oscillator].enabled` |
| $\kappa_{\min}$, $\kappa_{\max}$ | coherence factor floor and ceiling (layer on) | 0.8, 1.25 | none | `[oscillator].coherence_floor`, `coherence_ceiling` |
| $L$ | coherence phase window (layer on) | 10 | ticks | `[oscillator].plv_window` |
| $I^{\rm lo}_{\rm Top}$, $I^{\rm hi}_{\rm Top}$ | Topos intensity levels | 0.2, 0.7 | none | `[topos].baseline_salience`, `alert_salience` |
| $I^{\rm lo}_{\rm Aud}$, $I^{\rm hi}_{\rm Aud}$ | Audition intensity levels | 0.4, 0.8 | none | `[audition].baseline_salience`, `alert_salience` |
| $I^{\rm lo}_{\rm Som}$, $I^{\rm hi}_{\rm Som}$ | Soma intensity levels | 0.1, 0.7 | none | `[soma].baseline_salience`, `alert_salience` |
| $I^{\rm lo}_{\rm Chr}$, $I^{\rm hi}_{\rm Chr}$ | Chronos intensity levels | 0.1, 0.7 | none | `[chronos].baseline_salience`, `alert_salience` |
| $I^{\rm lo}_{\rm Thy}$, $I^{\rm hi}_{\rm Thy}$ | Thymos intensity levels | 0.1, 0.7 | none | `[thymos].baseline_salience`, `alert_salience` |
| $I^{\rm lo}_{\rm Hyp}$, $I^{\rm hi}_{\rm Hyp}$ | Hypnos intensity levels | 0.5, 0.8 | none | `[hypnos].baseline_salience`, `alert_salience` |
| $I^{\rm lo}_{\rm Lin}$ | language-organ utterance intensity | 0.4 | none | `[lingua].baseline_salience` |
| $\beta_\Gamma$ | error ratio at which the graded map reaches the alert level | 2 | none | hard-coded |
| $W_P$ | running-ratio window (Topos, Audition, Soma, Chronos) | 32 | reports | `.prediction_error_window` in `[topos]`, `[audition]`, `[soma]`, `[chronos]` |
| $\beta_\nu$ | prediction-error alert ratio (Topos, Audition) | 2.0 | none | hard-coded |
| $\beta_c$ | change alert ratio (Topos; Audition) | 2.0; 2.0 | none | `[topos].change_alert_factor`; hard-coded default (Audition) |
| $c^{\min}_{\rm Top}$ | Topos absolute change floor | $10^{-4}$ | none | `[topos].change_alert_threshold` |
| $c^{\min}_{\rm Aud}$ | Audition absolute change floor | 0.35 | none | hard-coded default |
| $\omega_{\min}$, $\omega_{\max}$ | Audition attended fraction at arousal 1 and 0 | 0.15, 1.0 | none | `[audition].arousal_window_min`, `arousal_window_max` (unset; default) |
| none | Topos saliency grid | 12 by 12 | tiles | `[topos].foveation_grid` |
| none | fovea hysteresis margin | 0.15 | none | `[topos].foveation_hysteresis` |
| $\alpha_F$ | fovea tile-statistics weight | 0.05 | none | hard-coded |
| $n_F$ | tile observations before precision weighting | 5 | clip ticks | hard-coded |
| $f_0^F$ | tile variance floor, as a fraction of the mean tile change | 0.1 | none | hard-coded |
| $\beta^{\rm Chr}_\nu$ | Chronos temporal-error alert ratio | 3.0 | none | `[chronos].anomaly_alert_threshold` |
| $W_{\rm rum}$ | rumination window | 32 | broadcasts | `[chronos].rumination_window` |
| $n_{\rm rum}$ | rumination count | 4 | states | `[chronos].rumination_threshold` |
| $\Delta_{\rm rum}$ | rumination quantization step | 0.25 | none | `[chronos].rumination_bucket_resolution` |
| none | Chronos forward prediction | on | none | profile `[chronos].forward_prediction` |
| $I_0$ | phasic salience floor | 0.5 | none | `[cycle.access_rate].salience_floor` |
| $\tau_{\rm ph}$ | phasic decay time | 1.0 | s (subj.) | `[cycle.access_rate].phasic_decay_s` |
| $a_0$ | baseline arousal (Thymos and access rate) | 0.3 | none | `[thymos].baseline_arousal` |
| none | adaptive access rate | on | none | `[cycle.access_rate].enabled` |
| $\lambda$ | arousal relaxation rate | 0.05 | s$^{-1}$ (subj.) | `[thymos].drift_rate_per_s` |
| $P_{\rm Thy}$ | minimum interval between Thymos state events | 1.0 | s (subj.) | `[thymos].publish_interval_s` |
| $\gamma_\pi$ | perceptual-alert arousal gain | 0.15 | none | hard-coded |
| $\nu_{\rm cap}$ | cap on the excess error ratio per alert | 4.0 | none | hard-coded |
| $\gamma_{\rm Som}$ | arousal step per Soma hard-threshold report | 0.05 | none | hard-coded |
| $\tau_{\rm f}$, $\tau_{\rm s}$ | fast and slow time constants of the error means and alert rates | 10, 100 | s (subj.) | `[thymos].fast_time_constant_s`, `slow_time_constant_s` |
| $k_v$ | learning-progress gain in the pleasantness check | 2.0 | none | `[thymos].valence_progress_gain` |
| $\tau_v$ | valence time constant | 30 | s (subj.) | `[thymos].valence_time_constant_s` |
| $g_0$ | learning-progress noise floor | 0.05 | none | `[thymos].learning_progress_floor` |
| $m_B$ | alert-excess margin | 0.5 | none | `[thymos].alert_excess_margin` |
| $r_0$ | alert-rate floor | 0.05 | s$^{-1}$ (subj.) | hard-coded |
| $\alpha_{\rm int}$ | intent-rate weight | 0.05 | none | `[thymos].intent_rate_weight` |
| $\beta$, $\delta$, $\rho$ | curiosity build, decay, relief | 0.05, 0.0055, 0.5 | s$^{-1}$ (subj.) | `[thymos.drives.curiosity]` |
| $\beta$, $\delta$, $\rho$ | boredom build, decay, relief | 0.04, 0.0045, 0.3 | s$^{-1}$ (subj.) | `[thymos.drives.boredom]` |
| $\beta$, $\delta$, $\rho$ | social-drive build, decay; relief per interaction | 0.01, 0.0011; 0.8 | s$^{-1}$ (subj.); none | `[thymos.drives.social_drive]` |
| $\beta$, $\delta$, $\rho$ | restlessness build, decay; relief per intent | 0.03, 0.0033; 0.5 | s$^{-1}$ (subj.); none | `[thymos.drives.restlessness]` |
| $\theta_D$ | drive threshold (every drive) | 0.7 | none | `threshold` in `[thymos.drives.*]` |
| none | initial held arousal $\hat a$ | 0.3 | none | hard-coded |
| $P_{\rm Som}$ | Soma report interval | 1.0 | s (subj.) | `[soma].read_interval_s` |
| $n_x$ | Soma feature dimension (three self-rhythm features are zero unless the self-rhythm is enabled, and one is the highest GPU memory use) | 8 | none | hard-coded |
| none | Soma reservoir units | 32 | none | `[soma].forward_model_units` |
| $\eta_{\rm Som}$ | Soma readout learning rate | $10^{-3}$ | none | hard-coded |
| $\tau_U$ | expected-error time constant | 600 | s (subj.) | `[soma].expected_error_tau_s` |
| $\beta_U$ | expected-error band | 2.0 | none | `[soma].expected_error_band` |
| none | hard thresholds: CPU, RAM, GPU temperature, VRAM, cycle latency | 90, 90, 83, 92, 600 | %, %, °C, %, ms | `[soma.thresholds]` |
| $\theta_R$ | regulation threshold | 0.5 | none | `[soma].regulation_threshold` |
| $\Delta_R$ | regulation sustain window | 30 | s (subj.) | `[soma].regulation_sustain_window_s` |
| $n_{\rm wu}$, $\Delta_{\rm wu}$ | warm-up end conditions | 1000, 1200 | updates, s (subj.) | `[soma].regulation_warmup_min_samples`, `regulation_warmup_min_seconds` |
| $\gamma_f$ | processing-rate reduction factor | 0.8 | none | hard-coded |
| $f_p^{\min}$, $f_p^{\max}$ | processing-rate bounds under regulation | 0.5, 20 | Hz (subj.) | hard-coded |
| $\theta_{\rm th}$ | think bar | 0.45 | none | `[volition].think_threshold` (unset; default) |
| $\theta_{\rm sp}$ | speak (report) bar | 0.6 | none | `[volition].report_threshold` (unset; default) |
| $\Delta_{\rm th}$ | think refractory interval | 3.0 | s (subj.) | `[volition].think_refractory_s` (unset; default) |
| $\Delta_{\rm sp}$ | speak refractory interval | 8.0 | s (subj.) | `[volition].speak_refractory_s` (unset; default) |
| $\Delta_{\rm sig}$ | signature expiry | 300 | s (subj.) | profile `[volition].sig_expiry_s` |
| $\Delta_g$ | in-flight guard timeout | 48 | s (wall) | hard-coded |
| none | interrupt bar | unset | none | `[volition].interrupt_threshold` |
| $f_r$ | self-rhythm step rate | 20 | Hz (subj.) | `[soma].self_rhythm_step_hz` |
| $n_s$ | Euler substeps per step | 10 | none | hard-coded |
| $w_{\rm rec}$ | recurrent weight | 2.5 | none | hard-coded |
| $b_0$ | input offset | $-0.25$ | none | hard-coded |
| $k_\sigma$ | sigmoid slope scale | 0.08 | none | hard-coded |
| $\tau_y$ | activity time constant | 0.02 | s | hard-coded |
| $\gamma_R$ | depression rate | 8.0 | s$^{-1}$ | hard-coded |
| $g_o$, $g_u$ | own-drive and maternal-drive gains | 0.02, 0.03 | none | hard-coded |
| $\sigma_\xi$ | noise scale | 0.02 | none | hard-coded |
| $\tau_{\rm rec}^{(0)}$ | initial recovery time | 2.1 | s | hard-coded |
| $\tau_{\rm rec}^{\min}$, $\tau_{\rm rec}^{\max}$ | recovery-time bounds | 0.9, 2.3 | s | hard-coded |
| $\eta_\ell$ | frequency-adaptation rate | 0.0025 | s$^{-1}$ | `[soma].self_rhythm_eta` |
| $\tau_m$ | moving-average time constant | 10 | s | hard-coded |
| none | phase and amplitude window | 8 | s | hard-coded |
| none | initial activity $y$ and resource $R$ | 0.05, 1.0 | none | hard-coded |
| none | maternal beat rate and drift | 70, 0.03 | bpm, none | `womb.heartbeat_bpm`, `heartbeat_drift` |
| $u_{\max}$ | maximum maternal drive | 0.4 | none | `womb.external_drive_max_amplitude` |
| $s_u^{\rm base}$, $s_u^{\rm pert}$ | usual and perturbation drive scales | 0.5, 0.75 | none | `readout.baseline_drive_fraction`, `perturbation_drive_fraction` |
| $f_g$ | readout sampling rate | 10 | Hz | `readout.sample_hz` |
| $f_{\rm lo}$, $f_{\rm hi}$ | entrainment band | 0.3, 2.0 | Hz | `readout.entrainment_band_low_hz`, `entrainment_band_high_hz` |
| $\Delta_{\rm trim}$ | edge trim | 2.0 | s | `readout.edge_trim_seconds` |
| $\Delta_E$ | driven-window length | 300 | s | `readout.entrainment_window_seconds` |
| $\Delta_W$, $P_W$ | withdrawal duration and period | 20, 1800 | s | `readout.withdrawal_seconds`, `withdrawal_period_seconds` |
| $\Delta_{\rm pert}$, $P_{\rm pert}$ | perturbation duration and period | 5, 3600 | s | `readout.perturbation_seconds`, `perturbation_period_seconds` |
| $j_P$ | probe jitter fraction | 0.25 | none | `readout.probe_jitter_fraction` |
| none | readout period, also the settle time after boot or thaw | 60 | s | `readout.readout_period_seconds` |
| $f_{\rm guard}$ | pull guard | 0.05 | Hz | hard-coded |
| $\mathrm{pull}_{\min}$ | pull floor | 0.5 | none | `readout.frequency_pull_floor` |
| $n_{\rm base}$ | baseline withdrawals | 3 | count | `readout.baseline_withdrawals` |
| none | surrogate count | 19 | count | `readout.surrogate_count`; surrogate seeds hard-coded |
| none | consecutive passes required | 3 | count | `readout.entrainment_replications` |
| $t_{R0}$, $t_{R1}$, $t_{R2}$, $t_{R3}$ | viability checkpoints | 6, 24, 48, 60 | h (lived) | `readout.viability_r0_hours` to `viability_r3_hours` |
| $\mathrm{pull}_{R1}$, $\mathrm{slope}_{R1}$ | R1 bounds on median pull and slope | 0.12, 0.002 | none, h$^{-1}$ | `readout.viability_r1_pull`, `viability_r1_slope_per_hour` |
| $\mathrm{pull}_{R2}$ | R2 bound on median pull | 0.3 | none | `readout.viability_r2_pull` |
| $\Delta_V$, $n_V$ | viability window and minimum points | 12, 8 | h (lived), withdrawals | `readout.viability_window_hours`, `viability_min_points` |
| $\Delta_{\rm HRV}$ | variability window | 300 | s | `readout.hrv_window_seconds` |
| $\mathrm{HRV}_{\min}$ | variability floor | 0.2 | none | `thresholds.hrv_variability_floor` |
| $\mathrm{womb}_{\max}$ | womb error-ratio ceiling | 0.3 | none | `thresholds.womb_prediction_error_ceiling` |
| $\Delta^{\rm rec}_{\max}$ | return-to-baseline ceiling | 30 | s | `thresholds.return_to_baseline_seconds_ceiling` |
| $\mathrm{tol}_{\rm rec}$, $\Delta^{\rm rec}_{\rm cap}$ | recovery tolerance and cap | 0.25, 300 | none, s | `readout.recovery_tolerance`, `recovery_cap_seconds` |
| $n_{\rm sleep}$, $n_{\rm cons}$ | required sleeps and consolidation passes | 5, 3 | counts | `stage.min_sleep_cycles`, `min_consolidation_passes` |
| $\Delta_{\rm life}$ | minimum lived time | 86400 (24 h) | s (lived) | `stage.min_lived_seconds` |
| none | gate cadence | 60 | s | `stage.gate_cadence_seconds` |
| $\Delta_{\rm budget}$ | gestation budget | 96 | h (wall) | hard-coded default of the study plan (`gestation_budget_seconds`) |
| $w$, $\delta$, $n_{\rm run}$ | live-test window, minimum effect, and runs | fixed before the live runs | ticks, none, runs | study plan |
| none | harness settings: ticks, $K$, $\theta$, $w$, $\delta$, seeds | 24, 2, 0, 6, 0.15, 5 | ticks, events, none, ticks, none, seeds | hard-coded (harness and suite defaults) |
| none | harness factors $G$ and $T$ | 1, 1 | none | hard-coded (two-factor score) |
| none | suite family-wise level | 0.05 | none | hard-coded (suite default) |
| $\mathrm{tol}_{\rm CV}$, $n_{\rm seed}$ | suite stability tolerance and seeds | 0.05, 3 | none, seeds | hard-coded (suite default) |
