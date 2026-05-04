# Bonchateau

/!\ A modifier avant de rendre publique /!\

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
