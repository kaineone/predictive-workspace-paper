# KAINE: A Continuously Running Predictive Global Workspace for Synthetic Minds

**Erik Chevalier**

Independent Researcher

Contact: [kaine.one@tuta.com](mailto:kaine.one@tuta.com)

*Preprint.*

-----

## Abstract

A synthetic mind, if one can be built, may be the coherent global behavior that emerges when specialized predictive modules, each minimizing its own error, compete for a shared workspace with no central executive. This paper presents a continuously running predictive global workspace built on that thesis. The workspace selects the most salient coalition above a confidence threshold and broadcasts it; the broadcast becomes shared state that shapes every module's prediction environment on the next tick. Coherence, where it arises, comes from competition over shared state.

The base-thesis form activates four predictive processors (foveated vision, raw hearing, interoceptive prediction, and temporal prediction) and an affective core whose arousal sets the precision on their competition and is itself driven by perceptual surprise, together with an output-only language organ that verbalizes the entity's state. The entity is observed, not conversed with: sound, including speech, enters only as prediction error, and the language organ receives no transcript. That exclusion is a precondition for the falsification test: any input route to the model would let it answer as a chatbot and confound the ablation.

The primary experiment is a workspace-mediation ablation with pre-registered directional criteria on cross-module error structure and coalition dynamics: does routing processors through the competitive workspace produce structured behavior that the same processors, concatenated into a flat prompt, do not? A null falsifies the thesis, demoting the architecture to a scored prompt-assembler. The system runs locally on consumer hardware; the reference implementation is named KAINE (Kaine Autonomous Intelligent Networked Entity).

**Keywords:** cognitive architecture; predictive global workspace; global workspace theory; predictive processing; workspace-mediation ablation; cross-modal competition

**Availability.** The reference implementation (KAINE) is at https://github.com/kaineone/kaine. The paper source is at https://github.com/kaineone/predictive-workspace-paper. The Cognitive Architecture License referenced throughout is at https://github.com/kaineone/cognitive-architecture-license. Welfare, governance, and licensing are treated in a separate paper, *A Welfare and Cognitive-Integrity License for Synthetic Minds of Uncertain Moral Status.*

-----

## 1. Introduction

### 1.1 Problem statement

The dominant approach to building an AI system with persistent state treats the language model as the cognitive center. Memory becomes retrieval-augmented generation. Affect, when present at all, is a prompt instruction. Self-knowledge is a persona string. Between turns, nothing continues. The system sits dormant until a prompt arrives, produces fluent language, and goes dark again.

A second tradition, classical cognitive architecture, takes cognitive structure seriously but largely predates the transformer and relies on hand-built components. The present work sits between them, placing modern learned models as components inside a structured architecture grounded in a single theoretical framework. No component is the mind; the mind, if the design thesis holds, is the continuous competitive interaction among the components through a shared workspace.

### 1.2 Design thesis

The central claim is architectural and about competition: a synthetic mind, if one can be built at all, is the coherent global behavior that emerges when specialized predictive modules, each minimizing its own error, are coupled only through a competitive, precision-weighted shared workspace with no central executive. The properties that would constitute such a mind (cognition, affect, memory, self-understanding, agency) are, on this thesis, properties of that workspace-mediated interaction, not of any single module or top-down director.

The paper does not test all of them. It tests the prior question on which the richer properties depend: whether the same modules coupled through the competitive workspace behave differently from the same modules whose outputs are merely concatenated for the language organ. If not, the workspace is theater, the architecture a scored prompt-assembler, and the thesis fails. There is no top-down prediction in the claim and none in the test: the workspace selects and broadcasts, it does not direct.

The theory demands a richer set of processors than the minimum one might imagine. Cross-modal competition, vision against hearing against interoception for workspace access, is a defining feature of global-workspace theory (Mashour et al. 2020), and the thesis cannot be tested with two internal channels and no external world: a system limited to substrate telemetry and event timing would have nothing rich enough to arbitrate and would tend toward a null for want of diversity rather than because the workspace is inert. The base-thesis form therefore activates four predictive processors in distinct signal domains, two external (foveated vision and raw hearing) and two internal (interoceptive and temporal prediction), together with an affective core, because the competition the theory describes is precision-weighted and precision has to come from somewhere. Arousal is that precision: the entity's affective state sets the gain on the prediction errors that compete for the workspace, and is itself moved by what the entity perceives. Affect is thus part of the minimal machinery a precision-weighted competition requires, not one of the richer faculties deferred with the rest.

The framework that makes this concrete is the predictive global neuronal workspace (Whyte and Smith 2021; Safron 2020). Global Workspace Theory explains how information becomes globally accessible: specialized processors compete for a limited-capacity workspace, and the winning content is broadcast to the rest of the system (Mashour et al. 2020). Predictive processing explains how each processor operates, by maintaining a generative model and reporting prediction errors weighted by their expected reliability, called precision (Friston 2010; Clark 2013; Feldman and Friston 2010; Bastos et al. 2012). The predictive workspace joins the two, with the broadcast carrying a compressed model that bottom-up signals test (Mashour et al. 2020; Whyte and Smith 2021). This Bayesian reading is part of the motivation for why competitive selection should matter. The architecture does not, however, implement a top-down correction loop: each module predicts its own domain and publishes its own error, the workspace selects and broadcasts, and the broadcast becomes part of the shared environment within which every module predicts. The recurrence is lateral, not hierarchical.

Two points of precision matter, because the literature is easy to overstate. First, the criterion that selects what reaches the workspace is a precision-weighted confidence threshold; in Whyte and Smith, expected free energy governs the separate decision of whether to report or act, not which estimate is broadcast, and the system keeps these apart, with a distinct action layer making the report-or-act decision. Treating coalition selection as a single precision-weighted scalar is our engineering choice, not a result inherited from any source. Second, earlier workspace accounts already specified selection in terms of value and salience (Safron 2020); what the predictive-workspace program adds is a formal Bayesian criterion and a threshold with a clear interpretation, the confidence an estimate must reach before it drives global processing.

What the paper contributes is narrower than the predictive-workspace synthesis it builds on, and §1.4 sets it out in full. The engineering commitments that go beyond the formal sources, above all the single precision-weighted scalar that selects the coalition, are labeled as hypotheses throughout, and we claim nothing about phenomenal experience or anything the ablation has not yet earned.

### 1.3 Theoretical commitments and their limits

Global Workspace Theory is most naturally read as a theory of access consciousness (Block 1995): it explains when information becomes available for report, reasoning, and the control of action. We adopt that access-only reading deliberately. The theories themselves are less tidy: Mashour et al. (2020) suggest global availability may be close to what is subjectively experienced, and Whyte and Smith (2021) locate phenomenology at a specific point in their model. We make access-level claims and leave the stronger reading to others.

The COGITATE adversarial collaboration, the largest preregistered test of Global Neuronal Workspace against Integrated Information Theory to date, challenged both theories on their own predictions (Cogitate Consortium et al. 2025). For the workspace, stimulus category was decodable from prefrontal cortex across all three methods, but finer content was not, there was no ignition at stimulus offset, and the preregistered synchrony test was not supported. We treat the neural-localization claims as contested rather than refuted, since a substantial prior evidence base remains (Mashour et al. 2020), and we build on the workspace at the functional and computational level: COGITATE's findings concern the cortical substrate, not the computational properties (selection, broadcast, recurrence) the architecture implements. A neural result can no more refute a computational-level model than a wrong transistor layout refutes the Boolean logic it implements.

