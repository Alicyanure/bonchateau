# ============================================
# BONCHATEAU - Incrémenter le jour
# ============================================
# Appelé à minuit (temps 0)

# Incrémenter le jour pour tous les joueurs
scoreboard players add @a jour 1

# Si le jour dépasse 7, revenir à 1 (lundi)
execute as @a if score @s jour matches 8.. run scoreboard players set @s jour 1

# Afficher le nouveau jour
execute as @a if score @s jour matches 1 run tellraw @s {"text":"🕒 Lundi - Nouvelle semaine !","color":"gold"}
execute as @a if score @s jour matches 2 run tellraw @s {"text":"🕒 Mardi","color":"gray"}
execute as @a if score @s jour matches 3 run tellraw @s {"text":"🕒 Mercredi","color":"gray"}
execute as @a if score @s jour matches 4 run tellraw @s {"text":"🕒 Jeudi","color":"gray"}
execute as @a if score @s jour matches 5 run tellraw @s {"text":"🕒 Vendredi","color":"gray"}
execute as @a if score @s jour matches 6 run tellraw @s {"text":"🕒 Samedi - Week-end !","color":"aqua"}
execute as @a if score @s jour matches 7 run tellraw @s {"text":"🕒 Dimanche - Repos !","color":"light_purple"}
