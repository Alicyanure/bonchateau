# Bonchateau - Minecraft 1.21


#### Notes de version 1.21 ####

Dans cette branche compatible en 1.21, on trouve les modules suivants :
# PNJ
  ->  Vous pouvez aire spawn des pnj customs à partir d'un ichier csv. Le fichier est simplifié et vous permet une customisation très poussée ! Par défaut, les pnj de Bonchateau sont créés par ce module.
# BANQUE
  ->  Des pnj banquiers peuvent spawnés. Ils permettent d'intéragir avec votre banque ! Vous pouvez déposer vos améthistes dans votre coffre numérique ou retirer de l'argent !
# MONNAIE
  ->  La monnaie de Bonchateau utilise des amétistes renomées (petite amétiste = pert = 10 centimes, moyenne amétiste = peore = 1 euro...) Les pnj savent les manipuler en tant qu'entités et les joueurs peuvent les convertirs eux-mêmes !

Prochains modules à venir : système de quêtes en intéraction avec les pnj.


#### Notes GitHub ####

Générer clef ssh : ssh-keygen -t rsa -b 4096 -C "PC-fixe-Mathilde"

Lire clef : cat ~/.ssh/id_rsa.pub 
=> tout copier (même commande et nom à la fin) 
=> à coller dans Github => >Settings => SSH Keys

Cloner le projet où tu veux : git clone git@github.com:Alicyanure/bonchateau.git

Statut, pour voir la diff entre local et en ligne : git st ou git statut

Lire le répertoire actuel : ls

Se déplacer : cd ./

Sauvegarder tout : git add .
Sauvegarder une partie : git add /chemin/nom_fichier ou nom_dossier

Préparer la sauvegarde à envoyer : git commit -m "le commentaire"

Envoyer la sauvegarde  (se positionner sur la bonne branche) : git push (après un "commit --amend") ajouter : --force 

Récupérer la sauvegarde (se positionner sur la bonne branche) : git pull

Créer une nouvelle branche et se positionner dessus : git co -b "nom_branche"    (co = check out)

Changer de branche : git co "nom_branche"

Metre à jour la branche secondaire par rapport à la branche principale (se positionner sur la branche secondaire) : git rebase "nom_branche_principale"
=> puis résoudre les conflits
=> puis : git rebase --continue
=> puis : git push force

Importer la branche secondaire sur la branche principale (se positionner sur la branche principale) : git merge "nom_branche_secondaire"
