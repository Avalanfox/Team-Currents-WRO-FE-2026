import time
import cv2
import numpy as np

from color_detection_v1 import get_blue_mask, get_orange_mask, get_largest_blob_coords


import time
import cv2
import numpy as np
from color_detection import get_blue_mask, get_orange_mask, get_largest_blob_coords

def main():
    video_stream = cv2.VideoCapture(0)
    video_stream.set(cv2.CAP_PROP_FRAME_WIDTH, 680)
    video_stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 420)
    
    current_state = "DETERMINE_DIRECTION"
    direction = None
    failed_frame_streak = 0
    MAX_ALLOWED_GLITCHES = 10
    
    while True:
        frame_acquired, current_frame = video_stream.read()
        
        if not frame_acquired:
            failed_frame_streak += 1
            if failed_frame_streak >= MAX_ALLOWED_GLITCHES:
                break
            continue
            
        failed_frame_streak = 0
        hsv_image = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)
        
        if current_state == "DETERMINE_DIRECTION":
            blue_mask = get_blue_mask(hsv_image)
            orange_mask = get_orange_mask(hsv_image)
            blue_data = get_largest_blob_coords(blue_mask)
            orange_data = get_largest_blob_coords(orange_mask)
            
            if blue_data is not None:
                direction = "anticlockwise"
                current_state = "RACE"
                
            elif orange_data is not None:
                direction = "clockwise"
                current_state = "RACE"

    video_stream.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

