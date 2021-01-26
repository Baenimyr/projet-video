from readBBoxes import *
import cv2


# Tracking function using OpenCV built-in tracker
def tracking(video_filename, bboxes_filename, debug=False, wait_time=10):
    
    predictions = {}
    bboxes = read_bboxes(bboxes_filename)  
    cap = cv2.VideoCapture(video_filename)
    
    # frames start at 1
    frame_number = 1
    tracking = False
    
    tracker = cv2.TrackerKCF_create()
    
    while(cap.isOpened()):
        
        ret, frame = cap.read()
        
        if not ret: break
            
        if tracking or frame_number in bboxes:
            
            # First object detection
            if not tracking:
                assert frame_number in bboxes
                current_bbox = bboxes[frame_number]
                tracking = True
                
                # Init tracker with 1st detection of the object
                tracker.init(frame, current_bbox)
            
            # Tracking
            else:
                
                # Find the new bbox for our object
                ret2, bbox = tracker.update(frame)
                
                # Only update if the tracker actually found the object
                if ret2: 
                    current_bbox = bbox
                    predictions[frame_number] = current_bbox
            
            if debug:
                # Show both computed bbox (green) and real bbox (red)
                x, y, w, h = current_bbox
                xt, yt, wt, ht = bboxes[frame_number]
                disp = frame.copy()
                cv2.rectangle(disp, (x, y), (x+w, y+h), (0, 0, 255), 2)
                cv2.rectangle(disp, (xt, yt), (xt+wt, yt+ht), (0, 255, 0), 2)
                
                cv2.imshow("img", disp)
                cv2.waitKey(wait_time)
                
        frame_number += 1
        
        
    return predictions

if __name__ == "__main__":
    
    predictions = tracking('../VIDEOS/BowlPlace1Subject1.mp4', '../GT/BowlPlace1Subject1_2_bboxes.txt', debug=True)