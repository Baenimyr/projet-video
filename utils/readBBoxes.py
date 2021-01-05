
# Function reading a bboxes file and returning a dictionnary of the bboxes found for each frame containing one 
def read_bboxes(bboxes_filename):
    
    bboxes = {}
    
    with open(bboxes_filename) as fp: 
        lines = fp.readlines() 
        
        for line in lines: 
            elts = line.split()
            
            if len(elts) == 2:
                assert(elts[1] == "0")
            else:
                assert(len(elts) > 2)
                assert(elts[1] == "1") 
                
                frame_number = (int)(elts[0])
                x = (int)(elts[2])
                y = (int)(elts[3])
                w = (int)(elts[4])
                h = (int)(elts[5])
                bboxes[frame_number] = (x, y, w, h)
                
    return bboxes



if __name__ == "__main__":
    
    bboxes = read_bboxes('../GT/BowlPlace1Subject1_2_bboxes.txt')

