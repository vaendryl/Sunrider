#in this file all the functions and classes related to AI are collected.

init python:
    import itertools #mess around with iterables (like lists)
    import heapq #This module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.

    class AI(renpy.store.object):
        """parent AI class"""
        def __init__(self,parent):
            self.parent = parent
            self.enemy_faction = ['Player'] #not used yet.
            self.preferred_distance = 0
            #the higher the less likely the unit is to approach kinetic users.
            self.kinetic_fear = 0.75

        def AI_estimate_damage(self):
            raise NotImplementedError

        def AI_attack_target(self):
            raise NotImplementedError

        def AI_basic_loop(self):
            raise NotImplementedError

        def AI_move_towards(self):
            raise NotImplementedError

        def AI(self):
            raise NotImplementedError

    class DefaultAI(AI):
        def __init__(self,parent):
            AI.__init__(self,parent)

        def AI_estimate_damage(self,pship,en = 0, range_reduction = 0):
            """this gets called on every possible target ship. it cycles through all the available
            weapons and sets the field 'damage_estimation' on the target ship with [WEAPON,ESTIMATED DAMAGE,PRIORITY] which
            then gets used by the rest of the AI"""
            parent = self.parent
            #the higher this number, the greater the effect hate has.
            priority_modifier = 1.5
            #quit when out of energy
            if en == 0: en = parent.en
            #init our result
            pship.damage_estimation = [None,0,0] #weapon,estimation,priority
            #failsafe
            if pship.hp < 1:
                return

            #cycle through all the weapons and find out which one is likely to be most
            #effective for each player ship
            for weapon in parent.weapons:
                #ignore this weapon if it's too expensive.
                if parent.en < weapon.energy_cost(parent):
                    continue
                else:
                    #get the accuracy for this weapon on this target. guess=True
                    accuracy = get_acc(weapon,parent,pship,True, range_reduction)

                    #check weapon type of this weapon and calculate how much damage this would do on this target.
                    ##KINETICS
                    if weapon.wtype == 'Kinetic' or weapon.wtype == 'Assault':
                        estimation = (weapon.damage-pship.armor*2)*weapon.shot_count*accuracy / 100.0
                        priority = int(estimation * (1 + (pship.hate/100.0)**priority_modifier/10))
                        #renpy.log('I estimate that {} would do {!s} damage on {}'.format(weapon.name,int(estimation),pship.name))
                        #renpy.log('based on hate I give this ship a priority of {}'.format(priority))
                        #if the priority on this combination is higher than the current best, replace it.
                        if pship.damage_estimation[2] < priority:
                            pship.damage_estimation = [weapon,int(estimation),priority]

                    ##MISSILES
                    if weapon.wtype == 'Missile' or weapon.wtype == 'Rocket':
                        #missiles use ammo so this needs to be checked.
                        if weapon.uses_missiles and parent.missiles <= 0:
                            return
                        elif weapon.uses_rockets and parent.rockets <= 0:
                            return
                        else:
                            estimation = (weapon.damage-pship.armor)*weapon.shot_count*accuracy / 100.0
                            estimation = estimation * estimate_flak(parent,pship)
                            priority = int(estimation * (1 + (pship.hate/100.0)**priority_modifier/10))
                            #renpy.log('I estimate that {} would do {!s} damage on {}'.format(weapon.name,int(estimation),pship.name))
                            #renpy.log('based on hate I give this ship a priority of {}'.format(priority))
                            if pship.damage_estimation[2] < priority:
                                pship.damage_estimation = [weapon,int(estimation),priority]

                    ##ENERGY
                    if weapon.wtype == 'Laser' or weapon.wtype == 'Pulse':
                        estimation = (weapon.damage-pship.armor)*weapon.shot_count*accuracy / 100.0
                        estimation = estimation * (100 - pship.shields) / 100.0
                        priority = int(estimation * (1 + (pship.hate/100.0)**priority_modifier/10))
                        #renpy.log('I estimate that {} would do {!s} damage on {}'.format(weapon.name,int(estimation),pship.name))
                        #renpy.log('based on hate I give this ship a priority of {}'.format(priority))
                        if pship.damage_estimation[2] < priority:
                            pship.damage_estimation = [weapon,int(estimation),priority]

                    ##MELEE
                    if weapon.wtype == 'Melee':
                        estimation = estimate_melee_damage(parent,weapon,pship) if pship.stype == 'Ryder' else 0
                        priority = int(estimation * (1 + (pship.hate/100.0)**priority_modifier/10))
                        #renpy.log('I estimate that {} would do {!s} damage on {}'.format(weapon.name,int(estimation),pship.name))
                        #renpy.log('based on hate I give this ship a priority of {}'.format(priority))
                        if pship.damage_estimation[2] < priority:
                            pship.damage_estimation = [weapon,int(estimation),priority]

            # if pship.damage_estimation[0] == None:
                # debuglog_add( 'all weapons can do no damage on the {}'.format(pship.name) )
            # else:
                # debuglog_add('{} has the highest damage({!s}) on the {} with a priority of {!s}'.format(pship.damage_estimation[0].name,pship.damage_estimation[1],pship.name,pship.damage_estimation[2]))

