'''Nicholas Boni
12/23/2024
'''

import json
# import creatures.people.careers as careers
# import items.quest_items as quest_items

# from locations.location import Location
# from creatures.people.hero import Hero

class Quest:
    """A Quest is a sequence of actions that can be taken by a user to move
    a storyline along.

    Quests contain a set of related characters, decisions, and outcomes.
    """
    def __init__(
            self,
            name='',
            start_loc_name='',
            characters={},
            items={},
            stage='',
            stages={},
            started=False,
            active=False,
            completed=False
    ):
        """Creates new Quest object.

        Args:
            name (str, optional): Quest name. Defaults to ''.
            start_loc_name (str, optional): Name of start location for this quest. 
                Defaults to ''.
            characters (dict, optional): Dict of quest characters. Currently unused.
                Defaults to {}.
            items (dict, optional): Dict of quest items. Currently unused.
                Defaults to {}.
            stage (str, optional): Current stage of this quest. Defaults to ''.
            stages (dict(str: str), optional): Dict of stage codes and strings related to
                this quest. Defaults to {}.
            started (bool, optional): Whether this quest has been started.
                Defaults to False.
            active (bool, optional): Whether this quest is currently active. 
                Defaults to False.
            completed (bool, optional): Whether this quest is completed. 
                Defaults to False.
        """        

        self.name = name
        self.start_loc_name = start_loc_name
        self.characters = characters
        self.items = items
        self.stage = stage
        self.stages = stages
        self.started = started
        self.active = active
        self.completed = completed

    def begin(self, start_loc):
        """Adds quest characters to quest start location.
        Sets `self.started`, `self.active` to True.

        Args:
            start_loc (Location): Start location of this quest. Quest characters
                will be added to start_loc.inhabitants.
        """        
        for character in self.characters:
            start_loc.inhabitants.append(character)
        self.started = True
        self.active = True

    def log(self):
        """Writes current quest status to `quests/quest_progress.json`.
        """        
        quest_status = {self.name: self.stage}
        with open('quests/quest_progress.json', 'w') as f:
            f.write( json.dumps(quest_status) )

    def set_stage(self, stage):
        """Checks that `stage` is in `self.stages`. If so, sets `self.stage`
        to `stage`.

        Args:
            stage (str): Quest stage to set. Must correspond to valid value
                in `quests/quests.json`.

        Raises:
            KeyError: If stage not in `self.stages`.
        """        
        if stage not in self.stages:
            raise KeyError(f'Tried to set stage that does not exist for this quest: \
                           "{stage}", \
                           {self.stages}'
                           )
        
        self.stage = stage
        self.log()
    
    def end(self):
        """Sets `self.active` to False, `self.completed` to True.
        """        
        self.active = False
        self.completed = True

    def end_msg(self):
        """Returns quest end stage message.

        Returns:
            str: Quest end stage message.
        """        
        with open('quests/quests.json') as f:
            quest_stages = json.load(f)
        
        quest_stage_msg = quest_stages[self.name][self.stage]

        return f'Plot completed: {self.name}\n' + quest_stage_msg
