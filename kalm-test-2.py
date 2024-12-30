import mechanics.fileops as fileops
import mechanics.printops as printops

def boot_game():
    printops.print_title_screen()
    player = fileops.load_game_or_new_game('mechanics/save_data.txt')

    player.location = "Meadow, center"

    print('\nYou start in the meadow.')

    return player

def main():
    player = boot_game()
    quests = fileops.load_quests()

    