#AI attacks
        def AI_attack_target(self,pship,weapon,counter=False):
            """instruct this ship to attack another ship with a specific weapon. it will do
            further checks to see if it can or should move closer. finally, it shows the attacking
            animation, gets the damage done and passes it through the target which handles things further"""
            parent = self.parent
            update_stats()

            #if the the weapon type is melee the ship may need to close in
            if weapon.wtype == 'Melee':
                if get_ship_distance(parent,pship) > 1:
                    debuglog_add('adjusting position for melee')
                    if parent.melee_location is None:
                        parent.AI_move_towards(pship,max_move_distance=1)
                    else:
                        parent.move_ship(parent.melee_location,BM)
                        parent.melee_location = None

            #maybe we want to get closer. first we need the current accuracy
            accuracy = get_acc(weapon,parent,pship,guess=True)
            debuglog_add('using {} on {}. accuracy is {}'.format(weapon.name, pship.name, accuracy))

            #calculate how far you can move and -still- use the weapon
            max_advance_distance = (parent.en - weapon.energy_cost(parent)) / parent.move_cost
            if max_advance_distance > 0:

                #if less than 75% try to move as much as possible while still being able to fire.
                if accuracy < 75:
                    debuglog_add('moving towards target because acc < 75')
                    if parent.AI_move_towards(pship,max_move_distance=max_advance_distance):
                        return
                    debuglog_add('unable to move')

                #if less than 25 give up on firing and just move closer, but no farther than 3 hexes. then evaluate again.
                elif accuracy < 25:
                    debuglog_add('charging target because acc < 25')
                    if parent.AI_move_towards(pship,max_move_distance=3, rush=True):
                        return
                    debuglog_add('unable to move')

            #set some values that are required by animations
            BM.attacker = parent
            BM.target = pship

            #if the target is dead, give up.
            if BM.target.hp < 0:
                return

            #call the attack animation if applicable. (melee is special)
            if weapon.wtype == 'Melee' or weapon.wtype == 'Support' or weapon.wtype == 'Curse':
                pass
            else:
                try:
                    animation_name = weapon.wtype.lower()
                    if weapon.animation_name != None:
                        animation_name = weapon.animation_name
                    renpy.call_in_new_context('atkanim_{}_{}'.format(parent.animation_name,animation_name))
                except:
                    show_message('missing animation. "atkanim_{}_{}" does\'t seem to exist'.format(parent.animation_name,weapon.wtype.lower()))

            #get the damage that will get passed to the target
            damage = weapon.fire(parent,pship,counter)

            #pass the damage value to the target, which will handle things further (like hit animations)
            #curses return something, but they don't do damage.
            if weapon.wtype != 'Curse':
                pship.receive_damage(damage,parent,weapon.wtype)

