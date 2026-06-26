import cv2
import numpy as np

COLOR_THRESHOLDS = {
    "green": [
        (np.array([40, 80, 60]), np.array([85, 255, 255]))
    ],
    "red": [
        (np.array([0, 120, 70]), np.array([10, 255, 255])),
        (np.array([170, 120, 70]), np.array([179, 255, 255]))
    ],
    "orange": [
        (np.array([5, 150, 100]), np.array([20, 255, 255]))
    ],
    "blue": [
        (np.array([100, 100, 60]), np.array([130, 255, 255]))
    ]
}

def get_green_mask(hsv_image):
    lower_bound, upper_bound = COLOR_THRESHOLDS["green"][0]
    green_mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
    return green_mask

def get_red_mask(hsv_image):
    
    low_red_lower, low_red_upper = COLOR_THRESHOLDS["red"][0]
    mask_low = cv2.inRange(hsv_image, low_red_lower, low_red_upper)

    high_red_lower, high_red_upper = COLOR_THRESHOLDS["red"][1]
    mask_high = cv2.inRange(hsv_image, high_red_lower, high_red_upper)

    red_mask = cv2.bitwise_or(mask_low, mask_high)
    return red_mask

def get_orange_mask(hsv_image):
    lower_bound, upper_bound = COLOR_THRESHOLDS["orange"][0]
    orange_mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
    return orange_mask

def get_blue_mask(hsv_image):
    lower_bound, upper_bound = COLOR_THRESHOLDS["blue"][0]
    blue_mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
    return blue_mask

def get_largest_blob_coords(binary_mask, min_surface_area=300):
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None
    
    largest_contour = max(contours, key=cv2.contourArea)
    if area < min_surface_area:
        return None
    
    x, y, width, height = cv2.boundingRect(largest_contour)
    return (x, y, width, height, area)
