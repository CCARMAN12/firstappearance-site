"""The First Appearance desktop mark, drawn to the site's own favicon geometry.

Rasterised rather than converted: cairosvg wants a system cairo this machine
may not have, and the mark is four shapes. Drawn at 4x and downsampled, which
is what gives the stroke its clean edge at 16px.
"""
from PIL import Image, ImageDraw

SCALE = 4
S = 1024 * SCALE
U = S / 32          # the favicon's viewBox unit
TEAL = (0x1F, 0x4E, 0x5F, 255)
WHITE = (0xFF, 0xFF, 0xFF, 255)

img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)

# the rounded square
d.rounded_rectangle([0, 0, S - 1, S - 1], radius=int(6 * U), fill=TEAL)

stroke = max(1, int(2.1 * U))
# envelope body
d.rounded_rectangle(
    [7.5 * U, 11 * U, 24.5 * U, 22.5 * U],
    radius=int(1 * U), outline=WHITE, width=stroke)
# the flap
d.line([(9 * U, 12.2 * U), (16 * U, 17.6 * U), (23 * U, 12.2 * U)],
       fill=WHITE, width=stroke, joint="curve")
# round the flap's ends, which ImageDraw.line leaves square
r = stroke / 2
for x, y in ((9 * U, 12.2 * U), (23 * U, 12.2 * U)):
    d.ellipse([x - r, y - r, x + r, y + r], fill=WHITE)

img.resize((1024, 1024), Image.LANCZOS).save("icon-1024.png")
print("drew icon-1024.png")

# Build a clickable desktop app from this icon:
#
#   for sz in 16 32 64 128 256 512 1024; do
#     sips -z $sz $sz icon-1024.png --out "fa.iconset/icon_${sz}x${sz}.png"
#   done
#   # rename the doubled sizes to the @2x names, then:
#   iconutil -c icns fa.iconset -o FirstAppearance.icns
#   osacompile -o "~/Desktop/First Appearance Live.app" \
#     -e 'open location "https://firstappearance.us"'
#   cp FirstAppearance.icns "<app>/Contents/Resources/applet.icns"
#
# Then DELETE Contents/Resources/Assets.car and the CFBundleIconName key.
# macOS prefers Assets.car over the .icns, so leaving it keeps the generic
# AppleScript icon no matter what you put in applet.icns.
