from person import *

class Faction:
    '''
    A Faction is a collection of Persons
    with a common in-game goal.

    It is defined with a name and a dictionary
    of members and their titles within the
    faction, and a dictionary of other factions
    and this faction's opinions on them.

    The primary function of a faction is to
    define the relationship between different
    characters in the game. Different factions
    have different opinions of each other, and
    of non-members.
    '''
    #################################################################

    def __init__(self,
                 name='generic_faction',
                 membership_dict={},
                 opinions_dict={}
                 ):
        '''
        Assigns the following characteristics:
        - name (str)
        - members (dict, keys = faction title (str), 
        values = Persons with that title (Person))
        - opinions of other factions (dict,
        keys = names of other factions (str),
        values = opinion of that faction (float -1 - 1,
        -1 = reviled, 0 = neutral, 1 = beloved))
        '''
        self.name = name
        self.members = membership_dict
        self.opinions = opinions_dict

    #################################################################

    def opinion(self,in_person):
        '''
        Accepts a Person object.

        Checks that Person's faction affiliation,
        then the opinion of this faction on theirs.

        Returns a float between -1 and 1 rating the opinion
        (-1 = reviled, 0 = neutral, 1 = beloved).
        '''
        if not isinstance(in_person,Person):
            input('ERROR IN FACTION: in_person is not Person, \
                  cannot determine faction opinion.')
            return 0
        
        if not in_person.faction:
            return 0
        else:
            for faction in self.opinions:
                if faction == in_person.faction:
                    return self.opinions[faction]
                
#################################################################
#################################################################
#################################################################

if __name__ == '__main__':

    Huns = Faction('Huns')
    Romans = Faction('Romans')
    Goths = Faction('Goths')
    Chinese = Faction('Chinese')
    
    huns_members = {'Attila': 'God-King',
                    'Steve': 'whipping boy'
    }
    
    huns_opinions = {Romans: -0.9,
                     Goths: 0.2,
                     Chinese: 0.7
    }

    Huns.members = huns_members
    Huns.opinions = huns_opinions

    romans_members = {'Augustus': 'Emperor',
                      'Romulus': 'Founder',
                      'Doof': 'idiot'
    }
    
    romans_opinions = {Huns: -0.6,
                       'Goths': -0.1,
                       'Celts': 0.6,
                       'Romans': 1
    }

    Romans.members = romans_members
    Romans.opinions = romans_opinions
    
    Caesar = Person(faction=Romans,allegiance=0.9)
    Attila = Person(faction=Huns,allegiance=0.7)
    poop = Person()

    print('Huns opinions:\n')
    for faction in Huns.opinions:
        print(f"{faction.name}: {Huns.opinions[faction]}")
        
    print(f'Romans\' opinion of poop: {Romans.opinion(poop)}')
    print(f"Romans' opinion of Attila: {Romans.opinion(Attila)}")
    print(f"Caesar's faction and allegiance: {Caesar.faction.name}, {Caesar.allegiance}")