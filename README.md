# Projet Vidéo IA

## Travail effectué

### Tracker OpenCV

Le fichier `./utils/trackerCv.py` implemente le tracking avec un tracker fourni par OpenCV. 
Etant donné une vidéo et les annotations (bboxes ground truth) associé la fontion `tracking` calcul à partir de la première box du fichier d'annotations les suivantes.
Il est possible de passer en mode `debug` pour visualiser les vraies bboxes (rouge) et celles calculées (vert) par le tracker OpenCV.
Il est possible de tester la fontion en lançant sur la vidéo d'exemple avec : `python3 trackerCv.py` dans le dossier `utils`. On observe que le résultat sur la vidéo de test n'est pas très satisfaisant.


## Pistes d'améliorations 

Du côté du tracking avec les trackers OpenCV, notre implémentation utilise le tracker KCF d'open CV qui donne sur la vidéo de test un résultat peu satisfaisant, cependant il y a d'autres trackers disponibles que nous n'avons pas testé (BOOSTING, MIL,...) et qui pourraient potentiellement donner de mailleurs résultats.
