#in this file all the functions and classes related to AI are collected.

init python:

    # class AI(renpy.object):
        #global class that manages AI might be useful in the future, akin to the BM


    import itertools #mess around with iterables (like lists)
    import heapq #This module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.

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
        
        
    def spawn_ryders(ship):
        """
        used by carrier class enemies to spawn ryders
        """
    
        available_spaces = get_all_in_radius(ship.location,1)
        free_spaces = []
        for hex in available_spaces:
            if get_cell_available(hex):
                free_spaces.append(hex)

        if len(free_spaces) > 0:
            spawning = True
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
            for eship in enemy_ships:
                if get_ship_distance(ship,eship) <= 3:
                    damage = eship.max_hp-eship.hp
                    if damage >= heal_weapon.damage * 0.75 and damage > most_damage:
                        most_damage = damage
                        heal_target = eship
            
            if heal_target != None:
                viable_options.append( (heal_weapon,heal_target) )
                
        #go through the list of curses and look for viable targets.
        for weapon in ship.weapons:
            if ship.en < weapon.energy_use:
                continue #on to the next weapon - there is not enough energy for this one.
                
            if not weapon.repair:  #we already handled these
                
                #handle curses
                if weapon.wtype == 'Curse':
                
                    #get a list of ships that do not have this curse on them already
                    viable_targets = []
                    for pship in player_ships:
                        if pship.modifiers[weapon.modifies][0] > weapon.buff_strength: #  e.g. 0 accuracy > -20 accuracy
                            viable_targets.append(pship)
                    if viable_targets == []:
                        continue #to next weapon
                    
                    if weapon.modifies == 'flak':
                        viable_targets = heapq.nlargest( 3 , viable_targets , key=lambda x:x.flak ) #return the 3 ships with the highest flak
                        for pship in viable_targets[:]:
                            if pship.flak < 10:
                                viable_targets.remove(pship)
                    elif weapon.modifies == 'shield_generation':
                        viable_targets = heapq.nlargest( 3 , viable_targets , key=lambda x:x.shield_generation )    
                        for pship in viable_targets[:]:
                            if pship.shield_generation < 10:
                                viable_targets.remove(pship)                        
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
                        for eship in enemy_ships:
                            for modifier in eship.modifiers:
                                magnitude, duration = eship.modifiers[modifier]
                                if magnitude < curse_weight: # e.g. -100 < -20   or  disable < aimdown etc. smaller means more powerful in this case
                                    viable_target = eship
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
            
        #are there any player ships nearby?
        templist = []        
        for pship in player_ships:
            if get_ship_distance(pship,self) <= 30:
                templist.append(pship)
        if len(templist) <= 1:
            return False
            
        #find a good target
        best_target = None
        best_count = None
        for pship in templist:
            #get a list of hexes in between self and the possible target.
            path = interpolate_hex(pship.location,self.location)
            
            #count the number of player ships in between the target and self
            target_count = 0
            for pship in templist:
                if pship.location in path:
                    target_count += 1
            
            #record best target
            if target_count < 2:
                if best_count is None or best_count < target_count:
                    best_target = pship
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
            renpy.call_in_new_context('atkanim_legion_vanguard') #TEST THIS
        except:
            show_message('missing legion vanguard animation')
            
        renpy.hide_screen('battle_screen')
        renpy.show_screen('battle_screen')
        renpy.pause(1)
        store.damage = 10000  #yeah, I know.
        store.hit_count = 1
        store.total_armor_negation = 0
        store.total_shield_negation = 0
        templist = player_ships[:]
        for ship in templist:
            if ship.location in BM.enemy_vanguard_path and BM.battlemode: #failsaves
                if ship in player_ships: #it's possible the ship was already deleted because of the boss being killed
                    BM.target = ship
                    ship.receive_damage(store.damage,self,'Vanguard') #TEST THIS
        renpy.hide_screen('battle_screen')
        renpy.show_screen('battle_screen')
        BM.enemy_vanguard_path = []
        return
        
    def estimate_flak(self,target):
        if self is None or target is None: return 100
        if self.location is None or target.location is None: return 100
        
        path = interpolate_hex(self.location,target.location) #get a list of locations between parent and target
        
        flak_strength = 1.0  #the lower this number the stronger, actually.
        for hex in path:
            for ship in player_ships:
                if ship.location is not None and not ship.flak_used:
                    if get_distance(ship.location,hex) <= ship.flak_range:
                        effective_flak = ship.flak + ship.modifiers['flak'][0]
                        if effective_flak > 100: effective_flak = 100
                        elif effective_flak < 0: effective_flak = 0
                        flak_strength = (100-effective_flak)/100.0 * flak_strength
                        ship.flak_used = True
                        
        
        for ship in player_ships:
            ship.flak_used = False
        
        return flak_strength
                        
            
                    
                
            
            
        
            
        
        
    
    
    
    
    
    
