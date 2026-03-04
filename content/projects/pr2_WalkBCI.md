Title: EEG-based Forward Movement and Turning MI Classification with and without Action Observation in Virtual Reality
Category: projects
Cover: images/projimages/pr2_cover.png
Slug: bci-walk
Date: 1/1/2026
Summary: I designed a EEG-Based Brain-Computer Interface (BCI) for forward movement and turning intention decoding in a VR environment and compared the neural signatures between Motor Imagery (MI) with and without Action Observation (AO).

## What are MI-BCIs?

Motor Imagery (MI) is defined as the mental simulation of a physical movement without actual execution. Imagine you are equipped with an EEG headset and we analyze the signals during some action, e.g. arm flexion. You would most likely show activation in the motor cortex region related to that movement. However, if instead of movement we captured your mental rehearsal of that action (MI of that action), the same regions would show activations. That opens a huge window of possibilities, since users with motor impairments but intact central nervous system (e.g. patients with ALS) can employ MI in Brain-Computer Interfaces to control devices directly with their brain signals.

Most papers so far have focused on upper-limb movements (for example arm movements), but navigation-based paradigms for forward movement and turning have recently gained more attention for wheelchair control. However, navigation MI presents substantial challenges compared to upper-limb paradigms. Forward movement and turning involve distributed, less localized cortical patterns across sensorimotor, parietal, and premotor areas, complicating consistent neural decoding.

## Combining Action Observation and Motor Imagery (AOMI) for BCI Training

In order to enhance BCI performance, the combination of Action Observation (AO) and MI has been shown as a promising strategy. As you can see in the figure below, combining AO and MI consists of mentally visualizing the execution of an action while simultaneously observing it happening (in this example in a third-person view). Meta-analyses demonstrate that AOMI facilitates motor representation and produces stronger cortical activation than MI alone. So far, no study has analyzed the potential of AOMI for a multitask navigation BCI, and that is exactly what we did.

![MI and AOMI comparison](/images/projimages/WalkBCI/MIvsAOMI.png)

## VR Environment for Locomotion and Turning MI and AOMI Decoding

Since AOMI requires the imagined action to be observed at the same time, we created an immersive Virtual Reality environment in Unity to provide navigation context. This environment consists of a forest with a grid-like network of paths where participants encounter sequential cues prompting forward movement or either left or right turning motor imagery, presented in a pseudo-randomized order.

![VR environment and BCI workflow](/images/projimages/WalkBCI/BCIworkflow.png)
*To the left, the experimental setup, grid structure of the VR environment visualized from above and a sample screenshot of the VR environment while standing. To the right, the locomotion and turning MI and AOMI BCI workflow.*

<video width="100%" controls>
  <source src="/images/projimages/WalkBCI/videosampleVR.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
*Sample recording of the VR environment showing three trial samples. Each trial follows the same sequence: it starts with a 2-second Standing period that serves as the baseline. An auditory cue then announces the movement task, and one second later a beep signals the start of the 2-second MI period. The MI period is immediately followed by a 2-second AOMI period, where participants continue their motor imagery while simultaneously observing the corresponding action in the VR environment.*

The final aims of this study were to first establish an EEG paradigm for capturing locomotion intentions in VR, to investigate the neural signatures of MI versus AOMI, and to compare classification performance between the two paradigms.

## Event Related Spectral Perturbation (ERSP) Analysis

After processing the data, we analyzed the Event Related Spectral Perturbations (ERSPs) of all actions compared to the baseline for both MI and AOMI. We can define ERSP as the dynamic changes in the power spectrum of EEG signals in response to a specific event (either MI or AOMI). The figure shows the grand average ERSP topographies across subjects for each action and frequency band, with blue areas indicating Event-Related Desynchronization (ERD) and red areas indicated Event-Related Synchronization (ERS). We focus mainly on ERD as it is the primary neurophysiological signature of functional engagement in the motor cortex; unlike ERS, which often represents a 'resting' or 'inhibitory' state, ERD is the direct manifestation of the brain processing the motor command during both MI and AOMI.

