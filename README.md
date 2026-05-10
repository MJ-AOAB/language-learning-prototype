# language-learning-prototype

Learning learning app
A multi activity language learning system built with Python and Tkinter
This project is an interactive desktop application designed to help learners practise vocabulary in a chosen language through three activities:
•	Memory Game
•	Speed Matching Game
•	Practise Mode (with optional audio recording/playback)
The system can support multiple native/learning languages currently supports English to Italian/polish, includes a points system, and was originally designed as part of a larger educational platform.

All audio files originally used in the project were recorded using my own voice and therefore are not included.
Audio related features remain in the code but are disabled in this public version.
________________________________________
 Features
Memory game
A classic matching pairs game:
•	10 vocabulary pairs (20 tiles total)
•	English ↔ target language
•	Tracks number of moves
•	Tracks completion time
•	Awards points for finishing
•	Fully interactive grid built using Canvas
Speed Game
A timed 60 second challenge:
•	Randomised vocabulary grid
•	A “question word” appears at the bottom
•	Player must click the matching translation
•	Score increases for each correct match
•	Timer starts on first click
•	Designed to build rapid recall
Practise Mode
A free exploration mode for vocabulary:
•	Displays a word in both languages
•	Arrows allow cycling through the word list
•	Originally included: 
o	Audio playback of the learning language word
o	User recording for pronunciation practice
•	These features are disabled in this version
(sound files are not included for privacy reasons)
Points & Progress
The system tracks:
•	Number of completed activities
•	Points earned (20 points per completed activity)
•	Intended to integrate with a larger platform (admin view, leaderboards, etc.)
________________________________________

Technologies Used
•	Python 3
•	Tkinter (GUI)
•	Canvas for custom drawing
•	Random for shuffling game boards
•	Time for timers and scoring
•	(Optional) sounddevice, scipy, playsound 
(disabled in this version)
________________________________________
How to Run
1.	Ensure Python 3 is installed
2.	Run the main script (contained in code.txt)
3.	Set username and password as “a” 
4.	Opens a basic user interface select a language for learning and native then select a module ( only food module is available)
5.	The application opens a window with four tabs: 
o	Memory
o	Speed
o	Practise
o	Exit

about Missing Audio Features
Originally, the system included:
•	Audio playback of vocabulary words
•	User voice recording
•	Submission of recordings for teacher review
These features relied on:
•	.wav files recorded by me
•	Additional audio libraries
Because the recordings contain my own voice, they are not included in this public version.
All audio related code remains in place but is commented out or inactive.

Design Documentation Included
The repository design docs since this was created as a part of a full software development cycle using waterfall
•	Requirements analysis
•	Interview with client
•	Feasibility report
•	Screen designs
•	Functional diagrams
•	Explanational document on design decisions
This provides a full view of the system’s intended architecture and user experience.
________________________________________
Possible Future Improvements
•	Ui update
•	Add image support for vocabulary
•	Implement a database for storing progress
•	Add more modules
•	Expand vocab options for modules
•	Package the system as an executable app
•	Add accessibility options (font scaling, colour themes)
•	Re enable audio using synthetic voices
•	Theoretically ai analysis of audio from users in practise
