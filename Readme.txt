Démarrage :


Projet développé en python3.9.


Pour le lancement :


“python main.py”


Librairies requises : 
-pygame
-PyQt5
-mutagen


Pour les installer utilisez : “pip install pygame”


Bon fonctionnement et guide d’utilisation :


Lorsque vous lancez le projet vous devrez vous connecter. Si vous ne possédez pas de compte vous devrez en créer un. Pourquoi faire ? Pour que tout ce que vous faites sur l’application soit lié à votre compte et dans ce cas vous garderez vos musiques aimées, vos playlist.


Une fois connectée vous aurez la possibilité de lancer des musiques parmi celles disponibles dans la base de données. 


Vous pourrez mettre un j’aime sur les musiques que vous préférez afin de les retrouver plus tard dans la rubrique prévu à cet effet (playlist de musiques likées).


Vous aurez la possibilité de modifier le volume, ainsi que de naviguer dans la musique au timer que vous souhaitez.


Des playlists se créent automatiquement en fonction de l’auteur et du nom de l’album quand les musiques sont importées.


Vous aurez aussi la possibilité de changer de mot de passe quand vous serez connecté.


Il existe aussi une barre pour rechercher les musiques. On peut les trouver en fonction du nom de la musique et du nom de l’auteur.


Il y a la possibilité de supprimer son compte si on le souhaite aussi.


La base de données se compose de trois classes: Utilisateurs, musiques et musiques likées.


Erreur possible : 


En cas d’erreur lors du lancement du projet au niveau des imports il faut supprimer les “blabla” qui corresponde à : “ from blabla.truc import chose”
Nous avons eu cette erreur et nous nous sommes aperçus que l’IDE considérait ces mots-clefs comme un package et non comme un répertoire comme on le voulait. Ce qui explique l’utilisation de git uniquement pour du versionning projet.