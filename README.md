# Projet Vidéo IA

## Réseaux

Dans les fichiers \'01 - \*\' nous avons créé un modèle de classification sur les images d'objets extraits des vidéos. Les réseaux de neurones commencent toujours par un réseau convolutionnel pré-entraîné parce que cela permet de gagner du temps de calcul à l’entraînement et avoir de meilleurs résultats. La classification se fait seulement parmi les 5 catégories d’objets. Le panel complet de classes comme dans ImageNet donne de très mauvais résultats, probablement parce qu’il est difficile de différencier des objets géométriquement proches, surtout sur des images base qualité dans notre cas et beaucoup de catégories sont inutilisées. Finalement, utiliser VGG16 comme réseau convolutionnel donne de très bon résultats (on utilise la métrique recall pour la classification).


## Tracking
Nous avons implémenté deux versions pour le tracking, une simple qui déplace la fenêtre autour de sa position, et une autre basée sur le diamond search.

### Tracker OpenCV

Le fichier `./utils/trackerCv.py` implémente le tracking avec un tracker fourni par OpenCV. 
Étant donné une vidéo et les annotations (bboxes ground truth) associé la fontion `tracking` calcul à partir de la première box du fichier d'annotations les suivantes.
Il est possible de passer en mode `debug` pour visualiser les vraies bboxes (rouge) et celles calculées (vert) par le tracker OpenCV.
Il est possible de tester la fontion en lançant sur la vidéo d'exemple avec : `python3 trackerCv.py` dans le dossier `utils`. On observe que le résultat sur la vidéo de test n'est pas très satisfaisant.

#### Ce qui ne fonctionne pas
- l'ébauche d'implémentation de move-to-data, le problème bloquant est l'isolation de la couche de sortie

### Traqueur par recherche locale
Le fichier `03 - Tracking.ipynb` tente de suivre les objets dans la vidéo en utilisant les réseaux précédant pour évaluer les boites englobantes.

La boite englobante précédante est utilisée comme point de départ.
Elle est modifiée de n pixels selon les 4 dimensions (x, y, hauteur, largeur) et les candidates sont évaluées par un réseau de classification.
La candidate qui maximise la catégorie est choisie pour la prochaine itération.
Quand le minimimum est trouvée, la taille des modification est diminuée pour raffiner le résultat.

Le problème est que le réseau de classification peut désigner l'objet avec certitude (1.0) même quand il n'est que partiellement englobé.
Donc la boite englobante suit l'objet traqué mais ne donne pas la boite englobante optimale.


## Pistes d'améliorations 

Du côté du tracking avec les trackers OpenCV, notre implémentation utilise le tracker KCF d'open CV qui donne sur la vidéo de test un résultat peu satisfaisant, cependant il y a d'autres trackers disponibles que nous n'avons pas testé (BOOSTING, MIL,...) et qui pourraient potentiellement donner de mailleurs résultats.
Pour la classification, il serait peut être utile de rajouter une dernière catégorie 'autre' pour que le RN apprenne à différencier les objets du décor et sache mieux les isoler sur l’image globale.