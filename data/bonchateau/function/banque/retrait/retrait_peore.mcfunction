# ============================================
# BONCHATEAU - Retrait 1 Peore
# ============================================

# Tag temporaire si solde suffisant
execute if score @s argent_banque matches 1.. run tag @s add peut_retirer

# Retrait
execute if entity @s[tag=peut_retirer] run give @s minecraft:medium_amethyst_bud[custom_name='{"text":"Peore","color":"light_purple","italic":false}',lore=['{"text":"Monnaie","color":"gray","italic":false}'],custom_data={bonchateau_monnaie:"peore",bonchateau_valeur:1}] 1
execute if entity @s[tag=peut_retirer] run scoreboard players remove @s argent_banque 1
execute if entity @s[tag=peut_retirer] run title @s actionbar {"text":"💰 Retrait de 1 Peore","color":"gold"}
execute if entity @s[tag=peut_retirer] run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1.2

# Solde insuffisant
execute unless entity @s[tag=peut_retirer] run title @s actionbar {"text":"❌ Solde insuffisant (vous n'avez aucun Peore en banque)","color":"red"}
execute unless entity @s[tag=peut_retirer] run playsound minecraft:block.note_block.bass master @s ~ ~ ~ 1 0.8

# Nettoyer
tag @s remove peut_retirer