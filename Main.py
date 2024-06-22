from PIL import Image
import matplotlib.pyplot as plt

try:
    gambar1 = Image.open('./images/gambar1.jpg')
    gambar2 = Image.open('./images/gambar2.jpg')
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit()


rotated_gambar1 = gambar1.rotate(180)


bw_gambar1 = rotated_gambar1.convert('L')


width1, height1 = bw_gambar1.size
width2, height2 = gambar2.size

new_height = max(height1, height2)
new_width = width1 + width2

combined_image = Image.new('RGB', (new_width, new_height))

combined_image.paste(bw_gambar1, (0, 0))
combined_image.paste(gambar2, (width1, 0))


rotated_gambar1.save('./output/rotated_gambar1.jpg')
bw_gambar1.save('./output/bw_gambar1.jpg')
combined_image.save('./output/combined_image.jpg')


import subprocess
subprocess.run(['xdg-open', './output/rotated_gambar1.jpg'])
subprocess.run(['xdg-open', './output/bw_gambar1.jpg'])
subprocess.run(['xdg-open', './output/combined_image.jpg'])

print("Proses gambar selesai.")
