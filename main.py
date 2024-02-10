from PIL import Image

def scale_image(input_image_path, inverse, new_width):
    keyboard_characters = [
        " ",".",",","-","~",":",";","=","!","*","#","$","@"
    ]
    with Image.open(input_image_path) as img:
        original_width, original_height = img.size
        aspect_ratio = original_height / original_width
        # Adjust aspect ratio for character dimensions
        char_aspect_ratio = 1.5  # Approximate aspect ratio of a character (height/width)
        new_height = int((new_width * aspect_ratio) / char_aspect_ratio)
               
        # Resize the image using the LANCZOS filter for high-quality downsampling
        new_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        if inverse.upper() == "Y":
            keyboard_characters = keyboard_characters[::-1]

        new_img = new_img.convert('L')
        pixel_map = new_img.load()
        width, height = new_img.size
        scale = 255 / (len(keyboard_characters) - 1)
        output = []

        for j in range(height):
            row = ""
            for i in range(width):
                # Ensure the value is within the bounds of keyboard_characters
                value = int(pixel_map[i, j] / scale)
                value = min(value, len(keyboard_characters) - 1)  
                character = keyboard_characters[value]
                row += character
            output.append(row)

        # Join the rows and print the ASCII art
        output_str = "\n".join(output)
        print(output_str)

def main():
    filepath = input("Type the file path to the image file: ")
    inverse = input("Do you want to invert the image (Y)es/(N)o: ")
    size = input("How wide (number of pixels) would you like the image to be: ")
    size = int(size)
    print("_" * size)
    scale_image(filepath, inverse, size)
    print("_" * size)

main()
