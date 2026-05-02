#execute if score @s argent_banque matches 1.. run give @s minecraft:medium_amethyst_bud 1
#execute if score @s argent_banque matches 1.. run scoreboard players remove @s argent_banque 1
#execute if score @s argent_banque matches 1.. run title @s actionbar {"text":"💰 Retrait effectué (-1)","color":"gold"}
#execute if score @s argent_banque matches 0 run title @s actionbar {"text":"❌ Solde insuffisant","color":"red"}

# ============================================
# BONCHATEAU - Retrait de monnaie à la banque
# ============================================
# Donne 1 Peore au joueur si son solde est suffisant

# Si le joueur a au moins 1 Peore en banque → retrait
#execute if score @s argent_banque matches 1.. run give @s minecraft:medium_amethyst_bud[custom_name='{"text":"Peore","color":"light_purple","italic":false}',lore=['{"text":"Monnaie","color":"gray","italic":false}'],custom_data={bonchateau_monnaie:"peore",bonchateau_valeur:1}] 1
#execute if score @s argent_banque matches 1.. run scoreboard players remove @s argent_banque 1
#execute if score @s argent_banque matches 1.. run title @s actionbar {"text":"💰 Retrait effectué (-1 Peore)","color":"gold"}
#execute if score @s argent_banque matches 1.. run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1.2

# Si le solde est insuffisant → message d'erreur
#execute if score @s argent_banque matches 0 run title @s actionbar {"text":"❌ Solde insuffisant","color":"red"}
#execute if score @s argent_banque matches 0 run playsound minecraft:block.note_block.bass master @s ~ ~ ~ 1 0.8

# ============================================
# BONCHATEAU - Retrait de monnaie à la banque
# ============================================

# Vérifier le solde UNE SEULE FOIS via tag temporaire
execute if score @s argent_banque matches 1.. run tag @s add peut_retirer

# Si le joueur peut retirer
execute if entity @s[tag=peut_retirer] run give @s minecraft:medium_amethyst_bud[custom_name='{"text":"Peore","color":"light_purple","italic":false}',lore=['{"text":"Monnaie","color":"gray","italic":false}'],custom_data={bonchateau_monnaie:"peore",bonchateau_valeur:1}] 1
execute if entity @s[tag=peut_retirer] run scoreboard players remove @s argent_banque 1
execute if entity @s[tag=peut_retirer] run title @s actionbar {"text":"💰 Retrait effectué (-1 Peore)","color":"gold"}
execute if entity @s[tag=peut_retirer] run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1.2

# Si solde insuffisant
execute unless entity @s[tag=peut_retirer] run title @s actionbar {"text":"❌ Solde insuffisant","color":"red"}
execute unless entity @s[tag=peut_retirer] run playsound minecraft:block.note_block.bass master @s ~ ~ ~ 1 0.8

# Nettoyer le tag temporaire
tag @s remove peut_retirer