#basic loop
        def AI_basic_loop(self):
            """this method gets called multiple times until the unit can't seem to
            expend more energy."""
            parent = self.parent
            if parent not in (player_ships if parent.faction == 'Player' else enemy_ships):
                return
            #renpy.log('{} starting AI_basic_loop'.format(parent.name))
            #renpy.log('I have {} energy'.format(parent.en))

            #init a result. [TARGET_SHIP,WEAPON,ESTIMATED_DAMAGE,PRIORITY]
            best_target = [None,None,0,0]

            #find the minimum amount of energy needed to fire the cheapest weapon.
            cheapest_weapon_cost = 999
            for weapon in parent.weapons:
                if weapon.energy_cost(parent) < cheapest_weapon_cost:
                    cheapest_weapon_cost = weapon.energy_cost(parent)

            #support ships don't care about shooting stuff.
            if not parent.support:

                #if the cheapest weapon is too expensive forget about shooting anything.
                if parent.en < cheapest_weapon_cost:
                    debuglog_add('not enough energy to fire any weapon')

                #units that just spawned don't get to fire.
                elif parent.just_spawned:
                    debuglog_add('will not fire because just spawned.')

                #carry on with finding a suitable target.
                else:
                    #create some damage estimates. first, cycle through all enemy ships and estimate damage.
                    for pship in (enemy_ships if parent.faction == 'Player' else player_ships):
                        if pship.location != None:
                            parent.AI_estimate_damage(pship)
                            #if we can finish off an enemy in one hit we will try.
                            if pship.hp < pship.damage_estimation[1] and pship.hp > 0:
                                parent.AI_attack_target(pship,pship.damage_estimation[0])
                                debuglog_add('I took an attack of opportunity against {}'.format(pship.name))
                                #we just spent some EN so end this method and have it get run again.
                                return

                    #find the target which has the highest priority value.
                    for pship in (enemy_ships if parent.faction == 'Player' else player_ships):
                        if pship.location != None:
                            weapon,damage,priority = pship.damage_estimation
                            if priority > best_target[3]:
                                best_target = [pship,weapon,damage,priority]

                    #debug logging
                    if best_target[0] == None:
                        debuglog_add('no good target was found')
                    else:
                        debuglog_add('best target is {} with an estimate of {!s} and a priority of {!s}'.format(best_target[0].name,best_target[2],best_target[3]))

            else: #is support
                pass

            #check if this unit has a melee weapon. if it does, it's okay to move closer than normal.
            can_melee = get_can_melee(parent)
            if can_melee:
                minimum_damage = 50
            else:
                minimum_damage = 10

            #decide whether to shoot or to move
            #if no good target was found or the estimated damage isn't worth it, move.
            if (best_target[0] == None or best_target[2] < minimum_damage) and parent.en >= parent.move_cost:
                debuglog_add('decided on moving towards an enemy ship')

                #find the enemy ships you want to move towards
                #the more hate and closer by the higher a priority it is to move towards.
                #if this ship can use melee, enemy ryders get double the priority they otherwise would.
                priority_target = [None,0]
                for ship in (enemy_ships if parent.faction == 'Player' else player_ships):
                    if ship.location != None:
                        distance = get_ship_distance(parent,ship)
                        priority = (1 + (ship.hate/100.0)**1.5/10) / float( (distance**1.6/10.0) )
                        if ship.stype == 'Ryder' and can_melee:
                            priority *= 2
                        if  priority > priority_target[1]:
                            priority_target = [ship,priority]
                parent.target = priority_target[0] #not sure if still used
                debuglog_add('I am going after the {} because of its weighted priority of {!s}'.format(priority_target[0].name,priority_target[1]))

                #get how far we can move and still fire the cheapest weapon.
                max_move = (parent.en - cheapest_weapon_cost) / parent.move_cost
                #actually move, but keep some energy in reserve.
                parent.AI_move_towards(parent.target,max_move_distance=max_move)
                return

            #if a target was found and the estimated damage is worth it, go shoot a fool.
            elif best_target[0] != None and best_target[2] > minimum_damage:
                debuglog_add('attacking {}'.format(best_target[0].name))
                target_ship,weapon,estimate,priority = best_target
                parent.AI_attack_target(target_ship,weapon)
                return
            #since both moving and shooting is not optimal, just waste whatever energy is left and end.
            else:
                if best_target[0] == None:
                    return
                else:
                    debuglog_add('can not find anything better to do, so I just attack with whatever')
                    parent.AI_attack_target(best_target[0],best_target[1])
                    return

