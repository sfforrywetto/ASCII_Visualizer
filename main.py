from PIL import Image
import svgwrite
import os

IMAGE_PATH = "input/i.png"
OUTPUT_PATH = "output/output1.svg"
WINDOW_SIZE = (1200, 800)
SCALE = int(input('Put the number of scale: '))  # lower = more detail

def get_brightness(r, g, b):
    return (0.299*r + 0.587*g + 0.114*b) / 255

def main():
    # Load and resize image
    img = Image.open(IMAGE_PATH)
    img = img.resize((WINDOW_SIZE[0] // SCALE, WINDOW_SIZE[1] // SCALE))
    pixels = img.load()
    width, height = img.size

    # Prepare SVG drawing
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    dwg = svgwrite.Drawing(OUTPUT_PATH, size=(WINDOW_SIZE[0], WINDOW_SIZE[1]))
    dwg.viewbox(0, 0, WINDOW_SIZE[0], WINDOW_SIZE[1])

    font_size = 8
    font_family = "Courier"

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y][:3]
            brightness = get_brightness(r, g, b)

            if brightness > 0.1:
                # Choose character based on brightness
                char = "." if brightness < 0.3 else "*" if brightness < 0.6 else "#"
                # Only draw non-black characters
                dwg.add(dwg.text(
                    char,
                    insert=(x * SCALE, y * SCALE),
                    fill="lime",
                    font_size=font_size,
                    font_family=font_family
                ))

    dwg.save()
    print(f"SVG saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
