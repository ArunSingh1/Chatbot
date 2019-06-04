


class Player:
    rating_rate = 5 #class variable
    numberofplayer = 0
    def __init__(self, first, last, goals, matches, typeofplayer):  # self becomes player1 like player1.first = first
        self.first = first  # instances instance varibles are unique, name email.
        self.last = last
        self.goals = goals
        self.matches = matches
        self.typeofplayer = typeofplayer
        Player.numberofplayer += 1                      #we dont need to change this variable for differet cases as rating so we use Player.
    def fullname(self):  # method
        return '{} {}'.format(self.first, self.last)
    def email(self):
        return self.first + '.' + self.last + '@football.com'
    def rating(self):
        self.goals = int(self.goals * self.rating_rate)   #self here gives us a ability to change rating rate for each instanses

    @classmethod
    def fromplayer(cls, playstr):
        first, last, goals,matches,typeofplayer = playstr.split('-')
        return cls(first, last, goals,matches,typeofplayer)


    @staticmethod
    def playday(day):
        if day.weekday() ==5 or day.weekday() ==6:
            return True
        return False

class Manager(Player): #Manager childs class extends the Player parent class
    rating_rate = 1.10
    def __init__(self,first, last, goals, matches, typeofplayer, country):
        super().__init__(first, last, goals, matches, typeofplayer)
        self.country = country

class Owner(Player):   #Owner childs class extends the Player parent class
    def __init__(self, first, last, goals, matches, typeofplayer, country, networth):
        super().__init__(first, last, goals, matches, typeofplayer)
        self.country = country
        self.networth = networth

class Selection_club(Player):
    def __init__(self, first, last, goals, matches, typeofplayer, player = None):
        super().__init__(first, last, goals, matches, typeofplayer)
        if player is None:
            self.player = []
        else:
            self.player = player

    def add_player(self,play):
        if play not in self.player:
            self.player.append(play)

    def remove_player(self,play):
        if play in self.player:
            self.player.remove(play)

    def list_players(self):
        for play in self.player:
            print("-->", play.fullname())

print(Player.numberofplayer)
player1 = Player('leionel', 'messi', 450,1000, 'attacker' )
player2 = Player('chris', 'ronaldo', 480,1000, 'attacker' )
player3 = Player('frank', 'lampard', 420,1000, 'midfeider')
man1 = Manager('chris', 'morris', 450,2500, 'midfeilder', 'russia') #new instance for child class manager
man2 = Manager('john', 'willis', 450,2500, 'midfeilder', 'england')  #new instance for child class manager

own1 = Owner('Jack', 'reacher', 450,2500, 'midfeilder', 'england', '18billion')   #new instance for child class owner with another attribute networth
own1 = Owner('will', 'Smith', 450,3000, 'goallie', 'england', '18billion')

selector1 = Selection_club('Arun', 'Singh', 480,2500,'attacker', player=[])

playstr = 'diago-proga-455-1000-gollie'

player4 = Player.fromplayer(playstr)

# print(player4.__dict__)
# print(man1.__dict__)

import datetime
mydate = datetime.date(2016,7,10)
print(Player.playday(mydate))
#
# print(man1.email)
# print(man1.country)
# print(man2.__dict__)
#
#
# print(own1.__dict__)

#print(selector1.__dict__)

selector1.add_player(player3)
selector1.add_player(player2)
(selector1.list_players())
(selector1.player)
#print(help(Manager))