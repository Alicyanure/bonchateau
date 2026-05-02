# Reset avancement
#advancement revoke @s only bonchateau:banque/interact_banquier

# Si le joueur a un moyen cristal → dépôt
#execute if entity @s[nbt={SelectedItem:{id:"minecraft:medium_amethyst_bud"}}] run function bonchateau:banque/depot

# Sinon → tentative de retrait
#execute unless entity @s[nbt={SelectedItem:{id:"minecraft:medium_amethyst_bud"}}] run function bonchateau:banque/retrait


# ============================================
# BONCHATEAU - Détection interaction banquier
# ============================================
# Appelé automatiquement par l'advancement

# Révoquer l'advancement pour permettre une nouvelle interaction
advancement revoke @s only bonchateau:banque/interact_banquier_depot

# Vérifier si le joueur a un Peore en main → dépôt
execute if items entity @s weapon.mainhand minecraft:medium_amethyst_bud[custom_data~{bonchateau_monnaie:"peore"}] run function bonchateau:banque/depot/depot_peore
execute if items entity @s weapon.mainhand minecraft:large_amethyst_bud[custom_data~{bonchateau_monnaie:"pedisme"}] run function bonchateau:banque/depot/depot_pedisme
execute if items entity @s weapon.mainhand minecraft:amethyst_cluster[custom_data~{bonchateau_monnaie:"penausme"}] run function bonchateau:banque/depot/depot_penausme
execute if items entity @s weapon.mainhand minecraft:nether_star[custom_data~{bonchateau_monnaie:"penerethisme"}] run function bonchateau:banque/depot/depot_penerethisme

# Sinon → tentative de retrait
#execute unless items entity @s weapon.mainhand minecraft:medium_amethyst_bud[custom_data~{bonchateau_monnaie:"peore"}] run function bonchateau:banque/retrait
