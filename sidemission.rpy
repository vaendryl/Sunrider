


label startsidemissioning:
    python:
        #If you don't do this bit, then money, command points and ships from the main game will not be available in your side mission.
        #Singleton pattern for SideBM implemented via the try... except bit.
        try:
            SideBM.money = BM.money
        except:
            SideBM = Sidemission()
            SideBM.money = BM.money
        SideBM.cmd = BM.cmd
        SideBM.ships = BM.ships

        #If you don't do this bit, then your side mission simply will not work.
        BM = SideBM

    #Put additional logic here if your 'side mission mode' looks special or whatever
    return


label stopsidemissioning:  #make sure you call this if you want the main story to work properly!
    python:
        #If you don't do this bit, then money, command points, and ships from your side missions will not be available in your main mission
        #Singleton pattern for MasterBM implemented using the try... except bit.
        #Not sure what will happen if you load a game that was saved during a sidemission and you're not synchronizing the MasterBM and the BM.
        try:
            MasterBM.money = BM.money
        except:
            MasterBM = Battle()
            MasterBM.money = BM.money
        MasterBM.cmd = BM.cmd
        MasterBM.ships = BM.ships

        #If you don't do this bit, then your main mission simply will not work.
        BM = MasterBM
    #Put additional logic here if your 'side mission mode' looks special or whatever
    return

init python:
    class Sidemission(Battle):

        def __init__(self, newstorylabel = 'YouForgotToSetTheStoryLabel'):
            Battle.__init__(self)
            self.storylabel = newstorylabel  #You need to set this, so that the battle loop will work.

        def jumptomission(self):
            renpy.jump(self.storylabel)

        #Uncomment this if you want your battlemanager to have the formation editor at the beginning of a mission.
        #def editableformations(self):
        #    return True

        #Uncomment this if you want to implement a special loss condition.  Call you_lose() if the player has lost.  If the player doesn't have any ships, it'll be hard to win...
        #def check_for_loss(self):
        #    if len(player_ships) == 0:
        #        self.you_lose()

        #Uncomment this if you want to do something funky when the player loses, like jumping to a prison storyline or whatever.
        #def you_lose(self):  #Separated for mod support, in case something other than 'better luck next time' or 'game over' is the consequence of losing
        #    show_message('You were defeated! I hope that the modder added a label for myprisonstoryline...')
        #    clean_battle_exit()
        #    renpy.jump('myprisonstoryline')

        #Uncomment this if you want to do something funky when a boss ship dies, as opposed to going straight to a victory condition
        #def boss_died(self, deadboss):
        #   if deadboss == Havoc:
        #       show_message('Cosette is taken out of the battle.  It turns out that her threat about a bomb on the Sunrider was true!')
        #       Sunrider.takedamage(400)
        #   else:
        #       self.you_win()

        #Uncomment this if you want to do a special check for your custom victory condition.  Note that if a boss ship is destroyed, it will call you_win()
        #def check_for_win(self):
        #    if len(enemy_ships) == 0:
        #        self.you_win()

        #Don't override you_win() unless you know exactly why you're doing it.

