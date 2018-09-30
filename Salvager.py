import textwrap
import time
import csv
from builtins import int


def show_game_directions():
    """
    Helps to direct player what needs to be done and explains game.
    """
    game_help = "'Salvager' is a text-based game where the player has to save a boy who has been tried to burn by a " \
                "murderer.\nSalvager will be the one who will save the boy by killing the murderer and extinguishing " \
                "the fire by a fire extinguisher in 10 Minutes. The boy is located in a room of an apartment which has"\
                " 6 rooms. Salvager has to collect a fire extinguisher, fire extinguisher use it"\
                "to extinguish fire an should use pistol to kill the murderer and save the boy in given time " \
                "if not because of fire, the house will burn down and Salvager " \
                "will die. Salvager will be rewarded points on the usage of his bullets, completion of the game " \
                "and completion time.\n"
    game_map = "Fire extinguisher is located in Kitchen and Living room \n Bullets are located in Bedroom " \
                    "drawers and at Entrance lobby \n You have already 5 bullets loaded in pistol!!!!"
    print(textwrap.dedent(game_help).strip())
    print(textwrap.dedent(game_map).strip())


def handle_user_input(user_input, state_options):
    """
    Handles user input and checks whether that is valid input or not, expected input is option number or option
    Invalid inputs are negative and out of rage value
    :param user_input: user selection can be int,String or flot
    :param state_options: list of options present in one room
    :return: String, action needs to perform
    """
    action = 'Invalid Input'
    position = -1
    try:
        user_input = int(user_input)
        if user_input <= 0 or user_input >= len(state_options):
            action = 'Invalid Input'
        else:
            action = state_options[user_input]
            position = user_input
    except ValueError:
        if type(user_input) == str:
            try:
                input = state_options.index(user_input)
                action = state_options[input]
                position = input
            except ValueError:
                action = 'Invalid Input'
    return action, position


# Number of bullets initially
bullets = 5


def check_bullets():
    """
    Checks if player has pistol loaded
    :return: boolean True if bullet is present and False if not
    """
    if bullets >= 1:
        return True
    else:
        return False


def decrement_bullets():
    """
    Decrements number of bullets left
    """
    global bullets
    bullets = bullets - 1


def increment_bullets():
    """
    Increment number of bullets
    """
    global bullets
    bullets = 5


# Reward points initially
reward = 0


def reward_calculator(points, action):
    """
    Adds and subtract reward points as per user action
    :rtype: object
    :param points: int, points for particular action
    :param action: Addition or subtraction
    """
    global reward
    if action == 'add':
        reward = reward + points
    elif action == 'subtract':
        reward = reward - points


def get_bullets_remaining():
    """
    Returns bullets remaining in pistol
    :return: int, Number of bullets left in pistol
    """
    global bullets
    return bullets


def get_reward_points():
    """
    Returns total reward points
    :return: total reward collected
    """
    global reward
    return reward


print(
    " Hi!! You are in Amazon forest enjoying your adventurous travel.\n Someone is screaming. Save! Save! Save!\n "
    "Voice is coming from house located in the trees. You see the smoke coming out.\n Run and save life and get "
    "Rewarded!!! Be a ‘SALVAGER’ ")
player_name = input(" Please enter your name 'Salvager'.\n")
print(player_name + ", save life and be Salvager!!!")

while True:
    help_option = input(
        "Do you know how to play game? If not, enter 'No' and help will be provided \nIf yes, enter 'Yes' and enjoy the "
        "game \n")
    if help_option.upper() == "NO":
        show_game_directions()
        break
    elif help_option.upper() == "YES":
        break
    else:
        print("Invalid input, Input Yes or No")

time.sleep(2)
print(
    "\n" + player_name + ", take a prudent decisions and save life in 10 minutes and or else murderer will run away and "
                         "you as well as boy will die because of fire")
time.sleep(2)

# Initializing list as each state of the game i.e options available in each room with 1st element stating State
options_in_entrance = ['You are in the Entrance of house', 'Do u think murderer is at corner, Shoot!!',
                       'Go to LivingRoom', 'Load gun by Bullets', 'Pickup oxygen_mask', 'Call Police']
options_in_living_room = ['You are in the Living room of house', 'Go to Kitchen', 'Go to Bedroom1', 'Go to Bedroom2',
                          'Pickup fire_extinguisher', 'Do u think murderer is at corner, Shoot!!']
options_in_kitchen = ['You are in the Kitchen of house', 'Go to GuestRoom', 'Pickup fire_extinguisher',
                      'Go to Bedroom1', 'Do u think murderer is at corner, Shoot!!', 'Go to LivingRoom',
                      'Load gun by Bullets']
options_in_bedroom1 = ['You are in the Bedroom1 of house', 'Laptop is here, check how to use fire extinguisher',
                       'Pickup first_Aid_Box', 'Go to Kitchen', 'Load gun by Bullets', 'Go to LivingRoom',
                       'Do u think murderer is at corner, Shoot!!']