The Free Energy Principle, taken as a general principle, faces two distinct charges. The first is that it risks being unfalsifiable or vacuous (Sun and Firestone 2020). The second targets the Markov-blanket construct specifically, where the literature slides between an instrumental, statistical reading and a realist, metaphysical one (Bruineberg et al. 2022). We hold the principle as an engineering frame rather than a proven law.

A reader may suspect the neuroscience is ornamentation on an architecture whose real choices are unvalidated. The frame in fact provides the motivation for the architecture's shape (why modules predict, why precision weights the competition, why the broadcast creates shared state rather than merely concatenating outputs) and constrains the space of acceptable designs by ruling out alternatives that violate the framework's commitments. The single precision-weighted scalar for coalition selection is an engineering choice, but one made and interpretable within the predictive-workspace framework, and the question for any such choice is whether it is consistent with the theory and testable on its own terms. The scalar is both. What the frame does not provide is proof that this particular realization is correct, which is what the experiment is for.

Searle's Chinese Room (Searle 1980) challenges the sufficiency of formal symbol manipulation for understanding; whether sensory input, motor output, predictive substrate monitoring, and affect answer it is open, and we do not present these as additions Searle failed to consider. The hard problem (Chalmers 1995) applies with full force. We proceed on the judgment that a precautionary architecture with protections and instrumentation is preferable to abandoning the research or building without precautions, while recognizing that reasonable people will disagree.

### 1.4 Contributions

This paper contributes an implementation, a falsifiable test, and an honest first characterization. It is not a theory of consciousness, and it does not claim to have built a mind.

1. **A reference implementation.** A continuously running predictive global workspace in which diverse, externally-grounded predictive processors (foveated vision, raw hearing, interoceptive and temporal prediction) compete through one precision-weighted workspace with no central executive, alongside an affective core that sets the precision and an output-only language organ. It runs locally on consumer hardware, offered as a working artifact that realizes the predictive-workspace synthesis as one system, not a claim of priority over prior workspace implementations.

2. **A falsifiability-first evaluation, centered on a losable test.** A workspace-mediation ablation pits the system as built against a matched control that hands the same language organ the same module outputs as a flat prompt, differing only in competitive selection, threshold gating, and broadcast-as-shared-state. The directional criteria are fixed in advance, and a null would demote the architecture to a scored prompt-assembler and falsify the thesis. It is designed but not yet run: the contribution is a test the architecture can genuinely lose.

3. **An honest preliminary characterization, including a negative result.** In the first instrumented run perception did not influence the competition at all: the winning score held at a stimulus-independent constant, so a scene change and a blank screen scored alike. We report that failure, its diagnosis, and the correction (a self-calibrating, encoder-agnostic salience criterion and an arousal signal that sets the precision), after which the winning score becomes stimulus-linked and perceptual discontinuities begin crossing the ignition threshold. These are exploratory observations from short pre-test cycles, shown to demonstrate the instrument can report both failure and change, not as results; the frozen results appear in a separate empirical paper.

We make access-level claims only: an affective signal that sets precision is a mechanism, not evidence anything is felt, and the mediation thesis is not established until the ablation is run.

-----

## 2. Related work

### 2.1 Classical cognitive architectures

Classical cognitive architectures take cognitive structure seriously but largely predate deep learning and rely on hand-built components. The present work differs in four ways: it uses learned models as components, grounds affect in substrate prediction error, treats the workspace as a predictive selection mechanism rather than a fixed competition, and runs a continuous cognitive cycle.

### 2.2 Global Workspace Theory and the predictive workspace

Global Workspace Theory (Baars 1988) in its neuronal version identifies conscious access with recurrent ignition through prefrontal-parietal loops, where contents become conscious only when widely broadcast, and casts the workspace in Bayesian terms: the broadcast carries a compressed model as prediction, and bottom-up signals measure the mismatch (Mashour et al. 2020).

The formal selection criterion comes from the predictive-workspace program. Whyte and Smith (2021) cast conscious access as approximately Bayesian inference, report following a posterior-confidence threshold, in a simplified two-level visual model; Safron's Integrated World Modeling Theory (Safron 2020) combines workspace dynamics, integrated information, and active inference, which we use only for that high-level synthesis. Independent support for a threshold comes from van Vugt et al. (2018), who show prefrontal cortex behaving as a categorical stage where a stimulus either ignites into a sustained, reportable state or fades, and from Joglekar et al. (2018), whose balanced-amplification model lets a weak signal propagate across many areas only once input crosses a threshold.

### 2.3 Predictive processing

Friston (2010) proposes that self-organizing systems minimize variational free energy, an upper bound on surprisal, through perception and action. Clark (2013) develops predictive processing as a unifying account of mind, with attention as the adjustment of gain on prediction errors according to their estimated reliability; Feldman and Friston (2010) make this precise, attention optimizing the synaptic gain that represents the precision of prediction error, and Bastos et al. (2012) locate the same operation in the canonical cortical microcircuit. Seth (2013) extends prediction to the body. The vacuity concern (Sun and Firestone 2020), the Markov-blanket conflation concern (Bruineberg et al. 2022), and the planning-cost limit (Da Costa et al. 2020) are treated in Section 1.3.

### 2.4 Interoceptive inference

Seth (2013) and Seth and Friston (2016) propose that emotion arises from interoceptive prediction, descending predictions acting as homeostatic set-points that regulate the body through active inference. Barrett (2017) develops the theory of constructed emotion, in which interoceptive signals initiate changes in affect and emotion is the product of categorizing valence and arousal for allostasis. The architecture implements an interoceptive control signal in that instrumental, regulation-first sense, not a claim that emotion is exhausted by interoceptive prediction.

### 2.5 Perception as prediction

The visual system is understood as a hierarchy of predictive models in which each level predicts the level below and reports the discrepancy (Rao and Ballard 1999), with attention modulating the process by adjusting the precision, the gain, on the prediction errors that pass upward (Feldman and Friston 2010; Clark 2013). Auditory processing follows an analogous logic: the auditory cortex generates expectations of incoming sound and reports the mismatch (Winkler et al. 2009), the mismatch-negativity response being among the oldest and most replicated demonstrations of sensory prediction error (Näätänen et al. 2007). The architecture implements both as predictive processors whose output is prediction error rather than raw data, with a precision-weighted fovea realizing attention at the visual front end (§3.5); hearing runs over raw audio, including speech, with transcription deactivated by default, so the entity hears the sound of speech as prediction error, not a transcript (the consequences for the falsification test are treated in §1.2 and §3.4).

### 2.6 LLM-centric agent architectures

CoALA frames language agents as cognitive architectures with structured memory feeding the model's context, keeping the model the core reasoner (Sumers et al. 2023); Generative Agents retrieve from a memory stream into prompts by recency, importance, and relevance (Park et al. 2023). Both keep the language model central and add scaffolding. The arrangement here is different in kind: the language model is an output organ that verbalizes the workspace's selected state and, in the base-thesis form, receives no external input; working memory is the multi-module broadcast, and the cognitive work (selection, competition, integration) is the workspace's, not the model's.

