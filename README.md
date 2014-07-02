#Sunrider
========

Beta 4
=======
* 2 new battles, 2 new ships types and lots of excitement. also a shower scene.
* changed the in-game store lay-out. you can now buy an upgrade to rocket damage too
* added AI/code for carriers that spawn ryders during battle
* added new unit icons to the R&D screen
* new buff unique to Sola/Nephalim: Awaken. boosts damage and accuracy for 3 turns at the cost of 100EN and 75HP
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
