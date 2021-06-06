# GLPOOTD

Projet développé en python3.9.

Pour le lancement :


“python main.py”


Librairies requises : 
-pygame
-PyQt5
-mutagen


Pour les installer utilisez : “pip install pygame”


Bon fonctionnement et guide d’utilisation :

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


Erreur possible : 


En cas d’erreur lors du lancement du projet au niveau des imports il faut supprimer les “blabla” qui corresponde à : “ from blabla.truc import chose”
Nous avons eu cette erreur et nous nous sommes aperçus que l’IDE considérait ces mots-clefs comme un package et non comme un répertoire comme on le voulait. Ce qui explique l’utilisation de git uniquement pour du versionning projet.
