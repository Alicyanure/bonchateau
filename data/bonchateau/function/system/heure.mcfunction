# --------------------------------------------------
# Bonchateau - Outil Debug Heure
# But : afficher l'heure actuelle du cycle Minecraft
# Unité identique à /time set <valeur>
# (0 → 23999)
# --------------------------------------------------

# Création de l'objectif si inexistant
scoreboard objectives add bc_temps dummy

# Récupère le temps actuel du cycle (0-23999)
execute store result score #heure bc_temps run time query daytime

# Affiche le résultat
tellraw @s ["",{"text":"[Bonchateau] Heure actuelle : ","color":"gold"},{"score":{"name":"#heure","objective":"bc_temps"},"color":"yellow"}]