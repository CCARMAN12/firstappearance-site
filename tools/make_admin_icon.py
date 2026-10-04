"""The admin mark: ascending bars on the palette's green.

Deliberately not the envelope. The two apps sit next to each other in the Dock
at 32px, and the same glyph in two teals is indistinguishable at that size --
the ground alone is not enough separation. Bars also say what the page is: the
admin view is revenue and pipeline, not mail.
"""
from PIL import Image, ImageDraw

SCALE = 4
S = 1024 * SCALE
U = S / 32
GREEN = (0x1F, 0x5F, 0x3A, 255)
WHITE = (0xFF, 0xFF, 0xFF, 255)

img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
d.rounded_rectangle([0, 0, S - 1, S - 1], radius=int(6 * U), fill=GREEN)

# three bars, ascending, sharing one baseline
BASE = 23.5
for x, top in ((8.5, 17.5), (14.5, 13.5), (20.5, 8.5)):
    d.rounded_rectangle([x * U, top * U, (x + 3) * U, BASE * U],
                        radius=int(0.9 * U), fill=WHITE)

img.resize((1024, 1024), Image.LANCZOS).save("admin-1024.png")
print("drew admin-1024.png")