#AI move towards
        def AI_move_towards(self, target, melee_distance = None, max_move_distance = 0, preferred_distance = 0,rush=False):
            """
            move towards an enemy, but pay attention to which cells offer protection
            if melee_distance == True  try to move right next to the target
            max_move_distance sets the max number of hexes to move
            preferred distance can be set to to not move too close
            rush means ignore defensive value of hexes
            """
            #some basic inits
            parent = self.parent
            if preferred_distance == 0: preferred_distance = self.preferred_distance
            if max_move_distance == 0: max_move_distance = parent.en/parent.move_cost
            if melee_distance is None: melee_distance = get_can_melee(parent)
            if target == None:
                debuglog_add('warning, movetarget is none!')
                return False
            if parent.location == None or target.location == None:
                debuglog_add('warning, parent location or target locaion is none!')
                return False
            old_spot = parent.location

            if max_move_distance == 0:
                debuglog_add('I cannot move due to lack of energy or I am not allowed to')
                return False

            #get the total distance between this ship and the target.
            travel_distance = get_ship_distance(parent,target)
            debuglog_add('total travel distance: {}'.format(travel_distance) )

            

            #make a list of all the spots this ship could move to.
            move_range = get_all_in_radius(old_spot,max_move_distance)
            valid_spots = []
            for hex in move_range:
                if get_cell_available(hex):
                    #check if you will get countered by moving to this hex. if you do, check if it's next to an enemy ryder
                    if get_counter_attack(hex, AI = parent.faction != 'Player'):
                        if not melee_distance:
                            continue
                        else:
                            #find out if a ryder is next to this hex. maybe put this in a function?
                            ryder_adj = False
                            shiplist = enemy_ships if parent.faction == 'Player' else player_ships
                            for ship in shiplist:
                                if ship.stype == 'Ryder' and get_distance(ship.location,hex) == 1:
                                    ryder_adj = True
                            #if a ryder is not next to this hex we have no business getting countered for nothing.
                            if not ryder_adj:
                                continue
                    # if distance < travel_distance:
                    valid_spots.append(hex)

            #if no proper spots were found, parent cannot move.
            if len(valid_spots) == 0:
                debuglog_add('there are no valid spots!')
                return False

            #in some cases defensive values get ignored, like with lead ships or when forced to.
            if (parent in BM.lead_ships or rush) and not parent.support:
                #find shortest possible distance from target
                debuglog_add('moving while ignoring defenses')
                shortest_distance = 999
                for hex in valid_spots:
                    distance = abs(get_distance(hex,target.location) - preferred_distance)
                    if distance < shortest_distance:
                        shortest_distance = distance

                #if no good spot was found, there's probably nothing to be done.
                if shortest_distance == 999 or shortest_distance == travel_distance:
                    debuglog_add('there is no spot that is closer')
                    return False

                debuglog_add('shortest distance: {}'.format(shortest_distance) )

                #there may be multiple spots at the best distance
                closest_spots = []
                for hex in valid_spots:
                    if abs(get_distance(hex,target.location) - preferred_distance) == shortest_distance:
                        closest_spots.append(hex)

                #this might be improvable :p
                if len(closest_spots) > 1:
                    best_hex = renpy.random.choice(closest_spots)
                else:
                    best_hex = closest_spots[0]

            else:
                #find hex that is close but also offers good defence
                debuglog_add('moving while looking for defensive spots')
                best_hex = None
                best_value = 0
                store.hex_values = {}
                for hex in valid_spots:
                    distance = abs(get_distance(hex,target.location) - preferred_distance)
                    if get_counter_attack(hex, AI = parent.faction != 'Player'):
                        if not melee_distance:
                            continue
                    value = 0
                    #support units don't actually care about getting closer at all - just defensive value.
                    if not parent.support:
                        value = (travel_distance - distance) * 75
                    value -= get_hex_lethal(parent,hex)
                    value += get_flak_at_hex(hex,ignore=[parent]) + get_shielding_at_hex(hex,ignore=[parent])
                    store.hex_values[hex] = value
                    if value > best_value:
                        best_hex = hex
                        best_value = value

            #calling move_ship() when not needed can lead to double counter attacks.
            if old_spot == best_hex:
                debuglog_add('best spot is the spot I am already at!')
                return False
            elif best_hex:
                parent.move_ship(best_hex, BM)
                debuglog_add('moving towards {}'.format( str(best_hex) ) )
                return True
            debuglog_add('moving failed because of unknown reason')
            return False

