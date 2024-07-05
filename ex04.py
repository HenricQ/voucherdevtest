def segs(hor, min, seg):
    seg += hor * 3600 + min * 60

    return seg


print(segs(2, 48, 13))