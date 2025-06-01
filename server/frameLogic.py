# this is where we handle the physical inputs for the InkyImpression screen

from imageData import ImageRequest


def display_image(image: ImageRequest):
    # This function will display the image on the InkyImpression screen
    # You can use the InkyImpression library to display the image
    print(f"Displaying image: {image.file_name}")