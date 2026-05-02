# ============================================
# BONCHATEAU - Tick principal (exécuté 20x/sec)
# ============================================
# ⚠️ Ce fichier doit rester LÉGER pour éviter le lag

# Mise à jour du temps Minecraft
execute store result score temps_minecraft bonchateau_time run time query daytime

# Mise à jour du HUD pour tous les joueurs
function bonchateau:system/affichage_hud

# Gestion du cycle jour/nuit des PNJ
function bonchateau:pnj/cycle_jour_nuit
