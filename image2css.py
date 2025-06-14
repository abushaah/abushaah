from PIL import Image
import os

def image_to_css(path, pixel_size=1):
    img = Image.open(path).convert('RGB')
    width, height = img.size
    shadows = []

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            hex_color = f'#{r:02x}{g:02x}{b:02x}'
            shadows.append(f'{x * pixel_size}px {y * pixel_size}px {hex_color}')

    box_shadow = ',\n  '.join(shadows)
    css = f'''
            <div class="pixel-art"></div>
            <style>
                .pixel-art {{
                width: {pixel_size}px;
                height: {pixel_size}px;
                box-shadow:
                    {box_shadow};
                }}
            </style>
        '''
    return css

# testing
if __name__ == "__main__":
    input_folder = "images"
    output_folder = "css"

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            image_path = os.path.join(input_folder, filename)
            css_art = image_to_css(image_path)
            output_filename = os.path.splitext(filename)[0] + ".css.html"
            output_path = os.path.join(output_folder, output_filename)

            with open(output_path, "w") as f:
                f.write(image_to_css(".png", pixel_size=5))

            print(f"CSS saved")