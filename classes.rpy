## This file declares all the classes in the battle engine
# 1) battle manager class
# 2) custom displayables
# 3) Action objects (these gets activated when you click a button)  [[DEFUNCT]]
# 4) battleship blueprint class
# 5) Weapon blueprint classes
# 6) library (specific ships/weapons)  [[MOVED]]
# 7) planet class
# 8) bonus stuff
# 9) actions

init -2 python:
    import pygame

        ##here the Battle class gets defined. it forms the core and spine of the entire combat engine.
        ##it gets initialized into an instance called BM, short for battlemanager
    class Battle(store.object): # handles managing a list of all battle units, handles turns and manages enemy AI

        def __init__(self):
            #when the first instance gets created a couple of default values get initialized.
            self.cmd = 0              #your command point total
            self.money = 0            #go on, set this to 999'999'999. you know you want to.
            self.seen_skirmish = False #if not seen skirmish before Ava explains it.
            self.save_version = config.version
            self.ships = []           #holds all ships to display on the map
            self.covers = []          #holds a list of all the cover on the map
            self.enemy_vanguard_path = []#stores the hexes that the enemy's vanguard will go through.
            self.player_vanguard_path = []#stores the hexes that the player's vanguard will go through (only used by AI).
            self.missiles = []        #all the missiles on screen. right now all missiles are fired one by one
            self.selected = None      #current selection
            self.hovered = None       #what unit are you hovering over
            self.target = None        #the current target of whatever attack is going on
            self.selectedmode = False #this makes the move target buttons appear
            self.targetingmode = False#keeps chance to hit target windows on screen etc
            self.moving = False       #set to true when a ship is moving from point a to b
            self.just_moved = False   #when True the button to take back your last movement is shown
            self.missile_moving = False #tells the battle screen a missile is moving from a to b
            self.phase = 'Player'     #keeps track of who's turn it is
            self.weaponhover = None   #the weapon you are hovering over. used for chance to hit target window and tooltips
            self.active_weapon = None #similar to weaponhover, but is used after you actually click a weapon so you can target something
            self.mission = 1          #what mission are we on? decides where to loop and is important for in battle events
            self.turn_count = 1       #most important when calculating command points awarded
            self.grid = []            #keep track of what cells in the grid are free and which are not.
            self.vanguard = False     #when True the battlemap shows the vanguard cannon being fired.
            self.active_strategy = [None,0] #you can have either 'full forward' or 'all guard' active, but not both.
            self.vanguardtarget = False #creates buttons to select vanguard fire direction
            self.warping = False      #used by the short range warp order. it makes an outline of the selected ship show at the mouse cursor
            self.targetwarp = False   #used by the short ranged warp order.  it creates buttons on the tiles
            self.showing_orders = False #This is True when the list of orders is visible.
            self.show_tooltips = True #hide or show tooltips
            self.debugoverlay = False #overlay coords etc for debug purposes
            self.show_grid = True     #show or hide the grid. no grid is much faster!
            self.formation_range = 6  #the farthest column the player can place units during the formation phase
            self.mercenary_count = 0  #the number of mercenaries in service to the Sunrider. [no longer used]
            self.remove_mode = False  #when True the player can easily remove units in skirmish
            self.player_ai = False
            self.end_turn_callbacks = []

            self.lowest_difficulty = 3 #lowest recorded difficulty. bragging rights!
            self.lead_ships = []
            self.mouse_location = (0,0)
            self.vanguard_damage = 800
            self.vanguard_range = 6
            self.orders = {
                'FULL FORWARD':[750,'full_forward'],
                'ALL GUARD':[750,'all_guard'],
                'REPAIR DRONES':[750,'repair_drones'],
                'VANGUARD CANNON':[2500,'vanguard_cannon']
                }
            self.order_used = False   #when True the orders button is hidden.
              #environment modififiers are initialized here and can be changed later
            self.environment = {
                'accuracy':100,
                'turndamage':0,
                'damage':0,
                'energyregen':0,
                }
            self.battlemode = False   #True during battle. when set to False the battle loop will end.
            self.stopAI = False       #when set to True all AI action is disabled.
            self.edgescroll = (0,0)
            self.xadj = ui.adjustment() #used by the viewport in the battlescreen
            self.yadj = ui.adjustment()

            #when True you can drag the main viewport (the battle map with the grid) around. this needs to be
            #disabled when text is showing on screen otherwise mouseclicks get eaten by the viewport and do not advance text
            #DEFUNCT!
            self.draggable = True
            self.debug_log = []
            #Battle log
            self.show_battle_log = False
            self.battle_log = []
            self.battle_log_yadj = ui.adjustment(adjustable=True)
            #dispatchers
            self.skirmish_dispatcher = { 'start'         : self.skirmish_start,
                                         'quit'          : self.skirmish_quit,
                                         'remove'        : self.skirmish_remove,
                                         'playermusic'   : self.skirmish_playermusic,
                                         'enemymusic'    : self.skirmish_enemymusic,
                                         "zoom"          : self.common_zoom,
                                         "next ship"     : self.common_next_ship,
                                         "deselect"      : self.common_deselect,
                                         "selection"     : self.skirmish_selection,
                                         "warptarget"    : self.skirmish_warptarget }
            self.formation_dispatcher = { "start"        : self.formation_start,
                                          "zoom"         : self.common_zoom,
                                          "next ship"    : self.common_next_ship,
                                          "deselect"     : self.common_deselect,
                                          "selection"    : self.formation_selection,
                                          "warptarget"   : self.formation_warptarget }
            self.battle_dispatcher = { "anime"            : self.battle_anime,
                                       "cheat"            : self.battle_cheat,
                                       "I WIN"            : self.battle_inst_win,
                                       "deselect"         : self.battle_deselect,
                                       "next ship"        : self.battle_next_ship,
                                       "previous ship"    : self.battle_previous_ship,
                                       "zoom"             : self.battle_zoom,
                                       "selection"        : self.battle_selection,
                                       "move"             : self.battle_move,
                                       "cancel movement"  : self.battle_cancel_movement,
                                       "RESURRECTION"     : self.battle_order_resurrection,
                                       "ALL GUARD"        : self.battle_order_all_guard,
                                       "FULL FORWARD"     : self.battle_order_full_forward,
                                       "REPAIR DRONES"    : self.battle_order_repair_drones,
                                       "SHORT RANGE WARP" : self.battle_short_range_warp,
                                       "RETREAT"          : self.battle_retreat,
                                       "VANGUARD CANNON"  : self.battle_order_vanguard_cannon,
                                       "toggle player ai" : self.toggle_player_ai,
                                       "endturn"          : self.battle_end_turn   }

              #stores a matrix of the grid to keep track of what spots are free. False is free, True is occupied
            for a in range(GRID_SIZE[0]):
                self.grid.append([False]*GRID_SIZE[1])
            self.battle_bg = "Background/space{!s}.jpg".format(renpy.random.randint(1,9))
            self.result = None #store result of ui.interact()

        #here we start defining a few methods which part of the battlemanager
        ## insert entry to battle log
        # @param type The list of tags
        # @param message The formatted string
        # @param position Determines position of log entry
        def battle_log_insert(self, type, message, position = None):
            entry = [type, message]
            #zero is not supposed to be
            if position:
                self.battle_log.insert(position, entry)
            else:
                self.battle_log.append(entry)
            self.battle_log_yadj.change(self.battle_log_yadj.value + 125)

        #trimming, in case this list can lead to or contribute to memory leaks.
        def battle_log_trimm(self):
            if len(self.battle_log) > 500:
                start = len(self.battle_log) - 500
                self.battle_log = self.battle_log[start:]
                self.battle_log_yadj.change(self.battle_log_yadj.value - (125 * start))

        ## pop entry from battle log
        # @param index The index of entry to remove
        def battle_log_pop(self, index = None):
            if index is None:
                self.battle_log.pop()
            else:
                self.battle_log.pop(index)
            self.battle_log_yadj.change(self.battle_log_yadj.value - 125)

        def select_ship(self,ship,play_voice = True):
            self.selected = ship
            if ship.faction == 'Player' and play_voice:
                a = renpy.random.randint(0,len(ship.selection_voice)-1)
                renpy.music.play('sound/Voice/{}'.format(ship.selection_voice[a]),channel = ship.voice_channel)
                del a

            if self.mission != 'skirmish' and BM.phase != 'formation':
                renpy.show_screen('commands')
                ship.movement_tiles = get_movement_tiles(ship)
                self.selectedmode = True

        def unselect_ship(self,ship):
            renpy.hide_screen('commands')
            self.selectedmode = False
            self.selected = None
            self.targetingmode = False
            if ship != None:
                ship.movement_tiles = []

        def dispatch_handler(self, result, dispatch_type = 'battle'):
            ui_action = None
            #check handling of dispatcher
            if result is None: return self.common_none
            elif isinstance(result, bool): return self.common_bool
            elif isinstance(result, list):
                disp_type = dispatch_type + "_dispatcher"
                ui_action = getattr(self, disp_type).get(result[0], self.common_unexpected)
            else:
                disp_type = dispatch_type + "_dispatcher"
                ui_action = getattr(self, disp_type).get(result, self.common_unexpected)
            return ui_action

        ########################################################
        ## Common dispatcher
        ########################################################
        def common_unexpected(self):
            self.debug_log.append("Unexpected dispatcher key: " + self.result)

        def common_none(self):
            pass

        def common_bool(self):
            pass

        def common_zoom(self):
            zoom_handling(self.result, self)

        def common_next_ship(self):
            templist = []
            for ship in player_ships:
                if ship.location == None:
                    templist.append(ship)

            if self.selected == None:
                if len(templist) > 0:
                    self.select_ship(templist[0])
            else:
                if self.selected.location != None:
                    set_cell_available(self.selected.location)
                if self.selected in templist:
                    index = templist.index(self.selected)
                else:
                    index = 0
                if index == (len(templist)-1):
                    index = 0
                else:
                    index += 1
                self.select_ship(templist[index])

            if self.selected != None:
                self.targetwarp = True
                renpy.show_screen('mousefollow')

        def common_deselect(self):
            #if you picked up an enemy unit that was already put down right clicking should delete it entirely
            #player ships automatically return to the blue pool to be placed again later.
            if self.selected != None:
                if self.selected in enemy_ships:
                    self.ships.remove(self.selected)
                    enemy_ships.remove(self.selected)
            self.targetwarp = False
            renpy.hide_screen('mousefollow')
            self.unselect_ship(self.selected)
        ########################################################
        ## Common dispatcher end
        ########################################################
        #------------------------------------------------------#
        ########################################################
        ## Skirmish dispatcher
        ########################################################
        #similar to formation. Should be merged?
        def skirmish_start(self):
            if len(enemy_ships) == 0:
                show_message('Please add at least 1 enemy ship')
                renpy.jump('mission_skirmish')
            player_ship_present = False

            for ship in player_ships:
                if ship.location != None:
                    player_ship_present = True
            if not player_ship_present:
                 show_message('Please add at least 1 player ship')
                 renpy.jump('mission_skirmish')

            renpy.hide_screen('player_unit_pool_collapsed')
            renpy.hide_screen('enemy_unit_pool_collapsed')
            renpy.hide_screen('player_unit_pool')
            renpy.hide_screen('enemy_unit_pool')
            renpy.hide_screen('mousefollow')
            renpy.hide_screen('battle_screen')
            renpy.hide_screen('store_union') #seems like it has trouble staying closed?
            self.battlemode = False

        def skirmish_quit(self):
            renpy.hide_screen('store_union') #seems like it has trouble staying closed?
            renpy.hide_screen('player_unit_pool_collapsed')
            renpy.hide_screen('enemy_unit_pool_collapsed')
            renpy.hide_screen('player_unit_pool')
            renpy.hide_screen('enemy_unit_pool')
            renpy.hide_screen('mousefollow')
            renpy.hide_screen('battle_screen')
            clean_battle_exit()
            self.battlemode = False
            BM.cmd = store.tempcmd
            BM.money = store.tempmoney
            BM.mission = None
            store.player_ships = store.player_ships_original
            renpy.jump('dispatch')

        def skirmish_remove(self):
            if self.remove_mode:
                self.remove_mode = False
            else:
                self.remove_mode = True

        def skirmish_playermusic(self):
            store.PlayerTurnMusic = self.result[1]
            show_message('Player music was changed')

        def skirmish_enemymusic(self):
            store.EnemyTurnMusic = self.result[1]
            show_message('Enemy music was changed')

        def skirmish_selection(self):
            # this result can be from one of the imagebuttons in the pool screens or returned from
            # MouseTracker because a hex with a unit in it was clicked.
            selected_ship = self.result[1]
            # BM.selected = selected_ship

            if self.remove_mode:
                if selected_ship.location != None:
                    if selected_ship.faction != 'Player':
                        if selected_ship in enemy_ships:
                            self.ships.remove(selected_ship)
                            enemy_ships.remove(selected_ship)
                            set_cell_available(selected_ship.location)
                    else:
                        set_cell_available(selected_ship.location)
                        selected_ship.location = None


            else:  #normal mode
                self.targetwarp = True
                renpy.show_screen('mousefollow')

                if selected_ship.faction == 'Player':
                    self.select_ship(selected_ship)
                else:
                    if selected_ship.location != None:
                        self.select_ship(selected_ship)
                        if selected_ship in enemy_ships:
                            self.ships.remove(self.selected)
                            enemy_ships.remove(self.selected)
                    else:
                        self.selected = deepcopy(selected_ship) #breaks alias
                        self.selected.weapons = self.selected.default_weapon_list

            if self.selected != None:
                if self.selected.location != None:
                    set_cell_available(self.selected.location)
                self.selected.location = None

        def skirmish_warptarget(self):
            # returned from MouseTracker if you click on an empty hex when BM.warptarget == True.
            if self.selected != None:
                new_location = self.result[1]
                set_cell_available(new_location,True)

                if self.selected.faction != 'Player':
                    enemy_ships.append(self.selected)
                    self.ships.append(self.selected)

                self.selected.location = new_location

                if self.selected.faction != 'Player' and pygame.key.get_mods() != 0:
                    self.selected = deepcopy(self.selected) #breaks alias
                else:
                    self.targetwarp = False
                    renpy.hide_screen('mousefollow')
                    self.unselect_ship(self.selected)

            sort_ship_list()
        ########################################################
        ## Skirmish dispatcher end
        ########################################################
        def skirmish_phase(self):
            self.result = ui.interact()
            self.dispatch_handler(self.result,'skirmish')()

        #------------------------------------------------------#
        ########################################################
        ## Formation dispatcher
        ########################################################
        def formation_start(self):
            #check if there are still player units that are not placed
            unplaced_units = False
            for ship in player_ships:
                if ship.location == None:
                    unplaced_units = True
            if unplaced_units:
                show_message('there are still ships you have not placed!')
            else:
                renpy.hide_screen('player_unit_pool_collapsed')
                renpy.hide_screen('enemy_unit_pool_collapsed')
                renpy.hide_screen('player_unit_pool')
                renpy.hide_screen('enemy_unit_pool')
                renpy.hide_screen('mousefollow')
                self.phase = 'Player'
                renpy.jump('mission{}'.format(self.mission))

        def formation_selection(self):
            # this result can be from one of the imagebuttons in the pool screens or returned from
            # MouseTracker because a hex with a unit in it was clicked.
            selected_ship = self.result[1]

            if selected_ship.faction == 'Player':
                self.targetwarp = True
                renpy.show_screen('mousefollow')
                self.select_ship(selected_ship)

                if self.selected.location != None:
                    set_cell_available(self.selected.location)
                self.selected.location = None

        def formation_warptarget(self):
            # returned from MouseTracker if you click on an empty hex when self.warptarget == True.
            if self.selected != None:
                new_location = self.result[1]

                #when setting up before a mission you can't put your ships farther to the right than column 7
                if new_location[0] > self.formation_range:
                    show_message('too far infield')
                else:
                    set_cell_available(new_location,True) #passing True actually sets it unavailable

                    if self.selected.faction != 'Player':
                        enemy_ships.append(self.selected)
                        self.ships.append(self.selected)

                    self.selected.location = new_location

                    if self.selected.faction != 'Player' and pygame.key.get_mods() != 0:
                        self.selected = deepcopy(self.selected) #breaks alias
                    else:
                        self.targetwarp = False
                        renpy.hide_screen('mousefollow')
                        self.unselect_ship(self.selected)
        ########################################################
        ## Formation dispatcher end
        ########################################################
        def formation_phase(self):
            self.phase='formation'
            while True:
                self.result = ui.interact()
                self.dispatch_handler(self.result,'formation')()
                if self.battlemode == False: #whenever this is set to False battle ends.
                    break
        #------------------------------------------------------#
        ########################################################
        ## Battle dispatcher
        ########################################################
        def battle_anime(self):
            if not hasattr(store,'damage'):
                store.damage = 50
            if not hasattr(self,'attacker'):
                self.attacker = sunrider
            if not hasattr(store,'hit_count'):
                store.hit_count = 1
            if not hasattr(store,'total_armor_negation'):
                store.total_armor_negation = 10
            if not hasattr(store,'total_shield_negation'):
                store.total_shield_negation = 10
            if not hasattr(store,'total_flak_interception'):
                store.total_flak_interception = 0
            if self.target == None:
                self.target = sunrider
            try:
                renpy.call_in_new_context('atkanim_legion_missile')
            except:
                show_message('animation label does not exist!')

        def battle_cheat(self):
            self.cmd = 99999
            for ship in player_ships:
                ship.en = 9999

        def battle_inst_win(self):
            instant_win()

        def battle_deselect(self):
            if self.active_weapon != None:
                self.active_weapon = None
                self.targetingmode = False
                self.weaponhover = None
            elif self.selected != None:
                self.unselect_ship(self.selected)
            else:
                pass

        def battle_next_ship(self):
            if self.selected == None:
                self.select_ship(sunrider)
                return

            if self.selected != None and len(player_ships) > 1:
                if self.selected.faction == 'Player':
                    index = player_ships.index(self.selected)
                    looping = True
                    while looping:
                        if index == (len(player_ships)-1):
                            index = 0
                        else:
                            index += 1
                        if player_ships[index].location != None:
                            looping = False
                    self.select_ship(player_ships[index])

        def battle_previous_ship(self):
            if self.selected != None and len(player_ships) > 1:
                if self.selected.faction == 'Player':
                    index = player_ships.index(self.selected)
                    looping = True
                    while looping:
                        if index == 0:
                            index = len(player_ships)-1
                        else:
                            index -= 1
                        if player_ships[index].location != None:
                            looping = False
                    self.select_ship(player_ships[index])

        #def battle_mousefollow_click(self):
        #    pass

        def battle_zoom(self):
            zoom_handling(self.result,self) #see funtion.rpy how this is handled. it took a LONG time to get it to a point I am happy with
            if self.selectedmode: self.selected.movement_tiles = get_movement_tiles(self.selected)
            # self.just_moved = True #zooming doesn't have to reset this button

        def battle_selection(self):
            # if self.result == None:
                # return
            self.target = self.result[1]
            self.hovered = None

            #if no ship is currently selected select the ship that was just clicked on.
            if self.selected == None:
                self.select_ship(self.target)
                return

            #you do not have a weapon active.
            if not self.targetingmode:
                #did you select the active ship?
                if self.target == self.selected:
                    self.unselect_ship(self.selected)
                else:
                    self.select_ship(self.target)
                return
            #you do have a weapon active.
            else:
                weapon = self.active_weapon
                #is this a valid target?
                if weapon.wtype == 'Melee':
                    if get_ship_distance(self.selected,self.target) > 1 or self.target.stype != 'Ryder':
                        return
                self.targetingmode = False

                #did you click the currently selected ship?
                if self.target == self.selected:
                    if weapon.wtype == 'Support':
                        pass  #you clicked your selected ship with a support weapon active. do not end the method.
                    else:
                        self.unselect_ship(self.result[1])
                        return #do end the method. this is important.
                #did you click an ally?
                elif self.target.faction == 'Player':
                    if weapon.wtype == 'Support' or weapon.wtype == 'Special':
                        if self.target.cth <= 0:
                            self.draggable = False
                            renpy.say('Ava',"No enemies in range, captain.")
                            self.draggable = True
                            self.targetingmode = True #try again
                            return #do end the method, this is important.
                        else:
                            #you clicked an ally unit with a support weapon active. do not end the method.
                            pass
                    else:
                        self.select_ship(self.target)
                        return

                #you clicked an enemy with an active weapon.
                else:
                    #check if you can hit the target. if not, let the player know he's stupid.
                    if self.target.cth <= 0:
                        self.draggable = False
                        renpy.say('Ava','It\'s hopeless, captain!')
                        self.draggable = True
                        return #do end the method, this is important.
                    else:
                        self.attacker = self.selected
                        if self.active_weapon.wtype == 'Curse' or self.active_weapon.wtype == 'Special':
                            weapon.fire(self.selected,self.target)
                            self.active_weapon = None
                            self.weaponhover = None
                            if self.selected != None:
                                self.selected.movement_tiles = get_movement_tiles(self.selected)
                            return

                        if self.active_weapon.wtype == 'Melee':
                            pass #do not show the atkanim, because there aren't any for melee.
                        else:
                            try:
                                animation_name = self.active_weapon.wtype.lower()
                                if weapon.animation_name != None:
                                    animation_name = weapon.animation_name
                                renpy.call_in_new_context('atkanim_{}_{}'.format(self.selected.animation_name,animation_name))
                            except:
                                show_message('missing animation. "atkanim_{}_{}" does\'t seem to exist'.format(self.selected.animation_name,self.active_weapon.wtype.lower()))
            #up till now nothing ended the method meaning it's okay to fire the weapon at the target - be it support or not.
            result = weapon.fire(self.selected,self.target)
            self.target.receive_damage(result,self.selected,weapon.wtype)
            if self.selected != None:
                self.selected.movement_tiles = get_movement_tiles(self.selected)
