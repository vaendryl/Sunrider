beta 7.1
------
* fixed some issues with skirmish
* hopefully fixed some crashing issues with support AI
* newly encountered enemy units get added to skirmish mode
* ton of bugfixes

beta 7
======
* renpy 6.18 is now officially released and the game now only runs on this version of ren'py.
* added a table of future costs to R&D screen
* added a battle log function (by DoumanAsh)
* skipping by holding ctrl (or toggle with tab) now skips animation completely making for faster combat. (by Endershadow)
* AI now tries moving closer before firing its weapon (by BlueOrange)
* enemy Legion can use a vanguard cannon on you!
* Flak path simulation is now updated for hex code.
* the AI now calculates flak between it and its target properly, causing a change in missile behaviour.
* vanguard path overlay is now always shown
* units flagged as a 'boss' no longer end skirmish upon death.
* units not participating in skirmish will not have their buff voices played in reaction to full forward or all guard
* not having the sunrider present (in skirmish) removes access to orders.
* fixed mercenaries getting permanently destroyed upon death in skirmish mode.
* added a store item that upgrades the vanguard cannon
* all guard order now gives 20 flak instead of 30
* flak buffs/curses modify counter-attack damage and -100 flak disables counters entirely.
* changed difficulty names and system. there are now 6 different options.
* the Liberty's disable ability also causes the shutoff and flakdown effect. (the Legion is immune to this ability!)
* added 'right click to cancel' effect to a few more screens like orders and preferences
* quite a few AI changes. you'll likely need to adapt your strategies.
* added a new [REDACTED]
* healing now generates a minor amount of hate.
* Paladin's assault energy cost went from 20 to 30, and its missiles were rebalanced to be more effective against armor.



patch 6.0b
======
* fixed full forward not overwriting all guard
* worked around possible crash in unit placement
* replaced .rpa archive with separate files. this could reduce lag in battle.
* fixed a problem with chigara's attack voice files

patch 6.0a
======
* bugfixes relating to enemy curses and the new order.
* the movement tile next to a unit capable of countering will show up red.

patch 6.0
======
* fixed infinite melee range exploit
* added AI for support units
* new item in the store: shield generator for the Sunrider (added by Endershadow)
* new order: All Guard. can not be used together with Full Forward

patch 5.2
======

* un-broke the skirmish mode. (oops)
* added player and enemy turn music selection into skirmish
* fixed the vanguard's tooltip
* changed "Energy Energy Cost" into "Energy Cost" (will require a reset to show up)
* fixed display of destruction loot of carrier-spawned ryders.
* very minor tweaks to the start of a new turn. (animation speed and sound) (requires a new game for full effect)

patch 5.1
======

* gravity gun can now be used on friendly targets as well.
* fixed some typos in the script
* fixed skirmish not ending properly after a defeat
* fixed game not ending properly after the after-credits scene (when using chapter select)
* fixed crash when clicking addon select screen
* fixed enemy phoenix not getting added properly to the Vesta mision
* chapter select gives no more than 4000 CP
* fixed being able to delete enemies during formation setup phase (at the start of battles 13, 14 and 15)

beta 5
======
* assimilated true hexmod [Azureflare is the best!]
* you can scroll down a bit further so that the status window doesn't cover units in the far bottom right
* greatly reduced lag by reworking much of the battle UI.
* Skirmish mode. use your ships with your upgrades against any combination of enemies you please. you don't get any money or CP though :)
* custom formations. choose your own starting positions from mission 12 onward!
* contract mercenary ships in the story to fight for you! you'll lose them permenantly if they get destroyed.
* added HP values on the player ships' HP bars too due to popular demand.
* added a new resurrect order. 2000 CP to get one of your ryders back
* reworked store backend. it'll be pretty easy to add a ton of new items to the shop. both for us and for modders.
* lower difficulty gives more command points. current and lowest difficulty setting are now displayed in the victory screen.
* R&D has been changed (again). 'submit' functionality is gone. instead, you can always 'sell' an upgrade for 80% of its cost. 
* upgrade costs rebalanced (requires a new game to take effect). kinetic damage is more expensive to upgrade while energy damage became cheaper. armor is now more expensive for ryders.


patch 4.2a
======
* fixes a bug with asaga not being visible in the Mnemosyne Abyss battle if you load the game during turn 1. 
* fixed a possible crash if you beat a boss with the vanguard cannon
* fixed a bug with 4.2 that erased the quantum warhead upgrade if you bought it on 4.1.
* upgrade window became more user friendly (by Renari)
* fixed a tooltip bug with short range warp.
* it's no longer possible to farm enemy carriers for unlimited money.

patch 4.2
======
* tooltips added by Quickman
* chapter select added by EnderShadow
* command point generation globally reduced.
* flak decay mechanic overhauled. you are now far less likely to get blown up in turn 1 by enemy missiles.
* weaker buffs and curses no longer overwrite stronger buffs. this includes the buff from the 'full forward' order.
* accuracy buffs no longer affect healing and other support skills.
* the range on the gravity gun is now infinite.
* enemy units surrender when their leader is destroyed which now gives you bonus money - half as much as if you had destroyed them. sniping the enemy leader asap is not much more economically viable.
* hard difficulty again decreases damage the player does by 25%

patch 4.1
======

* fixed a few crashes due to undefined variables
* fixed not being able to use orders first turn of a new battle if you used an order during the last turn of the previous one
* fixed a crash will happen if you destroy every unit in mission 11.
* fixed graphical issue with movement markers when selecting 'short range warp' while having a ship selected.
* fixed repair drone order costing CP when you don't have enough drones

