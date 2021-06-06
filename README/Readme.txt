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

Côté application :

En allumant l'application, vous avez la possibilité de vous connecter, ou de créer un compte si cela n'est pas déjà fait (l'adresse email ne doit pas déjà être utilisée par quelqu'un, un test est en place pour le vérifier. De plus, un test est présent pour vérifier si le mot de passe est le bon).

Une fois connecté, vous arrivez sur la page d'accueil. Cette dernière, comme la plupart des pages de l'application, possède la possibilité de naviguer parmis 3 pages sur la gauche : la page d'accueil, la page de recherche ainsi que la page de gestion de compte.

La page d'accueil :

Cette page donne la possibilité de naviguer parmi les musiques les plus écoutées / les playlists les plus écoutées / votre playlist likée.

La page de recherche :

Cette page donne la possibilité de rechercher un artiste ou une musique, mais également de voir les albums de ses artistes préférés. (en cliquant sur chacun des boutons, il est possible d'accéder à la page associée)

La page de gestion de compte :

Cette page offre la possibilité de modifier son compte, c'est-à-dire son mot de passe, ou de le supprimer, mais également de se déconnecter.

Chaque artiste possède sa propre page avec ses différents albums. En cliquant sur un album, on peut accéder à ses différentes musiques, et en cliquant sur les boutons de musiques, nous pouvons les écouter.

La musique apparaît en bas à gauche. Le titre et l'artiste est noté en dessous de la cover de l'album. De plus, un slider permet de naviguer dans la musique, et un timer dynamique y est présent.
Le bouton pause permet de mettre en pause la musique, la flèche de droite, de lire la musique suivante dans l'album, celle de gauche, la précédente, et le bouton like permet de mettre la musique dans sa playlist des musiques like (il est possible de la retirer en re-appuyant dessus).

Le nombre de streams des albums est égal à la somme des streams de chaque musique de ce dernier et chaque musique possède son propre nombre de streams.

Côté administrateur :

L'administrateur possède son propre pannel qui possède 5 pages.

La première page donne la possibilité d'ajouter toutes les musiques d'un coup (fonction qui automatise l'ajout de musique en lisant justement l'arborescence et en ajoutant chacune des musiques avec toutes ses données dans la base de données), ou alors d'ajouter les musiques en rentrant tous les champs nécessaires : titre ; artiste ; album ; type ; chemin de la musique ; chemin de l'image de la cover de l'album.

La deuxième page permet de supprimer toutes les musiques d'un coup ou une seule en rentrant son titre, son artiste et son album.

La troisième page donne la possibilité de voir la base de données liée aux musiques et de rechercher les informations d'une musique en particulier (se fait dans le terminal)

La quatrième page donne la possibilité de supprimer un membre (en rentrant son mail) ou tous les membres d'un coup.

La cinquièe page donne la possibilité de voir la base de données liée aux membres et de rechercher les informations d'un membre en particulier (se fait dans le terminal)

À NOTER :

Les musiques doivent être en format .ogg, chacune des musiques doit être en mono (et non stéréo). De plus, l'arborescence doit être respectée, comme les vidéos le montre dans le dossier README, c'est-à-dire, chaque musique doit être dans le dossier qui porte le nom de l'album, lui-même dans le dossier portant le nom de son artiste. De plus l'image , c'est-à-dire, la cover de l'album doit être dans le même dossier, avec pour format .jpg, et doit-être carrée. De plus, le fichier description.txt ne doit comporter qu'une ligne, sans espace avec le type de musique que l'album comporte.


Erreur possible : 


En cas d’erreur lors du lancement du projet au niveau des imports il faut supprimer les “blabla” qui corresponde à : “ from blabla.truc import chose”
Nous avons eu cette erreur et nous nous sommes aperçus que l’IDE considérait ces mots-clefs comme un package et non comme un répertoire comme on le voulait. Ce qui explique l’utilisation de git uniquement pour du versionning projet.