options_in_bedroom2 = ['You are in the Bedroom2 of house', 'Laptop is here, check how to use fire extinguisher',
                       'Pickup first Aid Box', 'Go to LivingRoom', 'Do u think murderer is at corner, Shoot!!']
options_in_guestroom = ['You are in the Guestroom of house', 'Do u think murderer is at corner, Shoot!!',
                        'Extinguish Fire and save boy', 'Go to Bedroom1', 'Go to Kitchen']
states_of_game = {'Entrance': options_in_entrance, 'LivingRoom': options_in_living_room,
                  'Kitchen': options_in_kitchen, 'Bedroom1': options_in_bedroom1,
                  'Bedroom2': options_in_bedroom2, 'GuestRoom': options_in_guestroom
                  }
# List to track moves of player
moves_of_player = []

# List storing reward points
points = dict(oxygen_mask=25, fire_extinguisher=50, first_Aid_Box=25, extinguish_fire=200, bullet_miss=25,
              bullet_hit=150)

# Variables to flag certain situations in game.
game = 'On'
murderer = 'Alive'
current_state = 'Entrance'
print_points_deducted = "{} points are deducted and your current reward points are {}"
print_points_awarded = "{} points are awarded and your current reward points are {}"
fire_extinguisher = 'Absent'

# Timer having end time as 10 minute
time_taken = 0
time_now = time.time()
start_time = time_now
end_time = time_now + (60 * 10)

# Start of the game, will run till game is not over and time is less than 10 minute
while time.time() < end_time and game == 'On':
    print("You have "+ str((end_time- time.time())/60)+" minutes to complete game")
    print(states_of_game[current_state][0])
    time.sleep(1)
    print("Choose from options below")
    for i, option in enumerate(states_of_game[current_state]):
        if i != 0:
            print(str(i) + ". " + option)
    user_input = input("Enter your choice:\n")
    action_required, position_of_action = handle_user_input(user_input, states_of_game[current_state])
    moves_of_player.append(action_required)
    if action_required == 'Invalid Input':
        print("Invalid input, enter the option number or option")
        continue
    elif action_required.find('Shoot') != -1:
        if check_bullets():
            if current_state != 'GuestRoom':
                decrement_bullets()
                print(
                    "Sorry, Murderer is not in this room and you have missed the shot, You have left with {} "
                    "bullets".format(get_bullets_remaining()))
                reward_calculator(points['bullet_miss'], 'subtract')
                print(print_points_deducted.format(str(points['bullet_miss']), get_reward_points()))
            else:
                decrement_bullets()
                if murderer != 'Dead':
                    print('You just killed murderer!!! Bravo')
                    murderer = 'Dead'
                    reward_calculator(points['bullet_hit'], 'add')
                    print(print_points_awarded.format(str(points['bullet_hit']), str(get_reward_points())))
                else:
                    print("Murderer is already killed")
        else:
            print("You don't have bullets left load your pistol")
    elif action_required.find('Go to') != -1:
        current_state = action_required.split("Go to")[1].strip()
        continue
    elif action_required.find('Bullets') != -1:
        increment_bullets()
        print("Your gun is loaded you have total 5 bullets in your gun")
        continue
    elif action_required.find('Pickup') != -1:
        reward_calculator(points[action_required.split("Pickup")[1].strip()], 'add')
        if action_required.split("Pickup")[1].strip() == 'fire_extinguisher':
            fire_extinguisher = 'Present'
        print("You may need " + action_required.split("Pickup")[1].strip() + " later, Good you picked it up")
        print(print_points_awarded.format(points[action_required.split("Pickup")[1].strip()], str(get_reward_points())))
        del (states_of_game[current_state][position_of_action])
        continue
    elif action_required.find("Police") != -1:
        print("Police has been informed about incidence and they will arrive shortly")
        del (states_of_game[current_state][position_of_action])
        continue
    elif action_required.find("Laptop") != -1:
        print("you have now learned to use fire extinguisher")
        continue
    elif action_required.find('Extinguish') != -1:
        if murderer == 'Dead' and fire_extinguisher == 'Present':
            print("You have saved the boy and won the game!!!!")
            print("You are 'Salvager' now")
            reward_calculator(points['extinguish_fire'], 'add')
            game = 'Over'
            time_taken = (time.time() - start_time) / 60
            break
        else:
            print("You must need fire extinguisher to extinguish fire and Murderer must be dead before saving boy")
time.sleep(1)


if 'Over' == game:
    print("Police are here and they gave you award and Titled you as a 'Salvager'")
    time.sleep(1)
    print("Total Points earned:" + str(get_reward_points()))
    time.sleep(1)
    with open('player_stats.csv', mode='a', newline='') as player_file:
        player_writer = csv.writer(player_file, delimiter=',')
        player_writer.writerow([player_name.upper(), get_reward_points(), time_taken])
    if time_taken != 0:
        print("Wooh!!! you completed game quite early!!!\n You completed it in " + str(time_taken) + " minute")
else:
    print("!!!!TIME OVER!!!!!!!")
    print('You lost')


print("Your path in the game was")
for i, choice in enumerate(moves_of_player):
    print("{}. {}".format(i + 1, choice))