#AI START
        def AI(self):
            """this method gets called directly to start the AI and it usually
            runs AI_basic_loop multiple times. this method is the primary one to
            overwrite to make custom AI's"""
            parent = self.parent
            #renpy.log('{} starting AI'.format(parent.name))
            #renpy.log('I have {} energy'.format(parent.en))
            if parent in BM.lead_ships:
                pass
                #renpy.log('I am a lead ship!')

            if BM.stopAI: return
            if parent.en == 0: return

            if parent.stype == 'Carrier' and parent.location != None:
                spawn_ryders(parent)
                return

            if parent.name == 'Legion':
                #let's bring the pain
                if BM.enemy_vanguard_path != [] and parent.en > 0:
                    should_fire = False
                    if parent.faction == 'Player':
                        #used by player_AI
                        for ship in enemy_ships:
                            if ship.location in BM.player_vanguard_path:
                                should_fire = True
                    else:
                        for ship in player_ships:
                            if ship.location in BM.enemy_vanguard_path:
                                should_fire = True

                    if should_fire:
                        fire_legion_vanguard(parent)
                        return
                    else:
                        if parent.faction == 'Player':
                            BM.player_vanguard_path = []
                        else:
                            BM.enemy_vanguard_path = []


            #################################### HOLD MY BEER, I'M DOING THIS

            if parent.stype == 'Assault Carrier' and parent.location != None:
                if renpy.random.randint(0,2) == 1:
                    spawn_ryders(parent,max=1)

            if parent.support and not parent.just_spawned:
                supporting = True
                while supporting:
                    supporting = support_AI(parent) #if this function returns False it couldn't support. therefore stop the loop and do something else, such as move.            

            parent.target = None
            BM.selected = parent
            parent.AI_running = True
            while parent.AI_running:
                #if for whatever reason the AI should stop doing stuff BM.stopAI will be True
                if BM.stopAI:
                    parent.AI_running = False
                    return

                #store the current EN value. if this doesn't change during a loop than there's nothing more the ship can do.
                starting_en = parent.en

                #if parent.target == None: ##I need to get back to this
                parent.AI_basic_loop()
                if starting_en == parent.en:
                      ##no (more) engine power was (/could be) used so we quit the AI

                    if parent.faction == 'Player':
                        if parent.name == 'Legion' and BM.player_vanguard_path == []:
                            result = get_vanguard_feasible(parent)
                            if result != False:
                                # message = "WARNING: Legion aims vanguard at {0}".format(result.name)
                                # show_message(message)
                                # BM.battle_log_insert([], message)
                                BM.player_vanguard_path = interpolate_hex(parent.location,result)
                    else:
                        if parent.name == 'Legion' and BM.enemy_vanguard_path == []:
                            result = get_vanguard_feasible(parent)
                            if result != False:
                                # message = "WARNING: Legion aims vanguard at {0}".format(result.name)
                                # show_message(message)
                                # BM.battle_log_insert([], message)
                                BM.enemy_vanguard_path = interpolate_hex(parent.location,result)
                    parent.AI_running = False
                    parent.just_spawned = False
                    return

    def cartesian_product(seq,n):
        """
        effectively this calculates all permutations of an iterable with replacement at length n.
        useful to get all the possible combinations of weapons a unit can use.
        """
        result = []
        for p in itertools.product(seq, repeat=n):
            result.append(p)
        return result

    def get_weapon_combinations(ship,en):
        """
        return a list containing (sub)lists of weapon combinations that are available for the given ship
        and the given energy pool. used to calculate hex value.
        """

        # failsaves
        if ship == None: return []
        if ship.weapons == None or ship.weapons == []: return []

        #init
        weapons = ship.weapons
        cheapest_weapon_cost = 9999
        result = []

        #check for cheapest weapon cost. you can never fire more times than your EN / cheapest_cost
        for weapon in weapons:
            if weapon.energy_use < cheapest_weapon_cost:
                cheapest_weapon_cost = weapon.energy_use

        #number of times the cheapest weapon can be fired.
        max_shots = en / cheapest_weapon_cost

        if max_shots <= 0:
            return []

        #all possible combinations. not all are possible with the energy limitations
        raw_permutations = cartesian_product(weapons,max_shots)

        #filter out all the combinations that can actually be fired in this sequence.
        for combination in raw_permutations:
            current_en = en
            temp_combination = [] #part of the combination can still be useful
            for weapon in combination:
                if current_en >= weapon.energy_use:
                    current_en -= weapon.energy_use
                    temp_combination.append(weapon)
                else:
                    break
            if temp_combination != []:
                if temp_combination not in result:
                    result.append(temp_combination)

        #the result needs to be cleaned from subsets that are already part of other combinations
        for a in result[:]:
            for b in result[:]:

                if len(a) < len(b):
                    intersection = list( set(a).intersection(b) )
                    if intersection == a:
                        if a in result:
                            result.remove(a)

        return result

    def scan_local_area(ship):
        if ship == None: return []
        if ship.location == None: return []

        move_range = ship.en/ship.move_cost
        cells_in_range = get_all_in_radius(ship.location,move_range)

        return cells_in_range

    def get_hex_lethal(self,location):
        """check if this location is dangerous. right now it only checks
        enemy kinetic accuracy."""
        if location is None or self is None: return 999
        highest_kinetic_acc = 0
        for pship in player_ships:
            for weapon in pship.weapons:
                if weapon.wtype == 'Kinetic':
                    distance = get_distance(pship.location,location)
                    estimated_accuracy = 70 + 50 - self.evasion - (15*distance)
                    if estimated_accuracy > highest_kinetic_acc:
                        highest_kinetic_acc = estimated_accuracy
        return highest_kinetic_acc * self.brain.kinetic_fear

    def estimate_melee_damage(self,weapon,target):
        """check if a melee attack is possible and what the expected damage would be."""
        if self is None or weapon is None or target is None: return 0
        if self.en < weapon.energy_cost(self): return 0

        distance = get_ship_distance(self,target) - 1
        max_distance = (self.en - weapon.energy_cost(self)) / self.move_cost
        if distance > max_distance: return 0

        possible_locations = clean_locations( get_in_ring(target.location,1) )
        for location in possible_locations[:]:
            if not get_cell_available(location):
                possible_locations.remove(location)
                continue
            if get_distance(location,self.location) > max_distance:
                possible_locations.remove(location)
        if len(possible_locations) == 0: return 0

        shortest_location = None
        shortest_distance = 99
        for location in possible_locations:
            distance = get_distance(self.location,location)
            if distance < shortest_distance:
                shortest_location = location
                shortest_distance = distance
        #currently there's no checking for counters and other reasons not to close in on a spot.
        self.melee_location = shortest_location
        return get_acc(weapon,self,target,guess = True,custom_range=1) * (weapon.damage-target.armor) * weapon.shot_count / 100

    def spawn_ryders(ship,max=None):
        """
        used by carrier class enemies to spawn ryders
        """

        #get all the free spaces around the parent
        free_spaces = []
        for hex in get_all_in_radius(ship.location,1):
            if get_cell_available(hex):
                free_spaces.append(hex)
        if len(free_spaces) == 0: return

        spawning = True
        spawn_count = 0
        while spawning:

            possible_spawn = []
            for spawn in ship.spawns:
                ryder,cost,weaponlist = spawn
                if ship.en >= cost:
                    possible_spawn.append(spawn)

            if len(possible_spawn) == 0:
                spawning = False
            else:
                spawn_location = renpy.random.choice(free_spaces)
                spawn = renpy.random.choice(possible_spawn)
                ryder,cost,weaponlist = spawn
                create_ship(ryder(),spawn_location,weaponlist)
                spawned_ship = enemy_ships[-1]
                spawned_ship.en = spawned_ship.move_cost * 2
                #reset the weapons to default in case they changed.
                for weapon in spawned_ship.weapons:
                    weapon.__init__()
                if spawned_ship.en > spawned_ship.max_en: spawned_ship.en = spawned_ship.max_en
                spawned_ship.just_spawned = True
                if max:
                    spawn_count += 1
                    if spawn_count >= max:
                        spawning = False

                if ship.faction is not 'Player':
                    if BM.turn_count <= 5:
                        enemy_ships[-1].money_reward *= 1.0 - (0.2*BM.turn_count)
                    else:
                        enemy_ships[-1].money_reward = 0

                renpy.pause(0.2)
                ship.en -= cost
                free_spaces.remove(spawn_location)

            if len(free_spaces) == 0:
                spawning = False

    def support_AI(ship):
        """
        find out what support skills are available, look at viable targets and curse the fuck out of them.
        """
        if ship == None: return False
        if ship.location == None: return False
        if ship.en == 0: return False
        if ship.just_spawned:
            ship.just_spawned = False
            return False

        can_heal = False
        heal_weapon = None
        viable_options = []  # [(weapon,target),...]

        #can I heal ships? with what 'weapon'? note: more than 1 repair skill is not supported
        for weapon in ship.weapons:
            if weapon.repair and ship.en >= weapon.energy_use:
                can_heal = True
                heal_weapon = weapon
                break

        #add the best healing target tot he list of options if it is viable to do so
        if can_heal:
            most_damage = 0
            heal_target = None
            for oship in (player_ships if ship.faction == 'Player' else enemy_ships):
                if get_ship_distance(ship,oship) <= 3 and oship.location != None:
                    damage = oship.max_hp-oship.hp
                    if damage >= heal_weapon.damage * 0.75 and damage > most_damage:
                        most_damage = damage
                        heal_target = oship

            if heal_target != None:
                viable_options.append((heal_weapon,heal_target))

        #go through the list of curses and look for viable targets.
        for weapon in ship.weapons:
            if ship.en < weapon.energy_use:
                continue #on to the next weapon - there is not enough energy for this one.

            if not weapon.repair:  #we already handled these

                #handle curses
                if weapon.wtype == 'Curse':

                    #get a list of ships that do not have this curse on them already
                    viable_targets = []
                    for oship in (enemy_ships if ship.faction == 'Player' else player_ships):
                        #warning, this code does not support abilities that modify more than 1 stat
                        if oship.modifiers[weapon.modifies][0] > weapon.buff_strength and oship.location != None: #  e.g. 0 accuracy > -20 accuracy
                            viable_targets.append(oship)
                    if viable_targets == []:
                        continue #to next weapon

                    if weapon.modifies == 'flak':
                        viable_targets = heapq.nlargest( 3 , viable_targets , key=lambda x:x.flak ) #return the 3 ships with the highest flak
                        for oship in viable_targets[:]:
                            if oship.flak < 10:
                                viable_targets.remove(oship)
                    elif weapon.modifies == 'shield_generation':
                        viable_targets = heapq.nlargest( 3 , viable_targets , key=lambda x:x.shield_generation )
                        for oship in viable_targets[:]:
                            if oship.shield_generation < 10:
                                viable_targets.remove(oship)
                    else:
                        viable_targets = heapq.nlargest( 3 , viable_targets , key=lambda x:x.hate )

                    if not viable_targets == []:
                        #which target ends up nominated is actually random. what's important is that it's a reasonable target.
                        viable_options.append( ( weapon,renpy.random.choice(viable_targets) ) )

                if weapon.wtype == 'Support':

                    if weapon.modifies == 'restore':
                        # worse curses take precedence over lesser ones.
                        viable_target = None
                        curse_weight = 0
                        for oship in (player_ships if ship.faction == 'Player' else enemy_ships):
                            if oship.location != None:
                                for modifier in oship.modifiers:
                                    magnitude, duration = oship.modifiers[modifier]
                                    if magnitude < curse_weight: # e.g. -100 < -20   or  disable < aimdown etc. smaller means more powerful in this case
                                        viable_target = oship
                                        curse_weight = magnitude

                        if viable_target != None:
                            viable_options.append( (weapon,viable_target) )

                    else: #other buffs
                        pass # not implemented

        #time to use one of the options.
        if viable_options != []:
            chosen_weapon,chosen_target = renpy.random.choice(viable_options)
            show_message('using {} on {}'.format(chosen_weapon.name,chosen_target.name) )
            ship.AI_attack_target(chosen_target,chosen_weapon)
            return True
        else:
            return False #wasn't able to do anything.

    def get_vanguard_feasible(self):
        """find out if firing the legion's vanguard is a good idea and what its target should be"""
        #boilerplate
        if self is None: return False
        if self.location is None: return False

        ring = get_in_ring(self.location,20) #ring around the battlefield

        #find a good target
        best_target = None
        best_count = 0
        for hex in ring:
            #get a list of hexes in between self and the possible target.
            path = interpolate_hex(hex,self.location)

            #count the number of player ships in between the target and self
            target_count = 0
            for oship in (enemy_ships if ship.faction == 'Player' else player_ships):
                if oship.location in path:
                    target_count += 1

            #record best target
            if target_count > 1:
                if best_count < target_count:
                    best_target = hex
                    best_count = target_count

        if best_target is not None:
            return best_target
        else:
            return False

    def fire_legion_vanguard(self):
        """fire the legion's vanguard at a target"""
        #boilerplate
        if self is None: return
        if self.location is None: return

        # renpy.music.play('Music/March_of_Immortals.ogg') #not sure if this will be used
        try:
            renpy.call_in_new_context('atkanim_legion_vanguard')
        except:
            show_message('missing legion vanguard animation')

        renpy.hide_screen('battle_screen')
        renpy.show_screen('battle_screen')
        store.damage = 10000  #yeah, I know.
        store.hit_count = 1
        store.total_armor_negation = 0
        store.total_shield_negation = 0
        store.total_flak_interception = 0
        if self.faction == 'Player':
            templist = enemy_ships[:]
            for ship in templist:
                if ship.location in BM.player_vanguard_path and BM.battlemode: #failsaves
                    if ship in enemy_ships:
                        BM.target = ship
                        ship.receive_damage(store.damage,self,'Vanguard')
            renpy.hide_screen('battle_screen')
            renpy.show_screen('battle_screen')
            BM.player_vanguard_path = []
        else:
            templist = player_ships[:]
            for ship in templist:
                if ship.location in BM.enemy_vanguard_path and BM.battlemode: #failsaves
                    if ship in player_ships:
                        BM.target = ship
                        ship.receive_damage(store.damage,self,'Vanguard')
            renpy.hide_screen('battle_screen')
            renpy.show_screen('battle_screen')
            BM.enemy_vanguard_path = []
        return

    def estimate_flak(self,target,adjustment = 10,shiplist='player_ships',ignore = []):
        if self is None: return 0
        if not hasattr(target,'location'):return 0
        if self.location is None or target.location is None: return 0
        if type(ignore) is not list: ignore = [ignore]

        path = interpolate_hex(self.location,target.location) #get a list of locations between parent and target

        flak_strength = 1.0  #the lower this number the stronger, actually.
        for hex in path:
            for ship in eval(shiplist):
                if ship in ignore: continue
                if ship.location is not None and not ship.flak_used:
                    if get_distance(ship.location,hex) <= ship.flak_range:
                        effective_flak = ship.flak + ship.modifiers['flak'][0] - adjustment #final -adjustment represents both torpedoes and the AI wearing down flak with missiles
                        if effective_flak > 100: effective_flak = 100
                        elif effective_flak < 0: effective_flak = 0
                        flak_strength = (100-effective_flak)/100.0 * flak_strength
                        ship.flak_used = True


        for ship in (enemy_ships if self.faction == 'Player' else player_ships):
            ship.flak_used = False

        return flak_strength

    def get_flak_at_hex(hex,AI=True,ignore=[]):
        """get an average flak value for a location based on all the opposing units and friendly flak"""
        if hex == None: return 0
        if type(ignore) is not list: ignore = [ignore]
        if AI:
            ships = player_ships
        else:
            ships = enemy_ships
        flak = 0
        locationholder = store.object()
        locationholder.location = hex
        shipcount = 0
        for ship in ships:
            flak += estimate_flak(ship,locationholder,adjustment=0,shiplist='enemy_ships' if AI else 'player_ships',ignore=ignore)
            shipcount += 1
        
        average_flak = (flak / shipcount) * 100  # e.g. (1,25 / 5) * 100 = 25
        return int(100 - average_flak)

    def get_shielding_at_hex(hex,AI=True,ignore=[]):
        if hex == None: return 0
        if type(ignore) is not list: ignore = [ignore]
        if AI:
            ships = enemy_ships
        else:
            ships = player_ships
        result = 0
        for ship in ships:
            if ship in ignore:
                continue
            if ship.shield_generation > 0 and get_distance(ship.location,hex) <= ship.shield_range:
                result += ship.shield_generation + ship.modifiers['shield_generation'][0]
        return result

    def get_can_melee(self):
        can_melee = False
        for weapon in self.weapons:
            if weapon.wtype == 'Melee':
                return True

    def get_melee_weapon(self):
        for weapon in self.weapons:
            if weapon.wtype == 'Melee':
                return weapon
        return None

    def attempt_melee(self):
        attacked = False
        melee_weapon = get_melee_weapon(self)

        while self.en >= melee_weapon.energy_cost(self):
            adjacent = False
            for ship in (enemy_ships if self.faction == 'Player' else player_ships):
                #TODO try to move next to a ryder
                if get_ship_distance(ship,self) == 1:
                    if ship.stype == 'Ryder':
                        if adjacent == False:
                            adjacent = ship
                        else:
                            #let's be a dick and choose to melee the ryder with lowest hp.
                            if adjacent.hp > ship.hp:
                                adjacent = ship
            if adjacent == False:
                return attacked
            else:
                attacked = True
                self.AI_attack_target(adjacent,melee_weapon)

        else:
            #the while never ran, the ship ran out of energy to melee or there was never a valid target.
            return attacked

    def disengage(self):
        BM.selected = self
        move_range = self.en / self.move_cost
        if move_range <= 0:
            return False

        move_range = get_all_in_radius(self.location,move_range)
        valid_spots = []
        for hex in move_range:
            if get_cell_available(hex):
                if get_counter_attack(hex, AI = True):
                    continue
                valid_spots.append(hex)

        best_hex = None
        best_average = 0
        for hex in valid_spots:
            distance = 0
            for ship in (enemy_ships if self.faction == 'Player' else player_ships):
                distance += get_ship_distance(self,ship)
            average = distance / len((enemy_ships if self.faction == 'Player' else player_ships))
            if average > best_average:
                best_average = average
                best_hex = hex

        if best_hex is not None:
            self.move_ship(best_hex,BM)

















