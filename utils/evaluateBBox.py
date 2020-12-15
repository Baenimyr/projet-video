import math

def IoU(true_box, predited_box):
    
    xt, yt, wt, ht = true_box
    x, y, w, h = predited_box
    
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