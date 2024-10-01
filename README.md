#SP23-bai-034 (Muhammad Hammad)   Maintainer
#SP23-bai-026 (Moiz Asif)        Collaborator
#Game Name : "Escape from the Iron Tower!"

Documentation for "Escape from the Iron Tower"
Overview
"Escape from the Iron Tower" is a text-based adventure game where players explore a mysterious tower, solve puzzles, collect items, and ultimately find a way to escape. The game is designed for two players who take turns interacting with the game environment, each contributing to the exploration and problem-solving.

Features
Exploration: Navigate through different rooms in the Iron Tower.
Inventory Management: Collect and use items to solve puzzles.
Turn-Based Gameplay: Players take turns making decisions and executing actions.
Saving and Loading: Save your progress and load previous game states.
Puzzles: Solve various puzzles to unlock new areas and advance the game.
Installation
To run the game, ensure you have Python installed on your system. You can download it from python.org.

Download the Game: Download the game source code (adventure_game.py) to your local machine.
Open Command Prompt or Terminal.
Navigate to the Directory where the game file is located.
Run the Game with the following command:
bash
Copy code
python adventure_game.py
Gameplay Instructions
Starting the Game: Upon launching the game, players will be greeted with a welcome message and prompted to enter commands.
Taking Turns: Players alternate turns, making decisions about where to move, what items to take, and how to interact with the environment.
Commands: Players can type commands to perform actions within the game.
Commands
Here is a list of commands you can use during the game:

Command	Description
go [direction]	Move to the specified direction (e.g., go north).
look	Redisplay the current room description.
inventory	Show the player's current items.
take [item]	Pick up an item from the current room.
drop [item]	Drop an item from your inventory.
use [item]	Use an item in the current room.
examine [object]	Get more details about an object in the room.
save	Save the current game state.
load	Load a previously saved game state.
quit	Exit the game.
help	Display available commands.
Examples of Gameplay
Example 1: Basic Navigation
plaintext
Copy code
You are at the entrance of the Iron Tower.
What would you like to do? go north
You are in the Main Hall.
What would you like to do? take key
Player has taken the key.
Example 2: Using Items
plaintext
Copy code
You are in the Basement. A heavy iron gate blocks your way.
What would you like to do? use wrench
You fix the lift with the wrench! You can now descend to the basement.
Example 3: Saving and Loading
plaintext
Copy code
What would you like to do? save
Game saved.
What would you like to do? load
Game loaded.
Example 4: Solving Puzzles
plaintext
Copy code
You are at the iron gate. It looks heavy and rusted.
What would you like to do? use oil_can
You use the oil can on the rusted gate. The gate creaks open, revealing a hidden passage!
Conclusion
"Escape from the Iron Tower" offers an engaging experience for players who enjoy puzzle-solving and exploration in a text-based format. The cooperative gameplay allows players to strategize together, enhancing the overall fun and interaction. Enjoy your adventure!