#            update_stats() - updated in receive_damage()
            self.active_weapon = None
            self.weaponhover = None
#            renpy.hide_screen('battle_screen')
#            renpy.show_screen('battle_screen')
            return #battle_selection end

        def battle_move(self): #this means you clicked on one of the blue squares indicating you want to move somewhere
            self.selected.move_ship(self.result[1],self) #result[1] is the new location to move towards
            update_stats()

        def battle_cancel_movement(self):
            #expect that any actions will remove cancel button
            self.battle_log_pop()
            ship = self.selected
            ship.en += get_distance(ship.location,ship.current_location)*ship.move_cost
            a = ship.location[0]-1  #make the next line of code a little shorter
            b = ship.location[1]-1
            self.grid[a][b] = False #tell the BM that the old cell is now free again

            ship.location = ship.current_location

            a = ship.location[0]-1  #make the next line of code a little shorter
            b = ship.location[1]-1
            self.grid[a][b] = True #tell the BM that the old cell is now free again

            ship.movement_tiles = get_movement_tiles(ship)

        def battle_order_resurrection(self):
            if self.cmd >= self.orders[self.result[0]][0]:
                self.cmd -= self.orders[self.result[0]][0]

                renpy.show_screen('ryderlist')
                result = ui.interact()

                if result[0] == 'deselect':
                    self.cmd += self.orders['RESURRECTION'][0]
                    renpy.hide_screen('ryderlist')
                    self.order_used = False
                    return

                elif result[0] == 'selection':
                    revived_ship = result[1]
                    renpy.hide_screen('ryderlist')
                    launch_location = get_free_spot_near(sunrider.location) #so useful
                    revived_ship.en = 0   #not sure about this
                    revived_ship.hp = revived_ship.max_hp
                    destroyed_ships.remove(revived_ship)
                    player_ships.append(revived_ship)
                    self.ships.append(revived_ship)
                    revived_ship.location = launch_location
                    set_cell_available(launch_location, True) #the optional True actually lets me set this cell /un/available
                    message = "ORDER: {0} is resurrected".format(revived_ship.name)
                    self.battle_log_insert(['order'], message)
                    BM.order_used = True

                    #Phoenix rising from the ashes!
                    if revived_ship.name == 'Phoenix':
                        revived_ship.en = revived_ship.max_en / 2

                    #wipe all modifiers after a res
                    for modifier in revived_ship.modifiers:
                        revived_ship.modifiers[modifier] = [0,0]

                    #play the resurrect voice
                    if hasattr(revived_ship,'resurrect_voice'):
                        if len(revived_ship.resurrect_voice) > 0:
                            renpy.music.play( 'sound/Voice/'+renpy.random.choice(revived_ship.resurrect_voice),channel=revived_ship.voice_channel )
            else:
                self.order_used = False

        def battle_order_all_guard(self):
            if self.cmd >= self.orders[self.result[0]][0]:
                self.cmd -= self.orders[self.result[0]][0]

                if self.active_strategy[0] == 'full forward':
                    show_message("Full Forward order cancelled!")
                    for ship in player_ships:
                        if ship.modifiers['accuracy'][0] == 15:
                            ship.modifiers['accuracy'] = [0,0]
                        if ship.modifiers['damage'][0] == 20:
                            ship.modifiers['damage'] = [0,0]

                self.active_strategy = ['all guard',4]

                succesful = False
                for ship in player_ships:
                    if ship.flak > 0:
                        if apply_modifier(ship,'flak',20,4): succesful = True
                    if ship.shield_generation > 0:
                        if apply_modifier(ship,'shield_generation',10,4): succesful = True
                    if apply_modifier(ship,'evasion',10,4): succesful = True
                if not succesful:
                    show_message('already active!')
                    self.order_used = False
                    self.cmd += self.orders[self.result[0]][0]
                else:
                    message = "ORDER: ALL GUARD"
                    self.battle_log_insert(['order'], message)
                    BM.order_used = True
                    store.show_message('all ships gained improved flak, shielding and evasion!')

                    random_ship = renpy.random.choice( get_player_ships_in_battle() )
                    random_voice = renpy.random.choice(random_ship.buffed_voice)
                    renpy.music.play('sound/Voice/{}'.format(random_voice),channel = random_ship.voice_channel)

                    for ship in player_ships:
                        ship.getting_buff = True
                    renpy.hide_screen('battle_screen')
                    renpy.show_screen('battle_screen')
                    renpy.pause(1)
                    for ship in player_ships:
                        ship.getting_buff = False
                    renpy.hide_screen('battle_screen')
                    renpy.show_screen('battle_screen')
                update_stats()

            else:
                renpy.music.play('sound/Voice/Ava/Ava Others 9.ogg',channel='avavoice')
                self.order_used = False

        def battle_order_full_forward(self):
            if self.cmd >= self.orders[self.result[0]][0]:
                self.cmd -= self.orders[self.result[0]][0]

                if self.active_strategy[0] == 'all guard':
                    show_message("All Guard order cancelled!")
                    for ship in player_ships:
                        if ship.modifiers['flak'][0] == 20:
                            ship.modifiers['flak'] = [0,0]
                        if ship.modifiers['shield_generation'][0] == 10:
                            ship.modifiers['shield_generation'] = [0,0]
                        if ship.modifiers['evasion'][0] == 10:
                            ship.modifiers['evasion'] = [0,0]

                self.active_strategy = ['full forward',4]

                succesful = False
                for ship in player_ships:
                    if apply_modifier(ship,'accuracy',15,4): succesful = True
                    if apply_modifier(ship,'damage',10,4): succesful = True
                if not succesful:
                    show_message('already active!')
                    self.order_used = False
                    self.cmd += self.orders[self.result[0]][0]
                else:
                    message = "ORDER: FULL FORWARD"
                    self.battle_log_insert(['order'], message)
                    BM.order_used = True
                    store.show_message('All ships gain 20% damage and 15% accuracy!')
                    random_ship = player_ships[renpy.random.randint(0,len(player_ships)-1)]
                    random_voice = renpy.random.randint(0,len(random_ship.buffed_voice)-1)
                    renpy.music.play('sound/Voice/{}'.format(random_ship.buffed_voice[random_voice]),channel = random_ship.voice_channel)
                    for ship in player_ships:
                        ship.getting_buff = True
                    renpy.hide_screen('battle_screen')
                    renpy.show_screen('battle_screen')
                    renpy.pause(1)
                    for ship in player_ships:
                        ship.getting_buff = False
                    renpy.hide_screen('battle_screen')
                    renpy.show_screen('battle_screen')

            else:
                renpy.music.play('sound/Voice/Ava/Ava Others 9.ogg',channel='avavoice')
                self.order_used = False

        def battle_order_repair_drones(self):
            if self.cmd >= self.orders[self.result[0]][0]:
                if sunrider.repair_drones != None:
                    if sunrider.repair_drones <= 0:
                        show_message('No available repair droids in storage!')
                        self.order_used = False
                        return
                    else:
                        sunrider.repair_drones -= 1
                self.cmd -= self.orders[self.result[0]][0]
                message = "ORDER: Repair drones restore 50% of Sunrider's hull integrity"
                self.battle_log_insert(['order'], message)
                show_message(message)
                BM.order_used = True
                sunrider.hp += int(sunrider.max_hp * 0.5)
                if sunrider.hp > sunrider.max_hp: sunrider.hp = sunrider.max_hp
                sunrider.getting_buff = True
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                a = renpy.random.randint(0,len(sunrider.buffed_voice)-1)
                renpy.music.play('sound/Voice/{}'.format(sunrider.buffed_voice[a]),channel = sunrider.voice_channel)
                del a
                renpy.pause(1)
                sunrider.getting_buff = False
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
            else:
                renpy.music.play('sound/Voice/Ava/Ava Others 9.ogg',channel='avavoice')
                self.order_used = False

        def battle_short_range_warp(self):
            if self.cmd >= self.orders[self.result[0]][0]:
                self.cmd -= self.orders[self.result[0]][0]
                if self.selected != None:
                    self.unselect_ship(self.selected)
                self.selected = sunrider #show the sunrider's label
                self.phase = None #disables the end turn button
                self.order_used = False #debug
                self.targetwarp = True
                renpy.hide_screen('commands')
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                renpy.show_screen('mousefollow')
                looping = True
                while looping:
                    result = ui.interact()
                    if result[0] == "warptarget":
                        new_location = result[1]
                        store.flash_locations = [ sunrider.location,new_location ]
                        self.warping = True
                        renpy.hide_screen('battle_screen')
                        renpy.show_screen('battle_screen')
                        renpy.hide_screen('mousefollow')
                        renpy.music.play('sound/large_warpout.ogg', channel = 'sound5')
                        renpy.pause(1.0, hard=True) #hard means unskippable
                        self.warping = False
                        x,y = self.selected.location
                        self.grid[x-1][y-1] = False
                        self.selected.location = new_location
                        x,y = self.selected.location
                        self.grid[x-1][y-1] = True
                        looping = False
                        self.phase = 'Player'
                        self.targetwarp = False
                        renpy.hide_screen('battle_screen')
                        renpy.show_screen('battle_screen')

                    if result[0] == "zoom":
                        zoom_handling(result,self)

                    if result[0] == 'deselect':
                        self.cmd += self.orders['SHORT RANGE WARP'][0]
                        looping = False
                        renpy.hide_screen('mousefollow')
                        self.phase = 'Player'
                        self.targetwarp = False
            else:
                self.order_used = False
                renpy.music.play('sound/Voice/Ava/Ava Others 9.ogg',channel='avavoice')

        def battle_retreat(self):
            clean_battle_exit()
            renpy.jump('retreat')

        def battle_order_vanguard_cannon(self):
            inrange = False
            #check to see if any enemy units are within reach of the VC
            for ship in enemy_ships:
                if get_distance(sunrider.location,ship.location) <= BM.vanguard_range:
                    inrange = True
            if inrange:
                if self.cmd >= self.orders[self.result[0]][0]:
                    self.cmd -= self.orders[self.result[0]][0]
                    self.vanguardtarget = True
                    looping = True
                    while looping:
                        result = ui.interact()

                        if result[0] == "selection":
                            if result[1].faction != 'Player' and get_ship_distance(sunrider,result[1]) <= BM.vanguard_range:
                                loc1 = sunrider.location
                                loc2 = result[1].location
                                listlocs = interpolate_hex(loc1, loc2)
                                hasship = False
                                for loc in listlocs:
                                    if not get_cell_available(loc):
                                        for ship in enemy_ships:
                                            if ship.location[0] == loc[0] and ship.location[1] == loc[1]:
                                                hasship = True
                                if not hasship:
                                    self.cmd += self.orders['VANGUARD CANNON'][0]
                                    looping = False
                                    self.vanguardtarget = False
                                    self.order_used = False
                                    return
                                renpy.music.play('Music/March_of_Immortals.ogg')
                                renpy.call_in_new_context('atkanim_sunrider_vanguard')
                                renpy.hide_screen('battle_screen')
                                renpy.show_screen('battle_screen')
                                renpy.pause(1)
                                store.damage = BM.vanguard_damage
                                store.hit_count = 1
                                store.total_armor_negation = 0
                                store.total_shield_negation = 0
                                store.total_flak_interception = 0
                                templist = enemy_ships[:]
                                self.battle_log_insert(['order'], "ORDER: FIRE VANGUARD CANNON")
                                for ship in templist:
                                    for tile in listlocs:
                                        if ship.location != None and self.battlemode: #failsaves. it's now legal for a location to be None
                                            if ship.location[0] == tile[0] and ship.location[1] == tile[1]:
                                            #if ship.location[1] == sunrider.location[1]:
                                            #    if ship.location[0]-sunrider.location[0] >=0:
                                            #        if ship.location[0]-sunrider.location[0] <=7:
                                                if ship in enemy_ships: #it's possible the ship was already deleted because of the boss being killed
                                                    self.target = ship
                                                    ship.receive_damage(BM.vanguard_damage,sunrider,'Vanguard')
                                looping = False
                                self.vanguardtarget = False
                                renpy.hide_screen('battle_screen')
                                renpy.show_screen('battle_screen')
                                BM.order_used = True

                        if result[0] == 'deselect':
                            self.cmd += self.orders['VANGUARD CANNON'][0]
                            looping = False
                            self.vanguardtarget = False
                            self.order_used = False

                else:
                    renpy.music.play('sound/Voice/Ava/Ava Others 9.ogg',channel='avavoice')
                    self.order_used = False
            else:
                renpy.say('Ava','It\'s hopeless, captain!')
                self.order_used = False

        def toggle_player_ai(self):
            self.player_ai = not self.player_ai

        def battle_end_turn(self):
            if self.targetingmode:
                self.battle_deselect()
            self.end_player_turn()
        ########################################################
        ## Battle dispatcher end
        ########################################################
        def start(self):
            self.battle_log_insert(['system'], "-------------BATTLE START-------------")
            BM.player_ai = False
            battlemode() #stop scrollback and set BM.battlemode = True
            update_stats()  #used to update some attributes like armour and shields
            renpy.show_screen('battle_screen')

            #new formation feature (only after mission 12 for now)
            if self.editableformations():
                self.phase = 'formation'

                for ship in player_ships:
                    if ship.location != None:
                        set_cell_available(ship.location)
                        ship.location = None

                renpy.show_screen('player_unit_pool_collapsed')
                renpy.show_screen('player_unit_pool')
                BM.selectedmode = False #failsafe
                BM.targetmode = False
                BM.selected = None #the selected unit doesn't show up in the pool
                self.formation_phase()
            else:
                self.jumptomission()

        def jumptomission(self):
            renpy.jump('mission{}'.format(self.mission))

        def editableformations(self):
            return (type(self.mission) != str and self.mission > 12) #apparently string>int is completely legal in python :o

        def battle(self):
            for ship in player_ships:
                if not hasattr(ship, 'blbl'):
                    ship.blbl = ship.lbl

            if self.player_ai:
                self.player_AI()
                self.toggle_player_ai()
                self.result = 'endturn'
            else:
                #battle_screen should be shown, and ui.interact waits for your input. 'result' stores the value return from the Return actionable in the screen
                self.result = ui.interact()

            if store.Difficulty < self.lowest_difficulty:
                self.lowest_difficulty = store.Difficulty

            self.just_moved = False #this sets it so you can no longer take back your move
            renpy.hide_screen('game_over_gimmick') #disables the screensaver gimmick

            if self.stopAI and sunrider.hp < 0:  #some failsafe checking. stopAI functions like an emergency stop for AI code
                renpy.jump('sunrider_destroyed')
            if hasattr(store,'mochi'):
                if hasattr(mochi,'hp'):
                    if mochi.hp < 0 and mochi in player_ships:
                        renpy.jump('sunrider_destroyed')

            #sanity check
            for ship in self.ships:
                if ship.hp <= 0:
                    destroyed_ships.append(ship)
                    if ship in player_ships:
                        player_ships.remove(ship)
                    if ship in enemy_ships:
                        enemy_ships.remove(ship)
                    if ship in self.ships:
                        self.ships.remove(ship)

            self.dispatch_handler(self.result)()

            self.check_for_loss()
            self.check_for_win()
            return

        def check_for_loss(self):
            if len(player_ships) == 0:
                self.you_lose()

        def you_lose(self):  #Separated for mod support, in case something other than 'better luck next time' or 'game over' is the consequence of losing
            if self.mission != 'skirmishbattle':
                renpy.jump('sunrider_destroyed')
            else:
                show_message('You were defeated! better luck next time...')
                clean_battle_exit()
                renpy.jump('dispatch')

        def boss_died(self, deadboss):
            if (self.mission != 'skirmishbattle'):
                self.you_win()

        def check_for_win(self):
            if len(enemy_ships) == 0:
                self.you_win()

        def you_win(self):
            self.stopAI = True
            if self.battlemode: #Ignore calls to you_win if we're not actually in battle mode.
                renpy.hide_screen('commands')
                self.battle_end()
                renpy.hide_screen('battle_screen')
            if renpy.has_label('after_mission{}'.format(BM.mission)):
                renpy.jump('after_mission{}'.format(BM.mission))

