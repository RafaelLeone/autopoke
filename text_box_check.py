import cv2


def is_text_box(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Define a threshold value (adjust as needed)
    threshold_value = 200
    
    # Create a binary image based on the threshold
    _, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
    
    # Count the number of white pixels in the binary image
    white_pixel_count = cv2.countNonZero(binary_image)
    
    # If there are enough white pixels, consider it a battle
    if white_pixel_count > 100000:
        return True
    else:
        return False
