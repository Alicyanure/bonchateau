#clear @s minecraft:large_amethyst_bud 1
#scoreboard players add @s argent_banque 1
#title @s actionbar {"text":"💰 Dépôt effectué (+1)","color":"gold"}

# ============================================
# BONCHATEAU - Dépôt de monnaie à la banque
# ============================================
# Retire 1 Peore de l'inventaire et ajoute 1 au score

# Retirer 1 Peore de la main du joueur
clear @s minecraft:nether_star[custom_data~{bonchateau_monnaie:"penerethisme"}] 1

# Ajouter 1 à l'argent en banque
scoreboard players add @s argent_banque 729

# Message de confirmation
title @s actionbar {"text":"💰 Dépôt de 1 Penerethisme (équivalent 729 Peore)","color":"gold"}
playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1.5
