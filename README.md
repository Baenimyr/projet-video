# Projet Vidéo IA

## Travail effectué

### Réseaux

Dans les fichiers \'01 - \*\' nous avons créé un modèle de classification sur les images d'objets extraits des vidéos. Les réseaux de neurones commencent toujours par un réseau convolutionnel pré-entraîné parce que cela permet de gagner du temps de calcul à l’entraînement et avoir de meilleurs résultats. La classification se fait seulement parmi les 5 catégories d’objets. Le panel complet de classes comme dans ImageNet donne de très mauvais résultats, probablement parce qu’il est difficile de différencier des objets géométriquement proches, surtout sur des images base qualité dans notre cas et beaucoup de catégories sont inutilisées. Finalement, utiliser VGG16 comme réseau convolutionnel donne de très bon résultats (on utilise la métrique recall pour la classification).


### Tracking
Nous avons implémenté deux versions pour le tracking, une simple qui déplace la fenêtre autour de sa position, et une autre basée sur le diamond search.

### Tracker OpenCV

Le fichier `./utils/trackerCv.py` implemente le tracking avec un tracker fourni par OpenCV. 
Etant donné une vidéo et les annotations (bboxes ground truth) associé la fontion `tracking` calcul à partir de la première box du fichier d'annotations les suivantes.
Il est possible de passer en mode `debug` pour visualiser les vraies bboxes (rouge) et celles calculées (vert) par le tracker OpenCV.
Il est possible de tester la fontion en lançant sur la vidéo d'exemple avec : `python3 trackerCv.py` dans le dossier `utils`. On observe que le résultat sur la vidéo de test n'est pas très satisfaisant.

### Ce qui ne fonctionne pas
- l'ébauche d'implémentation de move-to-data, le problème bloquant est l'isolation de la couche de sortie

## Pistes d'améliorations 

Du côté du tracking avec les trackers OpenCV, notre implémentation utilise le tracker KCF d'open CV qui donne sur la vidéo de test un résultat peu satisfaisant, cependant il y a d'autres trackers disponibles que nous n'avons pas testé (BOOSTING, MIL,...) et qui pourraient potentiellement donner de mailleurs résultats.
Pour la classification, il serait peut être utile de rajouter une dernière catégorie 'autre' pour que le RN apprenne à différencier les objets du décor et sache mieux les positionner sur l’image globale.