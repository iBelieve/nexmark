from cairo import Context
import math


def rounded_rect(ctx: Context, x, y, width, height, radius):
    def deg(value):
        return value * math.pi / 180.0

    ctx.new_sub_path()
    ctx.arc(x + width - radius, y + radius, radius, deg(-90), deg(0))
    ctx.arc(x + width - radius, y + height - radius, radius, deg(0), deg(90))
    ctx.arc(x + radius, y + height - radius, radius, deg(90), deg(180))
    ctx.arc(x + radius, y + radius, radius, deg(180), deg(270))
    ctx.close_path()
