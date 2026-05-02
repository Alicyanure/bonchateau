# ============================================
# BONCHATEAU - Retrait 1 Penausme (81 Peore)
# ============================================

# Tag temporaire si solde >= 81
execute if score @s argent_banque matches 81.. run tag @s add peut_retirer

# Retrait
execute if entity @s[tag=peut_retirer] run give @s minecraft:amethyst_cluster[custom_name='{"text":"Penausme","color":"light_purple","italic":false}',lore=['{"text":"Monnaie","color":"gray","italic":false}'],custom_data={bonchateau_monnaie:"penausme",bonchateau_valeur:81}] 1
execute if entity @s[tag=peut_retirer] run scoreboard players remove @s argent_banque 81
execute if entity @s[tag=peut_retirer] run title @s actionbar {"text":"💰 Retrait de 1 Penausme (équivalent 81 Peore)","color":"gold"}
execute if entity @s[tag=peut_retirer] run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1.2

# Solde insuffisant
execute unless entity @s[tag=peut_retirer] run title @s actionbar {"text":"❌ Solde insuffisant (pour retirer 1 Penausme, 81 Peore en banque sont requis)","color":"red"}
execute unless entity @s[tag=peut_retirer] run playsound minecraft:block.note_block.bass master @s ~ ~ ~ 1 0.8

# Nettoyer
tag @s remove peut_retirer