![ERSP Analysis](/images/projimages/WalkBCI/fig-ersp-final.png)
*Grand average ERSP topographies for (a) MI and (b) AOMI during forward movement, left turning, and right turning. Rows represent delta (2–4 Hz), theta (4–8 Hz), alpha (8–13 Hz), and beta (13–30 Hz) bands. Color scale shows ERSP power (dB); blue indicates ERD, red indicates ERS. White and gray markers denote significant ERD (one-tailed t-test, FDR-corrected): gray p<0.05, white p<0.01.*

For forward movement MI, we observe delta and theta band ERD over occipital regions, as well as ERD in alpha and beta bands over parietal regions. This aligns with findings from visual gait motor imagery, and interestingly enough, a similar pattern is observed for AOMI, only than for the alpha and beta bands it is more spread and shows higher significance in some channels.

For turning MI, we observe significant ERDs in parietal and frontal regions, mainly for beta bands but also appreciated in delta bands, which also aligns with previous literature.

However, both directions show similar bilateral parietal ERD without lateralized patterns, meaning we couldn't distinguish left from right turns based on spectral analysis alone. This is relevant because it shows that the classifier must rely on features beyond what we see in grand average ERSP. And also, unlike forward movement, turning AOMI showed minimal spatial or statistical differences compared to MI, which suggests that AOMI might not provide the same ERD amplification for turning.

## Data Classification

Data classification has been done in two steps. First, we performed binary classification between Standing and Forward Movement using EEGNet. Then, we performed four-class classification (Standing, Forward Movement, Left Turning and Right Turning). Since for the later task EEGNet alone showed limited performance, we developed a hierarchical ensemble classifier combining EEGNet and ShallowConvNet with weigthed voting. The hierarchical ensemble operates in two stages. Stage 1 performs binary classification between Standing and any action, combining all movement samples into a single class. Then, stage 2 classifies movement samples into Forward, Left, or Right turning.

<img src="/images/projimages/WalkBCI/fig-accs.png" alt="Binary and 4-class Classification Accuracies with MI and AOMI" style="width:70%; height:auto; display:block; margin:0 auto;" />
*Classification accuracy comparison between MI and AOMI paradigms. (a) Binary classification accuracy (Standing vs. Forward movement) using EEGNet. (b) Four-class classification (Standing, Forward movement, Left Turning, Right Turning) using hierarchical ensemble (EEGNet + ShallowConvNet).*

For binary classification, AOMI achieved a 79.8% accuracy compared to 75.4% for MI, a statistically significant increase. In fact, our AOMI performance exceeds previous gait intention work by [Hasan et al.](https://www.researchgate.net/publication/340680978_Prediction_of_gait_intention_from_pre-movement_EEG_signals_a_feasibility_study), demonstrating the advantage of combining AO with MI in VR.

For four-class classification, the hierarchical ensemble substantially outperformed direct EEGNet, achieving 62.9% for AOMI compared to EEGNet's 53.3%. This improvement comes from two factors: first, combining EEGNet and ShallowConvNet creates diverse decision boundaries that complement each other; second, the hierarchical structure naturally handles class imbalance by first separating Standing from any movement, then classifying the movement type.

Also, it is important to remark that AOMI advantage compared to MI alone also increased from 4.4% in binary to 11.8% in four-class classification. This result is notable considering the similar ERD profiles observed in both turning MI and AOMI, suggesting that turning AOMI contains subtle temporal dynamics or phase-locked features that are obscured in ERSP profiles. Also, it is possible that the hierarchical ensemble model likely exploits these non-linear, high-dimensional dependencies to differentiate between directional intentions, hence the better classification compared to EEGNet alone.

## Paper Presentation at BCI2026

This February, I had the honor of presenting our paper at [The 14th IEEE International Winter Conference on Brain-Computer Interface (BCI2026)](https://brain.korea.ac.kr/bci2026/) in South Korea, my first international conference ever. There, I met many other researchers specialized on BCIs and learned a lot about the newest technologies in the field and innovative applications. I also got invaluable feedback on how to expand my research and address my current limitations.

<img src="/images/projimages/WalkBCI/conference.png" alt="Pictures from my stay at the High1 resort in South Korea during the BCI2026 conference" style="width:70%; height:auto; display:block; margin:0 auto;" />


## About this Project

Although the EEG data is not publicly available for privacy reasons, the code for the VR Environment is available on Github, you can access it [through this link](https://github.com/PauBonco02/VR-Walking-MI-Experiment). If you have any doubts regarding the environment or want to learn more about all the data processing done, feel free to contact me!


