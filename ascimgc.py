import ascii_magic
from PIL import Image


art = ascii_magic.from_image_file(
    "Image path here",
    columns=300,
    width_ratio=2,
    mode=ascii_magic.Modes.HTML
    )
ascii_magic.to_html_file("your_name_file.html", art)

# art = ascii_magic.from_image(img, columns=90)
# ascii_magic.to_terminal(art)