#ending a turn
        def end_player_turn(self):
            self.battle_log_insert(['system'], "---------Player turn end---------")
            self.battle_log_trimm()
            renpy.hide_screen('commands')
            self.selected = None #some sanity checking
            self.target = None
            self.moving = False
            self.selectedmode = False
            self.targetingmode = False
            self.active_weapon = None
            self.weaponhover = None
            self.turn_count += 1
            renpy.music.play(EnemyTurnMusic)
            renpy.call_in_new_context('endofturn')

            for ship in self.ships:
                ship.flak_effectiveness = 100

            self.enemy_AI() #call the AI to take over
            self.battle_log_insert(['system'], "---------{0} turn end---------".format(self.phase))
            self.battle_log_trimm()
             ##I have NO idea why this dumb workaround is needed, but the destroy() method -somehow- doesn't want to jump to this label sometimes.
            if sunrider.hp < 0:
                renpy.jump('sunrider_destroyed')

            for ship in self.ships:
                ship.flak_effectiveness = 100
                ship.getting_curse = False #failsafes
                ship.getting_buff = False
            for ship in player_ships:
                ship.en = ship.max_en * (100 + ship.modifiers['energy regen'][0] ) / 100
                if ship.en < 0: ship.en = 0
                if ship.hp <= ((ship.hp / 100) * 25): ship.morale -= 5
            for ship in enemy_ships:
                if ship.hp <= ((ship.hp / 100) * 25): ship.morale -= 5
            self.active_weapon = None
            self.targetingmode = False
            self.target = None
            self.selected = None
            self.selectedmode = False
            self.order_used = False
            self.moving = False

            #run the end of turn callbacks
            if BM.end_turn_callbacks != []:
                for callback in BM.end_turn_callbacks:
                    callback()

            if self.battlemode:
                renpy.music.play(PlayerTurnMusic)
                renpy.call_in_new_context('endofturn')
            renpy.take_screenshot()

            # I've sometimes been getting this error for some silly reason:
            # WindowsError: [Error 183] Cannot create a file when that file already exists
            # may just be me, but to be safe I'll put a catch here
            try:
                renpy.save('beginturn')
            except:
                pass

        def player_AI(self):

              ##lead ships don't care about looking for other ships for protection
              ##other ships come to them! instead, lead ships typically go on the
              ##offensive, dragging allies along.
            self.support_ships = []
            self.lead_ships = []
            total_defense = 0
            update_stats()

            #support ships take their turn first, so they can improve the effects of all other units.
            for pship in player_ships:
                if pship.support:
                    self.support_ships.append(pship)

            for pship in player_ships:
                total_defense += pship.shield_generation + pship.flak + pship.armor
            average_defense = total_defense / float(len(player_ships))

              ##because I assume  most of the time there will be many mooks and only
              ##a few high defense ships the few that are are definitely above average.
              ##this method is very dynamic and doesn't rely on blueprint flags.
            for pship in player_ships:
                defense = pship.shield_generation + pship.flak + pship.armor
                if defense > average_defense and pship not in self.support_ships:
                    self.lead_ships.append(pship)

            for pship in self.support_ships:
                if BM.stopAI:
                    return

                pship.en = pship.max_en
                pship.lbl = im.MatrixColor(pship.blbl,im.matrix.brightness(0.3))

                #a number of people have reported crashes: Exception: ui.interact called with non-empty widget/layer stack.
                #this is but a work-around.
                try:
                    renpy.pause(AI_WAIT_TIME)
                except:
                    pass

                # if config.developer:
                    # renpy.pause()

                try:
                    if not pship.modifiers['energy regen'][0] == -100:
                        pship.AI()
                    else:
                        show_message('the {} is disabled!'.format(pship.name) )
                except:
                    pship.modifiers['energy regen'] = (0,0)
                    pship.AI()
                pship.lbl = pship.blbl

                ##the lead ships take their turn after the support ships.
            for pship in self.lead_ships:
                if BM.stopAI:
                    return

                pship.en = pship.max_en
                pship.lbl = im.MatrixColor(pship.blbl,im.matrix.brightness(0.3))

                try:
                    renpy.pause(AI_WAIT_TIME)
                except:
                    pass
                # if config.developer:
                    # renpy.pause()

                try:
                    if not pship.modifiers['energy regen'][0] == -100:
                        pship.AI()
                    else:
                        show_message('the {} is disabled!'.format(pship.name) )
                except:
                    pship.modifiers['energy regen'] = (0,0)
                    pship.AI()
                pship.lbl = pship.blbl

                ## the rest of the enemy units take their turns last
            for ship in player_ships:
                if BM.stopAI:
                    return
                #now all the non-lead and all the non-support ships take their turn
                if ship not in self.lead_ships and ship not in self.support_ships:

                    try:
                        if ship.modifiers['energy regen'][0] == -100:
                            show_message('the {} is disabled!'.format(ship.name) )
                            ship.en = 0
                        else:
                            ship.en = ship.max_en
                    except:
                        ship.modifiers['energy regen'] = (0,0)
                        ship.en = ship.max_en

                    ship.lbl = im.MatrixColor(ship.blbl,im.matrix.brightness(0.3))
                    try:
                        renpy.pause(AI_WAIT_TIME)
                    except:
                        pass
                    # if config.developer:
                        # renpy.pause()
                    ship.AI()
                    ship.lbl = ship.blbl

        def enemy_AI(self):

              ##lead ships don't care about looking for other ships for protection
              ##other ships come to them! instead, lead ships typically go on the
              ##offensive, dragging allies along.
            self.support_ships = []
            self.lead_ships = []
            total_defense = 0
            update_stats()

            #support ships take their turn first, so they can improve the effects of all other units.
            for eship in enemy_ships:
                if eship.support:
                    self.support_ships.append(eship)

            for eship in enemy_ships:
                total_defense += eship.shield_generation + eship.flak + eship.armor
            if len(enemy_ships) > 0:
                average_defense = total_defense / float(len(enemy_ships))
            else:
                average_defense = total_defense

              ##because I assume  most of the time there will be many mooks and only
              ##a few high defense ships the few that are are definitely above average.
              ##this method is very dynamic and doesn't rely on blueprint flags.
            for eship in enemy_ships:
                defense = eship.shield_generation + eship.flak + eship.armor
                if defense > average_defense and eship not in self.support_ships:
                    self.lead_ships.append(eship)

            for eship in self.support_ships:
                if BM.stopAI:
                    return

                eship.en = eship.max_en
                eship.lbl = im.MatrixColor(eship.blbl,im.matrix.brightness(0.3))
                try:
                    renpy.pause(AI_WAIT_TIME)
                except:
                    pass
                # if config.developer:
                    # renpy.pause()

                try:
                    if not eship.modifiers['energy regen'][0] == -100:
                        eship.AI()
                    else:
                        show_message('the {} is disabled!'.format(eship.name) )
                except:
                    eship.modifiers['energy regen'] = (0,0)
                    eship.AI()
                eship.lbl = eship.blbl

                ##the lead ships take their turn after the support ships.
            for eship in self.lead_ships:
                if BM.stopAI:
                    return

                eship.en = eship.max_en
                eship.lbl = im.MatrixColor(eship.blbl,im.matrix.brightness(0.3))

                #a number of people have reported crashes: Exception: ui.interact called with non-empty widget/layer stack.
                #this is but a work-around.
                try:
                    renpy.pause(AI_WAIT_TIME)
                except:
                    pass

                # if config.developer:
                    # renpy.pause()

                try:
                    if not eship.modifiers['energy regen'][0] == -100:
                        eship.AI()
                    else:
                        show_message('the {} is disabled!'.format(eship.name) )
                except:
                    eship.modifiers['energy regen'] = (0,0)
                    eship.AI()
                eship.lbl = eship.blbl

                ## the rest of the enemy units take their turns last
            for ship in enemy_ships:
                if BM.stopAI:
                    return
                #now all the non-lead and all the non-support ships take their turn
                if ship not in self.lead_ships and ship not in self.support_ships:

                    try:
                        if ship.modifiers['energy regen'][0] == -100:
                            show_message('the {} is disabled!'.format(ship.name) )
                            ship.en = 0
                        else:
                            if not ship.just_spawned: ship.en = ship.max_en
                    except:
                        ship.modifiers['energy regen'] = (0,0)
                        ship.en = ship.max_en

                    ship.lbl = im.MatrixColor(ship.blbl,im.matrix.brightness(0.3))

                    #a number of people have reported crashes: Exception: ui.interact called with non-empty widget/layer stack.
                    #this is but a work-around.
                    try:
                        renpy.pause(AI_WAIT_TIME)
                    except:
                        pass

                    ship.AI()
                    ship.lbl = ship.blbl


        def battle_end(self, lost = False):
            """ending the battle - reset values for next battle"""
            self.battlemode = False #this ends the battle loop
            if self.selected != None: self.unselect_ship(self.selected)
            self.targetingmode = False
            self.weaponhover = None
            self.hovered = None
            BM.enemy_vanguard_path = []
            renpy.hide_screen('tooltips')
            BM.phase = 'Player'

            if store.Difficulty < self.lowest_difficulty:
                self.lowest_difficulty = store.Difficulty

            if not lost:
                #show the victory screen
                renpy.music.stop()
                renpy.music.play('Music/Posthumus_Regium_Finale.ogg', loop = False)
                renpy.hide_screen('commands')
                self.draggable = False
                renpy.show_screen('victory')
                renpy.pause(3.0)
                renpy.hide_screen('victory')

                store.repair_cost = 0
                store.total_money = 0
                store.boss_killed = False
                store.surrender_bonus = 0
                for ship in destroyed_ships:
                    if ship.faction == 'Player':
                        store.repair_cost += int(ship.max_hp * 0.2)
                    else:
                        if ship.boss: store.boss_killed = True #check if a boss was killed
                        store.total_money += ship.money_reward

                if store.boss_killed:
                    for ship in enemy_ships:
                        if ship.hp > 0:
                            store.surrender_bonus += ship.money_reward / 2

                for ship in player_ships:
                    store.repair_cost += int((ship.max_hp - ship.hp)*0.1)

                store.net_gain = int(store.total_money + store.surrender_bonus - store.repair_cost)

                #SPACE WHALE TAX!
                if store.Difficulty == 5:
                    store.net_gain *= 0.8

                self.money += int(net_gain)

                #Captain and higher difficulties reduce the total CP you get per battle.
                difficulty_penalty = store.Difficulty - 1
                if difficulty_penalty < 0: difficulty_penalty = 0

                self.cmd += int((net_gain*10)/(BM.turn_count+difficulty_penalty))

                renpy.show_screen('victory2')
                renpy.pause(1)
                renpy.hide_screen('victory2')
                self.draggable = True

            self.turn_count = 1
            self.active_strategy = [None,0]
            self.ships = []
            self.selectedmode = False
            self.battle_log = []
            renpy.hide_screen("battle_log")

            VNmode() #return to visual novel mode. this mostly just restored scrolling rollback
            for ship in destroyed_ships:
                if self.mission == 'skirmish' or (ship.faction == 'Player' and not ship.mercenary):
                    player_ships.append(ship)
                    self.ships.append(ship)
            for ship in player_ships:
                self.ships.append(ship)
            for ship in player_ships:
                ship.en = ship.max_en
                ship.hp = ship.max_hp
                ship.morale = 100
                ship.hate = 100
                ship.total_damage = 0
                ship.total_missile_damage = 0
                ship.total_kinetic_damage = 0
                ship.total_energy_damage = 0
                ship.missiles = ship.max_missiles
                ship.location = None #this helps if you add new ships but don't know the current location of the existing ones.
                for modifier in ship.modifiers:
                    ship.modifiers[modifier] = [0,0]

            #reset the entire grid to empty and BM.ships with only the player_ships list
            clean_grid()
            self.covers = []
            renpy.hide_screen('battle_screen')
            renpy.hide_screen('commands')

            renpy.block_rollback()

    ## Displayables ##
    #custom displayables harness the power of pygame directly.

    class MouseTracker(renpy.Displayable):
        """
        this class keeps track of where the mouse is and what it does and relates
        drags and clicks to the viewport and the BM. This way the ships can be simple
        images instead of imagebuttons, reducing lag. I guess this doesn't have to be
        a displayable but it works so meh
        """

        def __init__(self,**kwargs):
            renpy.Displayable.__init__(self,**kwargs)
            self.width = 0
            self.height = 0
            self.mouse_has_moved = True
            self.rel = (0,0)

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            return render

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.mouse_has_moved = False
                self.rel = pygame.mouse.get_rel()

            if ev.type == pygame.MOUSEMOTION:
                self.mouse_has_moved = True
                renpy.hide_screen('game_over_gimmick')   #why this no werk?

                # if the left mouse button is pressed, it's a drag
                if ev.buttons[0] == 1:
                    if BM.draggable:
                        BM.xadj.change(BM.xadj.value - ev.rel[0] * 2)
                        BM.yadj.change(BM.yadj.value - ev.rel[1] * 2)
                        # if abs(ev.rel[0]) + abs(ev.rel[1]) > 5:

                mouse_location = get_mouse_location()

                #vanguard targeting
                if BM.vanguardtarget:
                    if BM.mouse_location != mouse_location and ev.buttons[0] != 1:
                        if get_distance(sunrider.location,mouse_location) <=BM.vanguard_range:
                            BM.mouse_location = mouse_location
                            self.mouse_has_moved = True
                            renpy.restart_interaction()


                #check for hovering over movement tiles
                if BM.selected != None:
                    if BM.mouse_location != mouse_location and ev.buttons[0] != 1:
                        if get_distance(BM.selected.location,mouse_location) <=4:
                            BM.mouse_location = mouse_location
                            self.mouse_has_moved = True
                            renpy.restart_interaction()

                #check for hovering over ships
                if BM.hovered != None:
                    if BM.hovered.location != mouse_location:
                        BM.hovered = None
                        renpy.restart_interaction()
                else:
                    for ship in BM.ships:
                        if ship.location == mouse_location:
                            BM.hovered = ship
                            renpy.restart_interaction()
                            break

            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                # being very careful that the mouse -did not move- recently before an actual click is registered
                # otherwise it's a drag
                if not self.mouse_has_moved and pygame.mouse.get_rel() == (0,0):
                    # show_message('tried to click')
                    mouse_location = get_mouse_location()

                    # if you are using short range warp or are in skirmish mode this is used
                    if BM.targetwarp:
                        if get_cell_available(mouse_location):
                            return ['warptarget',get_mouse_location()]

                    #move handling
                    elif BM.selected != None and BM.weaponhover == None:
                        if BM.selected.faction == 'Player':
                            if get_cell_available(mouse_location):
                                distance = get_distance(BM.selected.location,mouse_location)
                                if distance <= 4:  #perhaps not really needed anymore?
                                    move_range = int(float(BM.selected.en) / BM.selected.move_cost)
                                    if distance <= move_range:
                                        return [ 'move' , mouse_location ]

                    #sometimes it's possible to have nothing selected and still something left in BM.weaponhover
                    if BM.selected == None:
                        BM.weaponhover == None

                    #selection handling
                    if (BM.weaponhover == None or BM.active_weapon != None) and not BM.targetwarp:
                        for ship in BM.ships:
                            if ship.location == mouse_location:
                                return ['selection',ship]
                        if BM.vanguardtarget:
                            spoof_ship = store.object()
                            spoof_ship.location = mouse_location
                            spoof_ship.faction = 'Not the Player'
                            return ['selection', spoof_ship]

    class MouseFollow(renpy.Displayable):
        """
        this class creates an object that will display an image at the mouse cursor
        which gets redrawn every frame so it follows the cursor.
        """

        def __init__(self,child,**kwargs):
            renpy.Displayable.__init__(self,**kwargs)
            self.child = renpy.displayable(child)
            self.width = 0
            self.height = 0
            self.position = renpy.get_mouse_pos()

        def render(self, width, height, st, at):
            #create the basic Render from the passed displayable (the child)
            child_render = renpy.render(self.child, width, height, st ,at)
            #get the size of the label
            self.width, self.height = child_render.get_size()
            #make a new Render object with the size of the child.
            render = renpy.Render(self.width, self.height)
            #grab the mouse location
            x,y = renpy.get_mouse_pos()
            #adjust the position so that the middle of the label lines up with the mouse cursor
            self.position = (x - self.width / 2 , y - self.height / 2)
            #blitting means actually showing it on screen
            render.blit(child_render, self.position)
            # request a redraw asap (= next frame)
            renpy.redraw(self, 0)
            #return the render object so that renpy can do things with it.
            return render

        def event(self, ev, x, y, st):
            pass
            # if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:


        def visit(self):
           return [ self.child ]

    ##blueprints##

    class Battleship(store.object):
        """this class is the basis of all unit types in the game.
        these values are the default one if none are specified."""
        def __init__(self):
            self.brain = DefaultAI(self)
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = -1
            self.shield_color = '000'
            self.max_hp = 200
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.repair = 0
            self.flak = 0
            self.flak_range = 1
            self.flak_effectiveness = 100
            self.flak_used = False
            self.flaksim = None
            self.fireing_flak = False
            self.just_spawned = False
            self.melee_location = None
            self.morale_up = False
            self.morale_down = False
            self.morale = 100
            self.morale_acc = 0
            self.enemies = {}
            self.hate = 100 #this is actually how much the enemy hates you. aka threat
            self.attraction = 0 #AI uses this. ships that provide lots of cover attract others
            self.fear = {
                'kinetics':20,
                'missiles':20,
                'energy':20,
                }
            self.kinetic_dmg = 1  #normal damage at start. increased by upgrades
            self.kinetic_acc = 1
            self.kinetic_cost = 1
            self.energy_dmg = 1
            self.energy_acc = 1
            self.energy_cost = 1
            self.missile_dmg = 1
            self.missile_eccm = 0
            self.missile_cost = 1
            self.melee_dmg = 1
            self.melee_acc = 1
            self.melee_cost = 1
            self.move_cost_multiplier = 1.0
            #[display name, level,increase/upgrade,upgrade cost,cost multiplier]
            self.upgrades = {
                'max_hp':['Hull Plating',1,100,100,1.5],
                'max_en':['Energy Reactor',1,5,200,1.4],
                'move_cost_multiplier':['Move Cost',1,-0.05,100,2.5],
                'evasion':['Evasion',1,5,500,2.5],
                'kinetic_dmg':['Kinetic Damage',1,0.05,105,1.55],
                'kinetic_acc':['Kinetic Accuracy',1,0.05,100,1.5],
                'kinetic_cost':['Kinetic Energy Cost',1,-0.05,100,2.0],
                'energy_dmg':['Energy Damage',1,0.075,100,1.3],
                'energy_acc':['Energy Accuracy',1,0.05,120,1.5],
                'energy_cost':['Energy Cost',1,-0.05,100,1.8],
                'missile_dmg':['Missile Damage',1,0.10,100,1.5],
                'missile_eccm':['Missile Flak Resistance',1,1,100,1.5],
                'missile_cost':['Missile Energy Cost',1,-0.5,100,2.0],
                'max_missiles':['Missile Storage',1,1,500,3],
                'melee_dmg':['Melee Damage',1,0.05,100,1.5],
                'melee_acc':['Melee Accuracy',1,0.05,100,1.5],
                'melee_cost':['Melee Energy Cost',1,-0.05,100,2.0],
                'shield_generation':['Shield Power',1,5,500,2],
                'shield_range':['Shield Range',1,1,1000,5],
                'flak':['Flak',1,5,500,2],
                'base_armor':['Armor',1,1,100,1.3],
                'repair':['Repair Crew',1,50,500,2]
                }
            self.total_damage = 0  #refers to damage done, not taken. used by AI
            self.total_kinetic_damage = 0
            self.total_missile_damage = 0
            self.total_energy_damage = 0
            self.base_armor = 10
            self.armor = self.base_armor
            self.armor_color = '000'
            self.weapons = []
            self.default_weapon_list = []
            self.max_weapons = 9
            self.max_missiles = 0
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.move_cost = 50
            self.cmd_reward = 100
            self.money_reward = 100
            self.cth = 0
            self.getting_buff = False
            self.getting_curse = False
            self.boss = False
            self.mercenary = False  #if true you don't get it back upon death
            self.spawns = []
            self.support = False #used by AI to check whether to run support ability code
            self.location = None
            self.current_location = None
            self.next_location = None
            self.movement_tiles = []
            self.portrait = None
            self.death_animation = 'no_animation'  #the default death animation: none.
            self.miss_animation = 'no_animation' #gets called when this ship avoids getting hit
            self.id = 0 #used to identify enemy_ships more easily
              #modifiers list temporary (de)buffs.
              #these values represent the strength of the modifier and the number of turns it stays in effect
            self.modifiers = {
                'accuracy':[0,0],
                'move_cost':[0,0],
                'evasion':[0,0],
                'damage':[0,0],
                'armor':[0,0],
                'shield':[0,0],
                'flak':[0,0],
                'energy':[0,0],
                'stealth':[0,0],
                'shield_generation':[0,0],
                'energy regen':[0,0],
                }

        #return None if an attribute does not exist
        # def __getattr__(self,X):
            # return None

        def update_armor(self):
            self.armor = (self.base_armor * ( 100 + self.modifiers['armor'][0]) / 100.0 ) * self.hp / float(self.max_hp)
            self.armor = int(self.armor)
            self.armor_color = '000'
            if self.armor < self.base_armor: self.armor_color = '700'
            elif self.armor > self.base_armor: self.armor_color = '070'

        ## aplly hidden morale modifiers
        def update_morale(self):
            if self.morale > 200:
                if not self.morale_up:
                    self.morale_up = True
                    self.evasion += 5
                    self.morale_acc += 10
                if self.morale_down:
                    self.morale_down = False
                    self.evasion += 5
                    self.morale_acc += 10
            elif self.morale < 100:
                if not self.morale_down:
                    self.morale_down = True
                    self.evasion -= 5
                    self.morale_acc -= 10
                if self.morale_up:
                    self.morale_up = False
                    self.evasion -= 5
                    self.morale_acc -= 10
            else:
                if self.morale_up:
                    self.morale_up = False
                    self.evasion -= 5
                    self.morale_acc -= 10
                elif self.morale_down:
                    self.morale_down = False
                    self.evasion += 5
                    self.morale_acc += 10
            return

        def update_stats(self):
            try:
                if self.modifiers['energy regen'][0] == -100:
                    self.en = 0
            except:
                self.modifiers['energy regen'] = (0,0)

            self.shields = 0
            #update shield generation
            if self in player_ships:
                for ship in player_ships:
                    if get_ship_distance(self, ship) <= ship.shield_range:
                        actual_generation = ship.shield_generation
                        try:
                            mod,duration = ship.modifiers['shield_generation']
                        except:
                            ship.modifiers['shield_generation'] = [0,0]
                            mod,duration = (0,0)
                        if mod != 0: actual_generation += mod
                        if actual_generation < 0: actual_generation = 0
                        self.shields += actual_generation
            elif self in enemy_ships:
                for ship in enemy_ships:
                    if ship.shield_generation > 0:
                        if get_ship_distance(self, ship) <= ship.shield_range:
                            actual_generation = ship.shield_generation
                            try:
                                mod,duration = ship.modifiers['shield_generation']
                            except:
                                ship.modifiers['shield_generation'] = [0,0]
                                mod,duration = ship.modifiers['shield_generation']
                            if mod != 0:
                                actual_generation += mod
                            if actual_generation < 0:
                                actual_generation = 0
                            self.shields += actual_generation
            if self.shields > 100: self.shields = 100
            self.shield_color = '000'
            if self.shields > self.shield_generation: self.shield_color = '070'
            self.update_armor()
            self.update_morale()

        def receive_damage(self,damage,attacker,wtype):
            BM.attacker = attacker

            if damage == None:
                return
            if damage == 'no energy':
                renpy.say('ERROR','the {} does not have the energy for this attack'.format(attacker.name))
                return
            elif damage == 'no ammo':
                renpy.say('ERROR','the {} does not have enough ammo for this attack'.format(attacker.name))
                return
            elif damage == 'miss':
                BM.battle_log_insert(['attack'], "{0}'s attack misses".format(attacker.name))
                if wtype == 'Melee':
                    store.damage = damage
                    try:
                        renpy.call_in_new_context('melee_attack_player')
                    except:
                        pass #player probably attacked a non-ryder. silly players.
                else:
                    try:
                        renpy.call_in_new_context('miss_{}'.format(self.animation_name)) #show the miss animation
                    except:
                        show_message('missing animation. "miss_{}" does\'t seem to exist'.format(self.animation_name))
            else:

                #getting hit with the legion's vanguard means instant game over.
                if self.faction == 'Player' and wtype == 'Vanguard':
                    try:
                        renpy.call_in_new_context('hitlegion_{}'.format(self.animation_name)) #you just got pwnd, son.
                    except:
                        show_message('missing animation. "hitlegion_{}" does\'t seem to exist'.format(self.animation_name))
                    if not self.mercenary:
                        # show_message( 'the {} was obliterated. Game Over.'.format(self.name) )
                        renpy.jump('sunrider_destroyed') #game over
                        sunrider.hp = 0  #failsafe
                    # BM.stopAI = True   #inexplicably gives odd results
                    return

                #handle healing
                if wtype == 'Support':
                    #BM.battle_log.append("{0} is healed for {1} HP".format(self.name, str(int(damage))))
                    self.hp += int(damage)
                    if self.hp > self.max_hp:
                        self.hp = self.max_hp
                    return

                #havoc isn't allowed to die in the first turn
                if BM.mission == 2 and self.name == 'Havoc' and BM.turn_count == 1 and damage > self.hp:
                    try:
                        renpy.call_in_new_context('miss_{}'.format(self.animation_name)) #show the miss animation
                    except:
                        show_message('missing animation. "miss_{}" does\'t seem to exist'.format(self.animation_name))
                    return

                #collect and store data used by the AI
                attacker.total_damage += damage
                if wtype == 'Missile' or wtype == 'Rocket':
                    attacker.total_missile_damage += damage
                      #high levels of fear (of a damage type) changes AI behavior
                    self.fear['missiles'] += damage / 10
                if wtype == 'Kinetic' or wtype == 'Assault':
                    attacker.total_kinetic_damage += damage
                    self.fear['kinetics'] += damage / 10
                if wtype == 'Laser' or wtype == 'Pulse':
                    attacker.total_energy_damage += damage
                    self.fear['energy'] += damage / 10

                attacker.hate += damage*0.5  #damaging enemies increases how likely they are to target you
                self.hate -= damage  #getting damaged lowers your threat back down
                if self.hate < 100: self.hate = 100
                BM.target = self

                #difficulty fudging
                damage = get_modified_damage(damage,self.faction)

                store.damage = damage #the global variant is used by the health_animation screen

                  #if the attack hits, show the hit animation of the target based on weapon type
                BM.battle_log_insert(['attack'], "{0} inflicts {1} damage to {2}".format(attacker.name, damage, self.name))
                self.hp -= damage

                if wtype == 'Melee':
                    try:
                        renpy.call_in_new_context('melee_attack_player')
                    except:
                        pass
                else:
                    try:
                        renpy.call_in_new_context('hitanim_{}_{}'.format(self.animation_name,wtype.lower()))
                    except:
                        show_message('missing animation. "hitanim_{}_{}" doesn\'t seem to exist'.format(self.animation_name,wtype.lower()))

                if self.hp <= 0:
                    BM.battle_log_insert(['attack'], "{0} destroys {1}".format(attacker.name, self.name))
                    self.destroy(attacker)
                    update_stats()
                else:
                    self.update_stats()

        def destroy(self, attacker, no_animation = False):
              #first take care of some AI data tracking stuff
              #destroying enemy ships increases hate, but lowers enemy morale too
            self.en = 0 #this turns out to be useful especially for not having the AI do stuff with dead units.

            if self == BM.selected:   # useful when you suicide into a counter
                BM.unselect_ship(self)

            #hate/morale management
            self.hate = 100  #reset hate so that after getting resurrected it doesn't pull everything again.
            attaker.morale += 10
            #enemy loss morale affection
            if not self.faction == 'Player':
                attacker.hate += self.max_hp*0.3
                attacker.target = None
                #loss of lead ship leads to total morale degradation
                if self in lead_ships:
                    for eship in enemy_ships: eship.morale -= 10
                else:
                    for eship in enemy_ships:
                        if get_ship_distance(self,eship) <= 4:
                            eship.morale -= 10
                for pship in player_ships:
                    if get_ship_distance(self,eship) <= 4:
                        eship.morale += 10
            #player loss morale affection
            else:
                for eship in enemy_ships:
                    if get_ship_distance(self,eship) <= 4:
                        eship.morale += 10
                for pship in player_ships:
                    if get_ship_distance(self,eship) <= 4:
                        eship.morale -= 10

            #show the animation of the ship getting blown up
            if not no_animation:
                try:
                    renpy.call_in_new_context('die_{}'.format(self.animation_name)) #show the death animation
                except:
                    show_message('missing animation. "die_{}" does\'t seem to exist'.format(self.animation_name))

            #this list gets used after battle
            destroyed_ships.append(self)

            #list maintenance
            if self in enemy_ships:
                enemy_ships.remove(self)
            elif self in player_ships:
                player_ships.remove(self)

            #grid maintenance
            set_cell_available(self.location)

            #more list maintenance
            if self in BM.ships:
                BM.ships.remove(self)

            #did you lose a mercenary?   (not really used anymore)
            if self.mercenary and BM.mission != 'skirmish':
                BM.mercenary_count -= 1

            #killing a boss ends the battle (the rest surrenders)
            #if this was the last enemy ship you win too, but that can be handled by the battle manager
            if self.boss:
                BM.boss_died(self)

            BM.check_for_loss()
            BM.check_for_win()

        def register_weapon(self, weapon):
            if len(self.weapons) >= self.max_weapons:
                raise IndexError('ERROR: too many weapons assigned to the {}'.format(self.name))
            else:
                self.weapons.append(weapon)

        def remove_weapon(self, weapon):
            if weapon in self.weapons:
                self.weapons.remove(weapon)

        def set_location(self,xnew,ynew):
            if self.location != None:
                a,b = self.location
                if a > 0 and b > 0:
                    BM.grid[a-1][b-1] = False
            BM.grid[xnew-1][ynew-1] = True
            self.location = (xnew,ynew)

        def AI_estimate_damage(self,pship,en = 0, range_reduction = 0):  #part of the AI
            self.brain.AI_estimate_damage(pship,en,range_reduction)

        def AI_attack_target(self,pship,weapon,counter=False):
            self.brain.AI_attack_target(pship,weapon,counter)

        def AI_basic_loop(self):
            self.brain.AI_basic_loop()

        def AI_move_towards(self, target, melee_distance = False, max_move_distance = 0, preferred_distance = 0,rush=False):
            self.brain.AI_move_towards(target,melee_distance,max_move_distance,preferred_distance,rush)

        def AI(self):
            self.brain.AI()

        def move_ship(self, new_location,bm):
              ##play voices based on backwards or forwards motion
            if self.faction == 'Player':
                if self.location[0] > new_location[0]: #going west
                    a = renpy.random.randint(0,len(self.movebackward_voice)-1)
                    renpy.music.play('sound/Voice/{}'.format(self.movebackward_voice[a]),channel = self.voice_channel)
                    del a
                if self.location[0] < new_location[0]: #going east
                    a = renpy.random.randint(0,len(self.moveforward_voice)-1)
                    renpy.music.play('sound/Voice/{}'.format(self.moveforward_voice[a]),channel = self.voice_channel)
                    del a

            bm.selectedmode = False #this disables showing movement tiles
            renpy.hide_screen('commands')

            #sanity check and deduct movement cost
            total_move_cost = self.move_cost * get_distance(self.location,new_location)
            if self.en < total_move_cost:
                return
            else:
                self.en -= total_move_cost

            a = self.location[0]-1  #make the next line of code a little shorter
            b = self.location[1]-1
            bm.grid[a][b] = False #tell the BM that the old cell is now free again

            self.current_location = self.location #store a temporary location
            self.next_location = new_location
            bm.battle_log_insert(['detailed'], "{0} moved from {1} to {2}".format(self.name, str(self.current_location)[1:-1].replace(', ', '/'), str(self.next_location)[1:-1].replace(', ', '/')))
            self.travel_time = get_distance(self.location,new_location) * SHIP_SPEED
            self.location = None #this makes the imagebutton of this ship not be displayed on battle_screen
            bm.moving = True

            order_state = BM.order_used

            renpy.hide_screen('battle_screen')
            renpy.show_screen('battle_screen')

            renpy.pause(self.travel_time+0.3)
            BM.moving = False

            renpy.hide_screen('battle_screen')
            renpy.show_screen('battle_screen')

            BM.order_used = order_state

            self.location = new_location
            sort_ship_list()
            a = self.location[0]-1
            b = self.location[1]-1
            bm.grid[a][b] = True
            if self.faction == 'Player':
                BM.just_moved = True

            ## BLIND SIDE ATTACKS
            if self.faction == 'Player' and self.modifiers['stealth'][0] != 100:
                #player unit moves next to enemy unit

                for enemy in enemy_ships:
                    #if next to enemy, not dead and the enemy isn't cursed.
                    if get_ship_distance(self,enemy) == 1 and self in player_ships and enemy.modifiers['flak'][0] != -100:
                        counter = None
                        for weapon in enemy.weapons:
                            if weapon.wtype == 'Assault':
                                counter = weapon
                        if counter != None:
                            enemy.en = enemy.max_en
                            show_message('COUNTER ATTACK!')
                            BM.battle_log_insert(['attack'], "{0} counter-attacks {1}".format(enemy.name, self.name))
                            enemy.AI_attack_target(self,counter,True)
                            BM.just_moved = False
            else:
                #enemy moves next to player unit

                if self.name != 'Phoenix': #enemy phoenix is immune to counter attacks without having to buff itself.
                    for ship in player_ships:
                        if get_ship_distance(self,ship) == 1 and self in enemy_ships: #if next to enemy and -not dead-
                            counter = None
                            for weapon in ship.weapons:
                                if weapon.wtype == 'Assault':
                                    counter = weapon
                            if counter != None:
                                EN = ship.en
                                ship.en = 200
                                show_message('COUNTER ATTACK!')
                                BM.battle_log_insert(['attack'], "{0} counter-attacks {1}".format(ship.name, self.name))
                                self.update_stats()
                                try:
                                    renpy.call_in_new_context('atkanim_{}_{}'.format(ship.animation_name,counter.wtype.lower()))
                                except:
                                    show_message('missing animation. "atkanim_{}_{}" does\'t seem to exist'.format(ship.animation_name,counter.wtype.lower()))
                                damage = counter.fire(ship,self,True)
                                self.receive_damage(damage,ship,counter.wtype)
                                ship.en = EN

            bm.select_ship(self, play_voice = False) #you can control your ship again

        ### Weapon Blueprints ###
    class Weapon(store.object): #superclass of all weapon objects
        def __init__(self):
            self.damage = 0
            self.uses_missiles = False
            self.uses_rockets = False
            self.energy_use = 0
            self.hp_cost = 0
            self.acc_degradation = 15
            self.base_accuracy = 50
            self.wtype = ''
            self.name = 'unnamed'
            self.max_range = None
            self.animation_name = None
            self.shot_count = 1
            self.accuracy = 100
            self.tooltip = ''
            #a dict that keeps track of what specific fields on this class should be after a reset.
            self.keep_after_reset = {}

        ## Laser ##
    class Laser(Weapon): #starter laser weapon and parent of all other lasers
        def __init__(self):
            Weapon.__init__(self)
            self.damage = 300
            self.energy_use = 100
            self.acc_degradation = 10
            self.base_accuracy = 40
            self.wtype = 'Laser'
            self.name = 'Basic Laser'
            self.lbl = 'Battle UI/button_laser.png'

        def energy_cost(self, parent):
            return int(self.energy_use * parent.energy_cost)

        def fire(self, parent, target, counter = False): #firing lasers!
            target.update_armor()
            if parent.en < self.energy_cost(parent):  #energy handling
                return 'no energy'
            else:
                parent.en -= self.energy_cost(parent)
            accuracy = get_acc(self, parent, target)

            BM.battle_log_insert(['attack', 'laser'], "{0} attacks {1} with laser weapon".format(parent.name, target.name))
                ## actual damage calculation
            total_damage = 0
            store.total_armor_negation = 0
            store.total_shield_negation = 0
            store.total_flak_interception = 0
            store.hit_count = 0

            #cover mechanic. it returns true if cover is hit. see functions.rpy
            if cover_mechanic(self,target,accuracy):
                return 'miss'

            for shot in range(self.shot_count):
                if not get_shot_hit(accuracy,self.shot_count,parent.faction):
                    BM.battle_log_insert(['attack', 'laser', 'detailed'], "<{0}> miss".format(str(shot)))
                else:
                    damage = self.damage * parent.energy_dmg * renpy.random.triangular(0.95,1.05)  #add a little variation in the damage
                    damage = damage * (100 + parent.modifiers['damage'][0] + BM.environment['damage']) / 100.0
                    if target.shields > 0:
                        negation = damage * target.shields / 100.0
                        damage -= negation
                        store.total_shield_negation += int(negation)
                        BM.battle_log_insert(['attack', 'laser', 'detailed'], "<{0}>{1}'s shields negated {2} damage of {3}'s laser attack".format(str(shot), target.name, str(int(negation)), parent.name))

                    if damage <= target.armor:
                        damage = 1
                        store.total_armor_negation += damage
                        BM.battle_log_insert(['attack', 'laser', 'detailed'], "<{0}>{1}'s armour withstood {2}'s laser attack".format(str(shot), target.name, parent.name))
                    else:
                        damage -= target.armor
                        store.total_armor_negation += target.armor
                        BM.battle_log_insert(['attack', 'laser', 'detailed'], "<{0}>{1}'s armour negated {2} damage of {3}'s laser attack".format(str(shot), target.name, target.armor, parent.name))
                    total_damage += int(damage)
                    store.hit_count += 1

            if total_damage > 0:
                BM.battle_log_insert(['attack', 'laser'], "{0}'s shields negated {1} total damage of {2}'s attack".format(target.name, store.total_armor_negation, parent.name))
                BM.battle_log_insert(['attack', 'laser'], "{0}'s armour negated {1} total damage of {2}'s attack".format(target.name, store.total_armor_negation, parent.name))
                return total_damage
            else:
                return 'miss'

        ## GUNZ ##
    class Kinetic(Weapon): #starter Kinetic weapon
        def __init__(self):
            Weapon.__init__(self)
            self.damage = 150
            self.shot_count = 4
            self.energy_use = 50
            self.accuracy = 50
            self.wtype = 'Kinetic'
            self.name = 'Basic Guns'
            self.lbl = 'Battle UI/button_kinetic.png'

        def energy_cost(self, parent):
            return int(self.energy_use * parent.kinetic_cost)

        def fire(self, parent, target, counter = False): #firing gunz!
            target.update_armor()

            if parent.en < self.energy_cost(parent):  #energy handling
                return 'no energy'
            else:
                parent.en -= self.energy_cost(parent)

            BM.battle_log_insert(['attack', 'kinetic'], "{0} attacks {1} with kinetic weapon".format(parent.name, target.name))
            accuracy = get_acc(self, parent, target)
            if accuracy == 0: return 'miss'

            total_damage = 0
            store.hit_count = 0
            store.total_armor_negation = 0
            store.total_shield_negation = 0
            store.total_flak_interception = 0

            #cover mechanic. it returns true if cover is hit. see functions.rpy
            if cover_mechanic(self,target,accuracy):
                return 'miss'

            for shot in range(self.shot_count):
                if not get_shot_hit(accuracy,self.shot_count,parent.faction):
                    BM.battle_log_insert(['attack', 'kinetic', 'detailed'], "<{0}> miss".format(str(shot)))
                else:
                    damage = self.damage * parent.kinetic_dmg * renpy.random.triangular(0.95,1.05)  #add a little variation in the damage
                    damage = damage * (100 + parent.modifiers['damage'][0] + BM.environment['damage']) / 100.0
                    if counter:
                        #when countering, flak buffs give an extra damage bonus.
                        damage = damage * (100+parent.modifiers['flak'][0]) /100.0
                    if damage < target.armor *2:
                        store.total_armor_negation += damage - 1
                    else:
                        store.total_armor_negation += target.armor *2
                    damage -= target.armor * 2
                    if damage <= 1:
                        damage = 1 #it's rpg tradition you still do 1 damage against a big armored enemy :)
                        BM.battle_log_insert(['attack', 'kinetic', 'detailed'], "<{0}>{1}'s armour withstood {2}'s kinetic attack".format(str(shot), target.name, parent.name))
                    else:
                        BM.battle_log_insert(['attack', 'kinetic', 'detailed'], "<{0}>{1}'s armour negated {2} damage of {3}'s kinetic attack".format(str(shot), target.name, target.armor *2, parent.name))
                    total_damage += damage
                    store.hit_count += 1
            if total_damage == 0: return 'miss'
            BM.battle_log_insert(['attack', 'kinetic'], "{0}'s armour negated {1} total damage of {2}'s attack".format(target.name, store.total_armor_negation, parent.name))
            return int(total_damage)

        ## Missiles ##
    class Missile(Weapon): #starter Missile weapon
        def __init__(self):
            Weapon.__init__(self)
            self.damage = 60    #multiplied by shot count
            self.energy_use = 30
            self.uses_missiles = True
            self.ammo_use = 1
            self.accuracy = 60
            self.acc_degradation = 5
            self.wtype = 'Missile'
            self.name = 'Basic Missiles'
            self.type = 'standard'
            self.shot_count = 8
            self.eccm = 0
            self.lbl = 'Battle UI/button_missile.png'
            self.flaklist = []

        def energy_cost(self, parent):
            return int(self.energy_use * parent.missile_cost)

        def fire(self, parent, target, counter = False):
            target.update_armor()
            BM.missiles = []
            wName = "missile"

            if parent.en < self.energy_cost(parent):  #energy handling
                return 'no energy'
            else:
                parent.en -= self.energy_cost(parent)

            if self.uses_missiles:
                if self.ammo_use > parent.missiles:
                    return 'no ammo'
                else:
                    parent.missiles -= self.ammo_use
                    BM.battle_log_insert(['attack', 'missile'], "{0} attacks {1} with missiles".format(parent.name, target.name))
                    wName = "missile"

            if self.uses_rockets:
                if self.ammo_use > parent.rockets:
                    return 'no ammo'
                else:
                    parent.rockets -= self.ammo_use
                    BM.battle_log_insert(['attack', 'missile'], "{0} attacks {1} with rocket".format(parent.name, target.name))
                    wName = "rocket"

            accuracy = get_acc(self, parent, target)
            BM.selectedmode = False
            starting_location = parent.location
            BM.selected = parent
            BM.target = target

            missile = self.simulate(parent,target)
            BM.missile_moving = True

            order_state = BM.order_used

            renpy.hide_screen('battle_screen')
            renpy.show_screen('battle_screen')


            if missile.shot_down != None:
                remaining_wait = missile.shot_down
            else:
                remaining_wait = get_ship_distance(parent,target)*(MISSILE_SPEED)*15 # - target_wait
                remaining_wait = int(remaining_wait)/10.0  #round to 1 decimal
            renpy.pause(remaining_wait)
            BM.missile_moving = False

            renpy.hide_screen('battle_screen')
            renpy.show_screen('battle_screen')

            BM.order_used = order_state

            for ship in BM.ships:
                ship.flak_used = False
                ship.flaksim = None

            if missile == 'miss':
                BM.missiles = []
                return 'miss'
            else:
                pass

            total_damage = 0
            store.hit_count = 0
            store.total_armor_negation = 0
            store.total_shield_negation = 0
            #store.total_flak_interception = 0  # this is applied before it reaches the GUI; we'll let simulate() reset it instead

            #cover mechanic. it returns true if cover is hit. see functions.rpy
            if cover_mechanic(self,target,accuracy):
                return 'miss'

            for shot in range(missile.shot_count):
                if get_shot_hit(accuracy,self.shot_count,parent.faction):
                    damage = self.damage * parent.missile_dmg * renpy.random.triangular(0.95,1.05)  #add a little variation in the damage
                    damage = damage * (100 + parent.modifiers['damage'][0] + BM.environment['damage']) / 100.0
                    damage -= target.armor
                    store.total_armor_negation += target.armor
                    if damage <= 1:
                        damage = 1
                        BM.battle_log_insert(['attack', 'missile', 'detailed'], "<{0}> {1}'s armour withstood {2}'s {3}".format(str(shot), target.name, parent.name, wName))
                    else:
                        BM.battle_log_insert(['attack', 'missile', 'detailed'], "<{0}> {1}'s armour negated {2} damage of {3}'s {4}".format(str(shot), target.name, target.armor, parent.name, wName))
                    total_damage += damage
                    store.hit_count += 1
                else:
                    BM.battle_log_insert(['attack', 'missile', 'detailed'], "<{0}> miss".format(str(shot)))

            BM.missiles = []
            if total_damage == 0: return 'miss'
            BM.battle_log_insert(['attack', 'missile'], "{0}'s armour negated {1} total damage of {2}'s attack".format(target.name, store.total_armor_negation, parent.name))
            return int(total_damage)

        def simulate(self,parent,target):
            """simulate the path the missile takes on it's way to the target.
            the missile takes a tiny step every part of the main while loop and scans
            for enemy ships in range that have a flak greater than zero. when it finds one
            it runs the flak_intercept() method part of the MissileSprite class. the result is stored in
            the flaksim field on enemy units and is later used to show how many missiles
            got intercepted and when"""
            store.total_flak_interception = 0
            missile = MissileSprite(parent,target,self)
            BM.missiles.append(missile)
            path = interpolate_hex(parent.location,target.location) #get a list of locations between parent and target

            #store how much time has passed since the missile was launched. used to time the flak icon etc
            time = 0.5

            for ship in BM.ships:
                ship.flak_used = False

            for hex in path:
                for ship in BM.ships:
                    if ship.location is not None and not ship.flak_used:
                        if ship.faction != missile.parent.faction:
                            if missile.parent.faction != 'Player' and ship.faction != 'Player':
                                continue
                            if get_distance(hex,ship.location) <= ship.flak_range:
                                effective_flak = ship.flak + ship.modifiers['flak'][0]
                                if effective_flak > 100: effective_flak = 100
                                elif effective_flak < 0: effective_flak = 0

                                if effective_flak > 0:
                                    ship.flaksim = None
                                    ship.flaksim = (time,missile.flak_intercept(ship))
                                    if missile.shot_count == 0:
                                        missile.shot_down = time + MISSILE_SPEED
                                        for ship in BM.ships:
                                            ship.flak_used = False
                                        return missile

                time += MISSILE_SPEED

            for ship in BM.ships:
                ship.flak_used = False
            return missile

          ##this class is the missile shown on screen when missiles are fired##
    class MissileSprite(store.object):
        def __init__(self,parent,target,weapon):
            self.location = parent.location
            self.parent = parent
            self.target = target
            a = (parent.location[0] - target.location[0])*192
            b = (parent.location[1] - target.location[1])*120
              #calculate the angle between the attacker and the target
            self.angle = math.degrees(math.atan2(a,b))
            self.damage = weapon.damage
            self.shot_count = weapon.shot_count
            self.type = weapon.wtype
            if self.type == 'Missile':
                self.lbl = im.Rotozoom('Battle UI/map missile.png',self.angle,1.0)
            else:
                self.lbl = im.Rotozoom('Battle UI/map rocket.png',self.angle,1.0)
            self.eccm = parent.missile_eccm + weapon.eccm
            self.flak_degradation = 0.02  #this is how much flak effectiveness gets reduced by each missile
            self.next_location = None
            self.shot_down = None

        def flak_intercept(self,interceptor):
            shots_remaining = self.shot_count
            interceptor.flak_used = True
            effective_flak = (interceptor.flak-self.eccm)*interceptor.flak_effectiveness/100.0

            if effective_flak > 0:
                for shot in range(self.shot_count):
                    if renpy.random.randint(0,100) <= effective_flak:
                        shots_remaining -= 1
            shot_down = 0
            if self.shot_count > shots_remaining:
                shot_down = self.shot_count - shots_remaining
            interceptor.flak_effectiveness *= 1.0 - (self.shot_count * self.flak_degradation)
            if interceptor.flak_effectiveness < 33: interceptor.flak_effectiveness = 33
            self.shot_count = shots_remaining

            store.total_flak_interception += shot_down

            return shot_down

    class Melee(Weapon):
        def __init__(self):
            Weapon.__init__(self)
            self.damage = 400    #multiplied by shot count
            self.energy_use = 50
            self.ammo_use = 1
            self.max_range = 1
            self.accuracy = 140
            self.acc_degradation = 100
            self.wtype = 'Melee'
            self.name = 'Zantetsuken'  #lol
            self.type = 'Melee'
            self.shot_count = 1
            self.lbl = 'Battle UI/button_melee.png'

        def energy_cost(self, parent):
            return int(self.energy_use * parent.melee_cost)

        def fire(self, parent, target, counter = False):
            target.update_armor()

            #don't really want to fix this yet :D
            # if target.stype != 'Ryder':
                # return 0

            energy_cost = int(self.energy_use * parent.melee_cost)
            if parent.en < energy_cost:  #energy handling
                return 'no energy'
            else:
                parent.en -= energy_cost

            BM.battle_log_insert(['attack', 'melee'], "{0} attacks {1} melee".format(parent.name, target.name))
            accuracy = get_acc(self, parent, target)
            if accuracy == 0: return 'miss'
            total_damage = 0
            store.hit_count = 0
            store.total_armor_negation = 0
            store.total_shield_negation = 0
            store.total_flak_interception = 0
            for shot in range(self.shot_count):
                if not get_shot_hit(accuracy,self.shot_count,parent.faction):
                    BM.battle_log_insert(['attack', 'melee', 'detailed'], "<{0}> miss".format(str(shot)))
                else:
                    damage = self.damage * parent.melee_dmg * renpy.random.triangular(0.95,1.05)  #add a little variation in the damage
                    damage = damage * (100 + parent.modifiers['damage'][0] + BM.environment['damage']) / 100.0
                    if damage < target.armor *2:
                        store.total_armor_negation += damage -1
                    else:
                        store.total_armor_negation += target.armor *2
                    damage -= target.armor * 2
                    if damage <= 1:
                        damage = 1 #it's rpg tradition you still do 1 damage against a big armored enemy :)
                        BM.battle_log_insert(['attack', 'melee', 'detailed'], "<{0}>{1}'s armour withstood {2}'s melee attack".format(str(shot), target.name, parent.name))
                    else:
                        BM.battle_log_insert(['attack', 'melee', 'detailed'], "<{0}>{1}'s armour negated {2} damage of {3}'s melee attack".format(str(shot), target.name, target.armor * 2, parent.name))
                    total_damage += damage
                    store.hit_count += 1
            if total_damage == 0: return 'miss'
            BM.battle_log_insert(['attack', 'melee'], "{0}'s armour negated {1} total damage of {2}'s melee attack".format(target.name, store.total_armor_negation, parent.name))
            return int(total_damage)

    class Support(store.object):
        def __init__(self):
            self.repair = False
            self.self_buff = False #if true this skill automatically casts on self only
            self.damage = 0 #also used to repair
            self.uses_missiles = False
            self.uses_rockets = False
            self.max_range = None
            self.base_accuracy = 50
            self.energy_use = 60
            self.hp_cost = 0
            self.wtype = 'Support'
            self.end_of_turn_callback = None
            self.keep_after_reset = {} #used by save compat code.
            self.cumulative = False  #if true it does not overwrite but add to the current value.
            self.modifies = '' #what modifier key will it affect. e.g. 'accuracy'
            self.buff_strength = 0 #how many points does it increase a stat?
            self.buff_duration = 1

            #effective range is 3 cells away and always hits
            self.accuracy = 350
            self.acc_degradation = 100

            self.name = 'Empty Support Skill'
            self.shot_count = 1
            self.lbl = ''

        def fire(self,parent,target,counter = False,hidden=False):

            #handle callbacks
            if self.end_of_turn_callback is not None:
                if self.end_of_turn_callback not in BM.end_turn_callbacks:
                    BM.end_turn_callbacks.append(self.end_of_turn_callback)

            #energy  management
            if parent.en < self.energy_use:
                return 'no energy'
            else:
                parent.en -= self.energy_use
                #pretty much only relevant for awakaning skills
                if self.hp_cost:
                    parent.hp -= self.hp_cost
                    if parent.hp < 1: parent.hp = 1

            if self.self_buff:
                target = parent

            #if this is a healing skill
            if self.repair:
                healing = int(self.damage * renpy.random.triangular(0.8,1.2) )
                if self.wtype == 'Support':
                    target.getting_buff = True
                else:
                    target.getting_curse = True
                BM.selectedmode = False
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                if not target == parent and target.faction == 'Player':
                    a = renpy.random.randint(0,len(target.buffed_voice)-1)
                    renpy.music.play('sound/Voice/{}'.format(target.buffed_voice[a]),channel = target.voice_channel)
                    del a
                renpy.invoke_in_new_context( short_pause )
                target.getting_buff = False
                target.getting_curse = False
                if BM.phase == 'Player':
                    BM.selectedmode = True
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                if parent is target:
                    #heal itself
                    BM.battle_log_insert(['support', 'heal'], "{0} heals {1} HP".format(parent.name, str(int(healing))))
                else:
                    BM.battle_log_insert(['support', 'heal'], "{0} heals {1} for {2} HP".format(parent.name, target.name, str(int(healing))))

                #time to hear the lamentations of the women.
                parent.hate += healing / 5

                return healing

            elif self.modifies == 'restore':
                successful = False
                if parent is target:
                    BM.battle_log_insert(['support', 'debuff'], "{0} performs self-restoration".format(parent.name))
                else:
                    BM.battle_log_insert(['support', 'debuff'], "{0} attempts to restore {1}".format(parent.name, target.name))
                for modifier in target.modifiers:
                    if target.modifiers[modifier][0] < 0: #a modifier lower than 0 is assumed to be a curse
                        successful = True
                        BM.battle_log_insert(['support', 'debuff'], "{0} is healed from curse to its {1}".format(target.name, modifier.replace('_', ' ')))
                        target.modifiers[modifier] = [0,0]

                if not successful:
                    #there were no curses to remove
                    message = "No curses to remove from {0}".format(target.name)
                    BM.battle_log_insert(['support', 'debuff'], message)
                    show_message(message)
                    parent.en += self.energy_use
                    parent.hp += self.hp_cost
                    return 0

                else:
                    if not hidden:
                        target.getting_buff = True
                        BM.selectedmode = False
                        renpy.hide_screen('battle_screen')
                        renpy.show_screen('battle_screen')
                        if BM.phase == 'Player':
                            if not target == parent and target.faction == 'Player':
                                renpy.music.play( 'sound/Voice/{}'.format( renpy.random.choice(target.buffed_voice) ),channel = target.voice_channel )
                        message = "All curses were removed from the {}".format(target.name)
                        BM.battle_log_insert(['support', 'debuff'], message)
                        show_message(message)
                        target.getting_buff = False
                        if BM.phase == 'Player':
                            BM.selectedmode = True
                        renpy.hide_screen('battle_screen')
                        renpy.show_screen('battle_screen')
                    return 0

            #if it's a buff/curse
            else:

                #I should replace this with proper immunity flagging.
                if self.name == 'Disable' and target.name == 'Legion':
                    show_message( "The Legion is immune!" )
                    parent.en += self.energy_use
                    return 0

                successful = False
                if parent is target:
                    # let's hope that we cannot use self-debuff....
                    target.getting_buff = True
                    log_tags = ['support', 'buff']
                    BM.battle_log_insert(log_tags, "{0} uses {1}".format(parent.name, self.name))
                else:
                    if self.wtype == 'Support':
                        target.getting_buff = True
                        log_tags = ['support', 'buff']
                        BM.battle_log_insert(log_tags, "{0} uses {1} on {2}".format(parent.name, self.name, target.name))
                    else:
                        target.getting_curse = True
                        log_tags = ['support', 'debuff']
                        BM.battle_log_insert(log_tags, "{0} uses {1} on {2}".format(parent.name, self.name, target.name))
                if hasattr(self.modifies,"__iter__"):  #this checks is the var is an iterable (like a list). if it's not it should be a string.
                    for modifier in self.modifies:
                        if apply_modifier(target,modifier,self.buff_strength,self.buff_duration,self.cumulative): successful = True
                else:
                    if apply_modifier(target,self.modifies,self.buff_strength,self.buff_duration,self.cumulative): successful = True

                if not successful:
                    #wasted
                    message = "A stronger or similar effect is already present on {0}".format(target.name)
                    BM.battle_log_insert(log_tags, message)
                    show_message(message)
                    target.getting_buff = False
                    target.getting_curse = False
                    return 0

                update_stats()
                if target.getting_buff:
                    BM.battle_log_insert(['support', 'buff'], "{0} is buffed with {1}".format(target.name, self.name))
                else:
                    BM.battle_log_insert(['support', 'debuff'], "{0} is cursed with {1}".format(target.name, self.name))
                if not hidden:
                    BM.selectedmode = False
                    renpy.hide_screen('battle_screen')
                    renpy.show_screen('battle_screen')
                    if BM.phase == 'Player':
                        if not target == parent and target.faction == 'Player':
                            #this is what happens if you don't know about random.choice and you then can't be arsed to fix it everywhere
                            a = renpy.random.randint(0,len(target.buffed_voice)-1)
                            renpy.music.play('sound/Voice/{}'.format(target.buffed_voice[a]),channel = target.voice_channel)
                            del a
                        elif target.faction != 'Player':
                            if hasattr(parent,'cursing_voice'):
                                if len(parent.cursing_voice) > 0:
                                    renpy.music.play( 'sound/Voice/'+renpy.random.choice(parent.cursing_voice),channel=parent.voice_channel )
                    else:
                        #enemy turn
                        if target.faction == 'Player':
                            if hasattr(target,'cursed_voice'):
                                if len(target.cursed_voice) > 0:
                                    renpy.music.play( 'sound/Voice/'+renpy.random.choice(target.cursed_voice),channel=target.voice_channel )
                    renpy.invoke_in_new_context( short_pause )
                    if BM.phase == 'Player':
                        BM.selectedmode = True
                    renpy.hide_screen('battle_screen')
                    renpy.show_screen('battle_screen')
                target.getting_buff = False
                target.getting_curse = False

                if self.name == 'Disable':  #I should probably put stuff like this in the library at some point
                    parent.hate += 250

                return 0

        def energy_cost(self, parent):
            return int(self.energy_use)

    class Curse(Support):
        def __init__(self):
            Support.__init__(self)
            self.wtype = 'Curse'
            self.sort_on = 'pship.hate' #not used anymore. may be useful later though.

    class GravityGun(store.object):
        def __init__(self):
            self.repair = False
            self.self_buff = False #if true this skill automatically casts on self only
            self.damage = 0 #also used to repair
            self.uses_missiles = False
            self.uses_rockets = False
            self.max_range = None
            self.base_accuracy = 50
            self.energy_use = 60
            self.hp_cost = 0
            self.wtype = 'Special'
            self.modifies = '' #what modifier key will it affect. e.g. 'accuracy'
            self.buff_strength = 0 #how many points does it increase a stat?
            self.buff_duration = 1
            self.keep_after_reset = {} #used by save compatibility code
            self.tooltip = """
            Allows Claude to move any Ryder a single hex.
            This movement will provoke Blindside attacks, if you move an enemy Ryder
            into the range of a friendly unit with an Assault type weapon.
            Has unlimited range."""

            #always hits
            self.accuracy = 9999
            self.acc_degradation = 0

            self.name = 'Gravity Gun'
            self.shot_count = 1
            self.lbl = 'Battle UI/button_gravity.png'

        def fire(self,parent,target,counter=False):

            #only works on ryders
            if target.stype != 'Ryder':
                show_message('you can only use this ability on ryders!')
                return

            #energy handeling
            if parent.en < self.energy_use:
                return
            parent.en -= self.energy_use

            #make movement buttons appear
            BM.selectedmode = True

            #store the target's faction and weapons and EN value
            target_faction = target.faction
            target_weapons = target.weapons
            target_en = target.en

            #set the target up for the player to move it one space
            target.faction = 'Player'
            target.weapons = []
            target.en = target.move_cost
            BM.select_ship(target, play_voice = False)
            #show movement tiles around the target for 1 hex away
            target.movement_tiles = get_movement_tiles(target,1)

            #set up the loop
            looping = True
            cancel = False
            BM.weaponhover = None

            #movement loop
            while looping:
                result = ui.interact()

                # player clicked a spot to move to
                if result[0] == 'move':
                    #if we don't reset the faction now enemies will counter attack their own allies!
                    target.faction = target_faction
                    target.move_ship(result[1],BM) #result[1] is the new location to move towards
                    BM.battle_log_insert(['support'], "{0} used Gravity Gun on {1}".format(parent.name, target.name))
                    looping = False

                # player clicked the right mouse button
                if result[0] == 'deselect':
                    cancel = True
                    looping = False

            if cancel:
                #refund the energy cost of the gravity gun as the target never moved
                parent.en += self.energy_use

            #hand the target over back to the enemy (if applicable) and reset their weapons and energy.
            target.faction = target_faction
            target.weapons = target_weapons
            target.en = target_en

            #select the parent again (usually the bianca)
            BM.select_ship(parent, play_voice = False)
            #update the movement tiles as the target could now be blocking a spot the parent could have moved to before.
            parent.movement_tiles = get_movement_tiles(parent)
            #cancelling the movement just leads to annoying problem
            BM.just_moved = False
            return

        def energy_cost(self,parent):
            return self.energy_use

    class Cover(store.object):
        def __init__(self,location = (1,1)):
            self.location = location
            self.cover_chance = 50 #percentage chance of blocking an incoming attack
            self.max_hp = 500
            self.hp = self.max_hp
            self.label = 'Battle UI/asteroid cover.png'
            self.angle = renpy.random.randint(1,360)

        def receive_damage(self,damage):
            self.hp -= damage
            if self.hp <=0: self.destroy()

        def destroy(self):
            if self in BM.covers:
                BM.covers.remove(self)
                show_message('The asteroid was destroyed!')
                renpy.pause(0.5)

         ### WEAPONFIRE PARTICLE GENERATOR ###
    class FlakShield(object): #created for us by RenpyTom! thanks man!

        def __init__(self, d, generators, speed, angle=135, interval=0.05, dispersion=0):

            # The displayable we use.
            self.d = Transform(d, rotate=angle-90)
            # Are we running?
            self.running = True
            # A list of bullets that are in the air at
            # the moment.
            self.bullets = [ ]
            # The time the next bullets should be shot at.
            self.next_shot = None
            # The interval between shots.
            self.interval = interval
            # The locations of flak generators as (x, y) tuples.
            self.generators = generators
            # The angle bullets appear at.
            self.angle = angle
            # The dispersion between bullet angles.
            self.dispersion = dispersion
            # The speed of a bullet.
            self.speed = speed
            # The sprite manager.
            self.manager = SpriteManager(self.update)

        def update(self, st):
            if self.next_shot is None:
                self.next_shot = st
            if self.next_shot < st - 10 * self.interval:
                self.next_shot = st - 10 * self.interval

            # Generate shots.
            while self.next_shot <= st:
                if self.running:
                    for startx, starty in self.generators:
                            angle = (self.angle + renpy.random.uniform(-self.dispersion, self.dispersion)) / 180.0 * math.pi
                            xdt = 1.0 * self.speed * math.sin(angle)
                            ydt = 1.0 * self.speed * -math.cos(angle)
                            sprite = self.manager.create(self.d)
                            self.bullets.append((
                                self.next_shot,
                                startx,
                                starty,
                                xdt,
                                ydt,
                                sprite))
                self.next_shot += self.interval

            new_bullets = [ ]
            for b in self.bullets:
                startt, startx, starty, xdt, ydt, sprite = b
                t = st - startt
                sprite.x = startx + xdt * t
                sprite.y = starty + ydt * t
                if sprite.x < 0 or sprite.x > self.manager.width:
                    sprite.destroy()
                    continue
                if sprite.y < 0 or sprite.y > self.manager.height:
                    sprite.destroy()
                    continue
                new_bullets.append(b)

            self.bullets = new_bullets
            return 0

        def show(self):
            ui.layer('master')
            ui.add(self.manager)
            ui.close()

        def hide(self):
            ui.layer('master')
            ui.remove(self.manager)
            ui.close()

        def start(self):
            """
            Starts shooting flak.
            """
            self.running = True

        def stop(self):
            """
            Stops shooting flak.
            """
            self.running = False

    class Planet(store.object):
        def __init__(self, name, jumpLocation, xPos, yPos, showOnMapCondition):
            self.name = name
            self.jumpLocation = jumpLocation
            self.xPos = xPos
            self.yPos = yPos
            self.showOnMapCondition = showOnMapCondition
            if self not in planets:
                planets.append(self)

        def shouldShowOnMap(self):
        # showOnMapCondition is evaluated as a python expression.
        # the variable can contain something like "not bool" or "bool == False"
        # and it will be evaluated. This makes it perfect in the event that you
        # have multiple conditions that need to be true
            return eval(self.showOnMapCondition)

        def __eq__(self, other):
            if isinstance(self, other.__class__):
                if self.name == other.name and self.jumpLocation == other.jumpLocation and self.xPos == other.xPos and self.yPos == other.yPos and self.showOnMapCondition == other.showOnMapCondition:
                    return True
            return False

    class BonusItem(store.object):
        def __init__(self, image, text, jumpLoc, zoom):
            self.image = image
            self.text = text
            self.jumpLoc = jumpLoc
            self.zoom = zoom

    class Chapter(BonusItem, Action):
        def __init__(self, image, text, jumpLoc, zoom, startMoney = 0, lastMission = -1):
            self.image = image
            self.text = text
            self.jumpLoc = jumpLoc
            self.zoom = zoom
            self.startMoney = startMoney
            self.lastMission = lastMission

        def __call__(self):

            add_new_vars() #this actually should cover most of what you need...
            store.BM = Battle()
            store.MasterBM = store.BM
            store.BM.money = self.startMoney
            store.BM.cmd = self.lastMission * 1000
            if store.BM.cmd > 4000: store.BM.cmd = 4000  #you gain a lot over the course of the game but you typically spend a lot too.
            store.player_ships = []
            store.enemy_ships = []
            store.sunrider = None
            store.blackjack = None
            store.liberty = None
            store.phoenix = None
            store.bianca = None
            store.seraphim = None
            store.paladin = None
            store.havoc = None
            store.paradigm = None

            store.check1 = False
            store.check2 = False
            store.check3 = False
            store.check4 = False
            store.check5 = False
            store.check6 = False
            store.check7 = False
            store.check8 = False
            store.check9 = False

            store.captain_moralist = 0
            store.captain_prince = 0
            store.affection_ava = 0
            store.affection_asaga = 0
            store.affection_chigara = 0
            store.affection_icari = 0
            store.affection_claude = 0
            store.affection_tera = 0
            store.affection_sola = 0
            store.affection_cosette = 0

            store.MetAsaga = False
            store.ChigaraNamed = False
            store.ChigaraRefugee = False
            store.mission_pirateattack = False
            store.amissionforalliance = False
            store.missionforryuvia = False
            store.OngessTruth = False

            store.battlemusic = True

            store.galaxymission1 = False
            store.galaxymission2 = False
            store.galaxymission3 = False
            store.mission1 = None
            store.mission2 = None
            store.mission3 = None
            store.mission1_name = None
            store.mission2_name = None
            store.mission3_name = None

            for count in range(self.lastMission):
                setattr(store,'mission{}_complete'.format(count+1),True)

            store.mission4_complete = False
            store.mission7_complete = False

            store.ava_location = None
            store.asa_location = None
            store.chi_location = None
            store.pro_location = None
            store.gal_location = None
            store.cal_location = None
            store.res_location = None
            store.ica_location = None
            store.sol_location = None
            store.cla_location = None
            store.cos_location = None
            store.kry_location = None

            store.ava_event = None
            store.asa_event = None
            store.chi_event = None
            store.pro_event = None
            store.gal_event = 'jumptogalaxy'
            store.cal_event = 'ftltransponder'
            store.res_event = 'allocatefunds'
            store.ica_event = None
            store.sol_event = None
            store.cla_event = None
            store.cos_event = None
            store.kry_event = None

            store.warpto_occupiedcera = self.lastMission >= 1
            store.warpto_tydaria = self.lastMission >= 1
            store.warpto_astralexpanse = self.lastMission >= 2
            store.warpto_pactstation1 = self.lastMission >= 3
            store.warpto_versta = self.lastMission >= 5
            store.warpto_nomodorn = self.lastMission >= 8
            store.warpto_ryuvia = self.lastMission >= 10
            store.warpto_farport = self.lastMission >= 12
            store.warpto_ongess = self.lastMission >= 13 #not sure

            store.ep2_cancelwarp = False

            store.supportedasagacards = False
            store.Saveddiplomats = self.lastMission >= 8
            store.protectmochi = False

            ##new constants##

            TURN_SPEED = 0.75 #in seconds
            MOVE_IN_SPEED = 0.5 #for buttons and status displays
            MOVE_OUT_SPEED = 0.5
            MESSAGE_PAUSE = 0.75
            MISSILE_SPEED = 0.3
            SHIP_SPEED = 0.3
            ZOOM_SPEED = 0.1
            GRID_SIZE = (18,16) #(X,Y) aka (width,height)
            AI_WAIT_TIME = 0.5  #time in between highlighting an enemy unit and executing its action
            HEXW = 192   #width of hexagon (3.0 ** .5)/2.0 * HEXH
            HEXH = 222   #height of hexagon
            HEXD = 167   #vertical distance between hexagons (3/4) * HEXH
            SLIDEY = 0   #vertical offset .5 * HEXH
            SLIDEX = 96  #horixontal offset .5 * HEXW
            ADJY = 120.0/HEXD  #needed to make sure the displayables stay in the right place
            ADJX = 1.0   #192.0/HEXW
            MOVY = 60    #used to offset the displayables
            MOVX = 0

            store.all_enemies = [
                PactBomber(),  PactMook(),
                MissileFrigate(), PactCruiser(),
                PactCarrier(), PactOutpost(),
                PactBattleship(),RyuvianCruiser(),
                Havoc(), PirateBomber(),
                PirateGrunt(), PirateDestroyer(),
                PirateBase(),
                ]
            for ship in all_enemies:
                ship.location = None

            if self.lastMission >= 3:
                store.liberty_weapons = [LibertyLaser(),Repair(),AccUp(),Disable(),FlakOff(),ShutOff()]
                store.liberty = create_ship(Liberty(),None,store.liberty_weapons)

            if self.lastMission >= 9:
                store.bianca_weapons = [BiancaAssault(),GravityGun(),AccDown(),DamageUp(),Restore()]
                store.bianca = create_ship(Bianca(),None,store.bianca_weapons)

            if self.lastMission >= 10:
                store.seraphim_weapons = [SeraphimKinetic(),Awaken()]
                store.seraphim = create_ship(Seraphim(),(6,8),store.seraphim_weapons)

            for num in range(0, self.lastMission):
                renpy.call_in_new_context('mission' + str(num + 1) + '_inits')

            if self.lastMission >= 3:
                store.sunrider.register_weapon(SunriderPulse())
                store.cal_location = 'captainsloft'

            if self.lastMission >= 6:
                store.res_location = 'lab'

            if hasattr(store,'agamemnon'):
                if agamemnon in player_ships: player_ships.remove(agamemnon)

            if hasattr(store,'mochi'):
                if mochi in player_ships: player_ships.remove(mochi)

            if self.lastMission >= 10:
                if blackjack not in player_ships:
                    store.player_ships.append(store.blackjack)

            if self.lastMission >= 10:
                store.sunrider.repair_drones = 0

            if self.lastMission >= 11:
                BM.orders['SHORT RANGE WARP'] = [750,'short_range_warp']

            clean_grid() #cleans BM.grid, BM.ships, BM.covers and store.enemy_ships
            renpy.jump_out_of_context(self.jumpLoc)

    class StoreItem(store.object):
        """master class of all store objects
        the actual items are defined in the library"""
        def __init__(self):
            self.id = ''                 #unique name for this item
            self.visibility_condition = 'True' #when is this item visible in store?
            self.display_name = 'master item' #how it appears in the store
            self.cost = 0                #cost of this item
            self.tooltip = ''            #text explaining what this item does
            self.variable_name = None    #[string or None] what variable keeps track of how many of this item the player has?
            self.max_amt = 0             #maximum allowed of this item. irrelevant if self.amount_variable == None

            # if self not in store_items:
                # store_items.append(self)

        def __call__(self):
            self.buy()
            BM.money -= self.cost
            renpy.restart_interaction()

        def buy(self):
            #needs to be overwritten
            pass

        def isVisible(self):
            return eval(self.visibility_condition)

    ## CUSTOM ACTIONS ##
    class BonusPageNext(Action):
        def __init__(self):
            self.page = store.bonusPage + 1

        def __call__(self):
            if not self.get_sensitive():
                return

            store.bonusPage = self.page
            renpy.restart_interaction()

        def get_sensitive(self):
            return self.page is not None

    class BonusPagePrevious(Action):
        def __init__(self):
            self.page = store.bonusPage - 1
            if self.page < 0:
                self.page = 0

        def __call__(self):
            if not self.get_sensitive():
                return

            store.bonusPage = self.page
            renpy.restart_interaction()

        def get_sensitive(self):
            return store.bonusPage

    class ResetBonusPage(Action):
        def __call__(self):
            store.bonusPage = 0
            renpy.restart_interaction()

    class CreateShipAction(Action):
        def __init__(self, ship, weapons, location = None):
            self.ship = ship
            self.weapons = weapons
            self.location = location

        def __call__(self):
            #deepcopy is used to break aliasing (we don't want to add the same ship x times)
            create_ship(deepcopy(self.ship), self.location, self.weapons)

    class HoverWeapon(Action):
        def __init__(self, weapon):
            self.weapon = weapon

        def __call__(self):
            BM.weaponhover = self.weapon

            #wtype:'Support' targets only allies, wtype:'Special' targets everyone
            if BM.weaponhover.wtype == 'Support' or BM.weaponhover.wtype == 'Special':
                for ship in player_ships:
                    ship.cth = get_acc(BM.weaponhover, BM.selected, ship)
            else:
                ignore_evasion = False
                if BM.weaponhover.wtype == 'Curse' or BM.weaponhover.wtype == 'Special':
                    ignore_evasion = True

                for ship in enemy_ships:
                    ship.cth = get_acc(BM.weaponhover, BM.selected, ship, ignore_evasion)

            renpy.restart_interaction()

    class FireWeapon(Action):
        def __init__(self, weapon):
            self.weapon = weapon

        def __call__(self):
            BM.weaponhover = None
            if self.weapon.wtype == 'Support':
                if self.weapon.self_buff:
                    self.weapon.fire(BM.selected,BM.selected)
                    update_stats()
                    BM.selected.movement_tiles = get_movement_tiles(BM.selected)

                    renpy.restart_interaction()
                    return

            BM.targetingmode = True   #displays targeting info over enemy_ships
            BM.active_weapon = self.weapon
            BM.weaponhover = BM.active_weapon
            ignore_evasion = False

            #the hover thing is not 100% trustworthy so we calculate CTH again based on the selected weapon
            if BM.weaponhover.wtype == 'Curse':
                ignore_evasion = True
            for ship in enemy_ships:
                ship.cth = get_acc(self.weapon, BM.selected, ship, ignore_evasion)

            update_stats()

            renpy.restart_interaction()

    class ZoomAction(Action):
        def __init__(self,direction):
            self.direction = direction

        def __call__(self):
            zoom_handling(self.direction,BM)
            if BM.selectedmode: BM.selected.movement_tiles = get_movement_tiles(BM.selected)
            renpy.restart_interaction()

    class RestartInteraction(Action):
        def __init__(self):
            Action.__init__(self)

        def __call__(self):
            renpy.restart_interaction()
