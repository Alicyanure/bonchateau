# detect_retrait_droit.mcfunction

# Révoquer l'advancement
advancement revoke @s only bonchateau:banque/interact_banquier_retrait_droit

# Vérifier que la main est vide et retirer
execute run function bonchateau:banque/retrait/retrait_peore
