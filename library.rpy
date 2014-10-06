## this file defines all the different ships and weapons that you'll be using
## 1) player ships
## 2) PACT ships
## 3) pirate ships
## 4) weapons
## 5) store items

init 2 python:

###  PLAYER Ships ###

    class Sunrider(Battleship): # your ship!
        def __init__(self):
            super(Sunrider, self).__init__() # proper inheritance requires super()
            self.stype = 'Cruiser'
            self.name = 'Sunrider'
            self.animation_name = 'sunrider'
            self.faction = 'Player'
            self.max_hp = 1500
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 1
            self.max_rockets = 2
            self.repair_drones = None
            self.upgrades['base_armor'] = ['Armor',1,5,500,2]
            self.missiles = self.max_missiles
            self.rockets = 0
            self.evasion = -25  # cruisers are easy to hit
            self.lbl = 'Battle UI/label_sunrider.png'  #this is the battle avatar
            self.portrait = 'Battle UI/ava_portrait.png'
            self.flak = 40
            self.flak_range = 2
            self.move_cost = 30
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = 0
            self.base_armor = 15
            self.armor = self.base_armor
            self.test = 'test1234'
            self.test2 = 'test2'
            
            ####################UPGRADE BACKGROUND AND ICONS
            self.upgrade_menu = 'Menu/upgrade_sunrider.png'
            self.icon = 'Menu/upgrade_sunrider_button.png'
            self.hovericon = 'Menu/upgrade_sunrider_button_hover.png'
            
            ####################VOICES
            self.voice_channel = "avavoice"
            self.selection_voice = ['Ava/Ava Selection 1.ogg','Ava/Ava Selection 2.ogg','Ava/Ava Selection 3.ogg','Ava/Ava Selection 4.ogg','Ava/Ava Selection 5.ogg','Ava/Ava Selection 6.ogg','Ava/Ava Selection 7.ogg']
            self.moveforward_voice = ['Ava/Ava Move Forward 1.ogg','Ava/Ava Move Forward 2.ogg','Ava/Ava Move Forward 3.ogg']
            self.movebackward_voice = ['Ava/Ava Move Backward 1.ogg','Ava/Ava Move Backward 2.ogg','Ava/Ava Move Backward 3.ogg']
            self.buffed_voice = ['Ava/Ava Buffed 1.ogg','Ava/Ava Buffed 2.ogg','Ava/Ava Buffed 3.ogg']
            self.cursed_voice = ['Ava/Ava Cursed 1.ogg','Ava/Ava Cursed 2.ogg','Ava/Ava Cursed 3.ogg']

          ##the sunrider gets personal death code!
        def destroy(self,attacker,no_animation = False):
            BM.stopAI = True
            if not no_animation:
                try:
                    renpy.call_in_new_context('die_{}'.format(self.animation_name)) #show the death animation
                except:
                    show_message('missing animation. "die_{}" does\'t seem to exist'.format(self.animation_name))
            
            if BM.mission != 'skirmishbattle':
                a = self.location[0]-1  #make the next line of code a little shorter
                b = self.location[1]-1
                BM.grid[a][b] = False #tell the BM that the old cell is now free again
                player_ships.remove(self)
                BM.ships.remove(self)
                renpy.jump('sunrider_destroyed')
            else:
                BM.you_lose()

    class BlackJack(Battleship): # defining the Blackjack
        def __init__(self):
            super(BlackJack, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Black Jack'
            self.animation_name = 'blackjack'
            self.faction = 'Player'
            self.max_hp = 600
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 10
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 1
            self.missiles = self.max_missiles
            self.move_cost = 20
            self.hate = 100
            self.evasion = 25
            self.lbl = 'Battle UI/label_blackjack.png'  #this is the battle avatar
            self.portrait = 'Battle UI/asaga_portrait.png'
            self.sprites = {
                'standard':'gameplay/Animations/BlackJack/blackjack.png',
                'melee':'gameplay/Animations/BlackJack/blackjack_sword.png',
                'character':"Character/Asaga/asaga_plugsuit_point_happy.png"
                }
            self.flak = 35
            
            ####################UPGRADE BACKGROUND AND ICONS
            self.upgrade_menu = 'Menu/upgrade_blackjack.png'
            self.icon = 'Menu/upgrade_blackjack_button.png'
            self.hovericon = 'Menu/upgrade_blackjack_button_hover.png'
            
            ####################VOICES
            self.voice_channel = "asavoice"
            self.attack_voice = ["sound/Voice/Asaga/Asaga Melee 1.ogg","sound/Voice/Asaga/Asaga Melee 2.ogg","sound/Voice/Asaga/Asaga Melee 3.ogg","sound/Voice/Asaga/Asaga Melee 4.ogg"]
            self.no_damage_voice = ["sound/Voice/Asaga/Asaga No Damage 1.ogg","sound/Voice/Asaga/Asaga No Damage 2.ogg","sound/Voice/Asaga/Asaga No Damage 3.ogg","sound/Voice/Asaga/Asaga No Damage 4.ogg","sound/Voice/Asaga/Asaga No Damage 5.ogg","sound/Voice/Asaga/Asaga No Damage 6.ogg"]
            self.selection_voice = ['Asaga/Asaga Select 1.ogg','Asaga/Asaga Select 2.ogg','Asaga/Asaga Select 3.ogg','Asaga/Asaga Select 4.ogg','Asaga/Asaga Select 5.ogg','Asaga/Asaga Select 6.ogg','Asaga/Asaga Select 7.ogg']
            self.moveforward_voice = ['Asaga/Asaga Forward 1.ogg','Asaga/Asaga Forward 2.ogg','Asaga/Asaga Forward 3.ogg']
            self.movebackward_voice = ['Asaga/Asaga Backwards 1.ogg','Asaga/Asaga Backwards 2.ogg','Asaga/Asaga Backwards 3.ogg']
            self.buffed_voice = ['Asaga/Asaga Buffed 1.ogg','Asaga/Asaga Buffed 2.ogg']
            self.cursed_voice = ['Asaga/Asaga Cursed 1.ogg','Asaga/Asaga Cursed 2.ogg','Asaga/Asaga Cursed 3.ogg']
            self.resurrect_voice = ['Asaga/Asaga Revive 1.ogg','Asaga/Asaga Revive 2.ogg']


    class Liberty(Battleship):  #you can use any existing blueprint as a base, which makes things really easy.
        def __init__(self):
            super(Liberty, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Liberty'
            self.animation_name = 'liberty'
            self.faction = 'Player'
            self.max_hp = 475
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 8
            self.armor = self.base_armor
            self.en = self.max_en
            self.move_cost = 20
            self.evasion = 20
            self.lbl = 'Battle UI/label_liberty.png'  #this is the battle avatar
            self.portrait = 'Battle UI/chigara_portrait.png'
            self.sprites = {
                'standard':'gameplay/Animations/Liberty/side.png'
                }
            self.flak = 0
            self.shield_generation = 35
            self.shields = self.shield_generation
            self.shield_range = 1
            
            ####################UPGRADE BACKGROUND AND ICONS
            self.upgrade_menu = 'Menu/upgrade_liberty.png'
            self.icon = 'Menu/upgrade_liberty_button.png'
            self.hovericon = 'Menu/upgrade_liberty_button_hover.png'

            ####################VOICES
            self.voice_channel = "chivoice"
            self.selection_voice = ['Chigara/Selection Line 1.ogg','Chigara/Selection Line 2.ogg','Chigara/Selection Line 3.ogg','Chigara/Selection Line 4.ogg','Chigara/Selection Line 5.ogg','Chigara/Selection Line 6.ogg','Chigara/Selection Line 7.ogg',]
            self.moveforward_voice = ['Chigara/Move Forward Line 1.ogg','Chigara/Move Forward Line 2.ogg','Chigara/Move Forward Line 3.ogg']
            self.movebackward_voice = ['Chigara/Move Backward Line 1.ogg','Chigara/Move Backward Line 2.ogg','Chigara/Move Backward Line 3.ogg']
            self.buffed_voice = ['Chigara/Buffed Line 1.ogg','Chigara/Buffed Line 2.ogg']
            self.cursed_voice = ['Chigara/Cursed Line 1.ogg','Chigara/Cursed Line 2.ogg','Chigara/Cursed Line 3.ogg']
            self.cursing_voice = ['Chigara/Curse Line 1.ogg','Chigara/Curse Line 2.ogg','Chigara/Curse Line 3.ogg','Chigara/Curse Line 4.ogg','Chigara/Curse Line 5.ogg','Chigara/Curse Line 6.ogg','Chigara/Curse Line 7.ogg','Chigara/Curse Line 8.ogg','Chigara/Curse Line 9.ogg','Chigara/Curse Line 10.ogg']
            self.resurrect_voice = ['Chigara/Revive Line 1.ogg','Chigara/Revive Line 2.ogg']


    class Phoenix(Battleship):
        def __init__(self):
            super(Phoenix, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Phoenix'
            self.animation_name = 'phoenix'
            self.faction = 'Player'
            self.max_hp = 300
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 0
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 10
            self.hate = 100
            self.evasion = 50
            self.lbl = 'Battle UI/label_phoenix.png'  #this is the battle avatar
            self.portrait = 'Battle UI/icari_portrait.png'
            self.sprites = {
                'standard':'gameplay/Animations/Phoenix/side.png',
                'melee':'gameplay/Animations/Phoenix/melee.png',
                'character':"Character/Icari/icari_plugsuit_point_angry.png"
                }
            self.flak = 20
            self.upgrades['max_hp'] = ['Hull Plating',1,100,100,2.0]
            
            ####################UPGRADE BACKGROUND AND ICONS
            self.upgrade_menu = 'Menu/upgrade_phoenix.png'
            self.icon = 'Menu/upgrade_phoenix_button.png'
            self.hovericon = 'Menu/upgrade_phoenix_button_hover.png'

            ####################VOICES
            self.voice_channel = "icavoice"
            self.selection_voice = ['Icari/Icari Selection 1.ogg','Icari/Icari Selection 2.ogg','Icari/Icari Selection 3.ogg','Icari/Icari Selection 4.ogg','Icari/Icari Selection 5.ogg','Icari/Icari Selection 6.ogg','Icari/Icari Selection 7.ogg']
            self.attack_voice = ['sound/Voice/Icari/Icari Attacking Melee 1.ogg','sound/Voice/Icari/Icari Attacking Melee 2.ogg','sound/Voice/Icari/Icari Attacking Melee 3.ogg','sound/Voice/Icari/Icari Attacking Melee 4.ogg']
            self.no_damage_voice = ['Icari/Icari No Damage 1.ogg','Icari/Icari No Damage 2.ogg','Icari/Icari No Damage 3.ogg','Icari/Icari No Damage 4.ogg','Icari/Icari No Damage 5.ogg','Icari/Icari No Damage 6.ogg','Icari/Icari No Damage 7.ogg']
            self.moveforward_voice = ['Icari/Icari Move Forward 1.ogg','Icari/Icari Move Forward 2.ogg','Icari/Icari Move Forward 3.ogg']
            self.movebackward_voice = ['Icari/Icari Move Backward 1.ogg','Icari/Icari Move Backward 2.ogg','Icari/Icari Move Backward 3.ogg']
            self.buffed_voice = ['Icari/Icari Buffed 1.ogg','Icari/Icari Buffed 2.ogg']
            self.cursed_voice = ['Icari/Icari Cursed 1.ogg','Icari/Icari Cursed 2.ogg','Icari/Icari Cursed 3.ogg','Icari/Icari Cursed 4.ogg']
            self.resurrect_voice = ['Icari/Icari Revive 1.ogg','Icari/Icari Revive 2.ogg']

    class Bianca(Battleship):
        def __init__(self):
            super(Bianca, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Bianca'
            self.animation_name = 'bianca'
            self.faction = 'Player'
            self.max_hp = 400
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 4
            self.armor = self.base_armor
            self.en = self.max_en
            self.move_cost = 30
            self.evasion = 20
            self.lbl = 'Battle UI/label_bianca.png'  #this is the battle avatar
            self.portrait = 'Battle UI/claude_portrait.png'
            self.sprites = {
                'standard':'gameplay/Animations/Bianca/side.png'
                }
            self.flak = 0
            self.shield_generation = 35
            self.shields = self.shield_generation
            self.shield_range = 1
            
            ####################UPGRADE BACKGROUND AND ICONS
            self.upgrade_menu = 'Menu/upgrade_bianca.png'
            self.icon = 'Menu/upgrade_bianca_button.png'
            self.hovericon = 'Menu/upgrade_bianca_hover.png'

            ####################VOICES
            self.voice_channel = "clavoice"
            self.selection_voice = ['Claude/Selection 1.ogg','Claude/Selection 2.ogg','Claude/Selection 3.ogg','Claude/Selection 4.ogg','Claude/Selection 5.ogg','Claude/Selection 6.ogg','Claude/Selection 7.ogg',]
            self.moveforward_voice = ['Claude/Forward 1.ogg','Claude/Forward 2.ogg','Claude/Forward 3.ogg']
            self.movebackward_voice = ['Claude/Backward 1.ogg','Claude/Backward 2.ogg','Claude/Backward 3.ogg']
            self.buffed_voice = ['Claude/Buffed 1.ogg','Claude/Buffed 2.ogg']
            self.cursed_voice = ['Claude/Cursed 1.ogg','Claude/Cursed 2.ogg','Claude/Cursed 4.ogg','Claude/Cursed 5.ogg']
            self.cursing_voice = ['Claude/Curse 1.ogg','Claude/Curse 2.ogg','Claude/Curse 3.ogg','Claude/Curse 4.ogg','Claude/Curse 5.ogg','Claude/Curse 6.ogg','Claude/Curse 7.ogg','Claude/Curse 8.ogg','Claude/Curse 9.ogg','Claude/Curse 10.ogg']
            self.resurrect_voice = ['Claude/Revive 1.ogg','Claude/Revive 2.ogg']

    class Seraphim(Battleship):
        def __init__(self):
            super(Seraphim, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Seraphim'
            self.animation_name = 'seraphim'
            self.faction = 'Player'
            self.max_hp = 375
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 4
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 30
            self.hate = 100
            self.evasion = 20
            self.lbl = 'Battle UI/label_seraphim.png'  #this is the battle avatar
            self.portrait = 'Battle UI/sola_portrait.png'
            self.upgrades['kinetic_dmg'] = ['Kinetic Damage',1,0.075,100,1.4]
            self.upgrades['kinetic_acc'] = ['Kinetic Accuracy',1,0.075,100,1.4]
            self.upgrades['kinetic_cost'] = ['Kinetic Energy Cost',1,-0.05,100,1.8]
            self.sprites = {
                'standard':'gameplay/Animations/Seraphim/side.png',
                }
            self.flak = 0
            
            ####################UPGRADE BACKGROUND AND ICONS
            self.upgrade_menu = 'Menu/upgrade_seraphim.png'
            self.icon = 'Menu/upgrade_seraphim_button.png'
            self.hovericon = 'Menu/upgrade_seraphim_hover.png'

            ####################VOICES
            self.voice_channel = "solvoice"
            self.selection_voice = ['Sola/Selection 1.ogg','Sola/Selection 2.ogg','Sola/Selection 3.ogg','Sola/Selection 4.ogg','Sola/Selection 5.ogg']
            self.no_damage_voice = ['Sola/Evade 1.ogg','Sola/Evade 2.ogg','Sola/Evade 3.ogg','Sola/Evade 4.ogg','Sola/Evade 5.ogg','Sola/Evade 6.ogg']
            self.moveforward_voice = ['Sola/Forward 1.ogg','Sola/Forward 2.ogg','Sola/Forward 3.ogg']
            self.movebackward_voice = ['Sola/Backward 1.ogg','Sola/Backward 2.ogg','Sola/Backward 3.ogg','Sola/Backward 4.ogg']
            self.buffed_voice = ['Sola/Buffed 1.ogg','Sola/Buffed 2.ogg']
            self.cursed_voice = ['Sola/Curse 1.ogg','Sola/Curse 2.ogg','Sola/Curse 3.ogg','Sola/Curse 4.ogg']
            self.resurrect_voice = ['Sola/Revive1.ogg','Sola/Revive2.ogg']

    class Paladin(Battleship):
        def __init__(self):
            super(Paladin, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Paladin'
            self.animation_name = 'paladin'
            self.faction = 'Player'
            self.max_hp = 900
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 15
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 2
            self.missiles = self.max_missiles
            self.move_cost = 40
            self.hate = 100
            self.evasion = 10
            self.lbl = 'Battle UI/label_paladin.png'  #this is the battle avatar
            self.portrait = 'Battle UI/kryska_portrait.png'
            self.sprites = {
                'standard':'gameplay/Animations/Paladin/side.png',
                'character':"Character/Kryska/kryska_plugsuit_handonhip_focussmile.png"
                }
            self.flak = 18
            
            ####################UPGRADE BACKGROUND AND ICONS
            self.upgrade_menu = 'Menu/upgrade_paladin.png'
            self.icon = 'Menu/upgrade_paladin_button.png'
            self.hovericon = 'Menu/upgrade_paladin_button_hover.png'

            ####################VOICES
            self.voice_channel = "kryvoice"
            self.no_damage_voice = ["Kryska/No Damage 1.ogg","Kryska/No Damage 2.ogg","Kryska/No Damage 3.ogg","Kryska/No Damage 4.ogg","Kryska/No Damage 5.ogg","Kryska/No Damage 6.ogg"]
            self.selection_voice = ['Kryska/Selection 1.ogg','Kryska/Selection 2.ogg','Kryska/Selection 3.ogg','Kryska/Selection 4.ogg','Kryska/Selection 5.ogg','Kryska/Selection 6.ogg','Kryska/Selection 7.ogg']
            self.moveforward_voice = ['Kryska/Forward 1.ogg','Kryska/Forward 2.ogg','Kryska/Forward 3.ogg']
            self.movebackward_voice = ['Kryska/Backwards 1.ogg','Kryska/Backwards 2.ogg','Kryska/Backwards 3.ogg']
            self.buffed_voice = ['Kryska/Buffed 1.ogg','Kryska/Buffed 2.ogg']
            self.cursed_voice = ['Kryska/Cursed 1.ogg','Kryska/Cursed 2.ogg','Kryska/Cursed 3.ogg','Kryska/Cursed 4.ogg','Kryska/Cursed 5.ogg']
            self.resurrect_voice = ['Kryska/Revive 1.ogg','Kryska/Revive 2.ogg']

    class AllianceCruiser(Battleship):
        def __init__(self):
            super(AllianceCruiser, self).__init__()
            self.stype = 'Cruiser'
            self.name = 'Alliance Cruiser'
            self.animation_name = 'alliancecruiser'
            self.faction = 'Player'
            self.mercenary = True
            self.max_hp = 1200
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 12
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 1
            self.missiles = self.max_missiles
            self.move_cost = 30
            self.hate = 100
            self.evasion = 0
            self.lbl = 'Battle UI/label_alliancecruiser.png'  #this is the battle avatar
            self.default_weapon_list = [AllianceCruiserLaser(),AllianceCruiserMissile(),AllianceCruiserKinetic(),AllianceCruiserAssault()]
            self.portrait = None
            self.flak = 30
            self.flak_range = 2
            self.shield = 25
            self.shield_range = 1

            ####################VOICES
            self.voice_channel = "othvoice"
            self.no_damage_voice = ["sound/Voice/AllianceCruiser/We're Taking Fire.ogg"]
            self.selection_voice = ['AllianceCruiser/Alliance Cruiser Here.ogg','AllianceCruiser/Reporting For Duty.ogg']
            self.moveforward_voice = ['AllianceCruiser/Yes Sir.ogg']
            self.movebackward_voice = ['AllianceCruiser/Yes Sir.ogg']
            self.buffed_voice = ['AllianceCruiser/Reporting For Duty.ogg']
            self.cursed_voice = ['AllianceCruiser/Were Taking Fire.ogg']

    class AllianceBattleship(Battleship):
        def __init__(self):
            super(AllianceBattleship, self).__init__()
            self.stype = 'Battleship'
            self.name = 'Alliance Battleship'
            self.animation_name = 'alliancebattleship'
            self.faction = 'Player'
            self.mercenary = True
            self.max_hp = 2100
            self.hp = self.max_hp
            self.max_en = 120
            self.base_armor = 15
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 2
            self.missiles = self.max_missiles
            self.move_cost = 40
            self.hate = 100
            self.evasion = -25
            self.lbl = 'Battle UI/label_alliancebattleship.png'  #this is the battle avatar
            self.default_weapon_list = [AllianceBattleshipLaser(),AllianceBattleshipMissile(),AllianceBattleshipKinetic(),AllianceBattleshipCannon(),AllianceBattleshipAssault()]
            self.portrait = None
            self.flak = 30
            self.flak_range = 2
            self.shield = 25
            self.shield_range = 1

            ####################VOICES
            self.voice_channel = "othvoice"
            self.no_damage_voice = ["sound/Voice/AllianceBattleship/damage1.ogg","sound/Voice/AllianceBattleship/damage2.ogg","sound/Voice/AllianceBattleship/damage3.ogg"]
            self.selection_voice = ['AllianceBattleship/selection1.ogg','AllianceBattleship/selection2.ogg','AllianceBattleship/selection3.ogg']
            self.moveforward_voice = ['AllianceBattleship/move1.ogg','AllianceBattleship/move2.ogg']
            self.movebackward_voice = ['AllianceBattleship/move1.ogg','AllianceBattleship/move2.ogg']
            self.buffed_voice = ['AllianceBattleship/selection1.ogg','AllianceBattleship/selection2.ogg','AllianceBattleship/selection3.ogg']
            self.cursed_voice = ['AllianceBattleship/damage1.ogg','AllianceBattleship/damage2.ogg','AllianceBattleship/damage3.ogg']

    class UnionFrigate(Battleship):
        def __init__(self):
            super(UnionFrigate, self).__init__()
            self.stype = 'Frigate'
            self.name = 'Mining Union Frigate'
            self.animation_name = 'unionfrigate'
            self.faction = 'Player'
            self.mercenary = True
            self.max_hp = 475
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 4
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 20
            self.hate = 100
            self.evasion = 5
            self.blbl = 'Battle UI/label_unionfrigate.png'  #base(default) label
            self.lbl = self.blbl
            self.default_weapon_list = [UnionFrigateLaser(),ShdJam()]  #just this?
            self.portrait = None
            self.flak = 0
            self.flak_range = 0
            self.shield = 0
            self.shield_range = 0

            ####################VOICES
            self.voice_channel = "othvoice"
            self.no_damage_voice = ["sound/Voice/UnionFrigate/hit1.ogg"]
            self.selection_voice = ['UnionFrigate/selection1.ogg','UnionFrigate/selection2.ogg','UnionFrigate/selection3.ogg']
            self.moveforward_voice = ['UnionFrigate/attack1.ogg','UnionFrigate/attack2.ogg']
            self.movebackward_voice = ['UnionFrigate/attack1.ogg','UnionFrigate/attack2.ogg']
            self.buffed_voice = ['UnionFrigate/selection2.ogg']
            self.cursed_voice = ['UnionFrigate/attack1.ogg','UnionFrigate/attack2.ogg']
            self.cursing_voice = []


    class Agamemnon(Battleship):
        def __init__(self):
            super(Agamemnon, self).__init__()
            self.stype = 'Ship'
            self.name = 'Agamemnon'
            self.animation_name = 'agamemnon'
            self.faction = 'Player'
            self.max_hp = 800
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 8
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 50
            self.hate = 300
            self.evasion = 0
            self.lbl = 'Battle UI/label_agamemnon.png'  #this is the battle avatar
            self.portrait = None
            self.flak = 0
            self.flak_range = 0

            self.voice_channel = "avavoice"
            self.selection_voice = ['Agamemnon/beep1.ogg']
            self.moveforward_voice = ['Agamemnon/beep2.ogg']
            self.movebackward_voice = ['Agamemnon/beep2.ogg']
            self.buffed_voice = ['Agamemnon/beep2.ogg']
            self.cursed_voice = ['Agamemnon/beep2.ogg']

        def destroy(self,attacker,no_animation = False):
            BM.stopAI = True
            if not no_animation:
                try:
                    renpy.call_in_new_context('die_{}'.format(self.animation_name)) #show the death animation
                except:
                    show_message('missing animation. "die_{}" does\'t seem to exist'.format(self.animation_name))
            a = self.location[0]-1  #make the next line of code a little shorter
            b = self.location[1]-1
            BM.grid[a][b] = False #tell the BM that the old cell is now free again
            BM.ships.remove(self)
            player_ships.remove(self)
            renpy.jump('sunrider_destroyed')

    class Freighter(Battleship):
        def __init__(self):
            super(Freighter, self).__init__()
            self.stype = 'Ship'
            self.name = 'Freighter'
            self.animation_name = 'mochi'
            self.faction = 'Player'
            self.max_hp = 1000
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 10
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 50
            self.hate = 300
            self.evasion = 0
            self.lbl = 'Battle UI/label_mochi.png'  #this is the battle avatar
            self.portrait = None
            self.flak = 0
            self.flak_range = 0

            self.voice_channel = "avavoice"
            self.selection_voice = ['Agamemnon/beep1.ogg']
            self.moveforward_voice = ['Agamemnon/beep2.ogg']
            self.movebackward_voice = ['Agamemnon/beep2.ogg']
            self.buffed_voice = ['Agamemnon/beep2.ogg']
            self.cursed_voice = ['Agamemnon/beep2.ogg']

        def destroy(self,attacker,no_animation = False):
            BM.stopAI = True
            if not no_animation:
                try:
                    renpy.call_in_new_context('die_{}'.format(self.animation_name)) #show the death animation
                except:
                    show_message('missing animation. "die_{}" does\'t seem to exist'.format(self.animation_name))
            a = self.location[0]-1  #make the next line of code a little shorter
            b = self.location[1]-1
            BM.grid[a][b] = False #tell the BM that the old cell is now free again
            BM.ships.remove(self)
            player_ships.remove(self)
            renpy.jump('sunrider_destroyed')

    class PhoenixBoaster(Battleship):
        def __init__(self):
            super(PhoenixBoaster, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Unknown Hostile'
            self.animation_name = 'phoenixboaster'
            self.faction = 'PACT'
            self.max_hp = 700
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 30
            self.move_cost = 15
            self.base_armor = 4
            self.money_reward = 300
            self.armor = 4
            self.default_weapon_list = [PhoenixBoasterLaser(),PhoenixBoasterAssault()]
            self.blbl = 'Battle UI/label_phoenixboaster.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/Phoenix/boaster_side.png',
                }
            self.flak = 20
            self.flak_range = 1

    class PactBomber(Battleship):
        def __init__(self):
            super(PactBomber, self).__init__()
            self.stype = 'Ryder' #subtype bomber
            self.name = 'PACT Bomber'
            self.animation_name = 'pactbomber'
            self.faction = 'PACT'
            self.max_hp = 400
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 2
            self.max_rockets = 1
            self.money_reward = 75
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.base_armor = 10  #Ryders are not typically armored
            self.armor = self.base_armor
            self.evasion = 5
            self.move_cost = 30
            self.blbl = 'Battle UI/label_pactbomber.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.default_weapon_list = [PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()]
            self.sprites = {
                'standard':'gameplay/Animations/PACTBomber/side.png',
                }
            self.flak = 0
            self.flak_range = 0

    class SeraphimEnemy(Battleship):
        def __init__(self):
            super(SeraphimEnemy, self).__init__()
            self.stype = 'Ryder' #subtype bomber
            self.name = 'Ryuvian Ryder'
            self.animation_name = 'seraphimenemy'
            self.faction = 'PACT'
            self.max_hp = 375
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 0
            self.max_rockets = 0
            self.money_reward = 150
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.base_armor = 4  #Ryders are not typically armored
            self.armor = self.base_armor
            self.evasion = 20
            self.move_cost = 30
            self.default_weapon_list = [SeraphimEnemyKinetic()]
            
            
            self.blbl = 'Battle UI/label_seraphimenemy.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/SeraphimEnemy/side.png',
                }
            self.flak = 0
            self.flak_range = 0

    class Mochi(Battleship):
        def __init__(self):
            super(Mochi, self).__init__()
            self.stype = 'Ship'
            self.name = 'Mochi'
            self.animation_name = 'mochi'
            self.faction = 'Player'
            self.max_hp = 1200
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 15
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 200
            self.hate = 100
            self.evasion = -20
            self.lbl = 'Battle UI/label_mochi.png'  #this is the battle avatar
            self.portrait = None
            self.flak = 0
            self.flak_range = 0

            self.voice_channel = "avavoice"
            self.selection_voice = ['Agamemnon/beep1.ogg']
            self.moveforward_voice = ['Agamemnon/beep2.ogg']
            self.movebackward_voice = ['Agamemnon/beep2.ogg']
            self.buffed_voice = ['Agamemnon/beep2.ogg']
            self.cursed_voice = ['Agamemnon/beep2.ogg']

        def destroy(self,attacker,no_animation = False):
            BM.stopAI = True
            if not no_animation:
                try:
                    renpy.call_in_new_context('die_{}'.format(self.animation_name)) #show the death animation
                except:
                    show_message('missing animation. "die_{}" does\'t seem to exist'.format(self.animation_name))
            a = self.location[0]-1  #make the next line of code a little shorter
            b = self.location[1]-1
            BM.grid[a][b] = False #tell the BM that the old cell is now free again
            BM.ships.remove(self)
            player_ships.remove(self)
            renpy.jump('sunrider_destroyed')

### PACT ships ###

    class MissileFrigate(Battleship):
        def __init__(self):
            super(MissileFrigate, self).__init__()
            self.stype = 'Frigate'
            self.name = 'PACT Missile Frigate'
            self.animation_name = 'pactmissilefrigate'
            self.faction = 'PACT'
            self.max_hp = 400
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.move_cost = 30
            self.money_reward = 100
            self.max_missiles = 6   #a lot of missiles, but it's all it has. things go wrong when it's out anywway
            self.missiles = self.max_missiles
            self.default_weapon_list = [PactFrigateMissile()]
            self.evasion = 0 # frigates get no penalty and no bonus to evasion
            self.blbl = 'Battle UI/label_missilefrigate.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.flak = 0
            self.flak_range = 0

    class PactMook(Battleship):
        def __init__(self):
            super(PactMook, self).__init__()
            self.stype = 'Ryder'
            self.name = 'PACT Mook'
            self.animation_name = 'pactmook'
            self.faction = 'PACT'
            self.max_hp = 300
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 25
            self.move_cost = 20
            self.base_armor = 0
            self.money_reward = 50
            self.armor = 0
            self.default_weapon_list = [PACTMookLaser(),PACTMookMissile(),PACTMookAssault()]
            self.blbl = 'Battle UI/label_pactmook.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/PACTMook/side.png'
                }
            self.flak = 10
            self.flak_range = 1

    class PhoenixEnemy(Battleship):
        def __init__(self):
            super(PhoenixEnemy, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Phoenix'
            self.animation_name = 'phoenixenemy'
            self.faction = 'PACT'
            self.max_hp = 300
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 50
            self.move_cost = 10
            self.base_armor = 0
            self.money_reward = 200
            self.armor = 0
            self.default_weapon_list = [PhoenixEnemyMelee(),PhoenixAssault()]
            self.blbl = 'Battle UI/label_phoenixenemy.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/Phoenix/side_mirror.png',
                'melee':'gameplay/Animations/Phoenix/melee_mirror.png',
                'character':"Character/Icari/icari_plugsuit_point_crazylaugh.png"
                }
            self.flak = 20
            self.flak_range = 1

            self.voice_channel = "icavoice"
            self.attack_voice = ["sound/Voice/Icari/Icari Attacking Melee 1.ogg","sound/Voice/Icari/Icari Attacking Melee 2.ogg","sound/Voice/Icari/Icari Attacking Melee 3.ogg","sound/Voice/Icari/Icari Attacking Melee 1.ogg"]

    class Nightmare(Battleship):
        def __init__(self):
            super(Nightmare, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Nightmare'
            self.animation_name = 'nightmare'
            self.faction = 'PACT' #for now...
            self.max_hp = 3200
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 50
            self.move_cost = 10
            self.base_armor = 20
            self.money_reward = 800
            self.max_missiles = 2
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.armor = 30
            self.default_weapon_list = [NightmareLaser(),NightmarePulse(),NightmareMissile(),NightmareMelee()]
            self.blbl = 'Battle UI/label_nightmare.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/Nightmare/side.png',
                'melee':'gameplay/Animations/Nightmare/melee.png',
                }
            self.flak = 100
            self.flak_range = 2
            self.shield_generation = 100
            self.shields = self.shield_generation
            self.shield_range = 2

    class Arcadius(Battleship):
        def __init__(self):
            super(Arcadius, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Arcadius'
            self.animation_name = 'nightmare'
            self.faction = 'PACT' #for now...
            self.max_hp = 1000
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 37
            self.move_cost = 20
            self.base_armor = 4
            self.money_reward = 300
            self.max_missiles = 1
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.armor = 4
            self.default_weapon_list = [ArcadiusLaser(),ArcadiusPulse(),ArcadiusMissile(),ArcadiusMelee()]
            self.blbl = 'Battle UI/label_nightmare.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/Nightmare/side.png',
                'melee':'gameplay/Animations/Nightmare/melee.png',
                }
            self.flak = 40
            self.flak_range = 1
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = 0

    class PactElite(Battleship):
        def __init__(self):
            super(PactElite, self).__init__()
            self.stype = 'Ryder'
            self.name = 'PACT Elite'
            self.animation_name = 'pactelite'
            self.faction = 'PACT' #for now...
            self.max_hp = 700
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 30
            self.move_cost = 20
            self.base_armor = 3
            self.money_reward = 80
            self.max_missiles = 1
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.armor = 3
            self.default_weapon_list = [PACTEliteLaser(),PACTEliteMissile(),PACTEliteMelee(),PACTEliteAssault()]
            self.blbl = 'Battle UI/label_pactelite.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/PACTElite/side.png',
                'melee':'gameplay/Animations/PACTElite/melee.png',
                }
            self.flak = 30
            self.flak_range = 1
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = 0

    class PactSupport(Battleship):
        def __init__(self):
            super(PactSupport, self).__init__()
            self.stype = 'Ryder'
            self.name = 'PACT Support'
            self.support = True  #signifies to the AI this unit uses support skills
            self.animation_name = 'pactsupport'
            self.faction = 'PACT'
            self.max_hp = 450
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 40
            self.move_cost = 20
            self.base_armor = 0
            self.money_reward = 80
            self.max_missiles = 0
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.armor = 0
            self.default_weapon_list = [PactRepair(), DisableLite(), PactRestore(), PactFlakOff(), PactShutOff()]
            self.blbl = 'Battle UI/pactsupport_label.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/PACTSupport/side.png',
                }
            self.flak = 0
            self.flak_range = 0
            self.shield_generation = 25
            self.shields = self.shield_generation
            self.shield_range = 1

    class PactCruiser(Battleship):
        def __init__(self):
            super(PactCruiser, self).__init__()
            self.stype = 'Cruiser'
            self.name = 'PACT Cruiser'
            self.faction = 'PACT'
            self.animation_name = 'pactcruiser'
            self.max_hp = 900
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.money_reward = 300
            self.max_missiles = 2
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -25  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_pactcruiser.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()]            
            self.flak = 30
            self.flak_range = 2
            self.shield_generation = 25
            self.shields = self.shield_generation
            self.shield_range = 1
            self.base_armor = 30
            self.move_cost = 30
            self.armor = self.base_armor

    class RyuvianCruiser(Battleship):
        def __init__(self):
            super(RyuvianCruiser, self).__init__()
            self.stype = 'Cruiser'
            self.name = 'Ryuvian Cruiser'
            self.faction = 'PACT'
            self.animation_name = 'ryuviancruiser'
            self.max_hp = 1200
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.money_reward = 370
            self.max_missiles = 2
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -20  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_ryuviancruiser.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [RyuvianCruiserKinetic(),RyuvianCruiserMissile()]
            self.flak = 0
            self.flak_range = 0
            self.shield_generation = 50
            self.shields = self.shield_generation
            self.shield_range = 2
            self.base_armor = 30
            self.move_cost = 20
            self.armor = self.base_armor

    class PactOutpost(Battleship):
        def __init__(self):
            super(PactOutpost, self).__init__()
            self.stype = 'Station'
            self.name = 'PACT Outpost'
            self.faction = 'PACT'
            self.animation_name = 'pactstation'
            self.max_hp = 900
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 0
            self.max_rockets = 0
            self.money_reward = 1000
            self.boss = True
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -40  # cruisers are easy to hit
            self.blbl = 'Battle UI/pactstation.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [PACTOutpostLaser(),PACTOutpostKinetic()]
            self.flak = 0
            self.flak_range = 0
            self.shield_generation = 25
            self.shields = self.shield_generation
            self.shield_range = 2
            self.base_armor = 20
            self.armor = self.base_armor
            self.move_cost = 1000

    class PactBattleship(Battleship):
        def __init__(self):
            super(PactBattleship, self).__init__()
            self.stype = 'Battleship'
            self.name = 'PACT Battleship'
            self.faction = 'PACT'
            self.animation_name = 'pactbattleship'
            self.max_hp = 1600
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.money_reward = 500
            self.max_missiles = 2
            self.max_rockets = 1
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -40  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_pactbattleship.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [PACTBattleshipLaser(),PACTBattleshipKinetic(),PACTBattleshipAssault(),PACTBattleshipMissile(),PACTBattleshipRocket()]
            self.flak = 40
            self.flak_range = 2
            self.shield_generation = 40
            self.shields = self.shield_generation
            self.shield_range = 2
            self.base_armor = 40
            self.move_cost = 50
            self.armor = self.base_armor

    class PactCarrier(Battleship):
        def __init__(self):
            super(PactCarrier, self).__init__()
            self.stype = 'Carrier'
            self.name = 'PACT Carrier'
            #indicate what units this carrier can spawn. syntax: [ship,cost,weaponlist]
            self.spawns = [
                ( PactMook,50,[ PACTMookLaser(),PACTMookMissile(),PACTMookAssault() ] ),
                ( PactBomber,100,[ PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket() ] )
                ]
            self.faction = 'PACT'
            self.animation_name = 'pactcarrier'
            self.max_hp = 1900
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.money_reward = 500
            self.max_missiles = 0
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -50
            self.blbl = 'Battle UI/label_pactcarrier.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [PACTCarrierAssault()]
            self.flak = 60
            self.flak_range = 2
            self.shield_generation = 50
            self.shields = self.shield_generation
            self.shield_range = 2
            self.base_armor = 40
            self.move_cost = 50
            self.armor = self.base_armor

    class PactAssaultCarrier(Battleship):
        def __init__(self):
            super(PactAssaultCarrier, self).__init__()
            self.stype = 'Assault Carrier'
            self.name = 'PACT Assault Carrier'
            #indicate what units this carrier can spawn. syntax: [ship,cost,weaponlist]
            self.spawns = [
                ( PactElite,60,[ PACTEliteLaser(),PACTEliteMissile(),PACTEliteAssault(),PACTEliteMelee() ] ),
                ( PactSupport,60,[ PactRepair(), DisableLite(), PactRestore(), PactFlakOff(), PactShutOff() ] )
                ]
            self.faction = 'PACT'
            self.animation_name = 'pactassaultcarrier'
            self.max_hp = 2000
            self.hp = self.max_hp
            self.max_en = 120
            self.en = self.max_en
            self.money_reward = 500
            self.max_missiles = 2
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -30
            self.blbl = 'Battle UI/label_pactassaultcarrier.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [PACTAssaultCarrierAssault(),PACTAssaultCarrierMissile(),PACTAssaultCarrierKinetic(),PACTAssaultCarrierLaser()]
            self.flak = 45
            self.flak_range = 2
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = 0
            self.base_armor = 20
            self.move_cost = 30
            self.armor = self.base_armor

    class Legion(Battleship):
        def __init__(self):
            super(Legion, self).__init__()
            self.stype = 'Super Dreadnought'
            self.name = 'Legion'
            self.faction = 'PACT'
            self.animation_name = 'legion'
            self.max_hp = 26000
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.money_reward = 2000
            self.max_missiles = 5
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -70  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_legion.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [LegionLaser(),LegionKinetic(),LegionMissile()]
            self.flak = 100
            self.flak_range = 2
            self.shield_generation = 100
            self.shields = self.shield_generation
            self.shield_range = 2
            self.base_armor = 80
            self.move_cost = 50
            self.armor = self.base_armor


### pirate ships ###

    class PirateBomber(Battleship):
        def __init__(self):
            super(PirateBomber, self).__init__()
            self.stype = 'Ryder' #subtype bomber
            self.name = 'Pirate Bomber'
            self.animation_name = 'piratebomber'
            self.faction = 'Pirate'
            self.max_hp = 350
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 1
            self.max_rockets = 1
            self.money_reward = 80
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.base_armor = 8  #Ryders are not typically armored
            self.armor = self.base_armor
            self.evasion = 10
            self.move_cost = 30
            self.blbl = 'Battle UI/label_piratebomber.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/PirateBomber/bomber_side.png'
                }
            self.flak = 20
            self.flak_range = 1
            self.default_weapon_list = [PirateBomberMissile(),PirateBomberRocket(),PirateBomberAssault()]

    class Havoc(PirateBomber):
        def __init__(self):
            super(Havoc, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Havoc'
            self.animation_name = 'havoc'
            self.faction = 'Pirate'
            self.max_hp = 1000
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.boss = True
            self.max_missiles = 2
            self.max_rockets = 1
            self.money_reward = 300
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.base_armor = 14
            self.armor = 14
            self.evasion = 8
            self.move_cost = 30
            self.blbl = 'Battle UI/havoc.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/Havoc/havoc.png',
                'melee':'gameplay/Animations/Havoc/havoc_melee.png',
                'character':"Character/Cosette/cosette_plugsuit_front_evilsmile.png"
                }
            self.flak = 20
            self.flak_range = 2
            self.default_weapon_list = [HavocMelee(),HavocAssault(),HavocMissile(),HavocRocket()]
            
            ##voices##
            self.voice_channel = "cosvoice"
            self.attack_voice = ["sound/Voice/Cosette/Cosette Melee Attack 1.ogg","sound/Voice/Cosette/Cosette Melee Attack 2.ogg","sound/Voice/Cosette/Cosette Melee Attack 3.ogg","sound/Voice/Cosette/Cosette Melee Attack 4.ogg"]


    class PirateGrunt(Battleship):
        def __init__(self):
            super(PirateGrunt, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Pirate Grunt'
            self.animation_name = 'pirategrunt'
            self.faction = 'Pirate'
            self.max_hp = 275
            self.hp = self.max_hp
            self.max_missiles = 0
            self.max_rockets = 0
            self.base_armor = 0
            self.armor = 0
            self.money_reward = 50
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = 12
            self.move_cost = 20
            self.blbl = 'Battle UI/label_pirategrunt.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.default_weapon_list = [PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()]
            self.sprites = {
                'standard':'gameplay/Animations/PirateGrunt/side.png'
                }
            self.flak = 15
            self.flak_range = 1

    class PirateDestroyer(Battleship):
        def __init__(self):
            super(PirateDestroyer, self).__init__()
            self.stype = 'Destroyer'
            self.name = 'Pirate Destroyer'
            self.animation_name = 'piratedestroyer'
            self.faction = 'Pirate'
            self.max_hp = 500
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.move_cost = 30
            self.evasion = -10
            self.money_reward = 100
            self.blbl = 'Battle UI/label_piratedestroyer.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.default_weapon_list = [PirateDestroyerLaser(),PirateDestroyerKinetic()]
            self.flak = 0
            self.flak_range = 0

    class PirateBase(Battleship):
        def __init__(self):
            super(PirateBase, self).__init__()
            self.stype = 'Station'
            self.name = 'Pirate Base'
            self.faction = 'Pirate'
            self.animation_name = 'piratebase'
            self.max_hp = 1200
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 5
            self.max_rockets = 0
            self.boss = True
            self.money_reward = 1000
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -50  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_piratebase.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [PirateBaseKinetic(),PirateBaseAssault(),PirateBaseMissile()]
            self.flak = 30
            self.flak_range = 1
            self.shield_generation = 25
            self.shields = self.shield_generation
            self.shield_range = 2
            self.base_armor = 50
            self.armor = self.base_armor
            self.move_cost = 1000

    class PirateIronhog(Battleship):
        def __init__(self):
            super(PirateIronhog, self).__init__()
            self.stype = 'Destroyer'
            self.name = 'Pirate Ironhog'
            self.faction = 'Pirate'
            self.animation_name = 'pirateironhog'
            self.max_hp = 480
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 0
            self.max_rockets = 3
            self.boss = False
            self.money_reward = 175
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -10  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_pirateironhog.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [PirateIronhogAssault(),PirateIronhogRocket()]
            self.flak = 60
            self.flak_range = 1
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = 0
            self.base_armor = 7
            self.armor = self.base_armor
            self.move_cost = 20


### Weapons ###

##############SUNRIDER WEAPONS
    class SunriderLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 200
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 120
            self.wtype = 'Laser'
            self.name = 'Trinities'
            self.lbl = 'Battle UI/button_laser.png'
            self.tooltip = """
            Lasers are accurate even from long distances, but lack fire power.
            Mitigated by enemy shields."""

    class SunriderMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 50
            self.energy_use = 30
            self.shot_count = 10
            self.accuracy = 80
            self.uses_rockets = False
            self.uses_missiles = True
            self.wtype = 'Missile'
            self.name = 'Sunrider_Missile'
            self.lbl = 'Battle UI/button_missile.png'
            self.tooltip = """
            Fires a barrage of guided missiles at the enemy. While individually weak,
            their large numbers provide heavy fire power and great accuracy even
            at long range. Limited in supply. Enemy flak and heavy armor mitigate missiles."""

    class SunriderKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 400
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 70
            self.wtype = 'Kinetic'
            self.name = 'Sunrider\'s main guns'
            self.lbl = 'Battle UI/button_kinetic.png'
            self.tooltip = """
            Kinetics pack a punch, but are inaccurate against distant or small foes.
            Armor is twice as effective at mitigating kinetic weaponry."""

    class SunriderPulse(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 25
            self.energy_use = 40
            self.shot_count = 10
            self.accuracy = 90
            self.wtype = 'Pulse'
            self.name = 'Sunrider_Pulse'
            self.lbl = 'Battle UI/button_pulse.png'
            self.tooltip = """
            Fires a high volume of laser pulses. Even if the enemy evades one bolt,
            others may still strike. Collectively, they are more powerful than
            stream lasers, but cannot pierce armor. Also mitigated by shields."""

    class SunriderAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 12
            self.energy_use = 30
            self.shot_count = 20
            self.accuracy = 70
            self.wtype = 'Assault'
            self.name = 'Sunrider\'s Flak'
            self.lbl = 'Battle UI/button_assault.png'
            self.tooltip = """
            Assault guns spray explosive low caliber rounds at the enemy. Even if
            the enemy evades one round, others may hit. Armor is twice as
            effective against assault. Also used to shoot down incoming enemy missiles,
            but loses effectiveness against sustained barrages."""

    class SunriderRocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 800
            self.energy_use = 30
            self.shot_count = 1
            self.accuracy = 100
            self.uses_rockets = True
            self.uses_missiles = False
            self.eccm = 10
            self.wtype = 'Rocket'
            self.name = 'Thermonuclear warhead'
            self.lbl = 'Battle UI/button_rocket.png'
            self.tooltip = """
            Fires a large rocket at the enemy topped with a devastating warhead.
            Highly limited in supply. Can be shot down by enemy flak."""

##############ALLIANCE CRUISER WEAPONS
    class AllianceCruiserLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 200
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 120
            self.wtype = 'Laser'
            self.name = 'AllianceCruiser_Laser'
            self.lbl = 'Battle UI/button_laser.png'
            self.tooltip = """
            Lasers are accurate even from long distances, but lack fire power.
            Mitigated by enemy shields."""

    class AllianceCruiserMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 70
            self.energy_use = 30
            self.shot_count = 5
            self.accuracy = 100
            self.uses_rockets = False
            self.uses_missiles = True
            self.wtype = 'Missile'
            self.name = 'AllianceCruiser_Missile'
            self.lbl = 'Battle UI/button_missile.png'
            self.tooltip = """
            Fires a barrage of guided missiles at the enemy. While individually weak,
            their large numbers provide heavy fire power and great accuracy even
            at long range. Limited in supply. Enemy flak and heavy armor mitigate missiles."""


    class AllianceCruiserKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 400
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 75
            self.wtype = 'Kinetic'
            self.name = 'AllianceCruiser_Kinetic'
            self.lbl = 'Battle UI/button_kinetic.png'
            self.tooltip = """
            Kinetics pack a punch, but are inaccurate against distant or small foes.
            Armor is twice as effective at mitigating kinetic weaponry."""


    class AllianceCruiserAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 12
            self.energy_use = 30
            self.shot_count = 15
            self.accuracy = 70
            self.wtype = 'Assault'
            self.name = 'AllianceCruiser_Assault'
            self.lbl = 'Battle UI/button_assault.png'
            self.tooltip = """
            Assault guns spray explosive low caliber rounds at the enemy. Even if
            the enemy evades one round, others may hit. Armor is twice as
            effective against assault. Also used to shoot down incoming enemy missiles,
            but loses effectiveness against sustained barrages."""

##############ALLIANCE BATTLESHIP WEAPONS
    class AllianceBattleshipLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 250
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 110
            self.wtype = 'Laser'
            self.name = 'AllianceBattleship_Laser'
            self.lbl = 'Battle UI/button_laser.png'
            self.tooltip = """
            Lasers are accurate even from long distances, but lack fire power.
            Mitigated by enemy shields."""

    class AllianceBattleshipMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 80
            self.energy_use = 30
            self.shot_count = 8
            self.accuracy = 100
            self.uses_rockets = False
            self.uses_missiles = True
            self.wtype = 'Missile'
            self.name = 'AllianceBattleship_Missile'
            self.lbl = 'Battle UI/button_missile.png'
            self.tooltip = """
            Fires a barrage of guided missiles at the enemy. While individually weak,
            their large numbers provide heavy fire power and great accuracy even
            at long range. Limited in supply. Enemy flak and heavy armor mitigate missiles."""

    class AllianceBattleshipKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 430
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 65
            self.wtype = 'Kinetic'
            self.name = 'AllianceBattleship_Kinetic'
            self.lbl = 'Battle UI/button_kinetic.png'
            self.tooltip = """
            Kinetics pack a punch, but are inaccurate against distant or small foes.
            Armor is twice as effective at mitigating kinetic weaponry."""

    class AllianceBattleshipCannon(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 1100
            self.energy_use = 120
            self.shot_count = 1
            self.accuracy = 60
            self.wtype = 'Kinetic'
            self.name = 'AllianceBattleship_Cannon'
            self.lbl = 'Battle UI/button_cannon.png'
            self.animation_name = 'kinetic2' 
            self.tooltip = """
            The ultimate in interstellar destruction. Can punch holes through
            the toughest armor, but requires an enormous amount of energy. Ineffective against
            small targets."""


    class AllianceBattleshipAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 25
            self.energy_use = 30
            self.shot_count = 15
            self.accuracy = 63
            self.wtype = 'Assault'
            self.name = 'AllianceBattleship_Assault'
            self.lbl = 'Battle UI/button_assault.png'
            self.tooltip = """
            Assault guns spray explosive low caliber rounds at the enemy. Even if
            the enemy evades one round, others may hit. Armor is twice as
            effective against assault. Also used to shoot down incoming enemy missiles,
            but loses effectiveness against sustained barrages."""


###################BLACK JACK WEAPONS

    class BlackjackLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 200
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 110
            self.wtype = 'Laser'
            self.name = 'Blackjack_Laser'
            self.lbl = 'Battle UI/button_laser.png'
            self.tooltip = """
            Lasers are accurate even from long distances, but lack fire power.
            Mitigated by enemy shields."""


    class BlackjackMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 40
            self.energy_use = 20
            self.shot_count = 10
            self.accuracy = 70
            self.uses_rockets = False
            self.uses_missiles = True
            self.wtype = 'Missile'
            self.name = 'Blackjack_Missile'
            self.lbl = 'Battle UI/button_missile.png'
            self.tooltip = """
            Fires a barrage of guided missiles at the enemy. While individually weak,
            their large numbers provide heavy fire power and great accuracy even
            at long range. Limited in supply. Enemy flak and heavy armor mitigate missiles. 
            """

    class BlackjackPulse(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 30
            self.energy_use = 50
            self.shot_count = 8
            self.accuracy = 80
            self.wtype = 'Pulse'
            self.name = 'Blackjack_Pulse'
            self.lbl = 'Battle UI/button_pulse.png'
            self.tooltip = """
            Fires a high volume of laser pulses. Even if the enemy evades one bolt,
            others may still strike. Collectively, they are more powerful than
            stream lasers, but cannot pierce armor. Also mitigated by shields."""

    class BlackjackAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 14
            self.energy_use = 30
            self.shot_count = 20
            self.accuracy = 65
            self.wtype = 'Assault'
            self.name = 'Blackjack_Assault'
            self.lbl = 'Battle UI/button_assault.png'
            self.tooltip = """
            Assault guns spray explosive low caliber rounds at the enemy. Even if
            the enemy evades one round, others may hit. Armor is twice as
            effective against assault. Also used to shoot down incoming enemy missiles,
            but loses effectiveness against sustained barrages."""

    class BlackjackMelee(Melee):
        def __init__(self):
            Melee.__init__(self)
            self.damage = 400    #multiplied by shot count
            self.energy_use = 50
            self.ammo_use = 0
            self.accuracy = 70
            self.acc_degradation = 0
            self.wtype = 'Melee'
            self.name = 'Zantetsuken'  #lol
            self.type = 'Melee'
            self.shot_count = 1
            self.lbl = 'Battle UI/button_melee.png'
            self.tooltip = """
            Slice an enemy ryder for devastating damage. However, can only be used on adjacent
            ryders. Moving directly next to an enemy ryder will trigger an enemy blindside attack."""


#############################################LIBERTY WEAPONS

    class LibertyLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 100
            self.energy_use = 50
            self.shot_count = 1
            self.accuracy = 110
            self.wtype = 'Laser'
            self.name = 'Liberty_Laser'
            self.lbl = 'Battle UI/button_laser.png'
            self.tooltip = """
            Lasers are accurate even from long distances, but lack fire power.
            Mitigated by enemy shields."""


###################PALADIN WEAPONS

    class PaladinMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 80
            self.energy_use = 20
            self.shot_count = 5
            self.accuracy = 70
            self.uses_rockets = False
            self.uses_missiles = True
            self.wtype = 'Missile'
            self.name = 'Paladin_Missile'
            self.lbl = 'Battle UI/button_missile.png'
            self.tooltip = """
            Fires a barrage of guided missiles at the enemy. While individually weak,
            their large numbers provide heavy fire power and great accuracy even
            at long range. Limited in supply. Enemy flak and heavy armor mitigate missiles."""
            
    class PaladinAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 14
            self.energy_use = 30
            self.shot_count = 10
            self.accuracy = 70
            self.wtype = 'Assault'
            self.name = 'Paladin_Assault'
            self.lbl = 'Battle UI/button_assault.png'
            self.tooltip = """
            Assault guns spray explosive low caliber rounds at the enemy. Even if
            the enemy evades one round, others may hit. Armor is twice as
            effective against assault. Also used to shoot down incoming enemy missiles,
            but loses effectiveness against sustained barrages."""


    class PaladinKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 400
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 70
            self.wtype = 'Kinetic'
            self.name = 'Paladin_Kinetic'
            self.lbl = 'Battle UI/button_kinetic.png'
            self.tooltip = """
            Kinetics pack a punch, but are inaccurate against distant or small foes.
            Armor is twice as effective at mitigating kinetic weaponry."""

############################################# PACT MISSILE FRIGATE

    class PactFrigateMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 50
            self.shot_count = 6
            self.energy_use = 60

############################################# PIRATE GRUNT

    class PirateGruntLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 120
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

    class PirateGruntMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 30
            self.energy_use = 30
            self.shot_count = 8
            self.accuracy = 70

    class PirateGruntAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 15
            self.energy_use = 40
            self.shot_count = 10
            self.accuracy = 60
            self.wtype = 'Assault'


######################################### HAVOC

    class HavocMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 30
            self.energy_use = 30
            self.shot_count = 8
            self.accuracy = 70
            self.wtype = 'Missile'

    class HavocAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 18
            self.energy_use = 50
            self.shot_count = 15
            self.accuracy = 60
            self.wtype = 'Assault'

    class HavocRocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 300
            self.energy_use = 50
            self.uses_rockets = True
            self.uses_missiles = False
            self.eccm = 10
            self.wtype = 'Rocket'
            self.accuracy = 60
            self.shot_count = 1

    class HavocMelee(Melee):
        #wow, I never realized the Havoc had a multi hit melee attack
        def __init__(self):
            Melee.__init__(self)
            self.damage = 40    #multiplied by shot count
            self.energy_use = 50
            self.ammo_use = 0
            self.accuracy = 140
            self.acc_degradation = 100
            self.wtype = 'Melee'
            self.shot_count = 10

########################################## PIRATE BOMBER

    class PirateBomberMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 30
            self.energy_use = 30
            self.shot_count = 6
            self.accuracy = 70
            self.wtype = 'Missile'

    class PirateBomberAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 14
            self.energy_use = 50
            self.shot_count = 10
            self.accuracy = 60
            self.wtype = 'Assault'

    class PirateBomberRocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 375
            self.energy_use = 50
            self.uses_rockets = True
            self.uses_missiles = False
            self.eccm = 10
            self.wtype = 'Rocket'
            self.accuracy = 60
            self.shot_count = 1

########################################## PIRATE IRONHOG

    class PirateIronhogAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 19
            self.energy_use = 50
            self.shot_count = 23
            self.accuracy = 65
            self.wtype = 'Assault'

    class PirateIronhogRocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 275
            self.energy_use = 60
            self.uses_rockets = True
            self.uses_missiles = False
            self.eccm = 10
            self.wtype = 'Rocket'
            self.accuracy = 80
            self.shot_count = 4

########################################### PIRATE DESTROYER

    class PirateDestroyerLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 150
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

    class PirateDestroyerKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 250
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 60

################################################PACT CRUISER

    class PACTCruiserLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 200
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

    class PACTCruiserKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 350
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 55

    class PACTCruiserAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 13
            self.energy_use = 40
            self.shot_count = 15
            self.accuracy = 50
            self.wtype = 'Assault'

################################################RYUVIAN CRUISER

    class RyuvianCruiserMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 60
            self.energy_use = 60
            self.shot_count = 5
            self.accuracy = 110

    class RyuvianCruiserKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 350
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 60

################################################ENEMY SERAPHIM

    class SeraphimEnemyKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 300
            self.energy_use = 100
            self.shot_count = 1
            self.accuracy = 150


################################################PACT OUTPOST

    class PACTOutpostLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 150
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 110

    class PACTOutpostKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 150
            self.energy_use = 60
            self.shot_count = 2
            self.accuracy = 50

################################################PACT BATTLESHIP

    class PACTBattleshipLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 250
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

    class PACTBattleshipKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 500
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 55

    class PACTBattleshipAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 25
            self.energy_use = 30
            self.shot_count = 15
            self.accuracy = 50
            self.wtype = 'Assault'

    class PACTBattleshipMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 40
            self.energy_use = 40
            self.shot_count = 10
            self.accuracy = 80
            self.wtype = 'Missile'

    class PACTBattleshipRocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 700
            self.energy_use = 50
            self.uses_rockets = True
            self.uses_missiles = False
            self.eccm = 10
            self.wtype = 'Rocket'
            self.accuracy = 80
            self.shot_count = 1

################################################PACT ASSAULT CARRIER

    class PACTAssaultCarrierLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 320
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 100

    class PACTAssaultCarrierKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 350
            self.energy_use = 60
            self.shot_count = 2
            self.accuracy = 65

    class PACTAssaultCarrierAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 30
            self.energy_use = 30
            self.shot_count = 15
            self.accuracy = 55
            self.wtype = 'Assault'

    class PACTAssaultCarrierMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 50
            self.energy_use = 30
            self.shot_count = 10
            self.accuracy = 80
            self.wtype = 'Missile'

################################################LEGION

    class LegionLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 500
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 100

    class LegionKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 300
            self.energy_use = 50
            self.shot_count = 5
            self.accuracy = 65

    class LegionMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 200
            self.energy_use = 50
            self.shot_count = 10
            self.accuracy = 100
            self.wtype = 'Missile'


###################################################################PACT CARRIER

    class PACTCarrierAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 25
            self.energy_use = 30
            self.shot_count = 20
            self.accuracy = 50
            self.wtype = 'Assault'


#################################################PACT MOOK

    class PACTMookLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 140
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

    class PACTMookMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 30
            self.energy_use = 30
            self.shot_count = 9
            self.accuracy = 70

    class PACTMookAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 20
            self.energy_use = 40
            self.shot_count = 10
            self.accuracy = 60
            self.wtype = 'Assault'


######################################### PACT ELITE

    class PACTEliteMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 50
            self.energy_use = 30
            self.shot_count = 10
            self.accuracy = 70
            self.wtype = 'Missile'

    class PACTEliteAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 18
            self.energy_use = 40
            self.shot_count = 20
            self.accuracy = 65
            self.wtype = 'Assault'

    class PACTEliteLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 230
            self.energy_use = 60
            self.accuracy = 110
            self.shot_count = 1

    class PACTEliteMelee(Melee):
        def __init__(self):
            Melee.__init__(self)
            self.damage = 375
            self.energy_use = 50
            self.accuracy = 180
            self.acc_degradation = 100
            self.wtype = 'Melee'
            self.shot_count = 1

######################################### PACT SUPPORT

    class PactRepair(Support):
            def __init__(self):
                Support.__init__(self)
                self.repair = True
                self.damage = 300 #also used for heals
                self.energy_use = 60
                self.name = 'Repair I'
                self.shot_count = 1
                
    class DisableLite(Curse): #halves available EN
            def __init__(self):
                Curse.__init__(self)
                self.energy_use = 100
                self.accuracy = 9999
                self.modifies = 'energy regen'
                self.buff_strength = -50
                self.buff_duration = 2 
                self.name = 'Disable Lite'
                
    class PactRestore(Support):
            def __init__(self):
                Support.__init__(self)
                self.energy_use = 60
                self.modifies = 'restore'
                self.buff_strength = 1
                self.buff_duration = 1
                self.name = 'Restore'

    class PactFlakOff(Curse):
            def __init__(self):
                Curse.__init__(self)
                self.energy_use = 40
                self.modifies = 'flak'
                self.sort_on = 'pship.flak'
                self.accuracy = 9999
                self.buff_strength = -100
                self.buff_duration = 2
                self.name = 'Flak Off'

    class PactShutOff(Curse):  
        def __init__(self):
            Curse.__init__(self)
            self.energy_use = 40
            self.accuracy = 9999
            self.modifies = 'shield_generation'
            self.sort_on = 'pship.shield_generation'
            self.buff_strength = -100
            self.buff_duration = 2
            self.name = 'Shield Down'
            
            
############################################## PIRATE BASE

    class PirateBaseKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 100
            self.energy_use = 60
            self.shot_count = 5
            self.accuracy = 40

    class PirateBaseAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 13
            self.energy_use = 40
            self.shot_count = 15
            self.accuracy = 40
            self.wtype = 'Assault'

    class PirateBaseMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 20
            self.energy_use = 40
            self.shot_count = 15
            self.accuracy = 70

##############################################





### SUPPORT SKILLS ###

    class Repair(Support):
        def __init__(self):
            Support.__init__(self)
            self.repair = True
            self.damage = 300 #also used for heals
            self.energy_use = 80
            self.name = 'Repair I'
            self.shot_count = 1
            self.lbl = 'Battle UI/button_repair.png'
            self.tooltip = """
            Restores approximately 300 HP to target.
            Has a range of 3 hexes."""

    class AccUp(Support):
        def __init__(self):
            Support.__init__(self)
            self.modifies = 'accuracy'
            self.buff_strength = 15
            self.buff_duration = 3
            self.name = 'Aim Up'
            self.lbl = 'Battle UI/button_aimup.png'
            self.tooltip = """
            Adds an additional 15 points to the target's weapon accuracy.
            Has a range of 3 hexes."""

    class DamageUp(Support):
        def __init__(self):
            Support.__init__(self)
            self.modifies = 'damage'
            self.buff_strength = 20
            self.buff_duration = 3
            self.name = 'Damage Up'
            self.lbl = 'Battle UI/button_atkup.png'
            self.tooltip = """
            Increases the target's weapon damage by 20 percent.
            Has a range of 3 hexes."""

    class Restore(Support):
        def __init__(self):
            Support.__init__(self)
            self.modifies = 'restore'
            self.buff_strength = 1
            self.buff_duration = 1
            self.name = 'Restore'
            self.energy_use = 40
            self.lbl = 'Battle UI/button_restore.png'
            self.tooltip = """
            Removes all enemy status ailments from the target.
            Has a range of 3 hexes."""

    class Stealth(Support):
        def __init__(self):
            Support.__init__(self)
            self.self_buff = True
            self.energy_use = 20
            self.accuracy = 100
            self.acc_degradation = 100
            self.modifies = 'stealth'
            self.buff_strength = 100
            self.buff_duration = 1
            self.name = 'Stealth'
            self.lbl = 'Battle UI/button_stealth.png'
            self.tooltip = """
            Become immune to enemy blindsides for one turn."""

    class Awaken(Support):
        def __init__(self):
            Support.__init__(self)
            self.self_buff = True
            self.energy_use = 100
            self.accuracy = 100
            self.hp_cost = 75
            self.acc_degradation = 100
            self.modifies = ['damage','accuracy']
            self.buff_strength = 100
            self.buff_duration = 3
            self.name = 'Awaken'
            self.lbl = 'Battle UI/button_awaken.png'
            self.tooltip = """
            Temporarily overcharges the Seraphim's systems, providing
            an additional 100 additional points to accuracy as well as
            doubling weapon damage for three turns."""
            
    class AwakenAsaga(Support):
        def __init__(self):
            Support.__init__(self)
            self.self_buff = True
            self.energy_use = 100
            self.accuracy = 100
            self.hp_cost = 100
            self.acc_degradation = 100
            self.modifies = ['damage','evasion','armor']
            self.buff_strength = 100
            self.buff_duration = -1
            self.name = 'Awaken Asaga'
            self.lbl = 'Battle UI/button_asaawaken.png'
            self.end_of_turn_callback = self.callback
            self.tooltip = """
            Improves the Black Jack's damage, evasion and armor each turn, but also causes progressively more damage each turn until canceled."""
            
        def callback(self):
            a,b = blackjack.modifiers['damage']
            a = a + 50 
            blackjack.modifiers['damage'] = [a,b]
            a,b = blackjack.modifiers['evasion']
            a = a + 50 
            blackjack.modifiers['evasion'] = [a,b]
            a,b = blackjack.modifiers['armor']
            a = a + 50 
            blackjack.modifiers['armor'] = [a,b]
            # a,b = blackjack.modifiers['accuracy']
            # a = a + 50 
            # blackjack.modifiers['accuracy'] = [a,b]
            blackjack.update_stats()
            blackjack.hp -= (100 +  -b * 40 - 40)
            if blackjack.hp < 1: 
                blackjack.hp = 1
                blackjack.hate *= 2
            if self in blackjack.weapons:
                blackjack.weapons.remove(self)
                blackjack.weapons.append(EndAwakenAsaga())
            
    class EndAwakenAsaga(Support):
        def __init__(self):
            Support.__init__(self)
            self.self_buff = True
            self.energy_use = 0
            self.accuracy = 100
            self.lbl = 'Battle UI/button_asaawaken.png'
            self.tooltip = """
            Cancels the awakening effect"""
        
        def fire(self,parent,target,counter = False):
            blackjack.modifiers['damage'] = [0,0]
            blackjack.modifiers['evasion'] = [0,0]
            blackjack.modifiers['armor'] = [0,0]
            # blackjack.modifiers['accuracy'] = [0,0]
            blackjack.update_stats()
            BM.end_turn_callbacks = []
            blackjack.weapons.remove(self)
            blackjack.weapons.append(AwakenAsaga())
            
       
            
            

#### curse skills ####

    class AccDown(Curse):
        def __init__(self):
            Curse.__init__(self)
            self.energy_use = 30
            self.modifies = 'accuracy'
            self.accuracy = 9999
            self.buff_strength = -25
            self.buff_duration = 3
            self.name = 'Aim Down'
            self.lbl = 'Battle UI/button_aimdown.png'
            self.tooltip = """
            Reduces the target's weapon accuracy by 25 points."""

    class Disable(Curse): #takes away all EN
        def __init__(self):
            Curse.__init__(self)
            self.energy_use = 100
            self.accuracy = 9999
            self.modifies = ['energy regen','flak', 'shield_generation']
            self.buff_strength = -100
            self.buff_duration = 2 #has to be 2 or else the debuff won't last beyond the start of their next turn
            self.name = 'Disable'
            self.lbl = 'Battle UI/button_disable.png'
            self.tooltip = """
            Completely disables the target for one turn."""

    class FlakOff(Curse):
        def __init__(self):
            Curse.__init__(self)
            self.energy_use = 40
            self.modifies = 'flak'
            self.accuracy = 9999
            self.buff_strength = -100
            self.buff_duration = 2
            self.name = 'Flak Off'
            self.lbl = 'Battle UI/button_flak.png'
            self.tooltip = """
            The target can no longer fire flak at missiles for two turns."""

    class ShutOff(Curse):  #shuts down shield generation
        def __init__(self):
            Curse.__init__(self)
            self.energy_use = 60
            self.accuracy = 9999
            self.modifies = 'shield_generation'
            self.buff_strength = -100
            self.buff_duration = 2
            self.name = 'Shield Down'
            self.lbl = 'Battle UI/button_shutoff.png'
            self.tooltip = """
            Deactivates the target's shields for two turns."""

    class ShdJam(Curse):  #shuts down shield generation
        def __init__(self):
            Curse.__init__(self)
            self.energy_use = 40
            self.accuracy = 9999
            self.modifies = 'shield_generation'
            self.buff_strength = -15
            self.buff_duration = 1
            self.cumulative = True  #do not overwrite but add to the current modifier.
            self.name = 'Shield Jam'
            self.lbl = 'Battle UI/button_shdjam.png'
            self.tooltip = """
            Temporarily reduce the target's shield generation by 15 points. Can be used multiple times on the same target."""


###are these still used?##

    class Rocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 300   #multiplied by shot count
            self.energy_use = 50
            self.uses_rockets = True
            self.uses_missiles = False
            self.eccm = 10
            self.accuracy = 60    #seems low, but missiles have very low accuracy degradation over distance.
            self.wtype = 'Rocket'
            self.name = 'Basic Rockets'
            self.shot_count = 2
            self.lbl = 'Battle UI/button_rocket.png'

    class Flak(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 10
            self.energy_use = 40
            self.accuracy = 130
            self.acc_degradation = 100 #flak is only useful at point blank range
            self.shot_count = 30  #many shots, but any armor will block it
            self.wtype = 'Assault'
            self.name = 'Basic Flak'
            self.lbl = 'Battle UI/button_assault.png'

    class MachineGun(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 20
            self.energy_use = 40
            self.accuracy = 50
            self.shot_count = 15  #many shots, but any armor will block most
            self.wtype = 'Assault'
            self.name = 'Basic Assault'
            self.lbl = 'Battle UI/button_assault.png'

#################################################### PHOENIX BOOSTER

    class PhoenixBoasterLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 180
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

    class PhoenixBoasterAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 10
            self.energy_use = 30
            self.shot_count = 15
            self.accuracy = 60
            self.wtype = 'Assault'

########################################## PACT BOMBER

    class PACTBomberMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 30
            self.energy_use = 30
            self.shot_count = 8
            self.accuracy = 70
            self.wtype = 'Missile'

    class PACTBomberRocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 300
            self.energy_use = 50
            self.uses_rockets = True
            self.uses_missiles = False
            self.eccm = 10
            self.wtype = 'Rocket'
            self.accuracy = 60
            self.shot_count = 1

    class PACTBomberLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 140
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

 ###########################################PHOENIX

    class PhoenixAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 12
            self.energy_use = 30
            self.shot_count = 20
            self.accuracy = 65
            self.wtype = 'Assault'
            self.name = 'Phoenix_Assault'
            self.lbl = 'Battle UI/button_assault.png'
            self.tooltip = """
            Assault guns spray explosive low caliber rounds at the enemy. Even if
            the enemy evades one round, others may hit. Armor is twice as
            effective against assault. Also used to shoot down incoming enemy missiles,
            but loses effectiveness against sustained barrages."""

    class PhoenixMelee(Melee):
        def __init__(self):
            Melee.__init__(self)
            self.damage = 250    #multiplied by shot count
            self.energy_use = 40
            self.ammo_use = 0
            self.accuracy = 60
            self.acc_degradation = 0
            self.wtype = 'Melee'
            self.name = 'Zantetsuken'  #lol
            self.type = 'Melee'
            self.shot_count = 2
            self.lbl = 'Battle UI/button_melee.png'
            self.tooltip = """
            Slice an enemy ryder for devastating damage. However, can only be used on adjacent
            ryders. Moving directly next to an enemy ryder will trigger an enemy blindside attack."""


 ###########################################PHOENIX ENEMY
 
    class PhoenixEnemyMelee(Melee):
        def __init__(self):
            Melee.__init__(self)
            self.damage = 250    #multiplied by shot count
            self.energy_use = 40
            self.ammo_use = 0
            self.accuracy = 160 
            self.acc_degradation = 100  #this is needed for AI melee weapons or else range is infinite.
            self.wtype = 'Melee'
            self.name = 'Zantetsuken' 
            self.type = 'Melee'
            self.shot_count = 2
            self.lbl = 'Battle UI/button_melee.png'

################################################# SERAPHIM
    class SeraphimKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 300
            self.energy_use = 100
            self.shot_count = 1
            self.accuracy = 150
            self.tooltip = """
            Sola\'s rifle is an elegant weapon from a more civilized age.
            Incredibly powerful and accurate weapon, but demands much energy."""

################################################### BIANCA

    class BiancaAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 250
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 55
            self.wtype = 'Assault'
            self.name = 'Bianca Shotgun'
            self.lbl = 'Battle UI/button_kinetic.png'
            self.tooltip = """
            Provides reliable firepower, but highly inaccurate unless the target
            is nearby and large. Can also be used for blindside attacks."""
            
            
##################################################### UNION FRIGATE


    class UnionFrigateLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 175
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 120
            self.wtype = 'Laser'
            self.name = 'Trinities'
            self.lbl = 'Battle UI/button_laser.png'
            self.tooltip = """
            Lasers are accurate even from long distances, but lack fire power.
            Mitigated by enemy shields."""

###################################################### NIGHTMARE

    class NightmareMelee(Melee):
        def __init__(self):
            Melee.__init__(self)
            self.damage = 900    #multiplied by shot count
            self.energy_use = 30
            self.ammo_use = 0
            self.accuracy = 160
            self.acc_degradation = 100
            self.wtype = 'Melee'
            self.type = 'Melee'
            self.shot_count = 1

    class NightmareMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 100
            self.energy_use = 60
            self.shot_count = 15
            self.accuracy = 100
            self.wtype = 'Missile'

    class NightmareLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 575
            self.energy_use = 40
            self.shot_count = 1
            self.accuracy = 120

    class NightmarePulse(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 70
            self.energy_use = 30
            self.shot_count = 15
            self.accuracy = 85
            self.wtype = 'Pulse'

###################################################### ARCADIUS

    class ArcadiusMelee(Melee):
        def __init__(self):
            Melee.__init__(self)
            self.damage = 500    #multiplied by shot count
            self.energy_use = 30
            self.ammo_use = 0
            self.accuracy = 160
            self.acc_degradation = 100
            self.wtype = 'Melee'
            self.type = 'Melee'
            self.shot_count = 1

    class ArcadiusMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 50
            self.energy_use = 60
            self.shot_count = 10
            self.accuracy = 100
            self.wtype = 'Missile'

    class ArcadiusLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 300
            self.energy_use = 40
            self.shot_count = 1
            self.accuracy = 110

    class ArcadiusPulse(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 50
            self.energy_use = 40
            self.shot_count = 12
            self.accuracy = 78
            self.wtype = 'Pulse'


            
    ## store items ##
    # see classes.rpy for more details on what each field does
    
    class NewWarhead(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'new warhead'
            self.display_name = "WARHEAD AMMO"
            self.cost = 300            
            self.tooltip = 'Purchase warheads to allow the Sunrider to fire powerful rockets at the enemy. A rocket deals {} damage, but can be shot down by enemy flak. The Sunrider can carry a maximum of 2 at a time.'.format(sunrider.weapons[3].damage)
            self.variable_name = 'sunrider.rockets'    #this decides what is shown in the store after [owned:
            self.max_amt = 2    #you can buy no more than this number of this item. see previous field
            
        def buy(self): #here is where you decide what this item -does-.
            sunrider.rockets += 1
            
    class RocketUpgrade(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'Rocketupgrade1'
            self.display_name = "QUANTUM TORPEDO LICENSE"
            self.cost = 2000            
            self.tooltip = 'While the proliferation of nuclear warheads throughout the galaxy has made them readily available, more powerful weapons are regulated closely by the Alliance. With the payment of appropriate fees, the Union can replace your current stock of nuclear warheads with quantum warheads, permanently increasing the Sunrider\'s rocket damage to 1200.'
            self.visibility_condition = 'sunrider_rocket.damage < 1200'
            
        def buy(self):            
            store.sunrider_rocket.damage = 1200
            
    class RepairUpgrade(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'RepairUpgrade1'
            self.display_name = "PORTABLE REPAIR BOOSTER"
            self.cost = 750            
            self.tooltip = 'While extensive repairs require time in the dry dock, battlefield repairs are still a must for combat operations. These new portable repair drones will allow the Liberty to repair 200 more HP.'
            self.visibility_condition = 'store.chigara_repair.damage < 500'
            
        def buy(self):            
            store.chigara_repair.damage = 500
            
    class NewRepairDrone(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'repair drones'
            self.display_name = "REPAIR DRONE"
            self.cost = 400            
            self.tooltip = 'These autonomous robots can rapidly restore destroyed hull sections as well as complex electronic systems. They are a must have for all hostile operations.  Restores 50% of the Sunrider\'s HP on use. The Sunrider can carry a maximum of 8 at a time.'
            self.visibility_condition = 'sunrider.repair_drones != None'
            self.variable_name = 'sunrider.repair_drones'
            self.max_amt = 8            
            
        def buy(self):            
            sunrider.repair_drones += 1
            
    class ContractAllianceCruiser(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'alliance cruiser'
            self.display_name = "ALLIANCE CRUISER"
            self.cost = 2000            
            self.visibility_condition = 'store.mission12_complete'  #not sure
            self.variable_name = "get_shipcount_in_list('Alliance Cruiser',player_ships)"
            self.max_amt = 2            
            self.tooltip = 'With the Solar Congress\' declaration of war, countless Alliance battle cruisers have been called to the front lines. With a generous payment, the Mining Union can use its leverage in the Solar Congress to assign a fully operational Alliance battle cruiser as the Sunrider\'s escort. While slow, the Alliance battle cruiser is built like a brick and packs a punch. You can have up to {} in your fleet at any time'.format(self.max_amt)
            
        def buy(self):            
            create_ship(AllianceCruiser()) #location=None, weaponlist=[] i.e. default
            BM.mercenary_count += 1

    class ContractUnionFrigate(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'union frigate'
            self.display_name = "UNION FRIGATE"
            self.cost = 750            
            self.visibility_condition = 'store.mission12_complete'  #not sure
            self.variable_name =  "get_shipcount_in_list('Mining Union Frigate',player_ships)"
            self.max_amt = 4            
            self.tooltip = 'The Mining Union regularly fields a large private army to protect its shipping from pirates. With the payment of the appropriate fees, you too can have a Union security frigate watching your back. While small and lightly armed, these frigates are inexpensive and speedy. You can have up to {} in your fleet at any time'.format(self.max_amt)
            
        def buy(self):            
            create_ship(UnionFrigate()) #location=None, weaponlist=[] i.e. default
            BM.mercenary_count += 1         
            
    class SellWishallArtifact(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'wishall'
            self.display_name = "SELL WISHALL"
            self.cost = -10000            
            self.tooltip = 'The Wishall is an ancient Ryuvian artifact which allows its user to make one free command decision during the story. Alternately, you may decide to sell it here for an instant cash infusion of 10 000 credits.'
            self.visibility_condition = "store.wishall"
            
        def buy(self): #here is where you decide what this item -does-.
            store.wishall = False         

    class SunriderShieldUpgrade(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'sunrider_shield_upgrade'
            self.display_name = "SUNRIDER SHIELD UPGRADE"
            self.cost = 1500            
            self.tooltip = "Due to the Sunrider's unexpected departure from Cera, she was never outfitted with energy shielding. While her top of the line shield generator was lost with the fall of Cera, the Union can outfit the Sunrider with a basic shield generator. The Sunrider's shields can be further upgraded in the Research Lab after it is purchased."
            self.visibility_condition = 'store.sunrider.shield_generation == 0'

        def buy(self):            
            store.sunrider.shield_generation = 15
            store.sunrider.shields = store.sunrider.shield_generation
            store.sunrider.shield_range = 0
            
    class SunriderVanguardUpgrade(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'sunrider_vanguard_upgrade'
            self.display_name = "SUNRIDER VANGUARD UPGRADE"
            self.cost = 1100            
            self.tooltip = "Increase the Vanguard cannon's damage from 800 to 1000 damage and extend the range by 1 hex"
            self.visibility_condition = 'store.mission12_complete and BM.vanguard_damage < 1000'

        def buy(self):            
            BM.vanguard_damage = 1000
            BM.vanguard_range = 7
            
            
