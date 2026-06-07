def get_color(h, s, v):
    if v < 50:
        return "black"
    if s < 50 and v > 200:
        return "white"
    if h < 10 or h > 160:
        return "red"
    if 10 <= h < 25:
        return "orange"
    if 25 <= h < 35:
        return "yellow"
    if 35 <= h < 85:
        return "green"
    if 85 <= h < 130:
        return "blue"
    return "unknown"