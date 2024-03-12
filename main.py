import cv2


def convert_to_sketch(image_path, output_path='sketch.png'):

    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)

    # Apply GaussianBlur to the inverted image
    blurred_image = cv2.GaussianBlur(inverted_image, (111, 111), 0)

    # Invert the blurred image
    inverted_blurred_image = cv2.bitwise_not(blurred_image)

    # Sketch by dividing the grayscale image by the inverted blurred image
    sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)


    # Save the sketch
    cv2.imwrite(output_path, sketch)


# Example usage:
convert_to_sketch('img.jpg')
