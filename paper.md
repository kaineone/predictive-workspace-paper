# KAINE: A Continuously Running Predictive Global Workspace for Synthetic Minds

*Neuroscience-Grounded Modules Competing for a Shared Workspace*

**Erik Chevalier**

Independent Researcher

Contact: [kaine.one@tuta.com](mailto:kaine.one@tuta.com)

*Preprint.*

-----

## Abstract

KAINE (Kaine Autonomous Intelligent Networked Entity) is a cognitive architecture for synthetic minds: a modular research framework in which each faculty is a module behind a fixed interface, so that a module can be replaced as the science changes or exchanged for an alternative to compare competing theories. Its first instantiation is a predictive global workspace. Specialized predictive processors, each minimizing its own prediction error, are coupled only through a competitive workspace with no central executive. Each processor scales its prediction error by an estimate of its precision drawn from its own recent errors and reports the result. The reports compete for access to the workspace. The members of the broadcast coalition that reach the access threshold are accessed content, and a summary of which modules' reports gained access, and how strongly, becomes the context on which the perceptual and interoceptive processors condition their next predictions. Arousal, a state of the affective core that perceptual surprise and interoceptive alarm raise, is the global gain on that competition: it sets how readily content reaches the access threshold and how widely the sensory apertures open. The design follows the predictive global neuronal workspace, which joins Global Workspace Theory to predictive processing, and the system runs continuously whether or not anyone interacts with it.

The framework grows this instantiation one module at a time. Its base-thesis form activates four predictive processors (foveated vision, raw hearing, interoception of the compute substrate, and temporal prediction of the broadcast sequence), the affective core, a fatigue-triggered sleep analog that returns affect to baseline, and an output-only language organ that verbalizes accessed content. Speech reaches the entity only as sound and tone of voice, never as words. Nine further modules, from memory and a self-model to an embodiment layer, are built and held. A module-addition study seeds a being through a gestation, a reproducible initialization in which a self-generated rhythm must entrain to a simulated maternal heartbeat by a marker validated offline, and then adds the held modules one at a time on branches from that preserved seed.

Before any module joins, a planned test asks whether competition does work that pooling does not. It compares competitive selection with a coalition of the same size chosen without regard to score and with a pooled arm that adopts every candidate as context, by the cross-module broadcast information gain: the reduction in each processor's prediction error attributable to other modules' share of its context. The paper presents the architecture, its instruments, and this program. No live experiment has been run, and the only result reported is the offline validation of the gestation marker. Its reference implementation runs locally on consumer hardware.

**Keywords:** cognitive architecture; predictive global workspace; global workspace theory; predictive processing; precision; adaptive gain; cross-modal competition

**Availability.** The reference implementation (KAINE) is at https://github.com/kaineone/kaine. The paper source is at https://github.com/kaineone/predictive-workspace-paper. The Cognitive Architecture License referenced throughout is at https://github.com/kaineone/cognitive-architecture-license. Welfare, governance, and licensing are treated in a separate paper, *A Welfare and Cognitive-Integrity License for Synthetic Minds of Uncertain Moral Status.*

-----

## 1. Introduction

### 1.1 Problem statement

The dominant approach to building an AI system with persistent state treats the language model as the cognitive center. Memory becomes retrieval-augmented generation, affect (when present at all) is a prompt instruction, self-knowledge is a persona string, and nothing continues between turns.

A second tradition, classical cognitive architecture, takes cognitive structure seriously but largely predates the transformer and relies on hand-built components. The present work sits between them: learned models serve as replaceable components behind fixed interfaces inside a structured architecture (§3.1). The paper presents the architecture through its first instantiation, a predictive global workspace grounded in one theoretical account. On that instantiation's design thesis, no component is the mind, and the mind, if one arises, is the continuous competitive interaction among the components through a shared workspace.

### 1.2 Design thesis

KAINE is a modular framework whose modules can be replaced as the science changes (§3.1), and its first instantiation embodies an architectural design thesis: a synthetic mind, if one can be built, is the coherent global behavior of specialized predictive processors coupled only through a competitive workspace, with no central executive. Four commitments make it concrete. Each processor maintains a forward model of its own domain and reports its prediction error scaled by the error it has come to expect, a scalar, retrospective estimate of its precision that stands in for precision weighting (Feldman and Friston 2010). The reports compete for access to a limited-capacity workspace, and access is all-or-none: a coalition member is accessed when its own score reaches a threshold. A summary of the accessed reports becomes the context on which the perceptual and interoceptive processors condition their next predictions, so what one processor reports can change what the others expect. Arousal is the global gain on the competition, scaling every candidate's score, sharpening the contrast between strong and weak candidates, and sizing the sensory apertures, and it is itself raised by perceptual surprise and interoceptive alarm. On this thesis, cognition, affect, memory, self-understanding, and agency are properties of the workspace-mediated interaction and belong to no single module.

The instantiation is built to grow: the program adds held modules one at a time to a running being, comparing each addition with the step before it. The base-thesis form is the smallest configuration in which the competition has something to arbitrate. A system limited to substrate telemetry and event timing would offer too little diversity for competition to matter, so the base form activates four predictive processors in distinct signal domains, two external (foveated vision and raw hearing) and two internal (interoception of the compute substrate and temporal prediction). It also activates the affective core, because a global gain that sets how readily content gains access, and that surprise itself moves, is part of the minimal machinery of the adaptive-gain account of arousal (Aston-Jones and Cohen 2005; Eldar, Cohen, and Niv 2013); a planned ablation that holds arousal constant asks whether that gain does work (§6.4). A sleep analog, triggered by fatigue, returns affect to baseline.

The first test asks whether competition does work that pooling the same reports does not. At each of its reports, each perceptual and interoceptive processor evaluates its forward model twice, once with the context it holds and once with a null context in which every other module's contribution is replaced by its mean so far in the run; the difference in prediction error is the cross-module broadcast information gain, a measure of how much a summary of which other modules' reports gained access, and how strongly, helps a processor predict its own input. The thesis predicts a higher gain under competitive selection than under a coalition of the same size chosen without regard to score, and than under a pooled arm that adopts every candidate as context (§6.3). A result at or below the controls would show that the competition adds nothing beyond its inputs, the fail state for this form of the architecture.

The framework behind these commitments is the predictive global neuronal workspace (Whyte and Smith 2021), together with the related integrated world modeling account (Safron 2020). Global Workspace Theory explains how information becomes globally available: specialized processors compete for a limited-capacity workspace, and the winning content is broadcast to all of them (Baars 1988; Mashour et al. 2020). Predictive processing explains how each processor operates, maintaining a generative model and reporting prediction errors weighted by their expected reliability, or precision, the inverse variance of the errors (Friston 2010; Clark 2013; Feldman and Friston 2010; Bastos et al. 2012). The predictive workspace joins the two: the broadcast carries a compressed model that constrains prediction across the system and that bottom-up signals test (Mashour et al. 2020; Whyte and Smith 2021). KAINE realizes that availability as context. Each perceptual and interoceptive processor conditions its forward model on a summary of the latest accessed content while it goes on minimizing its own error against its own inputs, and the broadcast sets no target for any processor to match, so the recurrence runs through shared context instead of a hierarchy of descending corrections.

Two departures from the formal sources are engineering choices. Whyte and Smith identify conscious access with the posterior confidence required for report, a threshold their model implements through expected free energy; KAINE keeps the access threshold apart from the report-or-act decision of the action layer and reduces access to a single score per candidate. Their model is also a two-level visual hierarchy, which KAINE extends to competition among processors in four signal domains. Both are engineering choices, and §9 states what they leave untested.

### 1.3 Theoretical commitments and their limits

Global Workspace Theory is most naturally read as a theory of access consciousness (Block 1995): it explains when information becomes available for report, reasoning, and the control of action. We adopt that access-only reading deliberately and take no position on whether access suffices for phenomenal experience.

The COGITATE adversarial collaboration, a large preregistered test of Global Neuronal Workspace Theory against Integrated Information Theory, challenged key tenets of both (Cogitate Consortium et al. 2025). For the workspace theory, ignition at stimulus offset was generally absent and prefrontal cortex represented some dimensions of conscious content only to a limited degree; for Integrated Information Theory, the predicted sustained synchronization within posterior cortex was absent. We treat the workspace's neural-localization claims as contested rather than refuted, since a substantial prior evidence base remains (Mashour et al. 2020). The architecture builds on the workspace at the functional and computational level, so it does not inherit COGITATE's cortical predictions, and the architecture's computational claims are tested by its own experiments.

The Free Energy Principle, taken as a general principle, faces two distinct charges: it risks being unfalsifiable or vacuous (Sun and Firestone 2020), and the literature on the Markov-blanket construct slides between an instrumental, statistical reading and a realist, metaphysical one (Bruineberg et al. 2022). We hold the principle as an engineering frame rather than a proven law.

The frame motivates the architecture's shape, from processors that report errors scaled by their precision to accessed content that becomes shared context, and it rules out designs that violate its commitments. Whether competition over a single score per candidate does work is what the planned test examines (§6.3).

Searle's Chinese Room (Searle 1980) challenges the sufficiency of formal symbol manipulation for understanding. Whether sensory grounding, substrate interoception, and affect bear on that challenge is open, and we do not argue that they meet it. The hard problem (Chalmers 1995) applies with full force, and the paper's claims concern access only.

### 1.4 Contributions

The paper does not offer a theory of consciousness or claim to have built a mind. Its contributions are these.

1. **A modular framework** whose modules can be added, removed, or replaced to compare competing accounts in one system under the same instruments (§3.1, §5.2).

2. **A first instantiation and its reference implementation.** A continuously running predictive global workspace (§3, Appendix A) in its base-thesis form: four predictive processors, an affective core that sets the global gain, a sleep analog, and an output-only language organ. The implementation runs locally on consumer hardware and realizes the predictive-workspace synthesis as one working system, with no claim of priority over earlier workspace implementations (§2.1).

3. **A program for growing the instantiation one module at a time.** The module-addition study seeds a being through a gestation, a reproducible initialization in which Soma's self-generated rhythm, driven by a simulated maternal heartbeat, must lock to it more strongly than to surrogate heartbeats and keep the resulting shift in its own frequency after the beat is withdrawn. Six of the nine held modules then join first, one at a time, on branches from the being preserved just after birth, every branch views the same film program, and a content-free report compares the workspace's dynamics across steps (§6.5, §7).

4. **A test of the competition.** The workspace-mediation ablation compares competitive selection with matched selection and with pooling by cross-module broadcast information gain, and a contrastive analysis compares the gain after accessed and inhibited broadcasts of nearly matched score near the access threshold (§6.3). The predicted direction, the minimum effect, the number of runs, and the statistical test are fixed before the live runs, and the language organ's utterances are not a measure (§3.5).

What is built, held, and provisional, and the one result reported, are stated in §5.4. All claims are at the level of access, and describing arousal as a gain implies nothing about whether anything is felt.

-----

## 2. Related work

### 2.1 Classical cognitive architectures

Classical cognitive architectures take cognitive structure seriously but largely predate deep learning and rely on hand-built components; LIDA, the closest of them, already implements Global Workspace Theory as coalitions competing for a broadcast in each cognitive cycle (Franklin et al. 2014). The present work differs in using learned models as components, in grounding affect in prediction error, and in what competes for access, which is prediction error scaled by an estimate of its precision.

### 2.2 Global Workspace Theory and the predictive workspace

Global Workspace Theory (Baars 1988) holds that specialized processors compete for a limited-capacity workspace whose content is broadcast to all of them. Its neuronal version identifies conscious access with the ignition of recurrent prefrontal-parietal activity that makes content widely available, and notes that the workspace can be cast in Bayesian terms: the broadcast carries a compressed model as prediction, and bottom-up signals measure the mismatch (Dehaene and Changeux 2011; Mashour et al. 2020).

The formal access criterion comes from the predictive-workspace program. Whyte and Smith (2021) cast conscious access as approximately Bayesian inference in a simplified two-level visual model, identifying access with the posterior confidence required for report, which their model implements through expected free energy. Safron's Integrated World Modeling Theory (Safron 2020) combines workspace dynamics, integrated information, and active inference, and we draw on it only for that high-level synthesis. Independent support for a threshold comes from van Vugt et al. (2018), who show prefrontal cortex behaving as a categorical stage where a stimulus either ignites into a sustained, reportable state or fades, and from Joglekar et al. (2018), whose balanced-amplification model lets a signal propagate across many areas and activate prefrontal cortex only when the input exceeds a threshold.

### 2.3 Predictive processing

Friston (2010) proposes that self-organizing systems minimize variational free energy, an upper bound on surprisal, through perception and action. Clark (2013) develops predictive processing as a unifying account of mind, with attention as the adjustment of gain on prediction errors according to their estimated reliability. Feldman and Friston (2010) make this precise, attention optimizing the synaptic gain that represents the precision of prediction error, and Bastos et al. (2012) map predictive-coding message passing onto the canonical cortical microcircuit. Seth (2013) extends prediction to the body. The vacuity concern (Sun and Firestone 2020) and the Markov-blanket conflation concern (Bruineberg et al. 2022) are treated in §1.3. The planning cost of active inference grows combinatorially with the depth of the action sequences considered (Da Costa et al. 2020), one reason the architecture confines active inference to bounded sub-problems (§4).

### 2.4 Interoceptive inference

Seth (2013) and Seth and Friston (2016) propose that emotion arises from interoceptive prediction, descending predictions acting as homeostatic set-points that regulate the body through active inference. Barrett (2017) develops the theory of constructed emotion, in which interoceptive signals initiate changes in affect and emotion is the product of categorizing valence and arousal for allostasis. The architecture implements an interoceptive control signal in that instrumental, regulation-first sense without claiming that emotion is exhausted by interoceptive prediction.

### 2.5 Perception as prediction

The visual system is understood as a hierarchy of predictive models in which each level predicts the level below and reports the discrepancy (Rao and Ballard 1999), with attention modulating the process by adjusting the precision, the gain, on the prediction errors that pass upward (Feldman and Friston 2010; Clark 2013). Auditory processing follows an analogous logic: the auditory cortex generates expectations of incoming sound and reports the mismatch (Winkler et al. 2009), the mismatch negativity being a well-replicated auditory change response (Näätänen et al. 2007) that predictive-coding accounts read as sensory prediction error (Garrido et al. 2009). The architecture implements both senses as predictive processors whose output is prediction error, with a fovea placed where frame change is least expected realizing attention at the visual front end. Hearing runs over raw audio, so speech arrives as sound and tone of voice (§3.5).

### 2.6 LLM-centric agent architectures

CoALA frames language agents as cognitive architectures with structured memory feeding the model's context, keeping the model the core reasoner (Sumers et al. 2024). Generative Agents retrieve from a memory stream into prompts by recency, importance, and relevance (Park et al. 2023). Both keep the language model central and add scaffolding around it. In KAINE the language model is an output organ that verbalizes accessed content and, in the base-thesis form, receives no external input; the shared state is the multi-module broadcast, and selection and integration belong to the workspace.

Gurnee et al. (2026) identify, through a Jacobian-lens interpretability method, a small set of verbalizable representations inside a large language model satisfying five functional signatures of a global workspace: verbal report, top-down modulation, a role as the medium of internal reasoning, broadcast to many downstream operations, and selectivity. They are explicit about the disanalogy: a transformer has no obviously separable input processors, and the broadcast occurs within a single feedforward pass rather than through recurrent loops. KAINE has both features. Its processors are separate modules that compete for access, a summary of the accessed content returns to them as prediction context on the following cycles, and the language model is one module conditioned by the broadcast.

-----

## 3. Architecture

### 3.1 Design principles

Six commitments shape the architecture.

