from evaluateBBox import IoU
import math

# Computes important IoU values for given ground truth bboxes and predictions 
# (dictionary{frame_nb:bbox})
def evaluate_predictions(bboxes, predictions):
    
    size = len(bboxes)
    assert size == len(predictions)
    assert bboxes.keys() == predictions.keys()
    
    mean = 0
    minimum = math.inf
    maximum = -math.inf
    
    for key in bboxes.keys():
        
        score = IoU(bboxes[key], predictions[key])
        mean += score
        
        if score > maximum: maximum = score
        if score < minimum: minimum = score
            
    
    mean /= size
    
    
    return mean, minimum, maximum


# Test case
if __name__ == "__main__":
    
    mean, mini, maxi = evaluate_predictions({1:[834, 299, 156, 130], 3:[842, 280, 156, 130], 4:[854, 300, 150, 130]}, 
                                            {1:[834, 298, 156, 130], 3:[842, 296, 156, 130], 4:[854, 300, 156, 130]})

    print(f"Mean IoU = {mean}, Min = {mini} and Max = {maxi}.")