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
    print()     
def load_game():
    print()   
def main():
    print()      
        

main()