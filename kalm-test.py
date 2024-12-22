import random
import fileops
import printops
import person
import careers
import location

def main():
    printops.print_title_screen()
    player = fileops.load_game_or_new_game()

    kalm = location.Location(
        population = random.randint(20,35),
        input_name="Kalm",
        demographics={
            careers.Peasant: 1
        },
        generic_class=careers.Peasant
    )

    player.location = "Meadow, center"

    print('You start in the meadow.')

    while True:

        if player.location == "Meadow, center":
            print(fileops.get_in_game_text('world-text','meadow','center'))
            response = input('Will you leave the meadow? ')
            if response == 'info':
                fileops.get_in_game_text('world-text','meadow','center')
            elif response == 'y':
                player.location = "Meadow, rim"
                continue
            elif response == 'n':
                continue
            else:
                quit()

        elif player.location == "Meadow, rim":
            print(fileops.get_in_game_text('world-text','meadow','rim'))
            response = input('Leave the meadow? ')
            if response == 'y':
                player.location = 'Kalm, outskirts'
                continue
            elif response == 'n':
                player.location = 'Meadow, center'
                continue
            else:
                quit()
        
        elif player.location == "Kalm, outskirts":
            print(fileops.get_in_game_text('world-text','Kalm','outskirts'))
            response = input('Draw nearer, or turn back? (nearer/back) ')
            if response == 'nearer':
                player.location = 'Kalm, square'
                continue
            elif response == 'back':
                player.location = 'Meadow, rim'
            else:
                quit()

        elif player.location == 'Kalm, square':
            print(fileops.get_in_game_text('world-text','Kalm','square'))

            response = input('Enter the church? ')
            if response == 'save':
                fileops.save_file(player)
            elif response == 'y':
                player.location = 'Kalm, church, entrance'
            else:
                quit()

        elif player.location == 'Kalm, church, entrance':
            print(fileops.get_in_game_text('world-text','Kalm','church','entrance'))

            priest = careers.Priest(name='Douglas')
            response = input(
                fileops.get_in_game_text('world-text','Kalm','church','priest-worship-prompt')
            )

            if response == 'y':
                print(fileops.get_in_game_text('world-text','Kalm','church','priest-worship-y'))
                player.location = 'Kalm, church, altar'
                continue
            elif response == 'n':
                response = input(
                    fileops.get_in_game_text('world-text','Kalm','church','priest-seek-prompt')
                    )
                if response == 'nothing':
                    input(fileops.get_in_game_text('world-text','Kalm','church','priest-nothing'))
                    player.location = 'Kalm, square'
                    continue
                else:
                    quit()
            else:
                quit()

        elif player.location == 'Kalm, church, altar':
            print(fileops.get_in_game_text('world-text','Kalm','church','altar'))

            response = input(
                fileops.get_in_game_text('world-text','Kalm','church','altar-prompt')
            )

            if response == 'y':
                input(fileops.get_in_game_text('world-text','Kalm','church','altar-y'))
            elif response == 'n':
                input(fileops.get_in_game_text('world-text','Kalm','church','altar-n'))
            else:
                quit()
            
            player.location = 'Kalm, church, entrance'
            continue


if __name__ == '__main__':
    main()