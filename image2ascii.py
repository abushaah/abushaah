from PIL import Image
import os

# most common ASCII characters used for density, dark to light
ASCII_CHARS = "@%#*+=-:. "

def image_to_ascii(path, new_width=112):
    img = Image.open(path).convert("L")
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    img = img.resize((new_width, new_height))

    pixels = img.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel * (len(ASCII_CHARS) - 1) // 255] for pixel in pixels])

    ascii_lines = [ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width)]
    return "\n".join(ascii_lines)

# testing
if __name__ == "__main__":
    input_folder = "images"
    output_folder = "ascii"

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            image_path = os.path.join(input_folder, filename)
            ascii_art = image_to_ascii(image_path)
            output_filename = os.path.splitext(filename)[0] + ".txt"
            output_path = os.path.join(output_folder, output_filename)

            with open(output_path, "w") as f:
                f.write("```\n" + ascii_art + "\n```")

            print(f"ASCII saved")