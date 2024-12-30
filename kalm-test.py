import random
import mechanics.fileops as fileops
import mechanics.printops as printops
import creatures.people.careers as careers

from locations.location import Location
from quests.quest import Quest
from creatures.people.quest_characters.douglass_the_priest.douglass_the_priest import Douglass_the_Priest
from items.quest_items import Coin_for_Alms

def boot_game():
    printops.print_title_screen()
    player = fileops.load_game_or_new_game('mechanics/save_data.txt')

    player.location = "Meadow, center"

    print('\nYou start in the meadow.')

    return player

def generate_locations():
    locations = {}

    kalm_square = Location(
        population = random.randint(20,35),
        input_name="Kalm, square",
        demographics={
            careers.Peasant: 1
        },
        generic_class=careers.Peasant
    )
    locations[kalm_square.name] = kalm_square

    kalm_outskirts = Location(
        population=0,
        input_name='Kalm, outskirts',
        items=[Coin_for_Alms()]
    )
    locations[kalm_outskirts.name] = kalm_outskirts

    kalm_church_entrance = Location(
        0,
        'Kalm, church, entrance'
    )
    locations[kalm_church_entrance.name] = kalm_church_entrance

    return locations

def generate_quest_characters():
    characters = {}
    douglass = Douglass_the_Priest()

    characters[douglass.name] = douglass

    return characters

def generate_quests(quest_characters):

    quests={}

    give_alms = Quest(
        'Give Alms',
        'Kalm, church, entrance',
        [quest_characters]
    )
    quests[give_alms.name] = give_alms

    return quests
    

def main():
    player = boot_game()
    locations = generate_locations()
    quest_characters = generate_quest_characters()
    quests = generate_quests(quest_characters)

    while True:

        if player.location == "Meadow, center":
            print(fileops.get_in_game_text('mechanics/in_game_text.json','world-text','meadow','center'))
            response = input('\nMove to the rim of the meadow? (y/n) ')
            if response == 'info':
                fileops.get_in_game_text('mechanics/in_game_text.json','world-text','meadow','center')
            elif response == 'y':
                player.location = "Meadow, rim"
                continue
            elif response == 'n':
                continue
            else:
                quit()

        elif player.location == "Meadow, rim":
            print(fileops.get_in_game_text('mechanics/in_game_text.json','world-text','meadow','rim'))
            response = input('\nLeave the meadow? (y/n) ')
            if response == 'y':
                player.location = 'Kalm, outskirts'
                continue
            elif response == 'n':
                player.location = 'Meadow, center'
                continue
            else:
                quit()
        
        elif player.location == "Kalm, outskirts":
            print(fileops.get_in_game_text('mechanics/in_game_text.json','world-text','Kalm','outskirts'))
            if locations['Kalm, outskirts'].items:
                print('Something sparkles in the dirt.')
            response = input('\nWhat will you do? (info/town/meadow) ')
            if response == 'town':
                player.location = 'Kalm, square'
                continue
            elif response == 'meadow':
                player.location = 'Meadow, rim'
                continue
            elif response == 'info':
                player.find(locations['Kalm, outskirts'])
            else:
                quit()

        elif player.location == 'Kalm, square':
            print(fileops.get_in_game_text('mechanics/in_game_text.json','world-text','Kalm','square'))

            response = input('\nWhere will you go? (church/outskirts) ')
            if response == 'save':
                fileops.save_file(player,'mechanics/save_data.txt')
            elif response == 'church':
                player.location = 'Kalm, church, entrance'
                continue
            elif response == 'outskirts':
                player.location = 'Kalm, outskirts'
                continue
            else:
                quit()

        elif player.location == 'Kalm, church, entrance':
            print(fileops.get_in_game_text('mechanics/in_game_text.json','world-text','Kalm','church','entrance'))
            if quests['Give Alms'].completed:
                print('quest completed.')
                priest.chat(player,quests['Give Alms'])
                exit_response = input('Exit the church? (y/n) ')
                if exit_response == 'y':
                    player.location = 'Kalm, square'
                    continue
                elif exit_response == 'n':
                    continue
                else:
                    break

            elif not quests['Give Alms'].active and not quests['Give Alms'].completed:
                print('starting quest...')
                quests['Give Alms'].begin( locations['Kalm, church, entrance'] )
                # priest = locations['Kalm, church, entrance'].inhabitants['Douglass the Priest']
                priest = quest_characters['Douglass the Priest']   
                priest.chat(player,quests['Give Alms'])
            
            else:
                print('else')
                # quests['Give Alms'].set_stage('worship-n')
                # quests['Give Alms'].end()
                # quests['Give Alms'].log()
                # input(quests['Give Alms'].end_msg())                
                continue
                    
        elif player.location == 'Kalm, church, altar':
            print(fileops.get_in_game_text('mechanics/in_game_text.json','world-text','Kalm','church','altar','info'))

            response = input(
                fileops.get_in_game_text('mechanics/in_game_text.json','world-text','Kalm','church','altar','prompt')
            )

            if response == 'y' and player.has(Coin_for_Alms()):
                input(fileops.get_in_game_text('mechanics/in_game_text.json','world-text','Kalm','church','altar','alms-y'))
                quests['Give Alms'].set_stage('alms-y')
                quests['Give Alms'].end()
                quests['Give Alms'].log()
                print('\nPlot completed: Give Alms.')
                input(fileops.get_in_game_text('quests/quests.json','Kalm, church, entrance','Give Alms','worship-y','alms-y'))
            elif response == 'y' and not player.has(Coin_for_Alms):
                input('You have nothing to give.')
                quests['Give Alms'].set_stage('alms-n')
                quests['Give Alms'].end()
                quests['Give Alms'].log()
                print('\nPlot completed: Give Alms.')
                input(fileops.get_in_game_text('quests/quests.json','Kalm, church, entrance','Give Alms','worship-y','alms-n'))
            elif response == 'n':
                input(fileops.get_in_game_text('mechanics/in_game_text.json','world-text','Kalm','church','altar','alms-n'))
                quests['Give Alms'].set_stage('alms-n')
                quests['Give Alms'].end()
                quests['Give Alms'].log()
                print('\nPlot completed: Give Alms.')
                input(fileops.get_in_game_text('quests/quests.json','Kalm, church, entrance','Give Alms','worship-y','alms-n'))
            else:
                quit()
            
            player.location = 'Kalm, church, entrance'
            continue


if __name__ == '__main__':
    main()