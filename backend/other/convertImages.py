import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode("utf-8")
    return base64_string

# Replace 'path/to/your/photo.jpg' with the actual path to your image file
image_path = 'Images/Drinks/Nikka From The Barrel.jpeg'
base64_string = image_to_base64(image_path)

print(base64_string)