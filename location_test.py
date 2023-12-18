from random import choice

from fileops import save_file, load_game_or_new_game
from printops import print_title_screen
from person import Person
from careers import Archer, Warrior, Elder
from location import Location

def main():
    print_title_screen()
    hero = load_game_or_new_game()

    while True:
        action = input("Where wilt thou go? 'm' for mountain, 't' for town: ")
        
        if action == 'm':
            hero.location = 'Lonely Mountain'
        elif action == 't':
            hero.location = 'Kalm'
        elif action == 'save':
            save_file(hero)
            continue
        elif action == 'quit':
            break
        else:
            continue

        if hero.location == 'Lonely Mountain':
            lonely_mountain = Location(
                population=1,
                input_name='Lonely Mountain'                
                )
            
            guru = Person(
                LEVEL=100,
                INT=100,
                name='Guru Greg'
            )

            lonely_mountain.inhabitants = [guru]

            input('The mountain rises high above you...\n')
            if input('A guru sits meditating. Speak with him? ') == 'y':
                guru.chat(hero)

        elif hero.location == 'Kalm':
            kalm = Location(
                population=20,
                input_name='Kalm',
                demographics={
                    Archer: 0.1,
                    Warrior: 0.2,
                    Elder: 0.5
                    }
            )

            input('A bustling town with purple roofs, beset with snow...')
            
            person = choice(kalm.inhabitants)
            person.chat(hero)

if __name__ == '__main__':
    main()