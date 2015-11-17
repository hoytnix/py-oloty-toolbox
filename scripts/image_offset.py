resolution = (1920, 1080)

images = [
    (810, 0)
]

for image in images:
    x = resolution[0] - image[0]
    x /= 2

    y = resolution[1] - image[1]
    y /= 2

    print(x, y)