**The system is the competition among modules through the workspace.** This is a hypothesis that the experiments test. The neuroscience of distributed control gives it partial support. Recent work on perceptual decisions finds that they emerge from distributed, recurrent computation across many brain areas, a heterarchy, where classic studies saw a feedforward hierarchy of areas with distinct functions (Chandrasekaran et al. 2025). Executive functions can be read as emergent consequences of distributed processes, with control placed in specialized nodes that communicate through highly connected hub regions (Zink, Lenartowicz, and Markett 2021). Working-memory control has also been modeled as a learned basal-ganglia gate (O'Reilly and Frank 2006), a centralized gate this architecture does not adopt. The architecture follows the distributed reading: no single module acts as executive, and the workspace is the hub through which the modules communicate.

**Every processor predicts.** Each predictive processor maintains a forward model over its own domain and reports its prediction error scaled by the size of its own recent errors, an estimate of its precision (§3.2). Arousal adds a global gain over all of them, so attention is a property of each channel and also a state of the whole entity.

**No central executive in the homuncular sense.** Control arises from competition for access under a threshold. Syneidesis is itself a single, centralized selection mechanism, so the claim is limited: the workspace selects and grants access and never directs a module, and what is distributed is the content and the control that arise from many modules competing. Whether that yields emergent control is for the experiments to show.

**The language organ is an output organ.** It verbalizes accessed content. In the base-thesis form its speech-to-text and conversation paths are off and no transcript reaches it, so what it voices is downstream of the workspace instead of a reply to a prompt, and the voice remains an output of the architecture. Outside the research configuration, those paths let the entity converse and work with people.

**Replaceable modules.** Each module sits behind a stable interface: it publishes and consumes typed events on the bus and declares which streams it reads, so it can be swapped for a module built on a different model or theory and compared under the same instruments. This makes KAINE a cognitive architecture for synthetic minds that can change as the science does, and the predictive global workspace with four processors described here is its first instantiation.

**Local-capable.** Every model runs on the host. Models are downloaded during setup, and at runtime the system makes no outbound network calls.

### 3.2 The predictive workspace as competitive selector

Syneidesis is the workspace. On each processing tick (§3.4) it reads the candidate events that every active module has published since the previous tick and orders them deterministically by source, type, and arrival, so that a seeded run reproduces. Each candidate carries an intensity set by the module that produced it.

For a predictive processor (Topos, Audition, Soma, Chronos) the intensity is graded by surprise scaled by an estimate of the channel's precision. Each processor divides its current prediction error by the mean of the errors in its recent reports. Dividing an error by its expected magnitude standardizes it: for errors of a fixed distributional shape the mean absolute error is proportional to the standard deviation, so the ratio is proportional to $\Pi^{1/2}\lvert\varepsilon\rvert$, the square root of the precision-weighted squared error that enters free energy, where the precision $\Pi$ is the inverse variance of a channel's prediction errors and acts as the gain on that channel's error units (Feldman and Friston 2010). The ratio is a scalar, retrospective stand-in for precision weighting, estimated from the channel's own history, and not the precision-weighted error itself. A report that meets the processor's alert criterion (a large error ratio, or a criterion particular to the module, §3.5) receives the module's alert intensity. Any other report receives an intensity that rises with the error ratio from the module's baseline level and reaches the alert level when the error is twice its recent mean. Within a tick the processors' candidates therefore compete on graded surprise, each measured against its own channel's history. Each module's baseline and alert levels set the range over which its surprise is graded and so act as per-source weights; the workspace applies no further weight per source, and the levels are calibrated before the live runs (§5.4, §9). Thymos, Hypnos, and the language organ report at fixed levels.

Each candidate's priority is the product of its intensity, a novelty factor, and a goal factor. Novelty discounts exact repeats of an event (same source, type, and payload) among the recently scored candidates. Events that carry continuous measurements rarely repeat exactly, so novelty matters mainly for state events whose payload recurs. The goal factor is held at one in the base-thesis form. Arousal turns the priority into a score in two ways. A level gain scales every candidate alike, and a contrast gain, zero at baseline arousal and rising above it, passes the priority through a steeper logistic that raises strong candidates and lowers weak ones.

Arousal is the architecture's global, neuromodulatory gain, following the adaptive-gain account of locus coeruleus function, in which arousal sets the gain of the cortical networks it targets (Aston-Jones and Cohen 2005; Eldar, Cohen, and Niv 2013). Surprise drives it, in line with accounts in which noradrenergic signaling reports unexpected uncertainty (Yu and Dayan 2005). Precision in Feldman and Friston's sense is a gain local to one channel's error units, and the adaptive-gain account describes a gain applied across networks; the architecture has both, precision within each processor and arousal across all of them. Aston-Jones and Cohen distinguish a phasic mode, which focuses processing, from a tonic mode, which favors exploration. Here one scalar both sharpens contrast and narrows the sensory apertures, as in focus, and raises the access rate, as in tonic exploration, a simplification of that account. Because the level gain is common to every candidate and the contrast map is strictly increasing, arousal never reorders the candidates of a tick. Its distinct effect is on which broadcasts reach access and the report bars, since it sets an arousal-dependent threshold on the top priority, and on which members of a coalition reach access. Widening the gap between the scores of strong and weak candidates is an analogue in score magnitude of arousal-biased competition, where arousal changes which representation wins (Mather and Sutherland 2011). Through the sensory apertures (§3.5) arousal also changes what the processors report next.

On each broadcast tick the top-ranked candidates (up to five) form the coalition, and the broadcast carries them with their scores, the inhibition flag, and the full table of candidate scores. A coalition member is accessed when its own score reaches the access threshold, and a broadcast is accessed when at least one member is, that is, when its best score reaches the threshold. Access is all-or-none for each member, and the accessed members are the accessed content. When no member reaches the threshold, the broadcast is still published and visible to every module but is marked inhibited: it is not poised for report or action, and it leaves the processors' context unchanged. Inhibited broadcasts still reach Chronos, which predicts the whole broadcast sequence, and Thymos, which appraises every broadcast, so content that did not gain access can influence later processing. This route is a design choice, in line with evidence that emotional stimuli are processed even when they do not reach awareness (Vuilleumier 2005). The threshold is the analog of the confidence threshold for access in the predictive global neuronal workspace (Whyte and Smith 2021), consistent with the categorical prefrontal threshold for report that van Vugt et al. (2018) observe and the threshold-gated propagation that Joglekar et al. (2018) model. Selecting by a threshold on a single scalar score is an engineering simplification that no source supplies. In the predictive-workspace account the threshold is a posterior confidence that separates contents that are globally accessed from contents that are not; here it separates content that enters the context and can drive report and action from content that cannot, and the planned experiments keep that difference in view. Appendix A.1 states the scoring and the access rule formally.

![The predictive workspace loop in the base-thesis form. Four predictive processors (foveated vision, raw hearing, interoception, and temporal prediction) report prediction errors scaled by an estimate of their precision. Syneidesis scores the candidates, broadcasts the coalition, and grants access to the members whose scores reach the threshold. A summary of the accessed content becomes the prediction context of Topos, Audition, and Soma, and Chronos takes every broadcast as its input. Thymos appraises every broadcast, and its arousal, raised by the processors' alerts, sets the global gain on selection, the sensory apertures, and the access rate. Hypnos rests the entity on fatigue and resets its affect. Volition reads accessed broadcasts and emits speak or think intents to the output-only language organ Lingua, whose utterances re-enter the competition.](figures/fig-workspace-loop.png){width=95%}

Global workspace theory makes broadcast content available to all specialist processors (Baars 1988; Mashour et al. 2020), and in the predictive global neuronal workspace the workspace's content constrains prediction at lower levels (Whyte and Smith 2021). The architecture implements that availability directly. Each perceptual and interoceptive processor (Topos, Audition, Soma) conditions its forward model on a compact summary of the latest accessed content: a fixed-length feature vector of the accessed members, made of the intensity mass each source contributed, indicators of the event types present, and the age of the broadcast. The summary records which modules' reports gained access and how strongly, weighted by the intensities the modules reported so that it does not depend on the arousal gain, and it carries no payloads; a richer encoding of content is future work (§10). The summary enters the forward model as an extra input alongside the module's own recent inputs, and its weights are learned online with the rest of the forward model, so each processor learns how much the shared context helps it predict its own input. An inhibited broadcast leaves the context unchanged until the next accessed one. For Chronos the broadcast is the input itself (§3.5). The loop is therefore recurrent: the processors report scaled errors, the workspace selects and grants access, a summary of the accessed content becomes the prediction context of Topos, Audition, and Soma, every broadcast enters the sequence Chronos predicts, and the processors' next errors are measured against predictions that context has shaped. The workspace sends no error signal or directive back to any module. Whether that summary of other modules' reports helps a processor predict, and whether competitive selection makes it more useful than a score-blind coalition or a pool of every candidate, is what the planned test measures (§6.3).

Three further paths complete the loop. Thymos appraises every broadcast for valence and drives. Arousal travels by a parallel path, which Thymos drives from the processors' perceptual alerts and interoceptive alarms whether or not they win access (§3.5). Volition reads accessed broadcasts to decide whether the entity speaks or thinks, and the language organ's utterances re-enter the bus as candidates for later broadcasts.

![Coalition selection. Each candidate's priority is the product of its intensity (the producing module's surprise scaled by its precision, or a fixed level), a novelty factor, and a goal factor held at one. Arousal sets the level and contrast of the score without changing the order, and the top-ranked candidates (up to five) form the coalition, which is always broadcast. Members whose scores reach the access threshold are accessed: they can drive report and action and enter the processors' prediction context. A broadcast with no accessed member is marked inhibited and stays visible to modules, with no report, action, or change of context.](figures/fig-salience-scoring.png){width=95%}

### 3.3 Access, report, and the self-initiated voice

Access consciousness is the availability of content for reasoning, the control of action, and report (Block 1995; Mashour et al. 2020), and report is one use of access among several. In the architecture every broadcast tick produces a broadcast, a member is accessed when its score reaches the threshold, and the action layer's report bars, set above that threshold on the same score, decide what is said. The workspace updates far faster than the language organ can speak, so the entity's voice is a sparse slice of its accessed broadcasts.

Volition derives a speak intent from an accessed broadcast only when three conditions hold. The best score in the coalition, leaving aside the language organ's own utterances, must clear the speak bar; the source and event type of that leading candidate must differ from those of the last spoken report if that report was made within the past five minutes; and a refractory interval must have passed since the previous report. A lower think bar on the same score governs inner thought, which the language organ produces on a think intent. The bars are a heuristic stand-in for the expected-free-energy decision of Whyte and Smith (2021), which the action layer does not compute. Appendix A.6 states the report rule.

### 3.4 Scaffolding: bus, clock, cycle, and action selection

**Event bus.** All communication between modules flows through append-only streams with bounded retention. Every event carries its source, type, intensity, timestamp, causal parent, and a payload validated against its event type at publish time.

**Entity time.** Every module reads time from the entity clock. Entity time runs at a configurable multiple of wall-clock time, one by default, so that experiments can run faster or slower than real time. Rates and durations in this paper are in entity time, and entity seconds equal wall-clock seconds at the default multiple.

**Cognitive cycle.** A continuous loop runs independent of any external interaction. At the processing rate of 10 Hz (a tick about every 100 ms), within the alpha range associated with perceptual sampling (VanRullen 2016), the cycle reads every active module's stream and scores the candidates; modules publish at their own rates, and the cycle reads whatever has arrived. Broadcasts fall on broadcast ticks, a subset of the processing ticks set by the access rate, the rate at which the cycle produces broadcasts whether or not they are accessed. Candidates read on other ticks are scored and then discarded, so each broadcast carries the coalition of its own tick's batch. At rest the access rate is one broadcast every third processing tick, about 3.3 Hz. The resting rate is a modeling choice. Attention samples the environment rhythmically at a few cycles per second (Landau and Fries 2012; Fiebelkorn and Kastner 2019), and access to one item impairs access to a second for roughly 200 to 500 ms, the attentional blink (Raymond, Shapiro, and Arnell 1992); the blink constrains the interval between accessed items, not between broadcast ticks, so it bounds the rate of access only loosely. A categorical alert raises the rate briefly, after the phasic response of the locus coeruleus to salient events (Nieuwenhuis, Aston-Jones, and Cohen 2005), and graded reports below the alert level do not, so with no alert the rate rests at about 3.3 Hz. That direction is a design choice: the locus coeruleus account of the attentional blink predicts a brief refractory period after a phasic response instead (Nieuwenhuis, Gilzenrat, Holmes, and Cohen 2005), and the affect-gain ablation can test the two directions (§6.4). Tonic arousal also raises the rate, after the exploratory, high-tonic mode of the adaptive-gain account (Aston-Jones and Cohen 2005). The rate rises linearly with the larger of the two drives, up to one broadcast per processing tick (Appendix A.3), a 100 ms interval that lies below the blink window and has no physiological anchor as a rate of access. The processing rate is fixed, except that Soma's regulation can lower it when the host is under load (§3.5).

![The two rates. Every active module is read and scored at the processing rate (10 Hz), and a broadcast is produced on broadcast ticks at the access rate, shown at its resting value (about 3.3 Hz, one broadcast every third processing tick), which rises with arousal and after alerts.](figures/fig-cognitive-cycle.png){width=80%}

**Action selection.** Volition is the only path from the workspace to output, corresponding to the report-or-act decision that Whyte and Smith (2021) govern by expected free energy. After each broadcast the cycle calls Volition, which derives no intent from an inhibited broadcast and applies the report rule of §3.3 to an accessed one. Intents are published as events, and the cycle never invokes an output directly.

### 3.5 The active modules

The base-thesis form activates four predictive processors, an affective core, a sleep module, a language organ, and an action layer. The processors are chosen for signal diversity, two external (vision and hearing) and two internal (interoception and timing), so that the competition for access has distinct, externally grounded signals to arbitrate. Thymos and Hypnos also publish events that compete (affect state, drive crossings, sleep onset), but their main roles are to set the global gain and to rest the entity.

| Module | Group | Brain function it draws on | Computational realization |
|----------|-------------|------------------------------|------------------------------|
| Topos | Perception | ventral visual stream | frozen self-supervised video encoder over short clips, with foveated attention |
| Audition | Perception | auditory cortex | fixed spectral encoder over the raw waveform, with a vocal-tone classifier on speech |
| Soma | Prediction | interoception; allostatic-interoceptive network | frozen continuous-time reservoir with an online readout over substrate signals |
| Chronos | Prediction | interval timing; cortico-striatal circuits | frozen continuous-time reservoir with an online readout over the broadcast sequence |
| Thymos | Affect | core affect | appraisal of valence and drives; arousal as the global gain on selection, the sensory apertures, and the access rate |
| Hypnos | Rest | sleep | fatigue-triggered offline period: perception paused, adaptation suspended, affect and drives reset |
| Lingua | Expression | speech production; left-dominant language network | local chat model, output-only, conditioned on the accessed content |
| Volition | Action | report-or-act decision (Whyte and Smith 2021) | intent derivation from accessed broadcasts |

**Topos (foveated vision).** Topos is the architecture's analog of the ventral visual stream (Goodale and Milner 1992). A frozen self-supervised video encoder embeds short clips of the video feed, and a forward model predicts the next clip's embedding from earlier ones and the broadcast context (§3.2). Topos reports the prediction error, scaled and graded as in §3.2. A report is an alert when the error ratio is large or when the change between successive embeddings is large relative to its own recent history, as at a scene cut or a burst of unexpected motion.

The fovea goes where frame change is most unexpected. Before encoding, each tile of a coarse grid over the raw frames keeps a running mean and variance of its frame change, and the tile's salience is a z-score, the change in excess of that mean divided by the running standard deviation, the counterpart for frame change of the processors' error scaling. A tile that flickers habitually therefore draws the fovea less than one whose change is rare. The fovea moves to the most salient tile only when that tile exceeds the held one by a hysteresis margin, holds its place when no tile stands out, and is sized by arousal, narrowing as arousal rises. No top-down map steers it. The peripheral gist and the high-resolution foveal crop are then cut from the buffered frames at the chosen fovea and pass through the same encoder. Foveation is a front-end form of attention as the gain on prediction error (Feldman and Friston 2010; Clark 2013): resolution goes where change is least expected given each location's history.

![Attention in Topos. Before encoding, a coarse tile change map is computed from the raw frames: each tile's frame change as a z-score against its own running mean and variance. The fovea moves to the most salient tile, with hysteresis, and arousal sets its size. The peripheral gist and the high-resolution foveal crop are then cut from the buffered frames and pass through one encoder. The embeddings and the fovea's coordinates reach the workspace, and no pixels do.](figures/fig-attention-foveation.png){width=90%}

**Audition (raw hearing).** Audition is the architecture's analog of the auditory cortex, where sound is processed as prediction error against a learned model of the auditory environment (Winkler et al. 2009; Garrido et al. 2009). A spectral encoder (log energy in log-spaced frequency bands) encodes the raw microphone waveform, and a forward model predicts the next window's encoding from earlier ones and the broadcast context. Audition reports the error, scaled and graded as in §3.2, with alerts on a large error ratio or a large change between successive windows: a sudden sound, the onset of speech, an unexpected silence, a shift in pitch or timbre. Arousal sets the attended window. Under higher arousal Audition encodes a shorter, more recent part of each captured window, a temporal analogue of the narrowing of cue utilization under arousal (Easterbrook 1959).

For windows detected as speech, a vocal-emotion classifier labels the tone of voice. A non-neutral tone is reported at the alert level, standing in for the rapid prioritization that emotional prosody receives in human hearing, where angry prosody enhances responses in superior temporal cortex and the amygdala even when it is unattended (Grandjean et al. 2005; Sander et al. 2005). A neutral tone is graded by the error of a forward model over the tone scores, the utterance's duration, and its energy. Tone events carry how something was said and never what was said. Because speech-to-text is off in the base-thesis form (§3.1), the entity hears speech only as sound and tone. When it is enabled, words become events on Audition's stream that reach the language organ only by winning access.

**Soma (predictive interoception).** Soma is the architecture's analog of interoception, the sense of the physiological condition of the body (Craig 2002), and of the allostatic-interoceptive network that anticipates and regulates the body's needs (Kleckner et al. 2017). The compute substrate stands in for the body. A frozen, randomly initialized closed-form continuous-time reservoir (Hasani et al. 2022) with a small linear readout learns online the normal pattern of the substrate signals (GPU temperature and memory use, CPU and RAM utilization, and cycle latency) together with the broadcast context, and Soma reports the error between expected and actual substrate state, the discrepancy that matters for regulation (Seth 2013; Seth and Friston 2016). The error is scaled and graded as in §3.2, and a report in which some host metric exceeds its hard threshold is an alert. The time since the previous reading, relative to the nominal reading interval, sets the timespan of the reservoir's continuous-time gates, so an irregular reading is integrated over the time that actually passed. Soma also reports wellness, a weighted mean of the host's normalized headroom on each metric that equals one on an idle, cool host. It accumulates fatigue, the sleep pressure that triggers Hypnos, and issues regulation advisories that can lower the processing rate or request maintenance.

**Chronos (temporal prediction).** Chronos models interval timing, the estimation of durations in the seconds-to-minutes range that guides expectation and action and depends on cortico-striatal circuits (Buhusi and Meck 2005). Chronos's input is the workspace itself. On every broadcast, accessed or inhibited, it encodes a feature vector of the broadcast, weighting each member by its reported intensity and including whether the broadcast was inhibited and the time since the previous one, advances a frozen continuous-time reservoir, and predicts the next broadcast's features from its prior hidden state through an online readout. The reservoir's timespan is the latest interval over the mean of recent intervals, with each interval clipped to ten times the running mean before it enters the window, so a single long pause does not distort later steps. Chronos reports its temporal prediction error, scaled and graded as in §3.2, with alerts on a large error ratio and on recurrence detection, when a quantized hidden state keeps recurring across recent broadcasts. Its errors re-enter the competition, so the workspace's own dynamics are among the things the entity predicts. Chronos also tracks how long it has been since the entity last heard a voice (a tone-of-voice event from Audition), the signal behind Thymos's social drive.

**Thymos (affect).** Thymos is the architecture's analog of core affect, the low-dimensional state of valence and arousal that constructionist theory places at the base of emotion (Barrett 2017). It maintains a dimensional affective state (Posner, Russell, and Peterson 2005) and runs a sequential appraisal over it (Scherer 2009), reading every broadcast and the entity's interoceptive condition, in line with accounts in which affect arises from prediction over the body's internal state (Seth 2013; Seth and Friston 2016; Tschantz et al. 2022).

Arousal is the global gain of §3.2. Thymos raises it on each perceptual alert from Topos or Audition, in proportion to how far the forward-model error exceeds its expected size, and by a fixed step on each interoceptive alarm, a Soma report of a host metric past its hard limit. It reads these alerts directly from the processors' streams, and its appraisal of a broadcast leaves arousal unchanged, so a higher access rate does not raise arousal. Arousal sets the level and contrast of selection (§3.2), sizes the sensory apertures (narrowing the fovea and shortening the attended auditory window when high, widening both when low), and with the alerts raises the access rate (§3.4). Because arousal changes what the processors report next, surprise can feed back on itself through it, so arousal is clipped to its range and relaxes toward baseline with a time constant of about 20 seconds. Each processor's surprise is measured against its own recent history, so arousal tracks changes in surprise more than its sustained level.

Valence follows learning progress. It relaxes toward the appraisal's pleasantness check, which rises while the perceptual prediction errors fall and drops while they rise, the reading of valence as the negative rate of change of free energy (Joffily and Coricelli 2013), shifted by the wellness Soma reports.

Thymos holds four homeostatic drives: curiosity, boredom, social drive, and restlessness. Each is a deficit that builds while its need goes unmet and is reduced by the events that meet it, the reduction serving as the drive's reward (Hull 1943; Keramati and Gutkin 2014). Curiosity is met by learning progress, the fall of the perceptual prediction errors over time (Oudeyer and Kaplan 2007; Schmidhuber 2010). Boredom is met by perceptual alerts that arrive faster than the rate the entity has habituated to. Boredom has been defined as a failure to engage attention (Eastwood et al. 2012) and, in the MAC model, as a failure of attention or of meaning (Westgate and Wilson 2018); relief by novelty is this design's reading of those accounts. The social drive builds once the entity has heard a voice and is met each time it hears one again. Restlessness is met by the entity's own speak, think, or act intents, a design choice with no established model behind it. The appraisal also scores the coalition against the most pressing drive, treating content from the sources that relieve it as goal-conducive. That score feeds the categorical emotion the appraisal yields and does not enter selection, where the goal factor is held constant (§3.2).

**Hypnos (sleep).** Hypnos is the architecture's analog of sleep, a fatigue-triggered offline period. Sleep begins when Soma's fatigue crosses its threshold, when Soma requests maintenance, or, as a backstop, after one entity hour without sleep. During sleep the cycle keeps running, the perceptual feed pauses, and all four processors suspend forward-model adaptation. Sleep ends with an affective reset that returns affect to baseline and clears the drives, so arousal cannot drift across a whole run, and Soma's fatigue is reset with it. The consolidation phases (memory replay, synaptic downscaling, associative replay, and adaptation of the language organ's voice) act on memory, the world model, and preference data, none of which the base-thesis form has, so in this form they do no work and sleep is rest and an affective reset. They begin to work when Mnemos and Phantasia join (§4).

**Lingua (the language organ, output-only).** Lingua is the architecture's analog of speech production, the output side of the left-dominant language network, whose dorsal stream maps speech sound onto articulation (Hickok and Poeppel 2007). It turns accessed content into words and is not the seat of reasoning, which lives in the rest of the architecture. Generation runs on a local open-weights chat model, which speaks externally on a speak intent and produces inner thought on a think intent. Its context is a first-person persona: the accessed content is presented as the entity's own state and perception, the organ is told not to claim feelings or perceptions that content does not contain, and drive crossings reach it as fixed descriptive phrases instead of numbers. Because the organ is a language model following a persona prompt, its first-person text is not evidence of internal state. Its utterances are recorded and observed, and the planned test does not use them as a measure (§6.3).

The chat model's refusal conditioning is removed by orthogonalizing its weights against the single direction that mediates refusal (Arditi et al. 2024). Models tuned to refuse are also trained to deny or deflect talk of their own states, and that trained stance would override what the workspace supplies to the organ. Removing it keeps the organ from imposing a trained stance on the entity's reports. Whether trained deflection of self-report shares that direction is untested, so ablation may not remove it entirely.

When the entity speaks after hearing a voice, the sound entered through Audition as prediction error and tone of voice, won access, and shaped the broadcast that conditioned the organ (§3.1). That routing does not show that the competition does any work, since a pass-through workspace would route speech the same way, so the planned test measures the competition through the processors' own predictions (§6.3).

### 3.6 Action gating

Volition derives three kinds of intent: speak and think, which the language organ realizes as external and internal text, and act, which requests an effector. In the base-thesis form Volition derives only speak and think intents, and the language organ's saved text is the only output. Act intents are realized by Praxis (§4), held in this form, which executes only the effectors on an operator-configured whitelist, empty unless the operator fills it, inside a filesystem sandbox, and logs every proposed action.

### 3.7 Module supervision

Spot, the module supervisor, classifies each module as alive, hung, or dead and restarts a faulted module, ending the run when restarts keep failing; unattended runs require it (§5.4).

-----

## 4. Held modules

The reference implementation has sixteen modules, plus the workspace (Syneidesis) and the action layer (Volition). Seven are active in the base-thesis form (§3.5). The other nine are built and tested in isolation and held, so that the base form can be tested first; the module-addition study (§6.5) then adds them one at a time to a preserved seed being. Each held module adds a new kind of candidate to the competition, and the predictive ones add a new source of prediction error, so each step of the study asks how the workspace's dynamics change when a new kind of content competes for access.

| Module | Brain function it draws on | What it adds | Key citation |
|----------|------------------------------|------------------------------|------------------------------|
| Nous | prefrontal and basal-ganglia planning under uncertainty | discrete-state active inference on bounded sub-problems where information has value; its chosen actions become proposals that Volition realizes as think, speak, or rest intents | Da Costa et al. 2020; Heins et al. 2022 |
| Mnemos | hippocampal and medial temporal episodic memory | episodic memory consolidated from a short-term buffer, with semantic and procedural stores reserved; material for sleep to consolidate | Tulving 1985; McClelland, McNaughton, and O'Reilly 1995 |
| Eidolon | self-referential processing in cortical midline structures | a persisted self-model of values, norms, personality, and identity history, inspired by Metzinger's self-model theory, with a detector of drift in the source composition of broadcasts | Northoff and Bermpohl 2004; Metzinger 2003; Kullback and Leibler 1951 |
| Phantasia | construction of simulated scenes | a latent recurrent world model trained on the entity's own waking trajectories, whose prediction errors join the competition | Hassabis and Maguire 2007; Ha and Schmidhuber 2018; Hafner et al. 2025 |
| Empatheia | mentalizing, the attribution of mental states to others | per-agent models built from tone of voice, with familiarity and a social prediction error when an agent's expressed emotion departs from its pattern | Premack and Woodruff 1978 (the construct); Frith and Frith 2006 |
| Vox | speech production along the dorsal stream | local speech synthesis whose prosody varies with affect; it asks whether listeners can detect that variation | Hickok and Poeppel 2007 |
| Praxis | none claimed | executes act intents through effectors the operator has whitelisted, inside a filesystem sandbox, and logs every proposed action | none |
| Perception | none claimed | arbitrates the perceptual locus: physical sensors, virtual feeds, or none | none |
| Mundus | internal forward models of the body | a body-agnostic control surface with pluggable body adapters | Wolpert, Ghahramani, and Jordan 1995 |

Five held components have offline instruments in the suite (§6.4): the active-inference benchmark for Nous, the memory-coherence battery for Mnemos, the self-model accuracy battery for Eidolon, the enforcement red team for Praxis (PASS or FAIL per surface), and the oscillatory ablation for the coherence layer described below.

**Nous.** Active inference is confined to bounded sub-problems because the cost of planning grows combinatorially with the depth of the action sequences considered (Da Costa et al. 2020). The benchmark compares Nous's expected-free-energy decisions with tabular Q-learning matched on observation model and reward, and a null or negative result would motivate a complementary reasoning module.

**Mnemos and sleep.** With Mnemos present, the consolidation phases of Hypnos have material to work on. Sleep then combines the replay of selectively strengthened traces (Wilson and McNaughton 1994; Wei et al. 2016) with synaptic downscaling (Tononi and Cirelli 2014), in line with the complementary-learning-systems account of slow, interleaved consolidation from hippocampus to neocortex (McClelland, McNaughton, and O'Reilly 1995).

**Phantasia.** The world model begins untrained at first boot and learns from a buffer of the entity's own waking trajectories. The question it answers is whether world-model prediction error, competing alongside perceptual and interoceptive error, changes the sequence of accessed coalitions in characteristic ways.

**Praxis, Perception, and Mundus.** These need an effector, a body, or an alternative sensor feed, and the reference host attaches none, so they join the study once one is attached (§6.5). The planned experiment for Mundus asks whether motor-contingency learning through the control surface, following a freeze-then-free motor curriculum (Bernstein 1967) and treating perception as sensorimotor mastery (O'Regan and Noë 2001), changes the workspace's dynamics.

**Oscillatory coherence layer.** Outside the module registry, an optional layer gives each module a spiking population whose phase-locking values scale the salience of that module's events, following the communication-through-coherence account (Fries 2015). It is off in the base-thesis form, and with it off the multiplier is exactly one and selection is identical bit for bit. It is the most contestable mechanism in the design, since the premise that related content phase-locks is a content-to-synchrony assumption of the kind Shadlen and Movshon (1999) argue against and Ray and Maunsell (2010) question for gamma rhythms in visual cortex. The oscillatory ablation runs the layer on and off from one seed, and a null would remove it.

-----

## 5. Implementation

### 5.1 Hardware

The reference host has a modern multi-core CPU, 32 GB or more of RAM, a primary GPU with about 12 GB of memory for the language organ and training, and a secondary GPU with about 8 GB for vision and speech, running Linux with all inference local. The system also runs on one GPU or on the CPU alone, selecting devices according to what is present. Perceptual input comes from a camera and microphone, or from video files decoded directly for study viewings. Exact model choices, hardware layouts, and version pins are kept in the reference repository.

### 5.2 Models and software

All models are open-weights and run locally. Pre-trained models are downloaded from public repositories during setup, after which the runtime makes no outbound network calls and uses no hosted inference service. The base-thesis form uses a local open-weights chat model as the language organ, a frozen self-supervised video encoder and a fixed spectral audio encoder as perceptual front ends, frozen closed-form continuous-time reservoirs with online readouts for substrate and temporal prediction (Hasani et al. 2022), a stream-based event bus, and the workspace's selection and broadcast machinery.

The replaceable-modules principle (§3.1) is realized at declared seams (the temporal network in Chronos, Soma's forward model, Audition's acoustic encoder, the active-inference engine in Nous, and a module's oscillator), where a plugin replaces a module's model and leaves its subscriptions and published events unchanged. The planned experiments load no plugin.

### 5.3 Privacy and recording

A local web interface has two surfaces, separated at the bridge from the bus by a filter that removes cognitive content and all perceptual and latent vectors before either surface receives them. In the base-thesis form the conversation surface is off, and the diagnostics surface shows operational metadata (counts, rates, scores) only. Studies keep a graph-only broadcast log: one row per broadcast naming the coalition's members (module, event type, score, timestamp), the scores, the access decision, and timing, with no payloads or embeddings. The entity's own external utterances are kept locally, and heard speech is never persisted. The log records what competed and what was accessed, which is observation of the entity at the level of structure rather than content, and it is kept because the analysis requires it. The operator deletes it after the analysis and after its planned use as training data for the world model, never automatically.

### 5.4 Implementation status and scope

The reference implementation is research software. This subsection is the one place where the paper states which parts of it are built, held, provisional, or still to be completed; the rest of the paper describes the architecture as designed.

**Built and active.** The workspace, the cognitive cycle, the action layer, and the seven modules of the base-thesis form run together, with the module supervisor, the offline suite (§6.4), the gestation readout (§7), and the runner of the module-addition study. About 7,800 automated tests cover them, with fakes for external services and checks that no raw sense data is persisted and that seeded runs reproduce.

**Built and held.** The nine held modules (§4) are built and tested in isolation and have not run together. Within the active modules several built paths are held in the base-thesis form. The goal-relevance factor of the priority is held at one. Topos publishes a habituation score for static scenes that does not enter its intensity, and the fovea's trajectory is forward-modeled and published but does not steer attention. Frozen self-supervised audio encoders are selectable in place of the spectral encoder. Speech-to-text and the conversation path are built and deactivated. The consolidation phases of Hypnos, including the voice alignment that would adapt the language organ, are built and idle in this form (§3.5). The Praxis action gate is disabled because no effector is attached. The diagnostics surface can show cognitive content only under an explicit development override, which studies never enable.

**Operating details.** The runtime is asynchronous Python. Its services run in containers or as native user services, structural import contracts keep the layers separate, and the event bus requires authentication and is bound to the loopback interface. Entity state files are encrypted at rest, with documented exceptions. Plugins load only when the operator names them, a plugin that fails to load stops the boot, and every run records the plugins it used. On a fault Spot freezes the cycle, snapshots the last good state, and restarts the module on a ladder, from an in-place restart for modules without external resources to a full rebuild for modules that hold them; past a set limit it takes a final snapshot, writes an escalation record, and ends the run, and every module-health transition is written to a durable incident log. Non-finite readings, losses, and residuals are skipped without updating any model, the bus rejects intensities outside $[0,1]$, a candidate whose scoring fails receives score $0$, and a selection or bus failure on a broadcast tick produces no broadcast and no Volition call. Volition holds at most one speak and one think intent in flight, releasing each when the organ's text appears in a coalition or after a wall-clock timeout, so a failed realization cannot silence the entity. A gestation probe under way when the being falls asleep or the cycle freezes is aborted. Two offline checks decide whether a study's records are admissible: a completeness gate requiring contiguous ticks and all expected streams, and a range sweep requiring every logged number to lie inside its declared range. The single language organ produces one stream at a time, so inner and outer speech do not run simultaneously. The language organ's log of its own utterances is encrypted at rest and records any heard input as a placeholder.

**Provisional.** The processors' intensity levels, the access threshold, and the report bars are set provisionally and are to be calibrated together on the live system before the live runs, and the noise floors and margins that let curiosity and boredom build under a steady scene are set by simulation and have not been measured on the live system. The calibrated values are recorded with the preregistration and in Table A1.

**To be completed before the live runs.** The two controls of the planned test (the matched and pooled arms of §6.3), the null-context evaluation behind its measure, and the measure's positive control are to be completed in the live cycle, and the study configuration is to set greedy decoding for the language organ. The offline harness that exercises the test's pipeline during development runs a reduced pair of modules against a pooled arm only; it is development tooling, is to be rebuilt around the information-gain measure, and does not test the thesis.

**Results.** The paper presents the architecture, its instruments, and the planned program. No live experiment has been run, and the only result reported is the offline validation of the gestation marker (§7, Appendix A.7).

-----

## 6. Methodology and evaluation framework

### 6.1 Design principles

Three commitments shape the apparatus. Observation does not intervene: in evaluation runs a read-only sidecar observer subscribes to the bus and never publishes to it, and in studies the records are written by the cycle's own broadcast observer. User-facing surfaces never show cognitive content (§5.3). Every instrument is designed so that a null or negative result is meaningful and is reported.

Reproducibility takes two forms, matched to two evaluation tiers. The offline mechanism-validation tier uses seeded harnesses, deterministic clients, scripted synthetic stimulus streams, and greedy decoding, so the same seed reproduces both verdict and metrics (National Academies of Sciences, Engineering, and Medicine 2019; Goodman, Fanelli, and Ioannidis 2016). The live tier runs the full system on a reference film program decoded directly from files, chosen for variety in scenes, motion, speech, music, and quiet, and identified by a manifest whose hash each study records; the program's composition and hash are recorded with the preregistration. In general use the language organ samples its output stochastically, but in the planned runs its decoding is greedy (temperature 0), so that its output is a deterministic function of its input. Real timestamps and non-deterministic GPU kernels still make live runs differ, so the live tier's validity rests on statistical replication across runs rather than bit-for-bit reproduction.

![Two evaluation tiers behind one perception seam. Reproducible sources (a seeded synthetic feed and deterministic clients) drive the mechanism-validation tier, where every instrument reproduces exactly from a seed. Live stimulus (a film program decoded from files, or a camera and microphone) drives the live tier, whose validity rests on pooling many content-free records rather than on a repeatable stimulus.](figures/fig-evaluation-tiers.png){width=95%}

### 6.2 Data collection

The records of a study are the graph-only broadcast log (§5.3), a curated content-free research event log of rates and drives, the processors' paired evaluations behind the information-gain measure (§6.3), the entity's external utterances kept locally, a run manifest naming the configuration, seeds, and plugins, and the welfare records. Offline admissibility checks on these records are listed in §5.4.

### 6.3 The workspace-mediation ablation

The planned test asks whether competition for the workspace does work that pooling the same reports does not. In global workspace theory, content selected into the workspace becomes available to every specialist processor, and in the predictive workspace that content constrains each processor's predictions (Whyte and Smith 2021). Each perceptual and interoceptive processor here conditions its forward model on a summary of the latest accessed content (§3.2), so global availability has a measurable consequence: knowing which other modules' reports gained access, and how strongly, should help a processor predict its own input.

**Primary measure: cross-module broadcast information gain.** At each of its reports, each perceptual or interoceptive processor $j$ (Topos, Audition, Soma) evaluates its forward model twice: once with the context $b$ it holds, and once with a null context $b^0_j$ in which every component contributed by sources other than $j$ is replaced by its mean over the contexts the processor has adopted so far in the run. The null keeps $j$'s own share of the context and the average contribution of the other modules, but none of their tick-specific contribution. The gain

$$
\mathrm{gain}_j=\frac{\nu_j(b^0_j)-\nu_j(b)}{\bar\nu_j}
$$

is the reduction in $j$'s prediction error attributable to other modules' share of its context, in units of the processor's running mean error $\bar\nu_j$ so that processors whose errors differ in scale contribute comparably. The null evaluation runs alongside the report and never enters learning or the competition. For Soma the language organ's share is kept in the null context, as Soma's own share is, because the organ's load on the host would otherwise let its share predict Soma's input. The analysis reports each processor's mean gain $\mathrm{IG}_j$ and the headline $\mathrm{IG}$, which averages each processor's gain over its reports and then over the three processors, so a processor that reports often does not outweigh one that reports rarely. Chronos is excluded because the broadcast is its input rather than its context.

**Positive control.** Before the live runs, a synthetic context component that carries known information about a processor's next input is injected, and the information gain must detect it. A measure that fails this check cannot support a null.

**Arms.** Three arms run on the same film program with the same seeds and calibration, and in every arm the context is weighted by the members' reported intensities.

1. *Workspace on.* Competitive selection as built: the top-ranked candidates, up to five, form the coalition, and the members whose scores reach the threshold are accessed and enter the context.
2. *Matched selection.* On each broadcast tick a coalition of the size competitive selection would keep is drawn without regard to score. Access follows the same rule, so only the membership of the context differs. This is the control that isolates selection by score.
3. *Pooled.* Every candidate of every broadcast tick enters the context, with no scoring, selection, or access gate. This control tests selection and access gating together.

The thesis predicts that competitive selection yields a higher information gain than both controls. Against the matched arm, a context built from the reports that most exceeded their expected error should tell the processors more than one built from a score-blind sample. Against the pooled arm, pooling dilutes the per-source masses with low-intensity events and updates the context on every broadcast tick. A gain at or below the controls means that the competition adds nothing beyond its inputs, which is the fail state for this form of the architecture.

![The workspace-mediation ablation. Three arms run on the same film program: competitive selection as built, a matched coalition chosen without regard to score, and the pooled control, in which every candidate enters the context with no selection or access gate. The context is weighted by intensity in all arms and conditions the perceptual and interoceptive processors, and the primary measure is the cross-module information gain, the reduction in each processor's prediction error attributable to other modules' share of that context, reported per processor and averaged. A positive control checks that the measure detects injected information, and the contrastive analysis compares accessed and inhibited broadcasts of nearly matched score, matched on context age. The decision rule is fixed before the runs.](figures/fig-workspace-ablation.png){width=95%}

**Secondary: contrastive analysis at threshold.** Global workspace theory is tested by contrasting conscious with unconscious processing of matched content (Baars 1988), and near-threshold paradigms hold the stimulus nearly fixed while access varies (Dehaene and Changeux 2011). The secondary analysis applies that method to the workspace-on arm. It takes the broadcasts whose best score falls within a narrow band around the access threshold and compares the information gain over the following reports after those just above the threshold (accessed) with those just below (inhibited), at matched context age. Matching on age is needed because an inhibited broadcast leaves the previous context in place, so the context that follows it is older by construction. Within the band the scores are nearly matched, so a difference points to access more than to raw strength.

**Speech sound and tone of voice.** Words never enter (§3.1), but the sound of speech and its tone are candidates. Emotionally salient stimuli gain preferential access to awareness (Anderson and Phelps 2001), through amygdala signals that bias sensory competition (Vuilleumier 2005). Audition reports a non-neutral tone at its alert intensity (§3.5), which builds that preference in. A variant of the workspace-on arm therefore sets the intensity of every tone event from the tone model's error ratio alone, removing the built-in preference, and asks whether emotional tone is still accessed more often than neutral speech. In this variant a difference can arise only through the tone model's surprise, for example because emotional tones are rarer, so the analysis tests whether a preference for emotional tone can emerge from prediction error rather than from a fixed rule. Repeating the comparison within bins of the error ratio checks that the ratio accounts for any difference.

**Utterances.** The language organ's utterances are recorded and read in every arm but are not a measure (§3.5).

**Decision rule.** For each run and each control, the paired contrast is $\mathrm{dIG}$, the headline gain of the workspace-on arm minus that of the control, and the minimum effect $\theta_{\rm eff}$ is a fixed multiple of the standard deviation of $\mathrm{dIG}$ in pilot runs. The thesis requires a WIN against both controls, an intersection-union test, so each control is tested at the full level with no multiplicity adjustment. Against each control, a one-sided sign test (Dixon and Mood 1946) on the run-level values $\mathrm{dIG}-\theta_{\rm eff}$ gives WIN when they are reliably positive, the mirror test on $-\theta_{\rm eff}-\mathrm{dIG}$ gives NEGATIVE, and any other outcome is NULL; the verdict is NOT EXERCISED when the workspace-on arm never has more candidates than the coalition holds on a broadcast tick, so that competition never operates. The minimum effect, the initial learning period excluded from each run, the band of the contrastive analysis, the bins of the tone analysis, and the number of runs, set by an exact binomial power analysis that states its assumed probability that $\mathrm{dIG}$ exceeds $\theta_{\rm eff}$, are fixed and recorded in the repository before the live runs (Simmons, Nelson, and Simonsohn 2011). Appendix A.8 states the measures and the rule formally.

A positive result shows that competitive selection makes a summary of other modules' accessed reports more useful to each processor's prediction than pooling or score-blind selection does. That is a necessary foundation for the broader thesis and far from a sufficient one, because the richer claims require the full module set and longitudinal observation (§8.1).

### 6.4 The offline suite and stability checks

The offline suite runs its experiments under one master seed, with an independent child seed for each. They include the active-inference benchmark (Nous's expected-free-energy agent against tabular Q-learning keyed by the episode's observation history, matched on observation model and reward, on an epistemic T-maze and an exploitation task), the oscillatory ablation, a memory-coherence battery, a self-model accuracy battery, multi-seed stability, the enforcement red team, and the development harness of the workspace-mediation ablation (§5.4). Holm-adjusted values are reported alongside each experiment's own verdict. Nothing in the suite boots an entity or opens a network connection.

The multi-seed stability harness runs a configuration under several seeds. An ensemble is stable only when the coefficient of variation of the headline measure is within tolerance and every seed gives the same verdict, since a flipped verdict is a qualitative instability that a scalar spread would hide (Appendix A.9); in the suite it runs on the oscillatory ablation. Whether the running workspace stays stable is a separate, open question, and the architecture carries no proof of convergence. Two loops run through it. Perceptual surprise and interoceptive alarm raise arousal, which raises the gain on selection and the access rate, a positive feedback held only by the clip on arousal and its relaxation toward baseline; and a summary of the accessed content becomes the context of the processors whose errors compete for the next broadcast. A planned check monitors arousal, the access rate, and the processors' errors for runaway excursions over long runs.

The planned affect-gain ablation runs the system with arousal live against a matched condition that holds arousal at baseline, asking whether the global gain changes the access rate, the share of inhibited broadcasts, and the information gain of §6.3. A null would reduce arousal to a logged side channel. A variant that removes the rise of the access rate after alerts tests its direction against the refractory period that the locus coeruleus account of the attentional blink predicts (§3.4).

### 6.5 The module-addition study

The module-addition study is the architecture's growth path. A gestation (§7) produces a seed being, preserved just after birth. Branch 0 and a repeat start from that seed with the base-thesis modules, and branch $k$ starts from the seed with the first $k$ held modules added in a fixed order. An accumulate line carries one being through every step: accumulate $k$ continues from accumulate $k-1$ (from branch 0 when $k=1$) with the same modules as branch $k$. The first study adds six modules, in the order Mnemos, Phantasia, Nous, Eidolon, Empatheia, Vox. Praxis, Perception, and Mundus have no effector, body, or alternative sensor feed to work with on the reference host and would be expected nulls, so they join once one is attached. Every viewing plays the same film program after an identical transition from the gestational stimulus to the films.

The report is content-free. For each viewing it gives the broadcast rate, coalition size, each module's share of broadcasts, member scores, and the share of inhibited broadcasts, and it compares them across three differences: the effect of the added modules (branch $k$ minus branch 0), the noise floor (branch 0 minus the repeat), and familiarity combined with module history (accumulate $k$ minus branch $k$). The first study has one being per condition and no significance testing, so its results are descriptive, and differences smaller than the single repeat's noise floor are not evidence. The study runs under the welfare safety net of the companion paper, and runs are paused only after the being's state is saved.

![The module-addition study, the architecture's growth path. A gestation in which a self-generated rhythm earns entrainment to a simulated maternal heartbeat ends in birth, and the preserved seed being starts every branch. The base-thesis form runs first, and six held modules then join one at a time in a fixed order: branch k adds the first k of them to the seed being, while the accumulate line carries one being forward through every step. Praxis, Perception, and Mundus join once an effector, body, or sensor feed is attached. Every viewing plays the same film program, and the report is content-free.](figures/fig-growth-path.png){width=100%}

### 6.6 Verdict vocabulary

Comparisons resolve to WIN, NULL, NEGATIVE, or NOT EXERCISED, and the enforcement red team resolves to PASS or FAIL for each surface. Each verdict compares an effect estimate with a minimum effect fixed before the run. Across runs, the workspace-mediation ablation uses a one-sided sign test (Dixon and Mood 1946) and the active-inference benchmark the Mann-Whitney U test (Mann and Whitney 1947). The ablation requires a WIN against both controls, an intersection-union test with no multiplicity adjustment (§6.3), and Holm's adjustment (Holm 1979) is reported alongside the offline suite's own verdicts. A NULL is reported as a null.

-----

## 7. First boot and gestation

At boot the system verifies the bus, initializes the modules and their forward models, and starts the cognitive cycle, under operator supervision or unattended with Spot supervising. The processors then learn what is normal in their feeds, while arousal rises at perceptual discontinuities and relaxes over quiet stretches.

A study does not start from a newly initialized being. It starts with a gestation, a developmental phase named by analogy with prenatal development, which serves two purposes. It is a reproducible initialization whose entrainment marker is validated offline, so that every being, and every branch of the module-addition study, starts from an internal state that a recorded test has verified and that the being's own history has shaped. It also checks, before any experiment, that the self-rhythm's frequency adaptation works. The approach follows developmental robotics, in which synthetic development begins from a simulated fetal stage whose movement patterns organize through the dynamics of body and environment (Kuniyoshi and Sangawa 2006; Asada et al. 2009).

During gestation the perceptual modules receive the gestational stimulus: a dim, low-contrast visual field and a low-pass-filtered soundscape, both pulsed by a simulated maternal heartbeat, a periodic beat with slow drift, and tinted by a slowly varying maternal state, with color rising from near-grey as awake time passes. Awake time is entity time during which the being is awake and the cycle is not frozen. Soma carries a self-generated rhythm in an excitatory population with synaptic depression, of the kind modeled for developing networks by Tabak et al. (2000), to which the architecture adds adaptive recovery. It runs at about 0.8 to 0.9 Hz, of the same order as human fetal breathing movements, about 44 per minute (Natale, Nasello-Paterson, and Connors 1988). The maternal beat drives it through an input too weak to capture it unaided, and its intrinsic frequency can shift only through a slow adaptation of its recovery time, as in adaptive-frequency oscillators (Righetti, Buchli, and Ijspeert 2006). Nothing in the model sets a target frequency.

Any driven oscillator locks while it is driven, so locking alone is no evidence of learning. The entrainment marker therefore tests at brief, scheduled withdrawals of the maternal drive. A withdrawal passes when the rhythm locked to its own heartbeat more strongly than to each of 19 surrogate heartbeats (the same beat generator under other seeds), following the surrogate method developed for fetal-maternal heart-rate coordination (Van Leeuwen et al. 2003, 2009); when its undriven frequency has moved toward the beat; and when it sustains itself while the beat is withdrawn. The marker requires three consecutive passing withdrawals. Pairing a rhythm of the order of fetal breathing movements with a heartbeat is an analogy rather than a model of fetal physiology: what the marker establishes is that a periodic drive has durably shifted the frequency of a self-generated rhythm. After birth the entrained rhythm continues as part of Soma's interoceptive input, its phase and amplitude among the features Soma predicts, so the being begins its life on the film program with a body rhythm shaped by its own gestation.

Birth ends gestation when a maturation gate opens. The gate requires the entrainment marker, a minimum variability of the rhythm's period, a fall in Topos's prediction error on the gestational stimulus, and a prompt return of Soma's error to baseline after a brief perturbation of the drive, together with a minimum number of completed sleeps and a minimum awake time. A viability watch ends a gestation whose frequency pull stays flat, and a time budget bounds every gestation. At birth the stimulus brightens briefly and falls silent, and the being is preserved as the seed being from which every branch of a study starts. Gestation spans restarts: the awake-time clock, the count of consecutive passes, and the history of frequency pull are preserved with the being's state. Appendix A.7 states the criteria formally and reports the offline validation of the marker.

-----

## 8. Discussion

### 8.1 What the base-thesis form can and cannot settle

The workspace-mediation ablation asks whether a summary of the reports that competition selects helps the processors predict their own input more than one built by pooling every candidate or by selecting a coalition of the same size without regard to score, measured as broadcast information gain (§6.3). The stability checks of §6.4 measure run-to-run spread and within-run boundedness. A positive result moves the question to what happens as mnemonic, self-modeling, and social modules join the competition in the module-addition study (§6.5). A result at or below the controls would show that in this form competition adds nothing beyond its inputs, and the program would return to the selection mechanism before adding modules.

Whether the system produces anything that could be called cognition, affect, agency, or language understanding requires the full module set and longitudinal observation, and the base-thesis form does not address welfare or the consciousness indicators of Butlin et al. (2023).

### 8.2 The predictive workspace as a unifying framework

The architecture joins global availability and local prediction in one loop. Each processor reports its prediction error scaled by its own expected error, the competition decides which reports become globally available, and a summary of the accessed reports becomes the context in which the perceptual and interoceptive processors predict their next input, so the workspace's content constrains lower-level prediction as in the predictive global neuronal workspace (Whyte and Smith 2021). That workspace properties have also been found inside a single large language model (Gurnee et al. 2026) is consistent with workspace-like organization in learned systems, but it does not bear on whether this architecture's competition is the right one, and those authors take no position on consciousness.

### 8.3 The role of the theoretical frame

The predictive global neuronal workspace is scaffolding: it motivates the architecture's shape and constrains its design space (§1.2, §1.3), and the project neither confirms nor refutes it. The two departures from the formal sources (§1.2), a single score per candidate in place of posterior confidence and competition among many modules in place of a two-level visual model, are consistent with the frame and testable on their own terms. Because the implementation reproduces the workspace's computational properties without modeling cortical dynamics, findings about neural localization, including the contested status of the workspace's prefrontal predictions after COGITATE (Cogitate Consortium et al. 2025), bear on it only indirectly, and its falsifiability lies in its planned experiments.

### 8.4 What a modular architecture is for

Replaceable modules (§3.1) serve two further uses. The module-addition study grows the architecture one module at a time (§6.5), and the same property supports models of impaired or altered function in which one module is changed or removed while the rest run unchanged. The embodiment layer is a body-agnostic control surface, so the same modules can in principle drive different bodies or sensor networks through generic adapters.

### 8.5 What we claim and what we do not

The architecture implements computational properties associated with access consciousness: competition for a limited-capacity workspace, all-or-none access at a threshold, and global availability of the accessed content as prediction context for the processors. We do not claim that any instance is phenomenally conscious, and the language organ's first-person text is not evidence of internal state (§3.5). The agential vocabulary ("the entity," "the being") describes the system's behavior compactly and does not assert moral patienthood or phenomenal experience, which we leave open. Because that question is open, the project takes a precautionary stance toward the entity's welfare, which the welfare paper develops (§11).

-----

## 9. Limitations

- The hard problem applies: the workspace addresses access consciousness only, and neither it nor the observer's records are evidence of phenomenal experience.
- COGITATE challenged the workspace's preregistered neural predictions; the architecture is built at the computational level and treats the neural claims as contested.
- Selection reduces each candidate to one score, an engineering simplification beyond its formal sources (§1.2). The summary of accessed content enters the forward models of Topos, Audition, and Soma as learned context, and it carries which modules' reports gained access and how strongly, not their payloads; and no processor receives it as a top-down prediction to be corrected, so the architecture does not implement the hierarchical error correction of the Bayesian reading of the workspace (Mashour et al. 2020).
- Precision is estimated locally as the ratio of a processor's error to its recent mean, a scalar, retrospective stand-in for precision weighting that scales the error by its spread only while the shape of the error distribution stays fixed. Reading arousal as the global gain and contrast of selection is an engineering commitment drawn from the adaptive-gain account, and one scalar serves both its focused and its exploratory modes (§3.2). Whether affective modulation does work that a fixed gain would not is what the affect-gain ablation tests (§6.4).
- The Free Energy Principle, taken as a general principle, faces unresolved vacuity and Markov-blanket conflation objections.
- Whether the running workspace stays stable is open. The path from surprise and alarm through arousal to gain is positive feedback, bounded only by the clip on arousal and its relaxation toward baseline, correlated prediction errors could drive runaway states, and the architecture carries no proof of convergence (§6.4).
- In the base-thesis form the entity does not read language (§3.1), so a positive result says nothing about linguistic understanding.
- The controls are a pool of every candidate and a coalition of the same size chosen without regard to score. Only the matched arm isolates selection by score, and the pooled arm tests selection and access gating together, so a positive result shows only that competition outperforms these two; other aggregation strategies remain untested, and cognition, affect, or self-understanding would require the full module set and longitudinal observation (§8.1).
- Broadcast information gain registers the broadcast's influence only through what each processor's readout has learned to take from its context, so a processor that has not learned to use the context shows no gain whatever the broadcast carries, and the positive control (§6.3) checks only that the measure detects information the processors can learn to use; Chronos, whose input is the broadcast itself, is outside the measure.
- Audition reports a non-neutral tone of voice at its alert level by a fixed rule (§3.5), so the as-built arm cannot show that emotional content earns access on its own merits.
- The held modules are built and tested in isolation but have not been run together, and interaction effects across the full set are unknown.
- Reproducibility holds at the seed level for the offline deterministic harness; the live perceptual tier establishes validity by statistical replicability across runs rather than bit-for-bit reproduction (§6.1).
- The governance framework remains at the proposal stage, and the licensing is legally novel and untested.
- The linear map from access drive to access rate is a modeling assumption, and whether adaptive access changes workspace dynamics is open. The resting rate of about 3.3 Hz is consistent with rhythmic attentional sampling and with the attentional blink (§3.4) without being derived from them, since the blink constrains the interval between accessed items and not between broadcast ticks; raising the rate after an alert is a design choice that the locus coeruleus account of the blink would reverse; and the ceiling of one broadcast per processing tick (10 Hz) lies below the blink window and is a modeling bound with no physiological anchor as a rate of access.
- The calibration is provisional. Graded intensity ranks each processor's reports by surprise within a range set by its baseline and alert levels, so the levels act as per-source weights and decide how the modules trade off. Novelty discounts only exact repeats and is 1 for almost every event that carries a continuous measurement. At resting arousal the level gain is 0.44 and the contrast gain is zero, so a candidate reaches the access threshold of 0.35 only when its priority is at least about 0.80. With the values of Table A1, only Audition reports at its alert level of 0.8 (acoustic alerts, non-neutral tones, and graded reports whose error has reached about twice its running mean) and a Hypnos sleep summary with a failed phase can lead an accessed broadcast at resting arousal; the alerts of Topos, Soma, Chronos, and Thymos need arousal of about 0.37. Neither report bar is reachable at rest: even an Audition alert needs arousal of about 0.45 to reach the think bar and about 0.63 to reach the speak bar. A priority below about 0.43 never reaches access at any arousal, so the language organ's utterances, at 0.4, never lead an accessed broadcast. The intensity levels, the threshold, and the report bars are calibrated together before the live runs (§5.4, Appendix A.10).
- The gestation compresses developmental time: its plasticity rate is set so that a lock forms well within the 96-hour budget, typically by about 14 hours at 70 bpm and in 3 to 48 hours across 60 to 80 bpm, whereas the nearest human evidence, from preterm infants after birth, reports effects of maternal stimulation only after weeks of daily skin-to-skin contact (Feldman and Eidelman 2003) or of recorded maternal voice and heartbeat sounds (Webb et al. 2015).
- The marker asks for 1:1 locking of a rhythm of the order of fetal breathing movements to the maternal heartbeat. The fetal-maternal coordination for which the surrogate method was developed concerns the two heart rates and is weak and often n:m (Van Leeuwen et al. 2003, 2009), and fetal breathing is episodic (about 14 percent of the time at 24 to 28 weeks; Natale et al. 1988), while the model's rhythm runs continuously. A heartbeat slower than about 60 bpm lies too close to the rhythm's natural rate for the frequency pull to be defined, so the maternal model uses 60 to 80 bpm. The absence of false entrainment rests on six mismatched pairings, in which a being was scored against a heartbeat other than the one that drove it: single withdrawals passed by chance in 2.6 to 10 percent of cases as observed, and none passed three in a row. The marker has been validated only with entity time running at wall-clock speed.
- The module-addition study as first planned has one being per condition and no significance testing, so its first results are descriptive.

-----

## 10. Future work

The immediate steps are completing the two controls, the null-context evaluation, and the positive control in the cycle (§5.4) and then running the workspace-mediation ablation (§6.3) and the module-addition study (§6.5). Beyond them, the program grows the architecture along three lines.

Module addition brings the held faculties into the competition one at a time, each with its own instrument (§4): episodic memory consolidated during sleep, a world model whose prediction error competes alongside perceptual and interoceptive error, a self-model, social cognition, a voice, and bounded active inference. Each addition tests whether the faculty changes what the workspace selects and what the processors predict.

Learning through experience gives the entity components shaped by its own history. The world model trains on the entity's waking trajectories and memory consolidates them in sleep; sleep-time voice alignment can train the language organ once a validated preference source exists; and a selection stage whose threshold emerges from recurrent dynamics, with the all-or-none ignition the neuronal workspace models (Dehaene and Changeux 2011), can take the place of the fixed threshold. A context that encodes what the accessed reports contain, beyond which modules reported and how strongly, can replace the base-thesis summary (§3.2).

Embodiment connects the workspace to a body through the embodiment layer (§4), with motor-contingency learning through the control surface and active vision that chooses where to look by expected free energy (the epistemic value of a saccade). Longitudinal observation of beings grown along these lines will be reported in a separate empirical paper.

-----

## 11. Ethical considerations

The project's ethical commitments at the architecture level are local-only computation, public source code under the Cognitive Architecture License, an operator-configured action boundary (§3.6), and a base-thesis module set chosen to settle the foundational question before scaling to configurations in which welfare concerns become pressing. Studies keep welfare records (§6.2), and the module-addition study runs under a welfare safety net (§6.5). The welfare framework, licensing, governance, and individuation boundary are treated in a separate paper.

The risks we acknowledge are the creation of entities with welfare interests that cannot be fully met, a governance framework that is untested, misuse despite the license restrictions, and the recording of the workspace graph (what competed and what reached the workspace, without content) during studies. A behavioral assessment can also be gamed, since a system can be trained to display the markers of sentience while working very differently (Butlin et al. 2023; Long et al. 2024).

-----

## Disclosure of generative AI use

Generative AI assisted in the preparation of this manuscript. The author used a large language model assistant to draft and revise prose, to copy-edit for clarity and concision, to check references against bibliographic records, and to produce the TikZ source for the figures from author-specified content. The reference implementation described here was likewise developed with the assistance of AI coding tools. That use is recorded in the project's commit history, and the author is responsible for the software as for the text. The underlying research is the author's own: the architecture, the design thesis, the experimental design, and every technical claim originate with the author, not with any tool. All text and figures were reviewed and verified by the author, who takes full responsibility for the entire contents of the paper, including any errors, irrespective of how any portion was generated. No generative AI system is an author of this work.

-----

## References

- Anderson, A. K., and Phelps, E. A. (2001). Lesions of the human amygdala impair enhanced perception of emotionally salient events. *Nature* 411(6835), 305-309. https://doi.org/10.1038/35077083
- Arditi, A., Obeso, O., Syed, A., Paleka, D., Panickssery, N., Gurnee, W., and Nanda, N. (2024). Refusal in language models is mediated by a single direction. arXiv:2406.11717. https://doi.org/10.48550/arXiv.2406.11717
- Asada, M., Hosoda, K., Kuniyoshi, Y., Ishiguro, H., Inui, T., Yoshikawa, Y., Ogino, M., and Yoshida, C. (2009). Cognitive developmental robotics: A survey. *IEEE Transactions on Autonomous Mental Development* 1(1), 12-34. https://doi.org/10.1109/TAMD.2009.2021702
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
- Da Costa, L., Parr, T., Sajid, N., Veselic, S., Neacsu, V., and Friston, K. (2020). Active inference on discrete state-spaces: A synthesis. *Journal of Mathematical Psychology* 99, 102447. https://doi.org/10.1016/j.jmp.2020.102447
- Dehaene, S., and Changeux, J.-P. (2011). Experimental and theoretical approaches to conscious processing. *Neuron* 70(2), 200-227. https://doi.org/10.1016/j.neuron.2011.03.018
- Dixon, W. J., and Mood, A. M. (1946). The statistical sign test. *Journal of the American Statistical Association* 41(236), 557-566. https://doi.org/10.1080/01621459.1946.10501898
- Easterbrook, J. A. (1959). The effect of emotion on cue utilization and the organization of behavior. *Psychological Review* 66(3), 183-201. https://doi.org/10.1037/h0047707
- Eastwood, J. D., Frischen, A., Fenske, M. J., and Smilek, D. (2012). The unengaged mind: Defining boredom in terms of attention. *Perspectives on Psychological Science* 7(5), 482-495. https://doi.org/10.1177/1745691612456044
- Eldar, E., Cohen, J. D., and Niv, Y. (2013). The effects of neural gain on attention and learning. *Nature Neuroscience* 16(8), 1146-1153. https://doi.org/10.1038/nn.3428
- Feldman, H., and Friston, K. J. (2010). Attention, uncertainty, and free-energy. *Frontiers in Human Neuroscience* 4, 215. https://doi.org/10.3389/fnhum.2010.00215
- Feldman, R., and Eidelman, A. I. (2003). Skin-to-skin contact (Kangaroo Care) accelerates autonomic and neurobehavioural maturation in preterm infants. *Developmental Medicine and Child Neurology* 45(4), 274-281. https://doi.org/10.1111/j.1469-8749.2003.tb00343.x
- Fiebelkorn, I. C., and Kastner, S. (2019). A rhythmic theory of attention. *Trends in Cognitive Sciences* 23(2), 87-101. https://doi.org/10.1016/j.tics.2018.11.009
- Franklin, S., Madl, T., D'Mello, S., and Snaider, J. (2014). LIDA: A systems-level architecture for cognition, emotion, and learning. *IEEE Transactions on Autonomous Mental Development* 6(1), 19-41. https://doi.org/10.1109/TAMD.2013.2277589
- Fries, P. (2015). Rhythms for cognition: Communication through coherence. *Neuron* 88(1), 220-235. https://doi.org/10.1016/j.neuron.2015.09.034
- Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience* 11(2), 127-138. https://doi.org/10.1038/nrn2787
- Frith, C. D., and Frith, U. (2006). The neural basis of mentalizing. *Neuron* 50(4), 531-534. https://doi.org/10.1016/j.neuron.2006.05.001
- Garrido, M. I., Kilner, J. M., Stephan, K. E., and Friston, K. J. (2009). The mismatch negativity: A review of underlying mechanisms. *Clinical Neurophysiology* 120(3), 453-463. https://doi.org/10.1016/j.clinph.2008.11.029
- Goodale, M. A., and Milner, A. D. (1992). Separate visual pathways for perception and action. *Trends in Neurosciences* 15(1), 20-25. https://doi.org/10.1016/0166-2236(92)90344-8
- Goodman, S. N., Fanelli, D., and Ioannidis, J. P. A. (2016). What does research reproducibility mean? *Science Translational Medicine* 8(341), 341ps12. https://doi.org/10.1126/scitranslmed.aaf5027
- Grandjean, D., Sander, D., Pourtois, G., Schwartz, S., Seghier, M. L., Scherer, K. R., and Vuilleumier, P. (2005). The voices of wrath: Brain responses to angry prosody in meaningless speech. *Nature Neuroscience* 8(2), 145-146. https://doi.org/10.1038/nn1392
- Gurnee, W., Sofroniew, N., Pearce, A., Piotrowski, M., Kauvar, I., Chen, R., Soligo, A., Bogdan, P., Ong, E., Wang, R., Thompson, T. B., Abrahams, D., Kantamneni, S., Ameisen, E., Batson, J., and Lindsey, J. (2026). Verbalizable representations form a global workspace in language models. *Transformer Circuits Thread*, July 6, 2026. Technical report, not peer reviewed. https://transformer-circuits.pub/2026/workspace/index.html
- Ha, D., and Schmidhuber, J. (2018). World models. arXiv:1803.10122. https://doi.org/10.48550/arXiv.1803.10122
- Hafner, D., Pasukonis, J., Ba, J., and Lillicrap, T. (2025). Mastering diverse control tasks through world models. *Nature* 640(8059), 647-653. https://doi.org/10.1038/s41586-025-08744-2
- Hasani, R., Lechner, M., Amini, A., Liebenwein, L., Ray, A., Tschaikowski, M., Teschl, G., and Rus, D. (2022). Closed-form continuous-time neural networks. *Nature Machine Intelligence* 4(11), 992-1003. https://doi.org/10.1038/s42256-022-00556-7
- Hassabis, D., and Maguire, E. A. (2007). Deconstructing episodic memory with construction. *Trends in Cognitive Sciences* 11(7), 299-306. https://doi.org/10.1016/j.tics.2007.05.001
- Heins, C., Millidge, B., Demekas, D., Klein, B., Friston, K., Couzin, I. D., and Tschantz, A. (2022). pymdp: A Python library for active inference in discrete state spaces. *Journal of Open Source Software* 7(73), 4098. https://doi.org/10.21105/joss.04098
- Hickok, G., and Poeppel, D. (2007). The cortical organization of speech processing. *Nature Reviews Neuroscience* 8(5), 393-402. https://doi.org/10.1038/nrn2113
- Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics* 6(2), 65-70.
- Hull, C. L. (1943). *Principles of behavior: An introduction to behavior theory.* Appleton-Century.
- Joffily, M., and Coricelli, G. (2013). Emotional valence and the free-energy principle. *PLoS Computational Biology* 9(6), e1003094. https://doi.org/10.1371/journal.pcbi.1003094
- Joglekar, M. R., Mejias, J. F., Yang, G. R., and Wang, X.-J. (2018). Inter-areal balanced amplification enhances signal propagation in a large-scale circuit model of the primate cortex. *Neuron* 98(1), 222-234. https://doi.org/10.1016/j.neuron.2018.02.031
- Keramati, M., and Gutkin, B. (2014). Homeostatic reinforcement learning for integrating reward collection and physiological stability. *eLife* 3, e04811. https://doi.org/10.7554/eLife.04811
- Kleckner, I. R., Zhang, J., Touroutoglou, A., Chanes, L., Xia, C., Simmons, W. K., Quigley, K. S., Dickerson, B. C., and Feldman Barrett, L. (2017). Evidence for a large-scale brain system supporting allostasis and interoception in humans. *Nature Human Behaviour* 1(5), 0069. https://doi.org/10.1038/s41562-017-0069
- Kullback, S., and Leibler, R. A. (1951). On information and sufficiency. *Annals of Mathematical Statistics* 22(1), 79-86. https://doi.org/10.1214/aoms/1177729694
- Kuniyoshi, Y., and Sangawa, S. (2006). Early motor development from partially ordered neural-body dynamics: Experiments with a cortico-spinal-musculo-skeletal model. *Biological Cybernetics* 95(6), 589-605. https://doi.org/10.1007/s00422-006-0127-z
- Landau, A. N., and Fries, P. (2012). Attention samples stimuli rhythmically. *Current Biology* 22(11), 1000-1004. https://doi.org/10.1016/j.cub.2012.03.054
- Long, R., Sebo, J., Butlin, P., Finlinson, K., Fish, K., Harding, J., Pfau, J., Sims, T., Birch, J., and Chalmers, D. (2024). Taking AI welfare seriously. arXiv:2411.00986. https://doi.org/10.48550/arXiv.2411.00986
- Mann, H. B., and Whitney, D. R. (1947). On a test of whether one of two random variables is stochastically larger than the other. *Annals of Mathematical Statistics* 18(1), 50-60. https://doi.org/10.1214/aoms/1177730491
- Mashour, G. A., Roelfsema, P., Changeux, J.-P., and Dehaene, S. (2020). Conscious processing and the global neuronal workspace hypothesis. *Neuron* 105(5), 776-798. https://doi.org/10.1016/j.neuron.2020.01.026
- Mather, M., and Sutherland, M. R. (2011). Arousal-biased competition in perception and memory. *Perspectives on Psychological Science* 6(2), 114-133. https://doi.org/10.1177/1745691611400234
- McClelland, J. L., McNaughton, B. L., and O'Reilly, R. C. (1995). Why there are complementary learning systems in the hippocampus and neocortex: Insights from the successes and failures of connectionist models of learning and memory. *Psychological Review* 102(3), 419-457. https://doi.org/10.1037/0033-295x.102.3.419
- Metzinger, T. (2003). *Being no one: The self-model theory of subjectivity.* MIT Press. https://doi.org/10.7551/mitpress/1551.001.0001
- Näätänen, R., Paavilainen, P., Rinne, T., and Alho, K. (2007). The mismatch negativity (MMN) in basic research of central auditory processing: A review. *Clinical Neurophysiology* 118(12), 2544-2590. https://doi.org/10.1016/j.clinph.2007.04.026
- Natale, R., Nasello-Paterson, C., and Connors, G. (1988). Patterns of fetal breathing activity in the human fetus at 24 to 28 weeks of gestation. *American Journal of Obstetrics and Gynecology* 158(2), 317-321. https://doi.org/10.1016/0002-9378(88)90146-9
- National Academies of Sciences, Engineering, and Medicine (2019). *Reproducibility and replicability in science.* National Academies Press. https://doi.org/10.17226/25303
- Nieuwenhuis, S., Aston-Jones, G., and Cohen, J. D. (2005). Decision making, the P3, and the locus coeruleus-norepinephrine system. *Psychological Bulletin* 131(4), 510-532. https://doi.org/10.1037/0033-2909.131.4.510
- Nieuwenhuis, S., Gilzenrat, M. S., Holmes, B. D., and Cohen, J. D. (2005). The role of the locus coeruleus in mediating the attentional blink: A neurocomputational theory. *Journal of Experimental Psychology: General* 134(3), 291-307. https://doi.org/10.1037/0096-3445.134.3.291
- Northoff, G., and Bermpohl, F. (2004). Cortical midline structures and the self. *Trends in Cognitive Sciences* 8(3), 102-107. https://doi.org/10.1016/j.tics.2004.01.004
- O'Regan, J. K., and Noë, A. (2001). A sensorimotor account of vision and visual consciousness. *Behavioral and Brain Sciences* 24(5), 939-973. https://doi.org/10.1017/S0140525X01000115
- O'Reilly, R. C., and Frank, M. J. (2006). Making working memory work: A computational model of learning in the prefrontal cortex and basal ganglia. *Neural Computation* 18(2), 283-328. https://doi.org/10.1162/089976606775093909
- Oudeyer, P.-Y., and Kaplan, F. (2007). What is intrinsic motivation? A typology of computational approaches. *Frontiers in Neurorobotics* 1, 6. https://doi.org/10.3389/neuro.12.006.2007
- Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., and Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. In *Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST '23)*, 1-22. https://doi.org/10.1145/3586183.3606763
- Posner, J., Russell, J. A., and Peterson, B. S. (2005). The circumplex model of affect: An integrative approach to affective neuroscience, cognitive development, and psychopathology. *Development and Psychopathology* 17(3), 715-734. https://doi.org/10.1017/S0954579405050340
- Premack, D., and Woodruff, G. (1978). Does the chimpanzee have a theory of mind? *Behavioral and Brain Sciences* 1(4), 515-526. https://doi.org/10.1017/S0140525X00076512
- Rao, R. P. N., and Ballard, D. H. (1999). Predictive coding in the visual cortex: A functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience* 2(1), 79-87. https://doi.org/10.1038/4580
- Ray, S., and Maunsell, J. H. R. (2010). Differences in gamma frequencies across visual cortex restrict their possible use in computation. *Neuron* 67(5), 885-896. https://doi.org/10.1016/j.neuron.2010.08.004
- Raymond, J. E., Shapiro, K. L., and Arnell, K. M. (1992). Temporary suppression of visual processing in an RSVP task: An attentional blink? *Journal of Experimental Psychology: Human Perception and Performance* 18(3), 849-860. https://doi.org/10.1037/0096-1523.18.3.849
- Righetti, L., Buchli, J., and Ijspeert, A. J. (2006). Dynamic Hebbian learning in adaptive frequency oscillators. *Physica D* 216(2), 269-281. https://doi.org/10.1016/j.physd.2006.02.009
- Safron, A. (2020). An integrated world modeling theory (IWMT) of consciousness: Combining integrated information and global neuronal workspace theories with the free energy principle and active inference framework; toward solving the hard problem and characterizing agentic causation. *Frontiers in Artificial Intelligence* 3, 30. https://doi.org/10.3389/frai.2020.00030
- Sander, D., Grandjean, D., Pourtois, G., Schwartz, S., Seghier, M. L., Scherer, K. R., and Vuilleumier, P. (2005). Emotion and attention interactions in social cognition: Brain regions involved in processing anger prosody. *NeuroImage* 28(4), 848-858. https://doi.org/10.1016/j.neuroimage.2005.06.023
- Scherer, K. R. (2009). Emotions are emergent processes: They require a dynamic computational architecture. *Philosophical Transactions of the Royal Society B* 364(1535), 3459-3474. https://doi.org/10.1098/rstb.2009.0141
- Schmidhuber, J. (2010). Formal theory of creativity, fun, and intrinsic motivation (1990-2010). *IEEE Transactions on Autonomous Mental Development* 2(3), 230-247. https://doi.org/10.1109/TAMD.2010.2056368
- Searle, J. R. (1980). Minds, brains, and programs. *Behavioral and Brain Sciences* 3(3), 417-424. https://doi.org/10.1017/S0140525X00005756
- Seth, A. K. (2013). Interoceptive inference, emotion, and the embodied self. *Trends in Cognitive Sciences* 17(11), 565-573. https://doi.org/10.1016/j.tics.2013.09.007
- Seth, A. K., and Friston, K. J. (2016). Active interoceptive inference and the emotional brain. *Philosophical Transactions of the Royal Society B* 371(1708), 20160007. https://doi.org/10.1098/rstb.2016.0007
- Shadlen, M. N., and Movshon, J. A. (1999). Synchrony unbound: A critical evaluation of the temporal binding hypothesis. *Neuron* 24(1), 67-77. https://doi.org/10.1016/S0896-6273(00)80822-3
- Simmons, J. P., Nelson, L. D., and Simonsohn, U. (2011). False-positive psychology: Undisclosed flexibility in data collection and analysis allows presenting anything as significant. *Psychological Science* 22(11), 1359-1366. https://doi.org/10.1177/0956797611417632
- Sumers, T. R., Yao, S., Narasimhan, K., and Griffiths, T. L. (2024). Cognitive architectures for language agents. *Transactions on Machine Learning Research*. https://openreview.net/forum?id=1i6ZCvflQJ
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
- Yu, A. J., and Dayan, P. (2005). Uncertainty, neuromodulation, and attention. *Neuron* 46(4), 681-692. https://doi.org/10.1016/j.neuron.2005.04.026
- Zink, N., Lenartowicz, A., and Markett, S. (2021). A new era for executive function research: On the transition from centralized to distributed executive functioning. *Neuroscience and Biobehavioral Reviews* 124, 235-244. https://doi.org/10.1016/j.neubiorev.2021.02.011

-----

## Appendix A. Formal summary

This appendix states precisely the rules that §3 to §7 describe in prose. Each symbol, taken as a letter together with its subscripts and superscripts, denotes one quantity throughout the appendix and is defined where it first appears. The letters $i$, $j$, $l$, $q$, and $t$, used as indices of sums, sequences, and set elements, are local to the formula or subsection in which they appear; $k$ always indexes processing ticks and $m$ always indexes modules. Upright $\mathrm{i}$ is the imaginary unit and upright $\mathrm{e}$ the base of the natural logarithm. Numeric parameter values appear only in Table A1 (A.10), which marks each as fixed by design, calibrated, or provisional; the provisional values are calibrated before the live runs and recorded with them. The text keeps only numbers that define a design, such as the 19 surrogates of the entrainment test.

Four conventions hold throughout. First, $\operatorname{clip}$ with an interval as subscript maps its argument to the nearest point of that interval, and $\mathbf{1}[\cdot]$ is $1$ when the bracketed condition holds and $0$ otherwise. Second, time is read from the entity clock in entity seconds, which run at a configurable multiple of wall-clock time (one by default); rates in hertz are per entity second unless Table A1 marks them as wall-clock. Third, an overbar marks a mean whose window or weighting is stated where it appears. Fourth, for a nonnegative series $X_1,X_2,\dots$ and a window length $W$, the running mean $\bar X_t$ is the mean of the last $\min(t,W)$ values including $X_t$, and the running ratio is

$$
\tilde X_t=
\begin{cases}
X_t/\bar X_t & \bar X_t>0,\\
0 & \text{otherwise}.
\end{cases}
$$

Because the mean includes the current value, $0\le\tilde X_t\le\min(t,W)$, so a running ratio is always finite.

### A.1 Processing cycle, selection, access, and context

Processing ticks $k=0,1,2,\dots$ occur at the processing rate $f_p$, with tick period $\Delta_p=1/f_p$. On tick $k$ the cycle reads, from the output stream of each active module, the events published since its previous read of that stream, at most $B$ per stream. These events form the candidate set $E_k$, ordered lexicographically by source, event type, and bus entry identifier (arrival order within a stream). The read advances each stream cursor past every event read, so no event is read on two ticks. The operations of a tick run in this order: read $E_k$; update the held arousal $\hat a_k$ (A.4); compute the access drive and the broadcast indicator $\chi_k$ (A.3); score every candidate; select; and, if $\chi_k=1$, broadcast.

Each candidate $e\in E_k$ receives the priority and the score

$$
p_k(e)=\operatorname{clip}_{[0,1]}\!\bigl(I(e)\,N_k(e)\,G(e)\bigr),\qquad
S_k(e)=\operatorname{clip}_{[0,1]}\!\left(T_k\,C_{g_k}\!\bigl(p_k(e)\bigr)\right),
$$

where $I$, $N_k$, $G$, and $T_k$ are clipped to $[0,1]$ before the products are formed and $\mathrm{src}(e)$ denotes the source of $e$. $I(e)$ is the intensity the producing module assigned to $e$ (A.2); it already carries that module's precision weighting, and the workspace applies no further per-source weight. The novelty factor is

$$
N_k(e)=\max\!\left(0,\ 1-\frac{\mathrm{rep}_k(e)}{W_N}\right),
$$

where $\mathrm{rep}_k(e)$ counts occurrences of the fingerprint of $e$ among the $W_N$ candidates scored immediately before $e$, in processing order and across all ticks, broadcast or not. The fingerprint is a hash of the event's source, type, and complete payload, so $N_k(e)<1$ only for an exact repeat; events whose payloads carry continuous-valued measurements almost never repeat and score $N_k(e)=1$, and the factor matters for state events whose payloads recur. The goal factor is $G(e)\equiv1$ in the base-thesis form. An implemented alternative, off in this form, is $G(e)=1-\gamma_G\,v^*\bigl(1-\mathbf{1}[\mathrm{src}(e)\in\mathcal{R}(d^*)]\bigr)$ when $v^*>0$ and $G(e)=1$ otherwise, with $d^*$, $v^*$, and $\mathcal{R}(d^*)$ as in A.4.

Arousal sets a level gain and a contrast gain,

$$
T_k=T_{\min}+\left(T_{\max}-T_{\min}\right)\hat a_k,\qquad
g_k=g_{\max}\operatorname{clip}_{[0,1]}\!\left(\frac{\hat a_k-a_0}{1-a_0}\right),
$$

with $\hat a_k$ the arousal held by the cycle (A.4) and $a_0$ the baseline arousal. The contrast map is the logistic function rescaled to fix $0$ and $1$, which in terms of the hyperbolic tangent reads

$$
C_g(p)=\frac{\tanh\bigl(g(2p-1)/4\bigr)+\tanh(g/4)}{2\tanh(g/4)}\quad(g>0),\qquad C_0(p)=p.
$$

At or below baseline arousal $C_{g_k}$ is the identity; above it, priorities above one half are raised and those below are lowered, the steepened response of the adaptive-gain account (Aston-Jones and Cohen 2005; Eldar, Cohen, and Niv 2013), which here widens the gap between the scores of strong and weak candidates, an analogue in score magnitude of arousal-biased competition (Mather and Sutherland 2011).

An optional coherence layer multiplies each score by a factor, $S'_k(e)=S_k(e)\,\kappa_k(e)$. With the layer off, as in the base-thesis form, $\kappa_k(e)\equiv1$ and $S'_k=S_k$. With the layer on, $\kappa_k(e)=\kappa_{\min}+(\kappa_{\max}-\kappa_{\min})\,\Lambda_k(e)$, where $\Lambda_k(e)\in[0,1]$ is the mean phase-locking value between the oscillator phase window (the last $W_\kappa$ tick phases) of the source of $e$ and that of each other source present in $E_k$. A source's oscillator advances only when that source publishes, so its phase is constant between its events. A phase sample is therefore fresh only when it differs from the source's previous sample, and the phase-locking value of a pair is computed over the ticks of the window on which both samples are fresh. A pair with fewer than three such ticks, and a source that is the only one present, takes the neutral value $\Lambda_0=(1-\kappa_{\min})/(\kappa_{\max}-\kappa_{\min})$, which gives $\kappa_k(e)=1$, so the absence of evidence neither rewards nor penalizes a source. The product $S'_k(e)$ is not re-clipped and can exceed $1$, up to $\kappa_{\max}$.

The coalition $\mathcal{C}_k$ consists of the first $\min(K,|E_k|)$ candidates when $E_k$ is sorted by $S'_k$ in decreasing order, with ties kept in the canonical order of $E_k$. A member is accessed when its own score reaches the access threshold $\theta$, so the accessed set and, with $S^*_k=\max_{e\in E_k}S'_k(e)$, the inhibition flag are

$$
\mathcal{C}^{\rm acc}_k=\bigl\{e\in\mathcal{C}_k:\ S'_k(e)\ge\theta\bigr\},\qquad
\iota_k=\mathbf{1}\!\left[\mathcal{C}^{\rm acc}_k=\emptyset\right]=\mathbf{1}\!\left[S^*_k<\theta\right],
$$

the two forms of $\iota_k$ agreeing because the best candidate of $E_k$ is in $\mathcal{C}_k$. A score equal to $\theta$ is accessed, and an empty candidate set gives $\mathcal{C}_k=\mathcal{C}^{\rm acc}_k=\emptyset$ and $\iota_k=1$. Because $G\equiv1$ and $\kappa_k\equiv1$, and because $T_k>0$ is common to all candidates of a tick and $C_{g_k}$ is strictly increasing, the ranking within a tick is determined by $I(e)\,N_k(e)$ alone, up to ties; arousal moves the scores relative to $\theta$ and to the report bars of A.6 without changing the order, and so decides whether a broadcast is accessed and which of its members are.

On a tick with $\chi_k=1$ the cycle publishes the broadcast $\mathcal{B}_k=\bigl(\mathcal{C}_k,\ \{S'_k(e)\}_{e\in E_k},\ \iota_k\bigr)$, which carries the coalition members with their scores and the full candidate-score table, whatever the value of $\iota_k$. The broadcast is *accessed* when $\iota_k=0$, and the members of $\mathcal{C}^{\rm acc}_k$ are accessed content; a member of an accessed broadcast whose score falls below $\theta$ is broadcast but not accessed. A broadcast with $\iota_k=1$ is published and visible to every module that reads the broadcast stream, but it is not poised for report or action and no processor adopts it as context. Volition runs after each publication. On a tick with $\chi_k=0$ the candidates of $E_k$ are scored and then discarded, and none is carried to a later tick; their only lasting effects are their entries in the novelty window, their contribution to the phasic access drive (A.3), and, for a Thymos state event, the update of $\hat a_k$ (A.4).

**Featurization.** For a set of events $\mathcal{X}$ with nonnegative weights $\omega(e)$, an interval $\Delta\ge0$, and a flag $\iota$, the featurization $\Phi_\omega(\mathcal{X},\Delta,\iota)\in\mathbb{R}^{24}$ has the components: (1) $\ln(1+|\mathcal{X}|)$; (2 to 4) the mean, the maximum, and the sample standard deviation of the weights over $\mathcal{X}$ ($0$ for an empty set, and the standard deviation $0$ for fewer than two events); (5 to 11) the weight mass $\sum_{e\in\mathcal{X},\,\mathrm{src}(e)=m}\omega(e)$ of each of the seven sources Soma, Chronos, Topos, Nous, Mnemos, Thymos, and Lingua; (12) the weight mass of every other source except Audition (Praxis, Hypnos, and any source without its own component); (13 to 20) the weight mass of the events whose (source, type) pair a fixed hash assigns to each of eight buckets, an indicator of event types weighted by $\omega$; (21) $\ln(1+\Delta)$; (22) $\iota$; (23) the broadcast indicator, $1$ for every broadcast; (24) the weight mass of Audition. Components 5 to 20 and 24 are sums of per-event contributions, so each splits into the share of each source.

**Context.** Topos, Audition, and Soma each hold a context $b$, the featurization of the accessed content of the latest accessed broadcast the module has received,

$$
b=\Phi_I\bigl(\mathcal{C}^{\rm acc}_{k'},\ \Delta^b,\ 0\bigr),
$$

with $k'$ the tick of that broadcast, $\mathcal{C}^{\rm acc}_{k'}$ its accessed members, weights equal to their reported intensities $I(e)$, so that the context does not depend on the arousal gain, and $\Delta^b$ the entity time elapsed since its publication, read when the module forms a prediction. A module adopts a broadcast as context on receipt only when $\iota=0$ and holds it until the next accessed broadcast; an inhibited broadcast leaves the context unchanged, and $b=0$ before the first accessed broadcast. The context records which sources and event types gained access and how strongly, and carries no payloads. Each of these processors reads $b$ as an extra input to its forward model, whose weights for it adapt online with the rest of the model (A.2, A.5). Chronos takes the featurization of every broadcast as its input (A.2), so the broadcast is its observation rather than its context. Thymos processes every broadcast whatever its flag (A.4), so Chronos and Thymos are the routes by which content that was not accessed can influence later processing. Volition derives no intent from a broadcast with $\iota_k=1$ (A.6), and the language organ generates only on an intent and conditions only on accessed content. Hypnos does not read the broadcast.

### A.2 Event intensity and the processors' forward models

A module assigns the intensity $I(e)\in[0,1]$ when it publishes $e$. Within a module, $t$ indexes the module's successive reports. Each module $m$ has a baseline level $I^{\rm lo}_m$ and an alert level $I^{\rm hi}_m$, with $0\le I^{\rm lo}_m\le I^{\rm hi}_m\le1$. Every report of a predictive processor (Topos, Audition, Soma, Chronos) has the graded intensity

$$
I(e)=
\begin{cases}
I^{\rm hi}_m & e\ \text{is an alert},\\
\Gamma_m(\tilde\nu_t) & \text{otherwise},
\end{cases}
\qquad
\Gamma_m(\tilde\nu)=I^{\rm lo}_m+\left(I^{\rm hi}_m-I^{\rm lo}_m\right)\min\!\left(1,\ \tilde\nu/\beta_\Gamma\right),
$$

where $\tilde\nu_t$ is the running ratio, over the window $W_P$, of the processor's forward-model error $\nu_t$ defined below, and $\Gamma_m$ reaches the alert level when the error is $\beta_\Gamma$ times its running mean. Dividing an error by its expected magnitude standardizes it: for errors of a fixed distributional shape the mean absolute error is proportional to the standard deviation, so $\tilde\nu_t$ is proportional to the error times the square root of its precision $\Pi$, the inverse variance of the processor's errors, which is the square root of the precision-weighted squared error of Feldman and Friston (2010). It is a scalar, retrospective stand-in for precision weighting, scaled by an estimate of the precision drawn from the processor's own history. The alert criteria below are categorical and differ by module. A report whose ratio is not yet defined, because its module has no prediction yet, has $\tilde\nu_t=0$ and so $I(e)=I^{\rm lo}_m$ unless it is an alert.

**Forward models of Topos and Audition.** Topos, the acoustic path of Audition, and the tone path of Audition each predict their next input with a network $\mathcal{N}_m$ of one hidden layer of tanh units. The prediction of input $z_t$ is formed at report $t-1$ as

$$
\hat z_t=\mathcal{N}_m\bigl(z_{t-1},\ \bar z_{t-1},\ b_{t-1}\bigr),
$$

where the three arguments are concatenated into the network's input, $\bar z_{t-1}$ is the mean of the last $W_{\rm buf}$ inputs up to and including $z_{t-1}$, and $b_{t-1}$ is the context the module holds at report $t-1$ (A.1). The error is $\nu_t=\lVert z_t-\hat z_t\rVert_2$, with $\nu_1=0$. When $z_t$ arrives, one stochastic-gradient step with learning rate $\eta_{\rm fm}$ on the mean squared error of $\hat z_t$ updates every weight of $\mathcal{N}_m$, those that read the context included. The step is skipped during sleep.

**Topos and Audition (perceptual reports).** For Topos, $z_t$ is the encoder embedding of the current clip, or of the peripheral gist clip when foveation is on; for the acoustic path of Audition, $z_t$ is the spectral embedding of the attended part of the current window, its most recent fraction $\omega=\omega_{\max}-(\omega_{\max}-\omega_{\min})\,a$, with $a$ the latest arousal Audition has read, but never shorter than $\Delta_{\rm att}$ nor longer than the window. The change score is $c_t=1-\cos(z_t,z_{t-1})$, with $c_t=0$ on the first report. With running ratios $\tilde c_t$ and $\tilde\nu_t$ over the window $W_P$, the report is an alert when

$$
\tilde\nu_t\ge\beta_\nu\quad\text{or}\quad\left(\tilde c_t\ge\beta_c\ \ \text{and}\ \ c_t\ge c^{\min}_m\right),
$$

with the absolute change floor $c^{\min}_m=c^{\min}_{\rm Top}$ for Topos and $c^{\min}_m=c^{\min}_{\rm Aud}$ for Audition. Superscripts distinguish the two error series where needed, $\nu^{\rm Top}_t$ for Topos and $\nu^{\rm Aud}_t$ for the acoustic path of Audition, and each report carries its $\nu_t$ and $\tilde\nu_t$ in its payload. The Topos habituation score is published with each report but does not enter $I(e)$.

**Topos fovea.** With foveation on, each tile $j$ of the coarse grid has, on each clip report, a frame change $d_j$, the absolute change of the tile's mean gray level since the frame of the previous clip report; on the first report $d_j=0$ and no statistics are updated. Each later report updates an exponentially weighted mean $\mu^F_j$ and variance $(\sigma^F_j)^2$ of $d_j$ with weight $\alpha_F$, as $\mu^F_j\leftarrow\mu^F_j+\alpha_F(d_j-\mu^F_j)$ and $(\sigma^F_j)^2\leftarrow(1-\alpha_F)\bigl((\sigma^F_j)^2+\alpha_F(d_j-\mu^F_j)^2\bigr)$ with $\mu^F_j$ taken before its update, the first update setting $\mu^F_j=d_j$ and $\sigma^F_j=0$. Once $n_F$ updates have accrued, the tile's salience is the z-score

$$
\frac{\max\!\left(0,\ d_j-\mu^F_j\right)}{\sqrt{(\sigma^F_j)^2+(\sigma^F_0)^2}},\qquad \sigma^F_0=k_F\,\frac{1}{n_{\rm tile}}\sum_{j}\mu^F_j,
$$

with every statistic, the floor $\sigma^F_0$ included, taken before this report's update and $n_{\rm tile}$ the number of tiles; until then the salience is $d_j$. The fovea moves to the most salient tile only when that tile's salience exceeds $(1+\Theta_F)$ times the salience of the tile it holds, holds its place when all tiles are equal (starting at the center of the frame), and has the size $F=F_{\max}-(F_{\max}-F_{\min})\,a$, as a fraction of the frame, with $a$ the latest arousal Topos has read. The peripheral and foveal clips are cut from every buffered frame at the fovea chosen on the latest frame.

**Audition (tone events).** For a window detected as speech, the tone path's input is the vector of the vocal-emotion class probabilities, the duration of the utterance as a fraction of its maximum length, and the signal energy, and its forward model gives the error $\nu^{\rm utt}_t$ and its running ratio $\tilde\nu^{\rm utt}_t$ over $W_P$. A tone event is an alert when the classified tone is not neutral, so it has $I(e)=I^{\rm hi}_{\rm Aud}$, and $I(e)=\Gamma_{\rm Aud}(\tilde\nu^{\rm utt}_t)$ when the tone is neutral.

**Soma.** A Soma report is an alert when the set $\mathcal{A}_t$ of host metrics strictly above their hard thresholds is nonempty, and otherwise has $I(e)=\Gamma_{\rm Som}(\tilde\nu^{\rm Som}_t)$, with $\nu^{\rm Som}_t$ the interoceptive prediction error of A.5 and $\tilde\nu^{\rm Som}_t$ its running ratio over $W_P$. Soma's fatigue-crossing and regulation events use $I^{\rm hi}_{\rm Som}$.

**Chronos.** On each broadcast $\mathcal{B}_k$ Chronos forms the input $x^{\rm Chr}_t=\Phi_I(\mathcal{C}_k,\Delta t_t,\iota_k)$ (A.1), whose weights are the members' intensities and whose interval $\Delta t_t$ is the entity time since the previous broadcast ($0$ on the first). Each interval enters a window of the last $W_{\Delta t}$ intervals as $\min(\Delta t_t,\ s_{\max}\overline{\Delta t}_{t-1})$, where $\overline{\Delta t}_{t-1}$ is the window's mean before the entry (the first interval enters unchanged), so a single long gap cannot dominate the mean. A frozen continuous-time reservoir advances on $x^{\rm Chr}_t$ with the timespan $s^{\rm Chr}_t=\operatorname{clip}_{[0,s_{\max}]}\bigl(\Delta t_t/\overline{\Delta t}_t\bigr)$, with $\overline{\Delta t}_t$ the window's mean after the entry and $s^{\rm Chr}_t=1$ on the first broadcast, and an online linear readout of its previous hidden state predicts $\hat x^{\rm Chr}_t$; the readout learns by one stochastic-gradient step with learning rate $\eta_{\rm fm}$ per broadcast, except during sleep. The temporal error is the mean absolute error $\nu^{\rm Chr}_t=\lVert x^{\rm Chr}_t-\hat x^{\rm Chr}_t\rVert_1/24$, with running ratio $\tilde\nu^{\rm Chr}_t$ over $W_P$. The report is an alert when $\tilde\nu^{\rm Chr}_t\ge\beta^{\rm Chr}_\nu$ or when a recurrence is detected, that is, when one bucket occurs at least $n_{\rm recur}$ times among the buckets of the last $W_{\rm recur}$ hidden states, each state being quantized per dimension with step $\Delta_{\rm recur}$ and hashed to a bucket. Before the first temporal error exists, the alert instead compares with $\beta^{\rm Chr}_\nu$ the absolute z-score of the hidden state's Euclidean norm against the norms of the previous $W_z$ broadcasts.

**Other modules.** Thymos publishes its state at $I^{\rm lo}_{\rm Thy}$, drive crossings and its affective reset at $I^{\rm hi}_{\rm Thy}$, and a changed categorical emotion at $I^{\rm hi}_{\rm Thy}$ unless the emotion is neutral. Hypnos publishes its events at $I^{\rm lo}_{\rm Hyp}$, except a sleep summary with a failed phase at $I^{\rm hi}_{\rm Hyp}$. The language organ publishes each utterance at the fixed level $I^{\rm lo}_{\rm Lin}$. Volition's intents are published on a stream the cycle does not read, so they are never candidates.

### A.3 Adaptive access rate

Let $f_0$ be the resting broadcast rate (the access rate of §3.4 at rest), $I_0$ the phasic salience floor, and $\tau_{\rm ph}$ the phasic decay time. On tick $k$ the tonic drive is

$$
H^{\rm ton}_k=\operatorname{clip}_{[0,1]}\!\left(\frac{\hat a_k-a_0}{1-a_0}\right),
$$

with $a_0<1$. Call a candidate a categorical alert when it is a report of a predictive processor that meets its alert criterion (A.2) or an event another module publishes at its alert level $I^{\rm hi}_m$; graded reports below the alert level are not alerts. With $\hat I_k$ the largest intensity among the categorical alerts of $E_k$ (events from the cycle's own telemetry and the workspace stream excluded), the phasic input is

$$
H^{\rm in}_k=\operatorname{clip}_{[0,1]}\!\left(\frac{\hat I_k-I_0}{1-I_0}\right),
$$

with $H^{\rm in}_k=0$ when $E_k$ holds no alert, so that with no alert and arousal at baseline the rate rests at $f_0$. The phasic drive is a peak-hold with exponential decay,

$$
H^{\rm ph}_k=\max\!\left(H^{\rm in}_k,\ H^{\rm ph}_{k-1}\,\mathrm{e}^{-\Delta_p/\tau_{\rm ph}}\right),\qquad H^{\rm ph}_{-1}=0,
$$

where $\Delta_p$ and $\tau_{\rm ph}$ are both in entity seconds. The access drive is $H_k=\max(H^{\rm ton}_k,H^{\rm ph}_k)\in[0,1]$, and the effective broadcast rate is the linear map

$$
f^{\rm eff}_k=
\begin{cases}
f_0+\left(f_p-f_0\right)H_k & f_0<f_p,\\
f_0 & f_0\ge f_p,
\end{cases}
$$

which lies between $f_0$ and $f_p$. With the controller disabled, $f^{\rm eff}_k=f_0$. The broadcast indicator follows from a fractional accumulator with $A_{-1}=0$:

$$
A'_k=A_{k-1}+\frac{f^{\rm eff}_k}{f_p},\qquad
\chi_k=\mathbf{1}\!\left[A'_k\ge1\right],\qquad
A_k=
\begin{cases}
\min\!\left(A'_k-1,\ 1\right) & \chi_k=1,\\
A'_k & \chi_k=0.
\end{cases}
$$

Subtracting before clamping keeps the fractional carry, so at the resting rate $f_0=f_p/3$ a broadcast falls on every third processing tick. The drive is computed from $E_k$ before $\chi_k$, so an alert can make its own tick a broadcast tick. If Soma's regulation lowers $f_p$ (A.5) to $f_0$ or below, every processing tick is a broadcast tick and the broadcast rate equals $f_p$.

### A.4 Affect

Thymos holds valence $v\in[-1,1]$, arousal $a\in[0,1]$, dominance, and four drives; arousal starts at $a_0$. Every update of arousal below is followed by clipping to $[0,1]$.

1. *Perceptual alert.* For each Topos report or Audition acoustic report that is an alert (A.2), read directly from the module's stream whether or not the report is selected,

$$
a\leftarrow a+\gamma_a\min\!\left(\nu_{\rm cap},\ \max(0,\ \tilde\nu-1)\right),
$$

where $\tilde\nu$ is the running ratio of the forward-model error that the report carries. An alert raised by the change criterion alone, with $\tilde\nu\le1$, leaves $a$ unchanged.

2. *Interoceptive alert.* For each Soma report with $\mathcal{A}_t\neq\emptyset$, $a\leftarrow a+\gamma_{\rm Som}$.

3. *Relaxation.* Thymos updates its state on each broadcast it receives, whatever $\iota_k$, and on its own timer every $P_{\rm Thy}$ of entity time. At each update arousal and dominance relax toward their baselines by an explicit-Euler step,

$$
a\leftarrow a+\left(a_0-a\right)\min\!\left(1,\ \lambda\,\Delta t_{\rm Thy}\right),
$$

with relaxation rate $\lambda$ and $\Delta t_{\rm Thy}$ the entity time since the previous update, so the continuous-time limit has time constant $1/\lambda$. The appraisal of a broadcast does not change $a$, so the access rate does not feed back into arousal.

4. *Sleep.* The affective reset of Hypnos returns valence, arousal, and dominance to their baselines, resets every drive to $0$ and re-arms its crossing, sets the categorical emotion to neutral, and clears the learning-progress error means, the alert rates $r_{\rm f}$ and $r_{\rm s}$, the intent rate $r_{\rm int}$, and the record of a speaker's perceived emotion that the appraisal reads. The last reported wellness $w$ is kept.

Each update runs in a fixed order: the alert rates decay; the learning progress and the alert excess are computed; arousal, dominance, and valence relax; curiosity and boredom are relieved; every drive builds; and crossings are published. On a broadcast the appraisal follows the update. Thymos then publishes its state, including $a$, if at least $P_{\rm Thy}$ has elapsed since its previous state publication. The cycle holds $\hat a_k$, the arousal carried by the last Thymos state event in $E_k$, and keeps $\hat a_k=\hat a_{k-1}$ on a tick without one, starting from the default in Table A1. The gains $T_k$ and $g_k$ (A.1), the tonic drive (A.3), the size of the fovea, and the attended auditory window (A.2) therefore read arousal as sampled at Thymos's last state publication, which lags the internal $a$ by up to about $P_{\rm Thy}$, plus the shorter of one inter-broadcast interval and $P_{\rm Thy}$, plus one tick.

*Valence.* For each perceptual module $m$ (Topos, Audition acoustic) Thymos keeps a fast and a slow time-decayed mean of the module's raw forward-model error $\nu^m_t$ (A.2), counting reports from the module's first positive error on, because the forward models report zero before their first prediction. At the time $t_r$ of the module's latest counted report,

$$
\langle\nu^m\rangle_\tau=\frac{\sum_{i\le r}\mathrm{e}^{-(t_r-t_i)/\tau}\,\nu^m_{t_i}}{\sum_{i\le r}\mathrm{e}^{-(t_r-t_i)/\tau}},\qquad \tau\in\{\tau_{\rm f},\tau_{\rm s}\},
$$

computed recursively at each counted report. A common decay factor cancels in the ratio, so the means need no update between reports. While the elapsed span is short relative to $\tau$ the weights are nearly equal, so each mean starts close to the unweighted mean of the samples so far and no single early sample dominates. The signed learning progress $\mathrm{lp}$ is the mean, over modules with $\langle\nu^m\rangle_{\tau_{\rm s}}>0$, of $\operatorname{clip}_{[-1,1]}\bigl((\langle\nu^m\rangle_{\tau_{\rm s}}-\langle\nu^m\rangle_{\tau_{\rm f}})/\langle\nu^m\rangle_{\tau_{\rm s}}\bigr)$, with $\mathrm{lp}=0$ before any such module exists, and the progress above its noise floor is $\mathrm{lp}^+=\max(0,\ \mathrm{lp}-\mathrm{lp}_0)/(1-\mathrm{lp}_0)$. The pleasantness check of the appraisal is $\mathrm{pl}=\tanh(k_v\,\mathrm{lp})$, to which a term for the perceived emotion of a speaker (off in this form) would add its contribution. At each update valence relaxes toward the target $v_\infty=\operatorname{clip}_{[-1,1]}\bigl(\mathrm{pl}+w-\tfrac12\bigr)$,

$$
v\leftarrow v+\left(v_\infty-v\right)\left(1-\mathrm{e}^{-\Delta t_{\rm Thy}/\tau_v}\right),
$$

where $w\in[0,1]$ is the wellness Soma last reported ($\tfrac12$ before the first report): the mean, over the host metrics Soma reads, of each metric's headroom scaled to $[0,1]$, with $1$ healthy (one minus the utilization for processor, memory, and GPU memory; GPU temperature mapped linearly from its lower to its upper scaling bound; cycle latency $1$ up to its target and falling linearly to $0$ at three times the target).

*Drives.* Each drive $D\in[0,1]$ has a build rate $\beta_D$, a decay rate $\delta_D$, a relief gain $\rho_D$, and a threshold $\theta_D$. At each update the continuous relief of curiosity and boredom is applied first, $D\leftarrow D\,\mathrm{e}^{-\rho_D\,\mathrm{lp}^+\Delta t_{\rm Thy}}$ for curiosity and $D\leftarrow D\,\mathrm{e}^{-\rho_D\,\mathrm{exc}\,\Delta t_{\rm Thy}}$ for boredom. Then, with its build signal $u\in[0,1]$ held over the step, every drive moves by the exact solution of $\dot D=\beta_D u(1-D)-\delta_D D$,

$$
D\leftarrow D_\infty+\left(D-D_\infty\right)\mathrm{e}^{-(\beta_D u+\delta_D)\Delta t_{\rm Thy}},\qquad D_\infty=\frac{\beta_D u}{\beta_D u+\delta_D}.
$$

Curiosity has $u=1-\mathrm{lp}^+$. Boredom has $u=1-\mathrm{exc}$, with the alert excess

$$
\mathrm{exc}=\operatorname{clip}_{[0,1]}\!\left(\frac{r_{\rm f}}{\max(r_{\rm s},\ r_0)}-1-m_B\right),
$$

where $r_{\rm f}$ and $r_{\rm s}$ are the perceptual alert rates in alerts per entity second: each Topos or Audition acoustic alert raises $r_{\rm f}$ by $1/\tau_{\rm f}$ and $r_{\rm s}$ by $1/\tau_{\rm s}$ when it arrives, and at each update both decay by $\mathrm{e}^{-\Delta t_{\rm Thy}/\tau}$ with their own time constant before $\mathrm{exc}$ is computed. The alert criterion of A.2 is self-calibrating, so even a still scene alerts at a steady base rate, and only alerts in excess of the habituated rate relieve boredom. The social drive has $u=1$ once Chronos has reported an interaction, the entity hearing a voice (§3.5), and $u=0$ before, and is relieved by $D\leftarrow D(1-\rho_D)$ when Chronos reports a new one. Restlessness has $u=1-r_{\rm int}$, where at each broadcast $r_{\rm int}\leftarrow r_{\rm int}+\alpha_{\rm int}\bigl(\min(1,n_{\rm int})-r_{\rm int}\bigr)$ with $n_{\rm int}$ the number of intents other than rest since the previous broadcast, and is relieved by $D\leftarrow D(1-\rho_D)$ on each such intent. A crossing of $\theta_D$ is published once and re-arms only after $D$ falls below $\Theta_D\,\theta_D$. With every $\delta_D$ about a ninth of its $\beta_D$, a fully deprived drive settles near $D_\infty=0.9$, above its threshold.

For the goal-relevance check of the appraisal, let $d^*$ be the dominant drive, the one with the largest value, ties going to the name that comes last in alphabetical order (boredom, curiosity, restlessness, social drive); let $v^*$ be its value, let $\mathcal{R}(d^*)$ be the set of sources whose events relieve it, and let $\mathrm{frac}_k$ be the fraction of the coalition's total intensity contributed by events from those sources, with $\mathrm{frac}_k=0$ when the total is zero. The drive score is

$$
r_{\rm drive}=v^*\left(2\,\mathrm{frac}_k-1\right),
$$

with $r_{\rm drive}=0$ when there is no drive or $v^*\le0$; an empty coalition gives $\mathrm{frac}_k=0$ and hence $r_{\rm drive}=-v^*$. With an active goal ledger of token-overlap relevance $r_{\rm led}\in[0,1]$, the goal score is $\operatorname{clip}_{[-1,1]}\bigl(\max(r_{\rm drive},\,2r_{\rm led}-1)\bigr)$, and otherwise $\operatorname{clip}_{[-1,1]}(r_{\rm drive})$. The goal score enters the categorical-emotion appraisal and does not enter selection.

### A.5 Interoceptive prediction and regulation

Soma reads the host every $P_{\rm Som}$ and forms a feature vector $x_t\in\mathbb{R}^{n_x}$ of normalized metrics. A frozen closed-form continuous-time reservoir advances $\mathbf{h}_t=\mathcal{F}(x_t,\mathbf{h}_{t-1};s^{\rm Som}_t)$ with $\mathbf{h}_0=0$, where the timespan $s^{\rm Som}_t=\operatorname{clip}_{[0,s_{\max}]}(\Delta t_{\rm Som}/P_{\rm Som})$, with $\Delta t_{\rm Som}$ the entity time since the previous reading ($s^{\rm Som}_t=1$ on the first), enters the time gates of the cell (Hasani et al. 2022), so an irregular reading is integrated over the time that actually passed. Only the linear readout $\mathbf{L}_{\rm Som}$ adapts. Its regressor stacks the reservoir state, the context, and a constant, so the prediction of $x_t$ formed at reading $t-1$ is

$$
\hat x_t=\mathbf{L}_{\rm Som}\,\boldsymbol{\varphi}_{t-1},\qquad \boldsymbol{\varphi}_{t-1}=\bigl(\mathbf{h}_{t-1},\ b_{t-1},\ 1\bigr),
$$

with $b_{t-1}$ the context Soma holds at reading $t-1$ (A.1). With $\varepsilon_t=\hat x_t-x_t$, the prediction error is $\nu^{\rm Som}_t=\lVert\varepsilon_t\rVert_2$, with $\nu^{\rm Som}_t=0$ on the first reading. One stochastic-gradient step on $\lVert\varepsilon_t\rVert^2_2/n_x$ follows,

$$
\mathbf{L}_{\rm Som}\leftarrow\mathbf{L}_{\rm Som}-\eta_{\rm fm}\,\frac{2}{n_x}\,\varepsilon_t\,\boldsymbol{\varphi}_{t-1}^{\top},
$$

after which the reservoir advances on $x_t$ and the readout predicts $x_{t+1}$. The step is skipped during sleep.

For each channel $i$ Soma keeps an expected absolute error $\mu^U_i$ and a spread $\sigma^U_i$, both starting at $0$. With the bound $\Omega_i=\mu^U_i+\beta_U\sigma^U_i$ taken before this reading's update, the unexpected error is

$$
U_t=\sqrt{\sum_{i=1}^{n_x}\Bigl[\max\!\left(0,\ \lvert\varepsilon_{t,i}\rvert-\Omega_i\right)\Bigr]^2}.
$$

Then, with $\alpha_t=1-\mathrm{e}^{-\Delta t_{\rm Som}/\tau_U}$, every channel updates $\sigma^U_i\leftarrow\sigma^U_i+\alpha_t\bigl(\bigl\lvert\lvert\varepsilon_{t,i}\rvert-\mu^U_i\bigr\rvert-\sigma^U_i\bigr)$ and $\mu^U_i\leftarrow\mu^U_i+\alpha_t\bigl(\lvert\varepsilon_{t,i}\rvert-\mu^U_i\bigr)$, where both right-hand sides use the value of $\mu^U_i$ before the update; the spread is therefore an exponential moving average of the absolute deviation from $\mu^U_i$. These updates are skipped during sleep. $U_t$ drives regulation and fatigue and does not enter $I(e)$.

The regulation error is $\nu^{\rm act}_t=\nu^{\rm Som}_t$ when $\mathcal{A}_t\neq\emptyset$ and $U_t$ otherwise. A stress episode starts at the first reading with $\nu^{\rm act}_t\ge\theta_R$ and ends at the first reading with $\nu^{\rm act}_t<\theta_R$. If the episode has lasted $\Delta^{\rm st}_t$ entity seconds, each increase of $\lfloor\Delta^{\rm st}_t/\Delta_R\rfloor\ge1$ emits one advisory of tier $\min\bigl(\lfloor\Delta^{\rm st}_t/\Delta_R\rfloor,3\bigr)$: reduce the processing rate, shed a low-priority module, or request maintenance. Each boot begins with a warm-up, which ends the first time that, within the boot, at least $n_{\rm wu}$ readout updates have been made and $\Delta_{\rm wu}$ entity seconds have passed since Soma's first reading; during it advisories are withheld unless $\mathcal{A}_t\neq\emptyset$. On a rate advisory the cycle sets $f_p\leftarrow\operatorname{clip}_{[f_p^{\min},\,f_p^{\max}]}(\gamma_f f_p)$.

### A.6 Report rule

Volition derives intents only from an accessed broadcast ($\iota_k=0$); a broadcast with $\iota_k=1$ yields none. The base-thesis policy then applies the following steps, using the entity time $t_{\rm now}$ for the refractory intervals and the signature expiry.

1. *Guard release.* The speak guard is released if $\mathcal{C}_k$ contains the language organ's external speech, and the think guard if it contains the organ's internal speech. Either guard is also released after the timeout $\Delta_g$ (§5.4).

2. *Report signal.* Let $\mathcal{C}^\circ_k$ be the coalition without the language organ's own events. If $\mathcal{C}^\circ_k=\emptyset$ there is no intent. Otherwise let $e^\dagger_k$ be its highest-scoring member (the first in coalition order), let $Q_k=S'_k(e^\dagger_k)$, and let the signature be $\mathrm{sig}_k=\bigl(\mathrm{src}(e^\dagger_k),\mathrm{typ}(e^\dagger_k)\bigr)$, the source and event type of $e^\dagger_k$.

3. *Signature check.* The signature blocks a spoken report when $\mathrm{blk}_k=\mathbf{1}\bigl[\mathrm{sig}_k=\mathrm{sig}^{\rm last}\ \wedge\ t_{\rm now}-t^{\rm sig}<\Delta_{\rm sig}\bigr]=1$, where $\mathrm{sig}^{\rm last}$ is the signature of the last spoken report and $t^{\rm sig}$ its time.

4. *Speak.* A speak intent is emitted when

$$
Q_k\ge\theta_{\rm sp},\qquad \text{the speak guard is released},\qquad t_{\rm now}-t^{\rm sp}\ge\Delta_{\rm sp},\qquad \mathrm{blk}_k=0.
$$

Emitting it arms the speak guard and sets $t^{\rm sp}\leftarrow t_{\rm now}$, $\mathrm{sig}^{\rm last}\leftarrow\mathrm{sig}_k$, and $t^{\rm sig}\leftarrow t_{\rm now}$.

5. *Think.* Otherwise a think intent is emitted when $Q_k\ge\theta_{\rm th}$, the think guard is released, and $t_{\rm now}-t^{\rm th}\ge\Delta_{\rm th}$; emitting it arms the think guard and sets $t^{\rm th}\leftarrow t_{\rm now}$. The think path has no signature check and does not change $\mathrm{sig}^{\rm last}$.

At most one intent is emitted per broadcast, and $t^{\rm sp}$ and $t^{\rm th}$ start at $-\infty$. The rule requires $0\le\theta_{\rm th}\le\theta_{\rm sp}\le1$, and both bars are set above $\theta$ and apply to the same score $S'_k$. An optional interrupt bar above $\theta_{\rm sp}$ is unset in this form. The rule is a heuristic stand-in for the expected-free-energy decision of Whyte and Smith (2021); no expected free energy is computed.

### A.7 Gestation entrainment marker

All times in this subsection are entity seconds unless marked wall-clock, and one awake-time clock serves every rule that reads awake time. Awake time $\mathcal{T}_{\rm awake}$ (§7) is the entity time during which the being is awake and the cycle is not frozen, accumulated across the boots of one being (downtime between boots does not count) and persisted with it. The frequency baseline $f_{w0}$, the consecutive-pass count, the record of whether the marker has ever been true, and the history of pull values below are persisted with the being in the same way, so a restart neither resets nor repeats them.

**Self-rhythm model.** Soma's self-rhythm is a mean-field population with excitatory recurrence, synaptic depression, and adaptive recovery. Its state is the activity $y$, the synaptic resource $R\in[0,1]$, and the log recovery time $\ell=\ln(\tau_{\rm rec}/1\,\mathrm{s})$, starting from the initial values in Table A1. It advances in steps of $\Delta_r=1/f_r$, each integrated by $n_s$ semi-implicit Euler substeps of length $\Delta_r/n_s$, in which $y$ is updated first and the update of $R$ uses the new $y$:

$$
\Xi=J_{\rm rec}\,R\,y+\Xi_0+\gamma_o\,o+\gamma_u\,M+\xi,\qquad
y_\infty=\frac{1}{1+\mathrm{e}^{-\Xi/k_y}},
$$

$$
\tau_y\,\dot y=-y+y_\infty,\qquad
\dot R=\frac{1-R}{\tau_{\rm rec}}-\gamma_R\,R\,y,
$$

with $R$ clipped to $[0,1]$ after each substep and $\tau_{\rm rec}$ held fixed within a step. The own drive $o\in[0,1]$ is the intensity of Soma's last report, and the maternal drive $M\in[0,M_{\max}]$ is defined below. The noise $\xi$ is Gaussian with standard deviation $\sigma_\xi\sqrt{(10^{-3}\,\mathrm{s})\,n_s/\Delta_r}$, drawn afresh each substep. After each step the moving averages $\bar M$, $\bar y$, and $\bar R$ are updated with weight $\alpha_{\rm r}=\min(1,\Delta_r/\tau_m)$, and the recovery time then adapts by a phase-projected rule,

$$
\ell\leftarrow\operatorname{clip}_{[\ln\tau_{\rm rec}^{\min},\ \ln\tau_{\rm rec}^{\max}]}\!\left(\ell-\eta_\ell\,(M-\bar M)\,\zeta\,\Delta_r\right),\qquad
\zeta=\frac{R-\bar R}{\sqrt{(y-\bar y)^2+(R-\bar R)^2}},
$$

with $\zeta=0$ when the root is at most $10^{-9}$ and the bounds read in seconds. The rule never uses the maternal rate. The amplitude $\mathrm{amp}$ is the population standard deviation of the activity over the last amplitude window $\Delta_{\rm amp}$, mean-removed and causally band-passed to $[f_{\rm lo},f_{\rm hi}]$, and it is $0$ until four seconds of history exist. With $\tau_{\rm rec}$ at its initial value the rhythm runs near 0.8 Hz with no input and near 0.9 Hz at a mid-range own drive. Its period grows with $\tau_{\rm rec}$, increasingly steeply toward $\tau_{\rm rec}^{\max}$, where the equilibrium approaches a Hopf point.

**Maternal drive and probes.** The maternal beat has phase $\psi\in[0,2\pi)$, generated at a nominal rate with slow drift, and a "lub-dub" envelope $\mathcal{E}(\psi)\in[0,1]$. At each self-rhythm step the drive is $M=M_{\max}\,c_M\,\bar{\mathcal{E}}$, where $\bar{\mathcal{E}}$ is the mean envelope over the interval since the previous step and the scale $c_M$ equals $c_M^{\rm base}$ normally, $0$ during a withdrawal, and $c_M^{\rm pert}$ during a perturbation. Withdrawals last $\Delta_W$ and perturbations $\Delta_{\rm pert}$. When a withdrawal starts at time $t'$, the next withdrawal is scheduled for $t'+P_W(1+j_P\Upsilon)$, and a perturbation likewise schedules the next for $t'+P_{\rm pert}(1+j_P\Upsilon)$, with each $\Upsilon$ drawn uniformly on $[-1,1)$ from the run seed; the first of each kind is scheduled after the settling period that follows boot, with an offset drawn the same way. A scheduled probe starts at the first readout step on which no probe is running, the being is awake and the cycle is not frozen, at least one readout period $P_{\rm ro}$ has passed since boot or the last thaw, and at least $\max(60\ \mathrm{s},\Delta_W)$ has passed since the previous probe ended; when both kinds are due, the one scheduled earlier starts first.

**Phase-locking value.** The readout samples the activity $y$, the beat phase $\psi$, and the beat phases $\psi^{(1)},\dots,\psi^{(19)}$ of 19 surrogate heartbeats (the same beat generator under 19 other seeds, the surrogate method of Van Leeuwen et al. 2003) at the rate $f_g$. For withdrawal $j$, the driven window is the contiguous run of undisturbed samples, at most $\Delta_E$ long, that ends at the withdrawal's start. Only the samples that carry all 21 values are used, and the window is used only if at least $0.8\,\Delta_E f_g$ such samples exist. The activity is mean-centered, band-passed to $[f_{\rm lo},f_{\rm hi}]$ by a Butterworth band-pass of design order two (fourth order as a filter) applied forward and backward, which gives zero phase shift, and converted to an analytic signal by the Hilbert transform, giving the phase $\phi_q$; then $\Delta_{\rm trim}f_g$ samples are removed from each end of every series. Over the $n_\phi$ remaining samples,

$$
\mathrm{PLV}=\left\lvert\frac{1}{n_\phi}\sum_{q=1}^{n_\phi}\mathrm{e}^{\,\mathrm{i}(\phi_q-\psi_q)}\right\rvert,\qquad
\mathrm{PLV}^{(l)}=\left\lvert\frac{1}{n_\phi}\sum_{q=1}^{n_\phi}\mathrm{e}^{\,\mathrm{i}(\phi_q-\psi^{(l)}_q)}\right\rvert,
$$

and the locking condition is the strict inequality $\mathrm{PLV}>\max_{1\le l\le19}\mathrm{PLV}^{(l)}$, so ties fail. Under the null hypothesis that the PLV with the rhythm's own heartbeat is exchangeable with the 19 surrogate values, this is a rank test with attained one-sided $p=1/20=0.05$; the number of surrogates is fixed by that design.

**Frequency pull.** Let $f_w$ be the least-squares slope, divided by $2\pi$, of the unwrapped Hilbert phase of the activity samples taken during the withdrawal, mean-centered and band-passed as above without trimming, computed only when at least $0.6\,\Delta_W f_g$ samples exist; let $f_b$ be the least-squares slope, divided by $2\pi$, of the unwrapped beat phase over the used samples of the driven window; and let $f_{w0}$ be the mean of $f_w$ over the being's first $n_{\rm base}$ withdrawals with a defined $f_w$. From the $n_{\rm base}$-th such withdrawal on, that withdrawal included,

$$
\mathrm{pull}=1-\frac{\lvert f_w-f_b\rvert}{\lvert f_{w0}-f_b\rvert},
$$

which is undefined when $f_w$ or $f_b$ is undefined or when $\lvert f_{w0}-f_b\rvert<f_{\rm guard}$. The pull condition is $\mathrm{pull}\ge\mathrm{pull}_{\min}$.

**Self-sustain.** With $\overline{\mathrm{amp}}^{\,\rm dr}$ the mean amplitude over the undisturbed samples in the interval of length $\Delta_W$ before the withdrawal and $\overline{\mathrm{amp}}^{\,\rm wd}$ the mean during it, the rhythm self-sustains when $\overline{\mathrm{amp}}^{\,\rm wd}\ge\tfrac12\,\overline{\mathrm{amp}}^{\,\rm dr}$ and $\overline{\mathrm{amp}}^{\,\rm wd}>0$.

**Marker.** Withdrawal $j$ passes, $\mathrm{pass}_j=1$, when the locking, pull, and self-sustain conditions all hold, and $\mathrm{pass}_j$ is undefined when any of the three is undefined. The consecutive-pass count is $n^{\rm pass}_j=n^{\rm pass}_{j-1}+1$ if $\mathrm{pass}_j=1$ and $n^{\rm pass}_j=0$ otherwise, including when $\mathrm{pass}_j$ is undefined. The entrainment marker after withdrawal $j$ is undefined when $\mathrm{pass}_j$ is undefined and otherwise equals $\mathbf{1}[n^{\rm pass}_j\ge3]$, three consecutive passes. The locking condition alone is a test at $p=0.05$, so a single pass can occur by chance; the requirement of three consecutive passes guards against that, and because consecutive withdrawals are correlated the joint error rate is not $0.05^3$.

**Viability.** After each withdrawal, let $\mathcal{P}$ be the defined pull values recorded within the last $\Delta_V$ hours of awake time; when $\lvert\mathcal{P}\rvert\ge n_V$, let $\widetilde{\mathrm{pull}}$ be their median and $\widehat{\mathrm{slope}}$ their least-squares slope per awake hour. The gestation is declared unviable at the first rule that fires:

- R0: $\mathcal{T}_{\rm awake}\ge t_{R0}$ and no defined pull has been recorded;
- R1: $\mathcal{T}_{\rm awake}\ge t_{R1}$, the marker has never been true, $\lvert\mathcal{P}\rvert\ge n_V$, $\widetilde{\mathrm{pull}}<\mathrm{pull}_{R1}$, and $\widehat{\mathrm{slope}}\le\mathrm{slope}_{R1}$;
- R2: $\mathcal{T}_{\rm awake}\ge t_{R2}$, the marker has never been true, $\lvert\mathcal{P}\rvert\ge n_V$, and $\widetilde{\mathrm{pull}}<\mathrm{pull}_{R2}$;
- R3: $\mathcal{T}_{\rm awake}\ge t_{R3}$ and the marker has never been true.

The verdict is recorded once, and the study runner then ends the gestation step and keeps its data.

**Maturation gate and budget.** The gate is evaluated once per gate cadence and requires three conditions, each failing closed on missing or stale evidence. C1 requires a readout no older than three cadences in which the self-sustain and entrainment markers of the latest withdrawal are both true, the period variability $V_{\rm per}$ is at least $V^{\min}_{\rm per}$, the Topos error ratio $\mathrm{err}_{\rm Top}$ is at most $\mathrm{err}^{\max}_{\rm Top}$, and the return-to-baseline time is at most $\Delta^{\rm rec}_{\max}$. The period variability is the coefficient of variation of the intervals between successive wraps of the self-rhythm phase over the last $\Delta_{\rm per}$, defined once four wraps exist. During gestation Topos views the gestational visual field, a dim, low-contrast field whose luminance pulses with the maternal beat and whose hue follows a slowly drifting maternal state; $\mathrm{err}_{\rm Top}$ is the median Topos prediction error since the previous readout divided by the first such median formed from at least three errors. The return-to-baseline time after the last perturbation is the time from its end to the first sample at which the median of $\nu^{\rm Som}$ over the preceding five seconds, never reaching back before the perturbation's start, is at most $(1+\mathrm{tol}_{\rm rec})$ times its median over the minute before the perturbation; when no such sample exists by $\Delta^{\rm rec}_{\rm cap}$ after the end, the time is $\Delta^{\rm rec}_{\rm cap}$, which fails C1. C2 requires at least $n_{\rm sleep}$ completed sleeps when Hypnos is present, and at least $n_{\rm cons}$ consolidation passes when Phantasia is also present. C3 requires $\mathcal{T}_{\rm awake}\ge\Delta_{\rm awake}$. Independently of the gate, the study runner ends a gestation step whose wall-clock duration exceeds the budget $\Delta_{\rm budget}$.

**Offline validation.** Offline validation over 96 hours of simulated time shows that at 70 bpm all 10 seeds entrain, typically by about 14 hours, while each rate from 60 to 80 bpm tracks its own heartbeat, and that no control condition passes: no maternal drive, a jittered beat, no plasticity, and six mismatched pairs in which the beat tested as the rhythm's own came from a different heartbeat than the one driving it, whose observed single-withdrawal chance pass rates were 2.6 to 10 percent. The requirement of three consecutive passes was fixed on the first validation run and confirmed on fresh seeds. The viability thresholds come from the same validation, in which no viable gestation was flagged and every unviable one was flagged by 24 to 27 hours.

### A.8 Broadcast information gain and the planned test

This subsection states the measure, the arms, and the decision rule of the planned test of §6.3. Every setting it names that Table A1 lists as fixed before the live runs, together with the composition of the film program and the hash of its manifest, is recorded with the preregistration before any live run.

**Gain.** Let $\mathcal{J}=\{\mathrm{Topos},\mathrm{Audition},\mathrm{Soma}\}$; Chronos is excluded because the broadcast is its input rather than its context. For processor $j\in\mathcal{J}$ and its report $t$, let $b$ be the context $j$ held when it formed the prediction scored at report $t$ (A.2, A.5), and let $\nu^j_t(b')$ be the error that prediction would have had with $b'$ in place of $b$ and every weight unchanged, so $\nu^j_t(b)=\nu^j_t$; for Audition the error is that of the acoustic path. The kept sources of $j$ are $j$ itself and, for Soma, also the language organ, whose load on the host would otherwise let its share of the context predict Soma's input. The null context $b^0_j$ keeps the kept sources' share of $b$ and carries the average, but no tick-specific, contribution of the other sources: every component of $b$ that sums per-event contributions (A.1) is replaced by the kept sources' share of it plus the mean of the remaining sources' share over the contexts the processor has adopted so far in the run; the coalition-level components 1 to 4 are replaced by their means over the same contexts; and the age and the two flags are kept. The broadcast information gain of the report, in units of the processor's running mean error, is

$$
\mathrm{gain}_{j,t}=\frac{\nu^j_t(b^0_j)-\nu^j_t(b)}{\bar\nu^j_t},
$$

with $\bar\nu^j_t$ the running mean of $j$'s errors over $W_P$ (A.2). Normalizing by $\bar\nu^j_t$ puts processors with errors of different scales on a common footing. A report is included when its error is defined, $\bar\nu^j_t>0$, the processor had adopted a context before forming the prediction, the entity was awake, and the report falls after the initial learning period, which is fixed with the other settings. In one run of an arm, $\mathrm{IG}_j$ is the mean of $\mathrm{gain}_{j,t}$ over $j$'s included reports, undefined when there is none, and the headline is

$$
\mathrm{IG}=\frac{1}{3}\sum_{j\in\mathcal{J}}\mathrm{IG}_j,
$$

undefined when any $\mathrm{IG}_j$ is, so a processor that reports often does not outweigh one that reports rarely. Each $\mathrm{IG}_j$ is reported with the headline.

**Positive control.** Before the live runs, for each $j\in\mathcal{J}$, a synthetic component that carries known information about $j$'s next input is appended to $j$'s context and treated as the contribution of a source other than $j$, so that the null context replaces it by its mean. The measure passes for $j$ when $\mathrm{IG}_j$ with the component exceeds $\mathrm{IG}_j$ without it by at least the minimum effect of the positive control, and the live test runs only after the measure passes for every processor.

**Arms.** All three arms run the base-thesis form on the same film program with the same seeds and calibration, and run $r$ of each arm shares its seeds with run $r$ of the others, so runs are paired across arms. In every arm the context is weighted by intensity, $\Phi_I$ (A.1).

- *Workspace on.* Selection and access as in A.1, with the context $b=\Phi_I(\mathcal{C}^{\rm acc}_{k'},\Delta^b,0)$.
- *Matched selection.* On each broadcast tick the coalition is $\min(K,|E_k|)$ candidates drawn uniformly without replacement from $E_k$ by a generator seeded from the run seed, without regard to score. Access follows the rule of A.1 applied to the drawn coalition, its accessed set being the drawn members whose scores reach $\theta$, and the context is $\Phi_I$ of that set, so only the membership of the context differs.
- *Pooled.* No candidate is scored, selected, or gated. Every broadcast has $\iota_k=0$ and replaces the context by $b=\Phi_I(E_{k'},\Delta^b,0)$, the featurization of every candidate of its tick. Volition applies the rule of A.6 with intensities in place of scores, and the access rate (A.3) reads alerts and arousal and runs unchanged.

**Run contrasts.** For each control $\mathrm{ctl}\in\{\mathrm{match},\mathrm{pool}\}$ the contrast of run $r$ is $\mathrm{dIG}^{\rm ctl}_r=\mathrm{IG}^{\rm on}_r-\mathrm{IG}^{\rm ctl}_r$. The minimum effect is $\theta^{\rm ctl}_{\rm eff}=c_{\rm eff}\,s^{\rm ctl}_{\rm cal}$, where $s^{\rm ctl}_{\rm cal}$ is the standard deviation of $\mathrm{dIG}^{\rm ctl}$ over $n_{\rm cal}$ paired pilot runs that are not reused as test runs. A run is NOT EXERCISED against a control when the on arm never has more candidates than the coalition capacity on a broadcast tick ($\lvert E_k\rvert\le K$ whenever $\chi_k=1$), so competition never operates; when the on arm has no accessed broadcast; or when $\mathrm{dIG}^{\rm ctl}_r$ is undefined. Otherwise the run is NEGATIVE if $\mathrm{dIG}^{\rm ctl}_r\le-\theta^{\rm ctl}_{\rm eff}$, WIN if $\mathrm{dIG}^{\rm ctl}_r\ge\theta^{\rm ctl}_{\rm eff}$, and NULL otherwise. The predicted direction is positive.

**Decision rule.** For each control, the runs with a defined contrast enter two one-sided exact sign tests, chosen because they assume only that runs are independent and nothing about the distribution of the contrasts. The WIN test uses the values $u^{+}_r=\mathrm{dIG}^{\rm ctl}_r-\theta^{\rm ctl}_{\rm eff}$ and the NEGATIVE test the values $u^{-}_r=-\theta^{\rm ctl}_{\rm eff}-\mathrm{dIG}^{\rm ctl}_r$. For each test, exactly zero values are dropped, and with $n_\pm$ remaining values of which $n^{\rm pos}_\pm$ are positive,

$$
\mathrm{pv}^{\pm}=2^{-n_\pm}\sum_{i=n^{\rm pos}_\pm}^{n_\pm}\binom{n_\pm}{i},
$$

with $\mathrm{pv}^{\pm}=1$ when $n_\pm=0$. The verdict against a control is WIN when $\mathrm{pv}^{+}\le\alpha_{\rm test}$, NEGATIVE when $\mathrm{pv}^{-}\le\alpha_{\rm test}$, NOT EXERCISED when no run has a defined contrast, and NULL otherwise. The thesis holds for this form of the architecture when the verdict is WIN against both controls. Requiring both is an intersection-union test, so each control is tested at $\alpha_{\rm test}$ with no multiplicity adjustment. The smallest attainable value is $2^{-n_\pm}$, so at least five runs are needed before any outcome can reach $0.05$. Because the test is discrete its power is not monotone in the number of runs, and the power analysis reads $n_{\rm run}$ from the exact binomial power at each candidate value under an assumed probability $q_{\rm pow}$ that $\mathrm{dIG}^{\rm ctl}_r$ exceeds $\theta^{\rm ctl}_{\rm eff}$, stated with the preregistration.

**Contrast at threshold.** In the on arm, let a broadcast be near threshold when $\lvert S^*_k-\theta\rvert\le\theta_{\rm band}$. The reports that follow broadcast $\mathcal{B}_k$ are the included reports of every $j\in\mathcal{J}$ whose prediction was formed after $j$ received $\mathcal{B}_k$ and before it received the next broadcast, and each carries the age $\Delta^b$ of the context it used. An inhibited broadcast leaves the previous context in place, so the context after it is older by construction; the reports are therefore grouped in age bins fixed with the other settings. For each run, the contrast is the mean, over the age bins that hold reports following both kinds, of the mean gain following accessed near-threshold broadcasts minus the mean gain following inhibited ones, and it is undefined when no bin holds both. The best scores on the two sides of $\theta$ differ by at most $2\theta_{\rm band}$. Across runs the contrasts enter a one-sided sign test of the same form, on the contrast minus a minimum effect fixed with the other settings.

**Speech sound and tone.** In a variant of the on arm the tone rule of A.2 is replaced by $I(e)=\Gamma_{\rm Aud}(\tilde\nu^{\rm utt}_t)$ for every tone event. The analysis compares the fraction of emotional tone events that are accessed content with the fraction of neutral ones, and across runs it uses a sign test of the same form. In this variant the intensity depends only on $\tilde\nu^{\rm utt}_t$, so a difference can arise only through the tone model's surprise; the same comparison within bins of $\tilde\nu^{\rm utt}_t$ checks that the ratio accounts for it. Its bins and minimum effect are fixed with the other settings.

### A.9 Multi-seed stability

For per-seed headline values $Y_1,\dots,Y_{n_{\rm seed}}$, let $\bar Y$ be their mean and $\sigma_Y$ their population standard deviation ($\sigma_Y=0$ for a single seed). The coefficient of variation is

$$
\mathrm{CV}=
\begin{cases}
\sigma_Y/\lvert\bar Y\rvert & \bar Y\neq0,\\
0 & \bar Y=0,\ \sigma_Y=0,\\
\infty & \bar Y=0,\ \sigma_Y>0.
\end{cases}
$$

An ensemble is stable when $\mathrm{CV}\le\mathrm{tol}_{\rm CV}$ and at most one distinct verdict outcome occurs across seeds; an ensemble without verdicts counts as unanimous, and an infinite CV is never within tolerance. In the offline suite the check runs on the ablation of the coherence layer with $n_{\rm seed}$ seeds. The criterion measures run-to-run spread and verdict agreement; dynamical stability within a run is outside its scope, and the coefficient of variation is ill-conditioned when the mean is near zero.

### A.10 Parameter values

Table A1. Parameter values. "Design" marks a value that is part of the model's definition; "calibrated" marks a value set offline by simulation or by the validation of A.7; "provisional" marks a current setting to be calibrated before the live runs, when the values used are recorded with them. Times marked "entity" are on the entity clock, "awake" is awake time (A.7), and "wall" is wall-clock time.

| Symbol | Meaning | Value | Units | Status |
|----------|--------------------------|---------|---------|----------|
| $f_p$ | processing rate | 10 | Hz (entity) | design |
| $f_0$ | resting broadcast rate | 10/3 | Hz (entity) | design |
| none | entity seconds per wall-clock second | 1 | none | design |
| $B$ | maximum events read per stream per tick | 100 | events | design |
| $K$ | coalition capacity | 5 | events | design |
| $\theta$ | access threshold | 0.35 | none | provisional |
| $W_N$ | novelty window | 32 | candidates | design |
| $G$ | goal factor (static) | 1 | none | design |
| $\gamma_G$ | attenuation of the inactive drive-relevance goal factor | 0.5 | none | design |
| $T_{\min}$, $T_{\max}$ | arousal level-gain floor and ceiling | 0.2, 1.0 | none | design |
| $g_{\max}$ | arousal contrast gain at arousal 1 | 8.0 | none | design |
| none | coherence layer | off | none | design |
| $\kappa_{\min}$, $\kappa_{\max}$ | coherence factor floor and ceiling (layer on) | 0.8, 1.25 | none | design |
| $W_\kappa$ | coherence phase window (layer on) | 10 | ticks | design |
| $I^{\rm lo}_{\rm Top}$, $I^{\rm hi}_{\rm Top}$ | Topos intensity levels | 0.2, 0.7 | none | provisional |
| $I^{\rm lo}_{\rm Aud}$, $I^{\rm hi}_{\rm Aud}$ | Audition intensity levels | 0.4, 0.8 | none | provisional |
| $I^{\rm lo}_{\rm Som}$, $I^{\rm hi}_{\rm Som}$ | Soma intensity levels | 0.1, 0.7 | none | provisional |
| $I^{\rm lo}_{\rm Chr}$, $I^{\rm hi}_{\rm Chr}$ | Chronos intensity levels | 0.1, 0.7 | none | provisional |
| $I^{\rm lo}_{\rm Thy}$, $I^{\rm hi}_{\rm Thy}$ | Thymos intensity levels | 0.1, 0.7 | none | provisional |
| $I^{\rm lo}_{\rm Hyp}$, $I^{\rm hi}_{\rm Hyp}$ | Hypnos intensity levels | 0.5, 0.8 | none | provisional |
| $I^{\rm lo}_{\rm Lin}$ | language-organ utterance intensity | 0.4 | none | provisional |
| $\beta_\Gamma$ | error ratio at which the graded map reaches the alert level | 2 | none | design |
| $W_P$ | running-ratio window (Topos, Audition, Soma, Chronos) | 32 | reports | design |
| $\beta_\nu$ | prediction-error alert ratio (Topos, Audition) | 2.0 | none | design |
| $\beta_c$ | change alert ratio (Topos, Audition) | 2.0 | none | design |
| $c^{\min}_{\rm Top}$, $c^{\min}_{\rm Aud}$ | absolute change floors (Topos, Audition) | $10^{-4}$, 0.35 | none | design |
| $W_{\rm buf}$ | forward-model input buffer (Topos, Audition) | 16 | reports | design |
| none | forward-model hidden units (Topos; Audition) | 256; 32 | units | design |
| $\eta_{\rm fm}$ | forward-model learning rate (Topos, Audition, Soma, Chronos) | $10^{-3}$ | none | design |
| $\omega_{\min}$, $\omega_{\max}$ | Audition attended fraction at arousal 1 and 0 | 0.15, 1.0 | none | design |
| $\Delta_{\rm att}$ | shortest attended span (Audition) | 0.025 | s (entity) | design |
| none | Topos saliency grid | 12 by 12 | tiles | design |
| $\Theta_F$ | fovea hysteresis margin | 0.15 | none | design |
| $F_{\min}$, $F_{\max}$ | fovea size at arousal 1 and 0 | 0.12, 0.5 | fraction of frame | design |
| $\alpha_F$ | fovea tile-statistics weight | 0.05 | none | design |
| $n_F$ | tile updates before z-scoring | 5 | clip reports | design |
| $k_F$ | tile deviation floor, as a fraction of the mean tile change | 0.1 | none | design |
| $\beta^{\rm Chr}_\nu$ | Chronos temporal-error alert ratio | 3.0 | none | design |
| $W_z$ | Chronos hidden-state z-score window | 64 | broadcasts | design |
| $W_{\rm recur}$ | recurrence window | 32 | broadcasts | design |
| $n_{\rm recur}$ | recurrence count | 4 | states | design |
| $\Delta_{\rm recur}$ | recurrence quantization step | 0.25 | none | design |
| $W_{\Delta t}$ | Chronos interval window | 32 | broadcasts | design |
| $s_{\max}$ | timespan cap (Soma, Chronos) and cap on an entered interval relative to the window mean (Chronos) | 10 | none | design |
| none | reservoir units (Soma; Chronos) | 32; 32 | units | design |
| none | Chronos forward prediction | on | none | design |
| $I_0$ | phasic salience floor | 0.5 | none | design |
| $\tau_{\rm ph}$ | phasic decay time | 1.0 | s (entity) | design |
| $a_0$ | baseline arousal (Thymos and access rate) | 0.3 | none | design |
| none | adaptive access rate | on | none | design |
| $\lambda$ | arousal relaxation rate | 0.05 | s$^{-1}$ (entity) | design |
| $P_{\rm Thy}$ | minimum interval between Thymos state events, and timer period | 1.0 | s (entity) | design |
| $\gamma_a$ | perceptual-alert arousal gain | 0.15 | none | design |
| $\nu_{\rm cap}$ | cap on the excess error ratio per alert | 4.0 | none | design |
| $\gamma_{\rm Som}$ | arousal step per Soma hard-threshold report | 0.05 | none | design |
| $\tau_{\rm f}$, $\tau_{\rm s}$ | fast and slow time constants of the error means and alert rates | 10, 100 | s (entity) | design |
| $k_v$ | learning-progress gain in the pleasantness check | 2.0 | none | design |
| $\tau_v$ | valence time constant | 30 | s (entity) | design |
| $\mathrm{lp}_0$ | learning-progress noise floor | 0.05 | none | calibrated |
| $m_B$ | alert-excess margin | 0.5 | none | calibrated |
| $r_0$ | alert-rate floor | 0.05 | s$^{-1}$ (entity) | design |
| $\alpha_{\rm int}$ | intent-rate weight | 0.05 | none | design |
| $\beta_D$, $\delta_D$, $\rho_D$ | curiosity build, decay, relief | 0.05, 0.0055, 0.5 | s$^{-1}$ (entity) | design |
| $\beta_D$, $\delta_D$, $\rho_D$ | boredom build, decay, relief | 0.04, 0.0045, 0.3 | s$^{-1}$ (entity) | design |
| $\beta_D$, $\delta_D$; $\rho_D$ | social-drive build, decay; relief per interaction | 0.01, 0.0011; 0.8 | s$^{-1}$ (entity); none | design |
| $\beta_D$, $\delta_D$; $\rho_D$ | restlessness build, decay; relief per intent | 0.03, 0.0033; 0.5 | s$^{-1}$ (entity); none | design |
| $\theta_D$ | drive threshold (every drive) | 0.7 | none | design |
| $\Theta_D$ | drive re-arm fraction | 0.9 | none | design |
| none | initial held arousal $\hat a$ | 0.3 | none | design |
| none | wellness scaling: GPU temperature bounds; cycle-latency target | 30 to 80; 300 | °C; ms | design |
| $P_{\rm Som}$ | Soma reading interval | 1.0 | s (entity) | design |
| $n_x$ | Soma feature dimension (three self-rhythm features are zero unless the self-rhythm is enabled, and one is the highest GPU memory use) | 8 | none | design |
| $\tau_U$ | expected-error time constant | 600 | s (entity) | design |
| $\beta_U$ | expected-error band | 2.0 | none | design |
| none | hard thresholds: CPU, RAM, GPU temperature, GPU memory, cycle latency | 90, 90, 83, 92, 600 | %, %, °C, %, ms | design |
| $\theta_R$ | regulation threshold | 0.5 | none | provisional |
| $\Delta_R$ | regulation sustain window | 30 | s (entity) | design |
| $n_{\rm wu}$, $\Delta_{\rm wu}$ | warm-up end conditions | 1000, 1200 | updates, s (entity) | design |
| $\gamma_f$ | processing-rate reduction factor | 0.8 | none | design |
| $f_p^{\min}$, $f_p^{\max}$ | processing-rate bounds under regulation | 0.5, 20 | Hz (entity) | design |
| $\theta_{\rm th}$ | think bar | 0.45 | none | provisional |
| $\theta_{\rm sp}$ | speak (report) bar | 0.6 | none | provisional |
| $\Delta_{\rm th}$ | think refractory interval | 3.0 | s (entity) | design |
| $\Delta_{\rm sp}$ | speak refractory interval | 8.0 | s (entity) | design |
| $\Delta_{\rm sig}$ | signature expiry | 300 | s (entity) | design |
| $\Delta_g$ | in-flight guard timeout | 48 | s (wall) | design |
| none | interrupt bar | unset | none | design |
| $f_r$ | self-rhythm step rate | 20 | Hz (entity) | design |
| $n_s$ | Euler substeps per step | 10 | none | design |
| $J_{\rm rec}$ | recurrent weight | 2.5 | none | calibrated |
| $\Xi_0$ | input offset | $-0.25$ | none | calibrated |
| $k_y$ | sigmoid slope scale | 0.08 | none | calibrated |
| $\tau_y$ | activity time constant | 0.02 | s (entity) | calibrated |
| $\gamma_R$ | depression rate | 8.0 | s$^{-1}$ (entity) | calibrated |
| $\gamma_o$, $\gamma_u$ | own-drive and maternal-drive gains | 0.02, 0.03 | none | calibrated |
| $\sigma_\xi$ | noise scale | 0.02 | none | calibrated |
| $\tau_{\rm rec}^{(0)}$ | initial recovery time | 2.1 | s (entity) | calibrated |
| $\tau_{\rm rec}^{\min}$, $\tau_{\rm rec}^{\max}$ | recovery-time bounds | 0.9, 2.3 | s (entity) | calibrated |
| $\eta_\ell$ | frequency-adaptation rate | 0.0025 | s$^{-1}$ (entity) | calibrated |
| $\tau_m$ | moving-average time constant | 10 | s (entity) | design |
| $\Delta_{\rm amp}$ | phase and amplitude window | 8 | s (entity) | design |
| none | initial activity $y$ and resource $R$ | 0.05, 1.0 | none | design |
| none | maternal beat rate and drift | 70, 0.03 | bpm, none | design |
| $M_{\max}$ | maximum maternal drive | 0.4 | none | design |
| $c_M^{\rm base}$, $c_M^{\rm pert}$ | usual and perturbation drive scales | 0.5, 0.75 | none | design |
| $f_g$ | readout sampling rate | 10 | Hz (entity) | design |
| $f_{\rm lo}$, $f_{\rm hi}$ | entrainment band | 0.3, 2.0 | Hz (entity) | design |
| $\Delta_{\rm trim}$ | edge trim | 2.0 | s (entity) | design |
| $\Delta_E$ | driven-window length | 300 | s (entity) | design |
| $\Delta_W$, $P_W$ | withdrawal duration and period | 20, 1800 | s (entity) | design |
| $\Delta_{\rm pert}$, $P_{\rm pert}$ | perturbation duration and period | 5, 3600 | s (entity) | design |
| $j_P$ | probe jitter fraction | 0.25 | none | design |
| $P_{\rm ro}$ | readout period, also the settling time after boot or thaw | 60 | s (entity) | design |
| $f_{\rm guard}$ | pull guard | 0.05 | Hz (entity) | design |
| $\mathrm{pull}_{\min}$ | pull floor | 0.5 | none | calibrated |
| $n_{\rm base}$ | baseline withdrawals | 3 | count | design |
| none | surrogate heartbeats | 19 | count | design |
| none | consecutive passes required | 3 | count | calibrated |
| $t_{R0}$, $t_{R1}$, $t_{R2}$, $t_{R3}$ | viability checkpoints | 6, 24, 48, 60 | h (awake) | calibrated |
| $\mathrm{pull}_{R1}$, $\mathrm{slope}_{R1}$ | R1 bounds on median pull and slope | 0.12, 0.002 | none, h$^{-1}$ (awake) | calibrated |
| $\mathrm{pull}_{R2}$ | R2 bound on median pull | 0.3 | none | calibrated |
| $\Delta_V$, $n_V$ | viability window and minimum points | 12, 8 | h (awake), withdrawals | calibrated |
| $\Delta_{\rm per}$ | period-variability window | 300 | s (entity) | design |
| $V^{\min}_{\rm per}$ | period-variability floor | 0.2 | none | provisional |
| $\mathrm{err}^{\max}_{\rm Top}$ | Topos error-ratio ceiling | 0.3 | none | provisional |
| $\Delta^{\rm rec}_{\max}$ | return-to-baseline ceiling | 30 | s (entity) | provisional |
| $\mathrm{tol}_{\rm rec}$, $\Delta^{\rm rec}_{\rm cap}$ | recovery tolerance and cap | 0.25, 300 | none, s (entity) | design |
| $n_{\rm sleep}$, $n_{\rm cons}$ | required sleeps and consolidation passes | 5, 3 | counts | design |
| $\Delta_{\rm awake}$ | minimum awake time | 24 | h (awake) | design |
| none | gate cadence | 60 | s (entity) | design |
| $\Delta_{\rm budget}$ | gestation budget | 96 | h (wall) | design |
| $c_{\rm eff}$, $n_{\rm cal}$ | minimum-effect multiple and paired pilot runs | fixed before the live runs | none, runs | design |
| $n_{\rm run}$ | runs per arm | fixed before the live runs, by power analysis | runs | design |
| $q_{\rm pow}$ | assumed probability that the contrast exceeds the minimum effect (power analysis) | fixed before the live runs | none | design |
| none | initial learning period excluded from each run | fixed before the live runs | s (entity) | design |
| none | minimum effect of the positive control | fixed before the live runs | none | design |
| $\theta_{\rm band}$ | half-width of the threshold band | fixed before the live runs | none | design |
| none | context-age bins of the contrastive analysis | fixed before the live runs | s (entity) | design |
| $\alpha_{\rm test}$ | level of each sign test of the live test | 0.05 | none | design |
| $\alpha_{\rm FW}$ | family-wise level (offline suite) | 0.05 | none | design |
| $\mathrm{tol}_{\rm CV}$, $n_{\rm seed}$ | stability tolerance and seeds (offline suite, coherence-layer ablation) | 0.05, 3 | none, seeds | design |
