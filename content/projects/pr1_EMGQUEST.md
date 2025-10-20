Title: EMG Quest: a EMG-controlled Coop Game
Category: projects
Cover: images/projimages/pr1_cover.png
Slug: emg-quest
Date: 1/1/2025
Summary: A cooperative platformer controlled entirely by muscle signals. Two players use EMG sensors on their forearms to move their sprites through levels requiring teamwork and coordination.

For [2025 Suzukakedai's Science Day](https://www.isct.ac.jp/en/news/o9m7vvbpu0zh), Yoshimura Lab opened its doors to the public to share our latest research and innovations. Visitors experienced various BCI-related technologies, including EEG-based concentration level estimation and VR environments for complex task learning like juggling. My group, however, focused on developing a platform to control a game through electromyographic (EMG) signals: **EMG Quest**.

![EMG Quest Presentation Image](/images/projimages/pr1_emgquest.png)

## EMG Quest: Game and Controls

**EMG Quest** is just a short concept game created to test the use of EMG in unity for game control. It is a 2D cooperative platformer with 4 levels in which each player controls a square (red and blue). With two sensors in the forearm per player (one in the anterior and the other in the posterior region), they can trigger 3 different actions. Considering the right arm is used:

- **Flexing** the wrist to the left: **Move Left**
- **Extending** the wrist to the right: **Move Right**
- **Activating both** flexor and extensor muscles simultaneously: **Jump**

To advance to the next level, both characters must be in the door with the same color as them at the same time. Some mechanics that enforce the need for cooperation include using the other player like a platform and colored tiles only solid for the player with the same color. Here you have an example from the second level.

![Recording of the gameplay](/images/projimages/pr1_gamerecording.gif)

<video width="60%" controls muted>
  <source src="/images/projimages/pr1_video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## EMG sensors and data processing

We placed the sensors on the lower forearm: Channel 1 over the wrist flexor muscles and Channel 2 over the extensors. The EMG data streams directly into a Unity script that calculates the average power for each channel over 100ms intervals. Players can monitor real-time electrode activity through an in-game toggle menu, which also allows adjusting the power threshold for action activation.

![Electrode location summary](/images/projimages/pr1_hands.png)

## Reflections

EMG Quest successfully demonstrated that EMG-based game control can create engaging cooperative experiences. The system's responsiveness and the intuitive muscle-to-action mapping made it accessible even for first-time users at the Science Day. It was a great opportunity to see how people of all ages reacted to the technologies being developed in our lab, and a reminder of how accessible science can inspire the next generation.

EMG-based interactive systems like this have exciting **applications in rehabilitation**, where gamified muscle training can motivate patients recovering from injuries or neurological conditions. Beyond rehab, these systems can be extended to assistive technologies, human-computer interaction research, and even eSports for people with limited mobility.

Future iterations could explore more complex gesture recognition (like ML-based approaches) or additional game mechanics that leverage the unique properties of EMG Control.

## About this project

All the code for this project is available on Github, you can access it [through this link](https://github.com/PauBonco02/EMG-Controlled-Cooperative-Game). The repository includes the game assets, source code, and the plugins used for EMG signal recording and processing in Unity. Feel free to explore it and share any feedback!