import hashlib
import math

from gi.repository import Gio, GLib, GdkPixbuf


# From http: // en.wikipedia.org / wiki / HSL_and_HSV  # From_luma.2Fchroma.2Fhue
# Note that not all values are in the RGB gamut!
# Ported from Beru ebook reader
def hcy(h, c, y):
    hp = h * 6
    x = c * (1 - abs(hp % 2 - 1))
    r = 0
    g = 0
    b = 0
    if hp < 1:
        r = c
        g = x
    elif hp < 2:
        r = x
        g = c
    elif hp < 3:
        g = c
        b = x
    elif hp < 4:
        g = x
        b = c
    elif hp < 5:
        r = x
        b = c
    else:
        r = c
        b = x

    yr = 0.30
    yg = 0.59
    yb = 0.11

    m = y - (yr * r + yg * g + yb * b)

    return '#' + to_hex(r + m,) + to_hex(g + m,) + to_hex(b + m,)


def hcyrel(h, c, y):
    hp = h * 6
    yr = 0.30
    yg = 0.59
    yb = 0.11

    if hp < 1:
        a = yr
        b = yg
        c = yb
        ht = hp
    elif hp < 2:
        a = yg
        b = yr
        c = yb
        ht = 2 - hp
    elif hp < 3:
        a = yg
        b = yb
        c = yr
        ht = hp - 2
    elif hp < 4:
        a = yb
        b = yg
        c = yr
        ht = 4 - hp
    elif hp < 5:
        a = yb
        b = yr
        c = yg
        ht = hp - 4
    else:
        a = yr
        b = yg
        c = yb
        ht = 6 - hp
    c_max = min(y / (a + b * ht), (1 - y) / (b * (1 - ht) + c))
    return hcy(h, c * c_max, y)


def to_hex(v):
    if v < 0 or v > 1:
        raise Exception('Out of gamut')
    v = pow(v, 1 / 2.2)
    s = format(round(v * 255), 'X')
    if len(s) == 1:
        s = '0' + s
    return s


def get_matrix(md5):
    angle = int(md5[2:4], 16) / 256 * 2 * math.pi
    cos = math.cos(angle)
    sin = math.sin(angle)
    x = int(md5[4:6], 16) / 256 * 360
    y = int(md5[6:8], 16) / 256 * 540
    return ','.join(map(str, [cos, sin, -sin, cos, x, y]))


def get_cover(title, size=None):
    md5 = hashlib.md5(title.encode('utf-8')).hexdigest()
    hue = int(md5[:2], 16) / 256
    matrix = get_matrix(md5)

    text_color = hcy(0.167, 0.051, 0.051)
    highlight_color = hcy(hue, 0.35, 0.39)
    background_color = hcy(hue, 0.25, 0.25)
    bind_color = hcyrel(hue, 0.5, 0.03)

    resource = Gio.resources_lookup_data(
        '/io/mspencer/Nexmark/cover.svg', Gio.ResourceFlags.NONE)
    svg_template = resource.get_data().decode('utf-8')

    svg = svg_template.format(text_color=text_color,
                              highlight_color=highlight_color,
                              background_color=background_color,
                              bind_color=bind_color,
                              matrix=matrix,
                              title=title)

    stream = Gio.MemoryInputStream.new_from_bytes(
        GLib.Bytes.new(svg.encode('utf-8')))
    if size is not None:
        return GdkPixbuf.Pixbuf.new_from_stream_at_scale(stream,
                                                         width=size, height=size, preserve_aspect_ratio=True,
                                                         cancellable=None)
    else:
        return GdkPixbuf.Pixbuf.new_from_stream(stream, None)


if __name__ == '__main__':
    get_cover('Hello, world')
    get_cover('In His Steps')
