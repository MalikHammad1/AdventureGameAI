#SP23-bai-034 (Muhammad Hammad)   Maintainer
#SP23-bai-026 (Moiz Asif)        Collaborator
#Game Name : "Escape from the Iron Tower!"

# Data of rooms and items
rooms = {
    'entrance': {
        'description': "You are at the entrance of the Iron Tower. The door behind you is sealed shut.",
        'exits': {'north': 'main_hall'},
        'items': ['torch']
    },
    'main_hall': {
        'description': "You are in the Main Hall, a vast room with towering iron walls and gears turning around you.",
        'exits': {'south': 'entrance', 'east': 'workshop', 'west': 'library'},
        'items': ['key'],
        'puzzle': "locked_door"
    },
    'library': {
        'description': "You are in the Library. Books line the shelves, but one book stands out.",
        'exits': {'east': 'main_hall'},
        'items': ['ancient_book', 'map']
    },
    'workshop': {
        'description': "You are in the Workshop. Tools and gadgets are scattered across the tables.",
        'exits': {'west': 'main_hall', 'north': 'basement'},
        'items': ['wrench', 'oil_can'],
        'puzzle': "broken_lift"
    },
    'basement': {
        'description': "You are in the Basement. It’s cold and damp, and a large iron gate blocks the way forward.",
        'exits': {'south': 'workshop'},
        'items': [],
        'puzzle': "iron_gate"
    }
}

# Initial game's state
game_state = {
    'current_room': 'entrance',
    'inventory': [],  # Inventory for both players
    'players': {
        'Player 1': {'name': 'Player 1'},
        'Player 2': {'name': 'Player 2'}
    },
    'turn': 'Player 1'  # Player 1 will start game
}

def describe_room():
    room = rooms[game_state['current_room']]
    print(room['description'])
    if room['items']:
        print(f"You see the following items: {', '.join(room['items'])}")
    
def switch_turn():
    game_state['turn'] = 'Player 2' if game_state['turn'] == 'Player 1' else 'Player 1'

def move(direction):
    current_room = game_state['current_room']
    if direction in rooms[current_room]['exits']:
        game_state['current_room'] = rooms[current_room]['exits'][direction]
        describe_room()
    else:
        print(f"{game_state['turn']}, you can't go that way.")
def take(item):
    current_room = rooms[game_state['current_room']]
    if item in current_room['items']:
        game_state['inventory'].append(item)
        current_room['items'].remove(item)
        print(f"{game_state['turn']} has taken the {item}.")
    else:
        print(f"{game_state['turn']}, there is no {item} here.")  
def drop(item):
    if item in game_state['inventory']:
        rooms[game_state['current_room']]['items'].append(item)
        game_state['inventory'].remove(item)
        print(f"{game_state['turn']} has dropped the {item}.")
    else:
        print(f"{game_state['turn']}, you don't have {item} in your inventory.")      
def show_inventory():
    if game_state['inventory']:
        print(f"Inventory: {', '.join(game_state['inventory'])}")
    else:
        print("Your inventory is empty.")  
def save_game():
    with open('savedfile.txt', 'w') as save_file:  # Open file in write mode
        save_file.write(game_state['current_room'] + '\n')  # Write current room to the file
        save_file.write(','.join(game_state['inventory']) + '\n')  # Write inventory as a comma-separated string
        save_file.write(game_state['turn'] + '\n')  # Write the current player's turn
        print(f"{game_state['turn']}, game saved.")     
def load_game():
    try:
        with open('savedfile.txt', 'r') as save_file: 
            game_state['current_room'] = save_file.readline().strip() 
            game_state['inventory'] = save_file.readline().strip().split(',')  #reading inventory and splits by commmas!
            game_state['turn'] = save_file.readline().strip()  # current player's turn!
            print(f"{game_state['turn']}, game loaded.")
            describe_room()  # after loading room display!
    except FileNotFoundError:
        print(f"{game_state['turn']}, no saved game found.")
    except Exception as e:
        print(f"Error loading game: {e}")
   
def main():
    print("Welcome to 'Escape from the Iron Tower'!")
    print("Type 'HELP' for a list of commands!")
    describe_room()

    while True:
        print(f"\nIt's {game_state['turn']}'s turn.")
        command = input("What would you like to do? ").lower().split()
        
        if not command:
            continue
        
        action = command[0]
        if action == 'go':
            if len(command) > 1:
                move(command[1])
            else:
                print("Go where?")
        elif action == 'look':
            describe_room()
        elif action == 'take':
            if len(command) > 1:
                take(command[1])
            else:
                print("Take what?")
        elif action == 'drop':
            if len(command) > 1:
                drop(command[1])
            else:
                print("Drop what?")
        elif action == 'inventory':
            show_inventory()
        elif action == 'save':
            save_game()
        elif action == 'load':
            load_game()
        elif action == 'help':
            print("Commands: go [direction], look, take [item], drop [item], inventory, save, load, quit")
        elif action == 'quit':
            print("Exiting game. Goodbye!")
            break
        elif action == 'next':
            switch_turn()  # Switch to the next player's turn
        else:
            print("Command is INVALID. Type 'Help' for list of commands!")

        switch_turn()  # Automatically switch turn after each command
     
        