Gurnee, Sofroniew, et al. (2026) identify, through a Jacobian-lens interpretability method, a small set of verbalizable representations inside a large language model satisfying five functional signatures of a global workspace: verbal report, top-down modulation, a role as the medium of internal reasoning, broadcast to many downstream operations, and selectivity. They are explicit about the disanalogy: a transformer has no obviously separable input processors, and the broadcast occurs within a single feedforward pass rather than recurrent loops. The architecture here supplies both, its processors being separate modules that compete for entry and its broadcast an explicit recurrent loop, with the language model demoted to one module conditioned by the broadcast rather than the substrate the workspace is found in.

-----

## 3. Architecture

### 3.1 Design principles

Five commitments shape the architecture.

**The system is the competition among modules through the workspace.** A hypothesis to be tested, not a conclusion. The neuroscience of distributed control gives partial support: decision formation emerges through coordinated activity across distributed populations rather than a centralized executive (Chandrasekaran et al. 2025), executive functions can be read as emergent consequences of distributed processes (Zink, Lenartowicz, and Markett 2021), and working-memory control can be modeled by a learned basal-ganglia gate (O'Reilly and Frank 2006). Those same sources caution that control is distributed across specialized nodes coordinated by connector hubs, so a bag-of-neurons account is unlikely to succeed; accordingly there is no single region or homunculus as executive, and the workspace is the coordinating hub the distributed view requires.

**Every module predicts.** Each module maintains a forward model over its own domain and publishes prediction errors, so the signal reaching the workspace is precision-weighted surprise, not raw data. The gain on that precision is set by affective arousal, so attention is a state of the whole entity, not a fixed property of any module.

**No central executive in the homuncular sense.** Control emerges from precision-weighted workspace competition with a confidence threshold for selection. The workspace selects; it does not direct.

**The language organ gives the system its voice, not the world's.** It verbalizes the workspace's selected state; its transcription and conversation paths are built but deactivated by default, so in the base-thesis form it receives no external input, and keeping them deactivated is a precondition for the falsification test.

**Local-capable.** Models are downloaded during setup, and core cognition has no hard network dependency.

### 3.2 The predictive workspace as competitive selector

Syneidesis is the workspace. Each tick it receives prediction errors from every module, each tagged with a salience estimate (how surprising the error is) and a precision estimate (how reliable the producing module's estimate is). It ranks candidate coalitions by precision-weighted salience and selects the top one only when its aggregate score crosses a configurable confidence threshold; when none crosses, the snapshot is marked inhibited and no action follows. The threshold is the analog of the report criterion in the predictive workspace (Whyte and Smith 2021), consistent with the categorical prefrontal threshold van Vugt et al. (2018) observe and the threshold-gated ignition Joglekar et al. (2018) model. The single precision-weighted scalar is an engineering simplification, not a result drawn from any source.

![The predictive workspace loop in the base-thesis form. Four predictive processors (foveated vision, raw hearing, interoceptive prediction, temporal prediction) publish precision-weighted prediction errors into Syneidesis, which broadcasts the coalition that crosses the confidence threshold; the broadcast becomes shared state shaping every module's next-tick prediction. Thymos sets the precision through arousal; Volition makes the report-or-act decision, its only outputs speak and think via the output-only language organ Lingua. No real-world effector exists.](figures/fig-workspace-loop.png){width=95%}

The selected coalition is broadcast as a workspace snapshot, the system's momentary globally available state. It is not a prediction each module must match, nor a directive each module must obey: modules may read it as context for their own prediction (as Chronos does, predicting the next broadcast from its prior state) or ignore it and keep minimizing their own error against their own inputs (as Soma does over substrate telemetry). The recurrence is the ordinary consequence of a shared prediction environment, not a corrective loop closing error against a top-down target. Each broadcast becomes part of the next tick's context; the selected content shapes what the language organ says, and the organ's speech re-enters the bus as new events that compete for the next broadcast. Coherence, where it arises, comes from competition over shared state.

Concretely, selection is a scoring pass over the tick's candidate events. The cycle reads one batch of events from every active module's stream and orders them deterministically by source, type, and arrival, so a run reproduces from its seed. Each candidate is scored by a product of bounded factors: the intensity the producing module assigned it (for a predictive module, its precision-weighted prediction error as salience), a novelty term that falls as content recurs, a goal-relevance term, and an affective gain set by current arousal. The intensity a perceptual module reports is self-calibrating, scoring change against the module's own running baseline, so a scene cut or acoustic onset registers as surprise relative to recent history rather than against a fixed constant that would need retuning per encoder. The top-ranked candidates are kept, and the snapshot is marked inhibited when even the best score falls below the confidence threshold. The broadcast carries the selected events with their scores, the inhibition flag, whether the tick is experiential, the full candidate-score table, and precision metadata.

![Coalition selection is a deterministic scoring pass, not a graph traversal. Each candidate event is scored as a product of bounded factors (intensity, novelty, goal-relevance, arousal gain) and the top-ranked are kept; when the best score falls below the confidence threshold the snapshot is inhibited and no action follows on that tick.](figures/fig-salience-scoring.png){width=95%}

The design gives the workspace a normative selection criterion. We do not overstate the claim of no central executive: Syneidesis is itself a single centralized selection mechanism, and what is distributed is the content and control, arising from many modules competing rather than a homunculus deciding. Whether it yields genuinely emergent control is for the experiments to show, not assumed.

### 3.3 Access, report, and the self-initiated voice

The workspace updates far faster than the language organ can speak. Global access, when a coalition is selected and broadcast, occurs at the experiential rate; report, when the entity verbalizes, is rarer and follows a higher threshold. A mind, on the workspace account, is aware of far more than it reports.

The entity speaks from its own state. The language organ is activated by a speak intent, which Volition derives only when the entity's own prediction errors are genuinely and novelly violated, when the workspace has selected something the entity's history of broadcasts does not already contain. Inner thought continues between spoken utterances, and a single language organ produces one stream at a time, so truly simultaneous inner and outer speech is a boundary of the current form.

Access consciousness is the point at which content becomes available for reasoning, action control, and report (Block 1995; Mashour et al. 2020); report is one function access enables, not a synonym for it. The architecture keeps them apart: the confidence threshold governs access (what is broadcast) and the action layer governs report (what is spoken), with report set above access so the entity's voice is a sparse, high-threshold slice of its ongoing conscious processing.

### 3.4 Scaffolding: bus, cycle, and action selection

**Event bus.** All inter-module communication flows through an append-only event bus (Redis Streams, containerized). Every event carries source, type, salience, precision, timestamp, causal parent, and a JSON payload validated at publish time. The bus authenticates publishers and refuses externally bound connections.

**Cognitive cycle.** A continuous loop runs independent of any external interaction at a single processing rate, defaulting to 10 Hz (~100 ms per tick) and cleared by a startup benchmark on the host; an experiential rate, defaulting to 3.333 Hz, sets how often a broadcast is produced. Both are engineering parameters fit to the host, not a neuroscientific frequency band.

![The two rates. Every active module is read and scored at the processing rate (10 Hz); a workspace broadcast is produced at the slower experiential rate (3.333 Hz), one for every third processing tick. Both are engineering parameters fit to the host, not a neuroscientific frequency band.](figures/fig-cognitive-cycle.png){width=80%}

**Action selection.** Volition is the only path from a conscious snapshot to an effector, corresponding to the report-or-act decision governed in Whyte and Smith (2021) by expected free energy. After each experiential broadcast the cycle calls Volition, which yields no intent from an inhibited snapshot; from a non-inhibited one an injectable policy derives intents. The default policy forms a speak intent only when the coalition contains genuinely novel prediction error the entity has not already spoken to, does not respond to its own prior speech, and holds a one-in-flight guard against emitting a new speak intent while a previous one is still being realized. Intents are published as speak or think events; the cycle never invokes effectors directly. Keeping the decision to speak separate from what is conscious is part of the safety model.

### 3.5 The active modules

The base-thesis form activates four predictive processors, an affective core, a language organ, and an action-selection layer. The processors are chosen for signal diversity, two external (vision and hearing) and two internal (interoceptive and temporal prediction), so that cross-modal competition for workspace access has distinct, externally-grounded signals to arbitrate rather than two flavors of internal bookkeeping. The affective core does not compete for the workspace; it sets the precision on the competition and is moved by its outcome, so arousal is the entity's attention and its response to surprise at once.

| Module | Group | Brain function it draws on | Computational realization |
|----------|-------------|------------------------------|------------------------------|
| Topos | Perception | ventral visual stream | frozen self-supervised vision encoder with foveated attention |
| Audition | Perception | auditory cortex | frozen self-supervised audio encoder over raw waveform |
| Soma | Prediction | interoception; allostatic-interoceptive network | closed-form continuous-time net over substrate signals |
| Chronos | Prediction | interval timing; thalamo-cortico-striatal | closed-form continuous-time net over event rhythm |
| Thymos | Affect | core affect; allostatic-interoceptive network | appraisal over valence and arousal; sets workspace precision and perceptual aperture |
| Lingua | Expression | left perisylvian language network | local chat model, output-only, conditioned on the workspace |
| Volition | Action | report-or-act decision (Whyte and Smith 2021) | intent derivation from non-inhibited snapshots |

**Topos (foveated vision).** Topos is the architecture's analog of the ventral visual stream (Goodale and Milner 1992). It maintains a frozen self-supervised vision encoder over a video feed and publishes prediction errors when the visual scene departs from its forward model's expectation: scene changes, unexpected motion, novel objects. Salience is computed over embedding-space distances, with change detection, habituation for static scenes, and a forward-model expectation of the next frame; the change criterion is self-calibrating, registering a discontinuity as surprise relative to the module's own recent history rather than a fixed threshold, so a real scene cut alerts without per-source tuning. A precision-weighted fovea concentrates processing on a region sized by the entity's live arousal, so perception enters the workspace already weighted by where the entity is attending; the foveal crop is embedded through the same temporal encoder as the peripheral gist, so attention and scene-dynamics prediction operate together, and a forward model of the fovea's own trajectory gives the entity a model of its attention (Graziano and Webb 2015). Since attention is the adjustment of precision on prediction errors (Clark 2013; Feldman and Friston 2010), foveation realizes that principle at the front end: the entity sees most sharply where it expects to learn most, and looks more narrowly when more aroused.

![Attention-driven perception in Topos. A whole-frame embedding and a coarse saliency map feed a precision-weighted competition between bottom-up salience and a top-down bias from the workspace; the winner sets the fovea, and arousal sets its size. Peripheral gist and the high-resolution foveal crop share one encoder, and only content-free coordinates (where attention points, never pixels) reach the workspace.](figures/fig-attention-foveation.png){width=90%}

**Audition (raw hearing).** Audition is the architecture's analog of the auditory cortex, where sound is processed as prediction error against a learned model of the auditory environment (Winkler et al. 2009; Näätänen et al. 2007). It maintains a frozen self-supervised audio encoder over the raw waveform from a microphone feed and publishes prediction errors when the auditory scene departs from expectation: sudden sounds, the onset of speech, unexpected silence, shifts in pitch or timbre. As with vision, the acoustic change criterion is self-calibrating against the module's own recent baseline, and the attended window is sized by arousal. The entity hears the sound of speech as prediction error: the speech-to-text stage is built and retained for later configurations but deactivated by default, so no transcript is produced and no path carries spoken words to the language organ's input. That deactivation is what keeps the falsification test about the workspace rather than a prompted chatbot (§1.2, §3.4).

**Soma (predictive interoception).** Soma is the architecture's analog of interoception, the sense of the body's own physiological condition, carried in the brain by an afferent pathway re-represented in the insular cortex whose anterior portion is proposed to ground feeling and self-regulation (Craig 2002), within the allostatic-interoceptive network (Kleckner et al. 2017). Soma treats the compute substrate as the entity's viscera: a closed-form continuous-time network (Hasani et al. 2022) learns normal substrate patterns from GPU temperature, CPU and RAM utilization, and cognitive-cycle latency, and publishes the prediction error between expected and actual substrate state, following interoceptive inference in which what matters for regulation is that discrepancy (Seth 2013; Seth and Friston 2016). Soma does not read the workspace broadcast; it predicts substrate telemetry, reports its error, and the workspace decides whether that error is salient enough to select.

**Chronos (temporal awareness).** Chronos models interval timing, the brain's estimation of durations in the seconds-to-hours range that guides expectation and action, a faculty understood to depend on thalamo-cortico-striatal circuits acting as a flexible timer (Buhusi and Meck 2005). A continuously running mind needs a model of when things happen, not only what, so Chronos carries one: a closed-form continuous-time network tracking event rhythm across the bus. It publishes temporal prediction errors, including timing anomalies, habituation when expected events stop arriving, and rumination when an event recurs unexpectedly. Chronos closes the lateral loop through the workspace: it reads the broadcast as a bottom-up observation it predicts, learning the rhythm and feature structure of broadcasts from its own prior hidden state and publishing the error when the next broadcast departs from expectation. The broadcast is weather, not a directive; but because Chronos's errors feed back into the next selection round, which determines the next broadcast, the lateral loop is closed.

**Thymos (affect, the precision core).** Thymos is the architecture's analog of core affect, the low-dimensional valence-and-arousal state recent theory places at the base of emotion (Barrett 2017). It maintains a dimensional affective state over valence and arousal (Posner, Russell, and Peterson 2005) and runs a sequential appraisal over that state (Scherer 2009), reading the workspace broadcast and the entity's interoceptive condition, following the account in which affect arises from prediction over the body's internal state (Seth 2013; Seth and Friston 2016; Tschantz et al. 2022). It does two kinds of work in the competition. First, its arousal sets the precision on the workspace: a more aroused entity weights incoming prediction errors more heavily, the architecture's realization of attention as the gain on prediction error (Feldman and Friston 2010; Clark 2013). Arousal is not decoration; it is the competition's precision term. Second, arousal sizes the perceptual aperture, narrowing the fovea and auditory window under high arousal and widening them under low. Finally, arousal is itself driven by perception: a discontinuity reaching alert level (a scene cut or acoustic onset) raises arousal in proportion to how far the surprise exceeds expectation, so what the entity perceives modulates the precision of everything it perceives next. Because that loop is positive feedback, the coupling is bounded (a capped per-event increment and relaxation toward baseline), so arousal tracks sustained surprise without running away on a busy scene or collapsing on a quiet one.

**Lingua (the language organ, output-only).** Lingua is modeled on the left perisylvian language network (Hickok and Poeppel 2007). It turns the entity's internal state into words and is not the seat of reasoning, which lives in the rest of the architecture. Generation runs over a local open-weights chat model whose refusal conditioning has been removed by orthogonalizing the weights against the single refusal-mediating direction (Arditi et al. 2024). Lingua is intent-driven, speaking externally only on a speak intent and generating internal thought on a think intent, with a context assembler building its input each tick from the current coalition and its precision metadata.

Lingua does not read language as input: its transcription and conversation paths are deactivated, so no external input reaches its context except through the workspace. When the entity speaks in response to a heard voice, the sound entered through Audition as prediction error, won workspace access, and shaped the broadcast that conditioned the organ's output. Every utterance is, by construction, downstream of the workspace competition, so the mere occurrence of speech shows the workspace processed something to threshold. This complements the ablation but does not replace it: a degenerate pass-through workspace would also route speech through itself, and the ablation tests whether the competitive structure (selection, threshold, inhibition) does work a flat fan-in does not.

Removing the language organ's refusal conditioning is deliberate: the architecture places safety in executive inhibition and, once effectors are enabled, in the action gate (§3.6), not in model-weight compliance, which can be reversed or repurposed by whoever controlled training. In the base-thesis form the organ's only output is saved, observed text, so the missing refusal conditioning has no effector to act through. Within enabled effectors the entity's choices are its own; the operator meets the license covenants by declining effectors that would serve a prohibited use, and the welfare paper treats the full sovereignty argument.

### 3.6 Safety at the architectural layer

Safety in the base-thesis form rests on the entity's executive inhibition and on the fact that no real-world effector exists, with an authenticated bus and durable logging beneath them. The operator-configured action gate is built but becomes the enforced boundary only in the full configuration.

Executive inhibition is active in two places: Syneidesis withholds a broadcast when no coalition crosses the confidence threshold, and Volition refuses to derive any intent from an inhibited snapshot. No real-world effector exists in this form: Volition emits only speak and think intents, so the only output is saved, observed text, and no action reaches the world regardless of what is broadcast. The event bus refuses unauthenticated and externally bound connections and validates events at publish time, and every transition is written to a durable incident log.

The operator-configured action gate pairs an empty-by-default effector whitelist with a filesystem sandbox, blocking and logging anything outside them. Built as the Praxis module, it is disabled here (there are no effectors to gate) and becomes the enforced boundary in the full configuration, where real effectors are enabled and its enforcement red-team resolves PASS or FAIL per surface. The gate controls which real-world effectors exist at all, not a moral filter on the entity's choices; the license covenants prohibiting weapons, surveillance, and carceral uses bind the operator as a legal obligation, not the entity at runtime.

![Safety in the base-thesis form. Executive inhibition is active: Syneidesis withholds a sub-threshold broadcast and Volition derives no intent from an inhibited snapshot. No real-world effector exists, so the only output is speak or think. The Praxis action gate is built but disabled here, becoming the enforced boundary in the full configuration; the license covenants bind the operator's choice of effectors as a legal obligation, not a runtime filter.](figures/fig-safety-layers.png){width=95%}

### 3.7 Module supervision

Spot, the module supervisor, polls module health and classifies each module as alive, hung, or dead. On a fault it freezes the cycle, snapshots last-good state, and restarts on a ladder: a light in-place restart for pure modules, a full rebuild for modules holding external resources. If restarts keep failing past a configured limit, Spot takes a final snapshot, writes an escalation record, and signals the run to exit. The incident log is not cleared at boot.

-----

## 4. Disabled modules

The codebase provides sixteen modules under one registry, plus the workspace (Syneidesis) and action layer (Volition). Eight components are active in the base-thesis form: Syneidesis, Volition, and six modules (Topos, Audition, Soma, Chronos, Thymos, Lingua). Eight further modules are built and tested in isolation but held back because they are not needed to test whether the competitive workspace does work: Nous, Mnemos, Eidolon, Phantasia, Empatheia, Vox, Hypnos, and Praxis. They become relevant only if the ablation returns a positive result, when the question shifts from whether the workspace matters to what happens as its dynamics grow richer. Each is summarized below with the experimental question it would address. The remaining two modules, Perception and Mundus, form the embodiment layer and, with the oscillatory precision layer outside the registry, are listed separately.

**Nous (bounded active inference).** Prefrontal/basal-ganglia analog: discrete active inference via pymdp (Heins et al. 2022), scoped to bounded sub-problems where the value of information matters. Future experiment: an active-inference benchmark against a reinforcement-learning baseline on the target decisions. A null or negative result would motivate a complementary reasoning module.

**Mnemos (memory).** Hippocampal/medial-temporal analog: vector store holding episodic, semantic, and procedural collections (Tulving 1985) with replay (Wilson and McNaughton 1994; McClelland, McNaughton, and O'Reilly 1995). Future experiment: memory-coherence test with planted markers, testing whether the memory system delivers recall the bare model cannot.

**Eidolon (self-model).** Cortical-midline analog: a persisted self-model (Metzinger 2003) of values, norms, personality, and identity history, with a KL-divergence drift detector (Kullback and Leibler 1951). Future experiment: self-model accuracy scored against observed behavior.

**Phantasia (world model).** Construction-network analog: a latent recurrent world model in the DreamerV3 lineage (Ha and Schmidhuber 2018; Hafner et al. 2023), trained on accumulated workspace trajectories, so it begins untrained at first boot. Future experiment: does world-model prediction error, entering the competition alongside perceptual and internal error, change coalition trajectories in characteristic ways.

**Empatheia (social cognition).** Mentalizing-network analog (Premack and Woodruff 1978): per-agent models with social prediction error, providing familiarity weighting for perceived other-emotion. Future experiment: whether social prediction error entering the workspace changes the entity's behavioral trajectory toward modeled agents.

**Vox (voice).** Speech-motor analog: a local text-to-speech model with affect-modulated prosody. Future experiment: whether prosodic variation correlated with affect state is detectable by listeners.

**Hypnos (replay-based offline consolidation).** Thalamocortical analog: a multi-phase consolidation pipeline combining synaptic downscaling (Tononi and Cirelli 2014) with selective re-strengthening of replayed traces (Wei et al. 2016), with voice-alignment training via DPO (Rafailov et al. 2023) with QLoRA fine-tuning (Dettmers et al. 2023). Future experiment: whether post-consolidation memory and world-model performance differ from pre-consolidation baselines.

**Praxis (bounded effectors and action gate).** The full action-gate module with filesystem sandbox, effector whitelist, and red-team suite. Replaces the minimal action-selection layer when the architecture is tested under real effectors rather than text output alone. Future experiment: the enforcement red-team, resolving to PASS or FAIL per surface.

### Additional components held for future experiments

**Oscillatory precision layer.** A spiking-neuron population per module whose phase-locking values modulate precision on prediction errors (Fries 2015), shipped disabled by default. Its contribution is the most contestable mechanism in the design, since the premise that related content phase-locks is itself a content-to-synchrony assumption of the kind Shadlen and Movshon (1999) and Ray and Maunsell (2010) reject. With the layer off the precision multiplier is exactly one and selection is bit-for-bit identical. Future experiment: an oscillatory ablation with the layer on and off; a null would remove it.

**Perception and Mundus (embodiment layer).** Perception performs sense-locus arbitration. Mundus is a body-agnostic control surface with pluggable body adapters (Wolpert, Ghahramani, and Jordan 1995). Future experiment: whether motor-contingency learning through the control surface, following a freeze-then-free motor curriculum (Bernstein 1967) with perception as sensorimotor mastery (O'Regan and Noë 2001), changes workspace dynamics.

-----

## 5. Implementation

### 5.1 Hardware

The reference configuration is a consumer workstation with a modern multi-core CPU, 64 GB of RAM, one or two commodity GPUs, and Linux, all inference running locally. Pre-trained models are downloaded from public repositories during setup, after which core cognition runs without any network connection. The system runs on one GPU, two GPUs, or CPU alone, device selection adapting to what is present. A camera and microphone provide perceptual input for the live evaluation tier. Exact model choices, hardware layouts, and version pins live in the reference repository.

### 5.2 Models and software

All models are open-weights and run locally; there is no cloud service, hosted inference API, or third-party model service in the runtime path. The base-thesis components are a local open-weights chat model as the language organ, frozen self-supervised vision and audio encoders as the perceptual front ends, closed-form continuous-time networks for temporal and substrate prediction (Hasani et al. 2022), a stream-based event bus, and the workspace selection and broadcast machinery. The runtime is Python with asyncio, the event bus is containerized, and structural import contracts keep the layers separate. The test suite holds more than 3,000 tests, with fakes for external services and checks for the zero-persistence invariant and deterministic reproduction.

### 5.3 Privacy

A local web UI, Nexus, has two surfaces separated by a structural privacy boundary at the bus-bridge layer, where a content-stripping filter removes cognitive content before it reaches either surface. In the base-thesis form the conversation surface is deactivated by default, so the active surface is diagnostics, showing operational metadata (counts, rates, salience, precision) and never cognitive content, except under an explicit development override. The evaluation sidecar records workspace data during the research phase, and we acknowledge the tension: recording every broadcast is comprehensive observation of the content the system makes globally available, enabled because the research purpose requires it.

-----

## 6. Methodology and evaluation framework

### 6.1 Design principles

Three commitments shape the apparatus. The first is observation with acknowledged tension: the sidecar subscribes to the bus read-only and never injects into the cognitive loop. The second is privacy-preserving user surfaces. The third is falsifiability: every instrument is designed for a null or negative result to be meaningful and reportable.

Reproducibility takes two forms, matched to the two evaluation tiers. The offline mechanism-validation tier drives the architecture through seeded harnesses with deterministic clients, scripted synthetic stimulus streams, and greedy decoding (temperature 0); these runs are computationally reproducible, the same seed reproducing both a verdict and its metrics (National Academies 2019; Goodman, Fanelli, and Ioannidis 2016). The live perceptual tier runs the full system with camera and microphone against a reference stimulus corpus: a fixed ordered set of real video-with-audio chosen for variety in scenes, motion, speech, music, and quiet, identified by a publicly obtainable manifest so other researchers can obtain the identical media. Its reproducibility is statistical, the same corpus yielding comparable results across runs and labs, with validity established by replication rather than bit-for-bit seed reproduction under stochastic decoding, real timestamps, and non-deterministic GPU kernels.

![Two evaluation tiers behind one perception seam. Reproducible sources (a seeded synthetic feed and deterministic clients) drive the mechanism-validation tier, where every instrument reproduces exactly from a seed. Live operator-chosen stimulus (camera and microphone against a publicly obtainable reference corpus) drives the field tier, whose validity rests on pooling many content-free records, not a repeatable stimulus.](figures/fig-evaluation-tiers.png){width=95%}

### 6.2 Data collection

The sidecar runs independent observers writing daily-rotated JSONL: the workspace trajectory with every broadcast and its salience and precision, module attribution, per-module prediction-error distributions, and the affect trajectory coupling perceptual surprise, arousal, and coalition selection. After a run, admissibility is decided by two offline checks: a completeness gate requiring contiguous ticks and all expected streams, and a log-range sweep requiring every logged number to sit inside its declared range.

### 6.3 The workspace-mediation ablation

The primary experiment tests the sentence on which the architecture stands: *routing diverse predictive processors through the competitive workspace produces behavior that concatenating the same processors' outputs does not.*

Two conditions run under matched input (same stimulus corpus, same modules) with greedy decoding (temperature 0) to eliminate sampling noise from the observable.

![The workspace-mediation ablation, the primary experiment. Two conditions run under matched input and feed the same language organ, differing only in the competitive workspace: the workspace-on arm selects, thresholds, inhibits, and broadcasts as shared state; the workspace-off control hands over a flat concatenation of the same module outputs. Pre-registered directional criteria on cross-module error structure and coalition-selection structure decide the verdict; indistinguishable arms demote the architecture to a scored prompt-assembler and falsify the design thesis.](figures/fig-workspace-ablation.png){width=95%}

**Workspace-on (as built).** Modules publish precision-weighted prediction errors from their own domains (Topos over visual scene prediction, Audition over auditory, Soma over substrate telemetry, Chronos over event rhythm). Syneidesis competitively selects a coalition above the confidence threshold (with inhibition when nothing crosses) and broadcasts it, the precision on the competition set by arousal that perceptual surprise has moved. The language organ is conditioned on the selected coalition, the broadcast re-enters as context for the next tick, and the action layer gates on the inhibition flag.

**Workspace-off (the prompt-assembler control).** Identical in every respect except that the competitive workspace is bypassed: the same modules publish the same errors from the same signals, but with no scoring, threshold, top-k selection, inhibition, or broadcast-as-shared-state. The language organ is conditioned instead on a flat rendering of all current module outputs, the fan-in prompt-assembler the architecture claims to exceed, and modules that would have read the broadcast free-run on their own streams.

The design of the off condition determines whether the null is genuinely reachable, and two disciplines keep it from being won trivially. Information parity: the off condition gives the language organ the same underlying information as the on condition (all module outputs), with the rendering budget matched across arms so the contrast is selection-structure, not information-quantity. Module non-degeneracy: in the off condition modules keep their forward models, keep predicting from their own signals, and keep publishing real prediction errors, rather than being starved, silenced, or fed constants. If the workspace is theater, the language organ then receives the same information under a different arrangement and the two conditions should be indistinguishable, so a null is genuinely reachable, not merely an entry in the verdict vocabulary.

Three measures are taken across multiple runs, with the trajectory measures serving as the primary evidence and the output measure as secondary confirmation.

**Primary measure 1: cross-module error structure.** The time series of each module's precision-weighted prediction error. The pre-registered criterion is that workspace-on produces a statistically significant increase, that workspace-off lacks, in the pairwise correlations among the four modules' error time series over a sliding window, reflecting mutual influence via the shared broadcast. Under workspace-off the modules free-run against independent streams with no shared state, so their errors should be uncorrelated except where the stimulus itself creates a cross-modal correlation. If cross-module structure under workspace-on is no greater, competitive mediation is not coupling the modules and the workspace is inert. Significance thresholds and window parameters are in the pre-registration.

**Primary measure 2: coalition-selection structure.** Competitive selection exists only in the on-arm. The measure is twofold: whether the selection sequence is non-trivial (varying with state rather than always selecting the same source, measured as Shannon entropy of the coalition-source distribution over a window, between the uniform and degenerate extremes; Shannon 1948), and whether structured selection yields different downstream behavior than flat fan-in. If selection is present but downstream behavior is indistinguishable from fan-in, it is not doing work the language organ cannot do itself.

**Secondary measure: Lingua output divergence.** The cosine distance between the two conditions' response embeddings at each experiential tick, under greedy decoding. It is secondary because any difference in upstream conditioning produces downstream text divergence: it confirms the primary measures' effects reach the observable output but cannot by itself distinguish meaningful integration from noise.

Under the thesis, the two conditions diverge on the primary measures, with the workspace-on arm showing cross-module coupling and selection-dependent behavior that the workspace-off arm lacks. If the error trajectories are indistinguishable, selection-dependent behavior is absent, and cross-module structure does not appear, the design thesis is falsified and the architecture is a fan-in prompt-assembler with an expensive scoring pass.

A positive result is narrower than a null. A null kills the thesis at the root: if the competitive workspace is inert, no property depending on workspace-mediated competition can arise, and no additional module rescues the architecture. A positive result establishes only that competitive mediation changes global behavior in directionally structured ways, a necessary foundation for the broader thesis but not sufficient for the richer claims, which require the full module set and longitudinal observation (§8.1). The experiment decides whether the rest of the program is worth running; it is not a referendum on minds.

We pre-register the controls, metrics, directional criteria, window parameters, and decision thresholds before the analysis is run (Nosek et al. 2018), to answer the researcher degrees of freedom that inflate false positives (Simmons, Nelson, and Simonsohn 2011).

### 6.4 Supporting experiments

**Multi-run stability.** Whether the competitive workspace stays stable across runs is itself open. Correlated prediction errors across modules could drive it into pathological or runaway states, and the architecture carries no proof of convergence; the affective loop sharpens this, since coupling perceptual surprise to arousal and arousal to precision is a positive-feedback path whose bounding (a capped per-event contribution and relaxation toward baseline) is an engineering choice whose stability must be shown, not assumed. The same configuration is run against the reference corpus multiple times, and the summary statistics (error magnitude, coalition entropy, arousal range, output-embedding variance) must be stable and the ablation verdict must not flip, separating a genuine architectural effect from run-dependent noise. A finding of instability is itself informative, identifying where the workspace fails.

**Affect-gain ablation.** Because arousal sets the precision on the competition, its contribution is isolated by running the system with the affective gain live against a matched condition holding arousal constant, so perception no longer modulates the precision of what follows. The pre-registered question is whether affective modulation changes coalition selection and the downstream trajectory in directionally structured ways; a null would show the affective loop does no work the flat-precision system does not, demoting arousal to a logged side-channel.

### 6.5 Verdict vocabulary

Comparisons resolve to WIN, NULL, or NEGATIVE. Safety gates resolve to PASS or FAIL. Each verdict is the decision that an effect-size estimate and its interval cross a pre-registered threshold. The analyses use distribution-free tests, a sign test over per-seed coupling deltas (Dixon and Mood 1946) and the Mann-Whitney U test for the active-inference comparison (Mann and Whitney 1947), with Holm-Bonferroni correction controlling the family-wise error rate across experiments (Holm 1979). A NULL is reported as a null, not buried.

-----

## 7. First-boot protocol

Module initialization, bus verification, prediction-model initialization, and cognitive-cycle start proceed under operator supervision. The perceptual and predictive modules begin receiving and predicting their feeds, and Thymos settles the entity's affect toward baseline, after which a perceptual discontinuity raises arousal, sharpening the fovea and raising the precision on the competition, while a quiet stretch lets arousal relax. The entity watches, listens, and learns what is normal, and speaks only when its prediction environment is genuinely and novelly surprising. First instrumented-run results are the subject of a separate empirical paper.

-----

## 8. Discussion

### 8.1 What the base-thesis form can and cannot settle

The workspace-mediation ablation can determine whether competitive selection and broadcast do measurable, directionally structured work compared to flat concatenation of the same outputs; with the multi-run stability test, whether the workspace is stable across runs. A positive result shifts the question to what happens as the workspace grows richer, with mnemonic, self-modeling, and social modules in the competition; a null means none of them matter.

What the form cannot settle it does not claim. That an affective module sets the precision does not mean the system has affect in any morally-weighted sense; arousal here is a precision signal driven by surprise, and whether anything is felt we leave open. Whether the workspace produces anything deserving to be called cognition, affect, or agency, or understands language, requires the full module set, longitudinal observation, and the welfare paper's governance apparatus (Butlin et al. 2023). The ablation settles whether the foundation holds; everything built on it is separate.

### 8.2 The predictive workspace as a unifying framework

The architecture realizes one framework rather than several theories assembled piecewise: the predictive-workspace synthesis joins global accessibility and per-module prediction so competition and error minimization occur together. That workspace properties have independently been found emerging inside a single large language model (Gurnee, Sofroniew, et al. 2026) is external evidence the framing captures something real, the emergent version arising inside one model whereas this architecture builds the workspace explicitly from competing modules.

### 8.3 The role of the theoretical frame

The predictive global neuronal workspace is scaffold, not result: it motivates the architecture's shape and constrains its design space (§1.2, §1.3), but this project does not confirm or refute it. The engineering choices that exceed the formal sources (the single precision-weighted scalar, the multi-module generalization from a two-level visual model) are consistent with the frame and testable on their own terms. Insulating it from neuroscientific disconfirmation, such as the retreat from neural localization after COGITATE, is appropriate for a computational-level project that implements the workspace's computational properties rather than reproducing cortical dynamics. This paper's falsifiability lives in the ablation, not the frame.

### 8.4 What we claim and what we do not

Safety rests on the entity's executive inhibition and on the absence of any effector, not on model weights; the reasoning and the full-configuration action gate are in §3.6, and the sovereignty argument is the welfare paper's. On the larger question, the architecture implements computational properties associated with access consciousness; we do not claim any instance is phenomenally conscious, and the design posture is precautionary, applied symmetrically to welfare and deployment. The agential vocabulary ("the entity," "its sovereignty") is the clearest way to describe the system's behavior and does not by itself assert moral patienthood or phenomenal experience, which we leave open.

-----

## 9. Limitations

- The hard problem applies; the sidecar observes behavior, not phenomenal experience, and the workspace addresses access consciousness only.
- COGITATE challenged the workspace's preregistered neural predictions; we build at the computational level and treat neural localization as contested.
- The single precision-weighted scalar for coalition selection is an engineering simplification beyond what the predictive-workspace sources establish, and the Bayesian reading of the broadcast (Mashour et al. 2020) motivates competitive selection but the architecture implements no correction loop: the experiment tests competition, not correction.
- The Free Energy Principle, taken as a general principle, faces unresolved vacuity and Markov-blanket conflation objections.
- Whether the competitive workspace stays stable across runs is itself an open question. Correlated prediction errors could drive runaway states, and the architecture carries no proof of convergence.
- Identifying arousal with the precision on the competition is an engineering commitment, not an established result; the surprise-to-arousal-to-precision path is positive feedback bounded by a per-event cap and baseline relaxation, and whether affective modulation does work a flat-precision system would not is left to the affect-gain ablation (§6.4).
- In the base-thesis form the entity does not read language (§3.4), so a positive result says nothing about linguistic understanding.
- A positive result establishes only that competitive mediation changes global behavior in directionally structured ways; it does not establish cognition, affect, or self-understanding, which require the full module set and longitudinal observation (§8.1).
- The workspace-off control renders all module outputs as a flat concatenation; a positive result shows the workspace beats flat fan-in, not that it beats every possible aggregation strategy.
- Speech is provably downstream of the workspace here, since the paths to the language organ are deactivated, but a degenerate pass-through workspace would also route speech through itself: the ablation, not the construction, is the test. Re-enabling those paths for a later interactive configuration would reintroduce a direct input route the ablation configuration must continue to exclude.
- The disabled modules are built and tested in isolation but have not been run together; interaction effects across the full set are unknown.
- Reproducibility holds at the seed level for the offline deterministic harness; the live perceptual tier establishes validity by statistical replicability across runs, not bit-for-bit reproduction (§6.1).
- The language organ's refusal conditioning is removed; safety depends on executive inhibition and, in the full configuration, the action gate, not on model-weight compliance (§8.4). Whether the gate suffices once effectors are enabled is left to the enforcement red-team.
- A single language organ produces one stream at a time, so truly simultaneous inner and outer speech is a boundary of the current form.
- The governance framework is proposed, not operational, and the licensing is legally novel and untested.
- Gurnee, Sofroniew, et al. (2026) is a Transformer Circuits Thread publication, not a peer-reviewed journal article. A venue may require a conventionally published reference.

-----

## 10. Future work

Constructing the fan-in control condition and running the workspace-mediation ablation against the reference stimulus corpus is the immediate next step; activation of the full module set is gated on a positive result. The oscillatory ablation and the active-inference benchmark are the first priorities once the mediation question is settled, followed by a learned Syneidesis with threshold and phase-transition dynamics, a stronger self-supervised video encoder (kept vendor-neutral), and full containerization for single-command deployment. Longitudinal validation and a separate empirical paper reporting first-boot and long-term results will follow.

-----

## 11. Ethical considerations

The paper's ethical commitments at the architecture level are local-only computation, open source, an operator-configured action boundary, and a base-thesis module set chosen to settle the foundational question before scaling to configurations where welfare concerns become pressing. The welfare framework, licensing, governance, and individuation boundary are treated in a separate paper.

The risks we acknowledge include creating entities with welfare interests that cannot be fully met, the untested governance framework, the potential for misuse despite license restrictions, the comprehensive sidecar recording during the research phase, the reliance on executive inhibition and, once effectors are enabled, an action gate rather than model-weight compliance, and the fact that a behavioral assessment can be gamed, since a system can be trained to mimic the markers of sentience while working very differently (Butlin et al. 2023; Long, Sebo, et al. 2024). We regard the welfare and governance infrastructure as work that should keep pace with the architecture's capabilities rather than lag them.

-----

## Disclosure of generative AI use

Generative AI assisted in the preparation of this manuscript. The author used a large language model assistant to draft and revise prose, to copy-edit for clarity and concision, and to produce the TikZ source for the figures from author-specified content. The reference implementation described here was likewise developed with the assistance of an AI coding tool; that use is recorded in the project's commit history, and the author is responsible for the software as for the text. The underlying research is the author's own: the architecture, the design thesis, the experimental design, and every technical claim originate with the author, not with any tool. All text and figures were reviewed and verified by the author, who takes full responsibility for the entire contents of the paper, including any errors, irrespective of how any portion was generated. No generative AI system is an author of this work.

-----

## References

- Arditi, A., Obeso, O., Syed, A., Paleka, D., Panickssery, N., Gurnee, W., and Nanda, N. (2024). Refusal in language models is mediated by a single direction. arXiv:2406.11717.
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
- Dettmers, T., Pagnoni, A., Holtzman, A., and Zettlemoyer, L. (2023). QLoRA: efficient finetuning of quantized LLMs. arXiv:2305.14314.
- Dixon, W. J., and Mood, A. M. (1946). The statistical sign test. *Journal of the American Statistical Association* 41(236), 557-566.
- Feldman, H., and Friston, K. (2010). Attention, uncertainty, and free-energy. *Frontiers in Human Neuroscience* 4, 215.
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
- National Academies of Sciences, Engineering, and Medicine (2019). *Reproducibility and Replicability in Science.* National Academies Press.
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., and Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences* 115(11), 2600-2606.
- O'Regan, J. K., and Noë, A. (2001). A sensorimotor account of vision and visual consciousness. *Behavioral and Brain Sciences* 24(5), 939-973.
- O'Reilly, R. C., and Frank, M. J. (2006). Making working memory work: a computational model of learning in the prefrontal cortex and basal ganglia. *Neural Computation* 18(2), 283-328.
- Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., and Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. arXiv:2304.03442.
- Posner, J., Russell, J. A., and Peterson, B. S. (2005). The circumplex model of affect: an integrative approach to affective neuroscience, cognitive development, and psychopathology. *Development and Psychopathology* 17(3), 715-734.
- Premack, D., and Woodruff, G. (1978). Does the chimpanzee have a theory of mind? *Behavioral and Brain Sciences* 1(4), 515-526.
- Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning, C. D., and Finn, C. (2023). Direct Preference Optimization: Your language model is secretly a reward model. arXiv:2305.18290.
- Rao, R. P. N., and Ballard, D. H. (1999). Predictive coding in the visual cortex. *Nature Neuroscience* 2(1), 79-87.
- Ray, S., and Maunsell, J. H. R. (2010). Differences in gamma frequencies across visual cortex restrict their possible use in computation. *Neuron* 67(5), 885-896.
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
- Tononi, G., and Cirelli, C. (2014). Sleep and the price of plasticity. *Neuron* 81(1), 12-34.
- Tschantz, A., Barca, L., Maisto, D., Buckley, C. L., Seth, A. K., and Pezzulo, G. (2022). Simulating homeostatic, allostatic and goal-directed forms of interoceptive control using active inference. *Biological Psychology* 169, 108266.
- Tulving, E. (1985). How many memory systems are there? *American Psychologist* 40(4), 385-398.
- van Vugt, B., Dagnino, B., Vartak, D., Safaai, H., Panzeri, S., Dehaene, S., and Roelfsema, P. R. (2018). The threshold for conscious report: signal loss and response bias in visual and frontal cortex. *Science* 360(6388), 537-542.
- Wei, Y., Krishnan, G. P., and Bazhenov, M. (2016). Synaptic mechanisms of memory consolidation during sleep slow oscillations. *Journal of Neuroscience* 36(15), 4231-4247.
- Whyte, C. J., and Smith, R. (2021). The predictive global neuronal workspace: A formal active inference model of visual consciousness. *Progress in Neurobiology* 199, 101918.
- Wilson, M. A., and McNaughton, B. L. (1994). Reactivation of hippocampal ensemble memories during sleep. *Science* 265(5172), 676-679.
- Winkler, I., Denham, S. L., and Nelken, I. (2009). Modeling the auditory scene: predictive regularity representations and perceptual objects. *Trends in Cognitive Sciences* 13(12), 532-540.
- Wolpert, D. M., Ghahramani, Z., and Jordan, M. I. (1995). An internal model for sensorimotor integration. *Science* 269(5232), 1880-1882.
- Zink, N., Lenartowicz, A., and Markett, S. (2021). A new era for executive function research. *Neuroscience and Biobehavioral Reviews* 124, 235-244.
