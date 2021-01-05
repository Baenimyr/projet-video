from evaluateBBox import IoU
import math

def evaluate_predictions(bboxes, predictions):
    
    size = len(bboxes)
    assert size == len(predictions)
    
    mean = 0
    minimum = math.inf
    maximum = -math.inf
    
    for i in range(size):
        
        score = IoU(bboxes[i], predictions[i])
        mean += score
        
        if score > maximum: maximum = score
        if score < minimum: minimum = score
            
    
    mean /= size
    
    
    return mean, minimum, maximum


# Test case
if __name__ == "__main__":
    
    mean, mini, maxi = evaluate_predictions([[834, 299, 156, 130], [842, 280, 156, 130], [854, 300, 150, 130]], 
                                            [[834, 298, 156, 130], [842, 296, 156, 130], [854, 300, 156, 130]])

    print(f"Mean IoU = {mean}, Min = {mini} and Max = {maxi}.")