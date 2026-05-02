# ============================================
# BONCHATEAU - Cycle jour/nuit des PNJ
# ============================================
# Appelé depuis tick.mcfunction

# MATIN (2000 ticks)
execute if score temps_minecraft bonchateau_time matches 2000 if score @a[limit=1] jour matches 1..5 run function bonchateau:pnj/spawn_jour
execute if score temps_minecraft bonchateau_time matches 2000 if score @a[limit=1] jour matches 6 run function bonchateau:pnj/spawn_samedi_matin
execute if score temps_minecraft bonchateau_time matches 2000 if score @a[limit=1] jour matches 7 run function bonchateau:pnj/spawn_dimanche_matin

# Incrémenter le jour à minuit
execute if score temps_minecraft bonchateau_time matches 0 run function bonchateau:system/incrementer_jour

# SOIR (12000 ticks)
execute if score temps_minecraft bonchateau_time matches 12000 run function bonchateau:pnj/spawn_nuit