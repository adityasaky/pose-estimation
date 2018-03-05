width = 120
height = 160

width_meters = 40
height_meters = 80

def scalex(x):
    return int(width * (width_meters * 0.5 + x) / width_meters)


def scaley(y):
    return height - 1 - int(height * (height_meters * 0.5 + y) / height_meters)


x = 0
y = -20

print "x -> " + str(scalex(x))
print "y -> " + str(scaley(y))
