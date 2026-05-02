# ============================================
# BONCHATEAU - Spawn automatique des PNJ
# Généré automatiquement depuis bc_pnj.csv
# NE PAS MODIFIER MANUELLEMENT CE FICHIER
# ============================================

# PNJ : Lilian Diemert (0001)
summon minecraft:villager 364 76 748 {Tags:["pnj_bonchateau","pnj_0001"],CustomName:'{"text":"Lilian Diemert","color":"white","bold":true}',CustomNameVisible:1b,NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,IsBaby:0b,VillagerData:{profession:"minecraft:fisherman",level:5,type:"minecraft:snow"},Offers:{Recipes:[{buy:{id:"minecraft:medium_amethyst_bud",count:1,components:{"minecraft:custom_name":'{"text":"Peore","color":"light_purple","italic":false}',"minecraft:lore":['{"text":"Monnaie","color":"gray","italic":false}'],"minecraft:custom_data":{bonchateau_monnaie:"peore",bonchateau_valeur:1}}},buyB:{id:"minecraft:small_amethyst_bud",count:3,components:{"minecraft:custom_name":'{"text":"Pert","color":"light_purple","italic":false}',"minecraft:lore":['{"text":"Monnaie","color":"gray","italic":false}'],"minecraft:custom_data":{bonchateau_monnaie:"pert",bonchateau_valeur:0.11}}},sell:{id:"minecraft:cod",count:2},maxUses:999999,uses:0,rewardExp:0b},{buy:{id:"minecraft:small_amethyst_bud",count:5,components:{"minecraft:custom_name":'{"text":"Pert","color":"light_purple","italic":false}',"minecraft:lore":['{"text":"Monnaie","color":"gray","italic":false}'],"minecraft:custom_data":{bonchateau_monnaie:"pert",bonchateau_valeur:0.11}}},sell:{id:"minecraft:string",count:1},maxUses:999999,uses:0,rewardExp:0b}]}}

# ============================================
# FIN DU FICHIER
# ============================================
tellraw @a {"text":"§a✔ 1 PNJ(s) spawné(s) avec succès !"}