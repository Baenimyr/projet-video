import math

def IoU(true_box, predicted_box):
    
    xt, yt, wt, ht = true_box
    x, y, w, h = predicted_box
    
    # Get the coordinates of the intersection area
    x_start = max(xt, x)
    y_start = max(yt, y)
    x_end = min(xt + wt, x + w)
    y_end = min(yt + ht, y + h)

    # Compute intersection area
    I = max(0, x_end - x_start) * max(0, y_end - y_start)
    
    # Compute area of each box
    bt_area = wt * ht
    bp_area = w * h
    
    # Compute union of the boxes
    U = bt_area + bp_area - I
    
    # Intersection over union
    return I / U
    
    
def boites_voisines(boite: (int, int, int, int), image_dim: (int, int), pas:int = 5):
    """ Construit un itérateur sur des variations de la boite.
    @param image_dim: dimensions de l'image à ne pas déborder
    """
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dw in (-1, 0, 1):
                for dh in (-1, 0, 1):
                    r = (boite[0] + dx * pas, boite[1] + dy * pas, boite[2] + dw * pas, boite[3] + dh * pas)
                    if r[0] >= 0 and r[1] >= 0 and r[0] + r[2] < image_dim[0] and r[0] + r[3] < image_dim[1] and 0 < r[2] and 0 < r[3]:
                        yield r
