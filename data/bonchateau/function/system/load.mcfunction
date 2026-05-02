# ============================================
# BONCHATEAU - Chargement du datapack
# Version : 1.21
# ============================================

tellraw @a {"text":"§8§l > §6§l[bonchateau 1.21 07-02-26] §8§l< §7Datapack (re)loaded !"}

# ============================================
# SUPPRESSION DES SCORES HUD
# ============================================
scoreboard players reset * HUD

# ============================================
# CRÉATION DES SCOREBOARDS
# ============================================

# --- Informations joueur ---
scoreboard objectives add argent_banque dummy "Argent en banque"
scoreboard objectives add jour dummy "Jour"
scoreboard objectives add lieu dummy "Lieu"
scoreboard objectives add classe dummy "Classe"

# --- HUD fusionné pour sidebar ---
scoreboard objectives add HUD dummy "Journal"
scoreboard objectives modify HUD displayname "~Journal~"

# --- Temps Minecraft pour le cycle jour/nuit ---
scoreboard objectives add bonchateau_time dummy "Temps Minecraft"

# ============================================
# INITIALISATION DES FAUX JOUEURS HUD
# ============================================
scoreboard players set 💰. Argent HUD 0
scoreboard players set 🏰 Lieu HUD 0
scoreboard players set 🗡 Classe HUD 0

# ============================================
# AFFICHAGE DU HUD À DROITE
# ============================================
scoreboard objectives setdisplay sidebar HUD

# ============================================
# INITIALISATION DES JOUEURS
# ============================================
# Initialiser les scores de tous les joueurs connectés
#execute as @a unless score @s argent_banque matches 0.. run scoreboard players set @s argent_banque 0
#execute as @a unless score @s jour matches 1.. run scoreboard players set @s jour 1
#execute as @a unless score @s lieu matches 0.. run scoreboard players set @s lieu 0
#execute as @a unless score @s classe matches 0.. run scoreboard players set @s classe 0

# ============================================
# SUPPRESSION DES VILLAGEOIS VANILLA
# ============================================
# Supprimer tous les villageois existants (pour éviter les doublons)
kill @e[type=minecraft:villager]

# ============================================
# SPAWN DES PNJ (MODE JOUR PAR DÉFAUT)
# ============================================
time set 0250
function bonchateau:pnj/spawn_jour

# ============================================
# SPAWN DES PNJ
# ============================================
# Générer le banquier
#function bonchateau:banque/spawn_banquier

# Générer tous les PNJ depuis le fichier généré
# (à décommenter quand le fichier sera créé)
# function bonchateau:pnj/bc_pnj_summon

# ============================================
# LANCEMENT DU HUD
# ============================================
function bonchateau:system/affichage_hud

# ============================================
# FIN DU CHARGEMENT
# ============================================
tellraw @a {"text":"§a✔ Système initialisé avec cycle jour/nuit !"}

