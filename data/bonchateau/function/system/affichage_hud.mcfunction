# ============================================
# BONCHATEAU - Affichage HUD
# ============================================
# Met à jour les valeurs affichées dans la sidebar

# Copier les scores de chaque joueur vers les faux joueurs
# Note : On prend le premier joueur trouvé (pour serveur solo/LAN)
# Pour du multi-joueur pur, il faudrait un système plus complexe

#execute as @a[limit=1] run scoreboard players operation "§6💰 Argent" HUD = @s argent_banque
#execute as @a[limit=1] run scoreboard players operation "§f🕒 Jour" HUD = @s jour
#execute as @a[limit=1] run scoreboard players operation "§b🏰 Lieu" HUD = @s lieu
#execute as @a[limit=1] run scoreboard players operation "§c🗡 Classe" HUD = @s classe


#execute as @a run title @s actionbar [{"text":"💰 Argent en banque : ","color":"gold"},{"score":{"name":"@s","objective":"argent_banque"},"color":"green"},{"text":" | 📅 Jour : ","color":"gray"},{"score":{"name":"@s","objective":"jour"},"color":"white"},{"text":" | 📍 Lieu : ","color":"aqua"},{"score":{"name":"@s","objective":"lieu"},"color":"aqua"}]

# Mettre à jour les scores numériques
execute as @a run scoreboard players operation 💰. Argent HUD = @s argent_banque
execute as @a run scoreboard players operation 🏰 Lieu HUD = @s lieu
execute as @a run scoreboard players operation 🗡 Classe HUD = @s classe

# ============================================
# AFFICHAGE DU JOUR EN TEXTE
# ============================================
# Modifier le displayname de l'objectif "jour" selon le jour actuel
# Cela met à jour automatiquement la ligne "🕒_Jour" dans le HUD

# Réinitialiser tous les jours
scoreboard players reset 🕒 Lundi HUD
scoreboard players reset 🕒 Mardi HUD
scoreboard players reset 🕒 Mercredi HUD
scoreboard players reset 🕒 Jeudi HUD
scoreboard players reset 🕒 Vendredi HUD
scoreboard players reset 🕒 Samedi HUD
scoreboard players reset 🕒 Dimanche HUD

# Afficher le bon jour selon le score
execute as @a[limit=1] if score @s jour matches 1 run scoreboard players set 🕒 Lundi HUD 1
execute as @a[limit=1] if score @s jour matches 2 run scoreboard players set 🕒 Mardi HUD 2
execute as @a[limit=1] if score @s jour matches 3 run scoreboard players set 🕒 Mercredi HUD 3
execute as @a[limit=1] if score @s jour matches 4 run scoreboard players set 🕒 Jeudi HUD 4
execute as @a[limit=1] if score @s jour matches 5 run scoreboard players set 🕒 Vendredi HUD 5
execute as @a[limit=1] if score @s jour matches 6 run scoreboard players set 🕒 Samedi HUD 6
execute as @a[limit=1] if score @s jour matches 7 run scoreboard players set 🕒 Dimanche HUD 7

# Afficher le HUD dans la sidebar
scoreboard objectives setdisplay sidebar HUD

# Copier le score du jour dans le HUD (affichera la valeur avec le bon nom)
#execute as @a run scoreboard players operation "🕒_Jour" HUD = @s jour
