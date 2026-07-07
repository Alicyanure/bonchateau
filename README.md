# Bonchateau - Minecraft 1.21


#### Notes de version 1.21 ####

Dans cette branche compatible en 1.21, on trouve les modules suivants :
# PNJ
  ->  Vous pouvez faire spawn des pnj customs à partir d'un fichier csv. Le fichier est simplifié et vous permet une customisation très poussée ! Par défaut, les pnj de Bonchateau sont créés par ce module.
# BANQUE
  ->  Des pnj banquiers peuvent spawnés. Ils permettent d'interagir avec votre banque ! Vous pouvez déposer vos améthystes  dans votre coffre numérique ou retirer de l'argent !
# MONNAIE
  ->  La monnaie de Bonchateau utilise des améthystes renommées (petite améthyste = pert = 10 centimes, moyenne améthyste = peore = 1 euro...) Les pnj savent les manipuler en tant qu'entités et les joueurs peuvent les convertir eux-mêmes !
# AFFICHAGE
  ->  Affiche en continu à droite de l'écran : l'argent en banque, le jour de la semaine sur lequel est calé le cycle de vie des pnj.
# CYCLE DE VIE
  ->  Chaque pnj dort chez lui la nuit, auprès de son/sa partenaire de vie et de ses enfants. Le matin, ils se lèvent et profitent ensemble de leur temps libre. La journée, les enfants sont à l'école et les adultes travaillent. Et les week-ends ? Repos ! Ce cycle donne vie à la ville de Bonchateau et rend votre expérience immersive.

Prochains modules à venir : système de quêtes en interaction avec les pnj.


#### Version 1.21 Release Notes ####

This branch, compatible with Minecraft 1.21, includes the following modules:
# NPC
  ->  You can spawn custom NPCs from a CSV file. The file format is simplified while allowing extensive customization! By default, all Bonchateau NPCs are created using this module.
# BANK
  ->  Banker NPCs can spawn. They allow players to interact with their bank! You can deposit your amethysts into your digital vault or withdraw money!
# CURRENCY
  ->  Bonchateau's currency uses renamed amethysts (Small Amethyst = Pert = €0.10, Medium Amethyst = Peore = €1.00...). NPCs can handle them as entities, and players can exchange them themselves!
# DISPLAY
  ->  Continuously displays on the right side of the screen: your bank balance and the current day of the week used by the NPC life cycle.
# LIFE CYCLE
  ->  Every NPC sleeps at home during the night with their life partner and children. In the morning, they wake up and enjoy some free time together. During the day, children go to school while adults work. And on weekends? They rest! This cycle brings the town of Bonchateau to life and makes your experience more immersive.

Upcoming modules: Quest system with NPC interactions.


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