Beta 4
=======
* 2 new battles, 2 new ships types and lots of excitement. also a shower scene.
* changed the in-game store lay-out. you can now buy an upgrade to rocket damage too
* added AI/code for carriers that spawn ryders during battle
* added new unit icons to the R&D screen
* new buff unique to Sola/Seraphim: Awaken. boosts damage and accuracy for 3 turns at the cost of 100EN and 75HP
* spoiler: new order avaiable later in the game: short range warp. 
* orders have become more expensive
* new sprite for rockets moving across the game map
* minor AI tweaks
* debuf voices implemented


patch 3.1a~c
========
minor bugfixes

patch 3.1
========
* fixed not being able to load after a game over.
* fixed the game crashing after loading an old save file where the phoenix hadn't been created.
* fixed old missiles showing up when you fire your own.
* fixed non-player factions shooting each other's missiles
* fixed rockets taking their EN cost twice
* fixed shielding not getting calculated properly
* fixed being able to roll back by scrolling up in the wrong place in the upgrade screen.
* fixed 'end turn' button remaining on screen (and active) during enemy turn



* improved various scene transitions
* improved unit movement animation
* rockets are now less likely to get shot down by flak compared to regular missiles. warning: this means enemy rockets are more dangerous too!
* blackjacks missiles are nerfed. from 10 misiles per salvo to 6 missiles. this cuts her max damage by 40%. the Sunrider should logically be able to fire a lot more missiles than a Ryder could.
* missile accuracy upgrade has been replaced by flak resistance upgrade. every point in this new stat reduces enemy flak% by 1. this change is visually reflected in the targeting window when hovering over a missile or rocket weapon.
* added a button on the R&D screen that will remove all upgrades and refunds (most) of the money you spent on them. this will also update new balance changes. this feature is not guaranteed to be in the final game and mostly is there for debug/testing purposes.
* added a button that will undo your previous movement. this button is only available right after making a momevement and only when you did not trigger a counter attack. known issue: hovering over a weapon button wil also make the button disappear.




beta 3
=======

changed:
* enemy phoenix is now immune to counter attacks
* changed EN upgrades to go in units of 5 (thanks ledabot)
* fixed not being able to use a weapon because game didn't check for cost upgrades when deciding when a button is clickable
* accuracy upgrades affect a weapons base accuracy, which overall makes these upgrades more effective and easier to understand.
* added a cover mechanic. Asteroids can be spawned in a battle that will have a chance of blocking attacks aimed at a unit on the same cell; until the asteroid is destroyed.
* rewrote buff code to make it neater and more flexible
* stealth is now fully auto self-cast. adding more skills like this will be easy.
* rewrote weapon button display code to be neater. this technique will be useful rewriting ship display code.
* rewrote selection code so it's neater and more rugged. been wanting to do that for a long time
* pretty massive rewrite of ship display code. much much less messy now. I don't think I managed to make it more efficient though, regretably.
* added a new secret weapon
* added HP value on enemy HP bar. removed EN bar
* added basic debuff functionality
* shields new deduct damage before armor and 'total damage negated by armor' is a bit more accurate
* hovering over an enemy unit will make it's HP value show on top of everything else.
* fixed counter attack bug with phoenix
* shield curse implemented
* Kinetics and Energy upgrades now only show up for the units that have weapons of that type
* added icons and stat details to show the actual effect of upgrades
* unit voices will now react to HP level after damage instead of before.
* new missile animation on map. much faster and more fluid.
* expanded old save file compatibility. affection ratings etc no longer are reset. 
* upgrades are reflected in the status window details about the currently hovered weapon
* flak/shield ranges and values now take into account flakoff/shutoff debuffs
* target of a missile attack no longer shows assault animation.


patch notes 2.1
---------------

*fixed*:

  * missiles deducting energy cost twice
  * bonus menu
  * not being able to load from the main menu after credits
  * pulse weapons always missing on the pirate base (still only does minimal damage)
  * pirate bombers can now be attacked by melee
  * game crash when attacking the phoenix with the booster attached with a melee attack
  * fixed flak no longer working after shooting down all the missiles in a salvo.
  * player ships sometimes counter attack twice
  * added 2 cruisers in mission 8 to make it harder to end the battle prematurely.
 
*balance changes*:

  * vanguard cannon now costs 1500 command points
  * upgrading maximum EN is significantly more expensive
  * upgrading EN costs of specific weapon types is slightly less expensive (over time)
  * Tactical nuclear warheads have become cheaper and more powerful. 300$ for 800 damage. recommended against (pirate) bases!
  * you can only use 1 order per turn

beta 2 v2.00
============

* 3 new missions, 1 new unit and 1 new character and lots of story!
* added melee attacks and created dynamic animations for them  
* blind side attacks. any unit moving right next to another unit will get counter attacked by assault type weapons
* upgrading is completely overhauled and much morefunctional
* AI slightly modified

Beta 1
========
1.06 patch notes
----------------

* disabled saving/loading during the enemy turn. instead, a warning will appear.
* fixed possible crash caused by Vanguard cannon when used to kill a boss (and other units)
* darkend the background during victory screen and destroyed units don't suddenly pop up anymore
* increases size of HP and EN values in status window

* "end turn' button shows red if there are ships with full energy left. it shows green when there are none. 
I think a confirmation popup would be too invasive.
* fixed transition glitch at the end of mission 2
* pressing [ or ] now cycles through player ships. if you start a new game on 1.06 then the middle mouse 
button will also work.
* lowered the default volume of music
* right click deselects weapon or ship (new game required)
* added experimental option for edge scrolling.

1.06a
-------

* fixed crash after killing a boss
* hopefully really fixed the Vanguard crash issue
* fixed crash when clicking middle mouse while selecting an enemy
* right click exits the save menu screen
* middle click will select the sunrider if no units are selected.

1.06b 
------

* fixed bug introduced by commenting out some critical code
