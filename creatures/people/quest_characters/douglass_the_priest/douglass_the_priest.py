'''Nicholas Boni
12/23/2024'''

import mechanics.fileops as fileops
from creatures.people.careers import Priest

class Douglass_the_Priest(Priest):
    def __init__(self):
        super().__init__(name='Douglass')

    def get_convo(self,*args):
        outstr = f'{self.name}: ' + fileops.get_in_game_text(
            'creatures/people/quest_characters/douglass_the_priest/douglass_the_priest.json',
            *args
            )
        return outstr

    def chat(self, other, quest=None):
        if quest:
            if quest.started and not quest.completed:
                if other.location == 'Kalm, church, entrance':
                    print()
                    worship_response = input(
                        self.get_convo('worship-prompt')
                    )
                    if worship_response == 'y':
                        print( self.get_convo('worship-y') )
                        other.location = 'Kalm, church, altar'

                    elif worship_response == 'n':
                        print()
                        seek_response = input( self.get_convo('worship-n-seek-prompt') )
                        if seek_response == 'nothing':
                            print(self.get_convo('nothing-worship-n'))
                        quest.set_stage('worship-n')
                        quest.end()
                        quest.log()
                        print('Plot completed: Give Alms.')
                        input(fileops.get_in_game_text(
                            'quests/quests.json','Kalm, church, entrance','Give Alms','worship-n'
                            )
                        )
            else:
                seek_response = input(self.get_convo('worship-y-seek-prompt'))
                
                if seek_response == 'directions':
                    print(self.get_convo('directions'))
                elif seek_response == 'nothing':
                    if quest.stage == 'worship-n':
                        print(self.get_convo('nothing-worship-n'))
                    else:
                        print(self.get_convo('nothing-worship-y'))
                
                if quest.stage == 'alms-y':
                    if seek_response == 'food':
                        print(self.get_convo('food-worship-y-alms-y'))
                    elif seek_response == 'shelter':
                        print(self.get_convo('shelter-worship-y-alms-y'))

                if quest.stage == 'alms-n':
                    if seek_response == 'food':
                        print(self.get_convo('food-worship-y-alms-n'))
                    elif seek_response == 'shelter':
                        print(self.get_convo('shelter-worship-y-alms-n'))              

        else:
            super().chat(self, other)