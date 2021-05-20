# Create a function that returns the number of frames shown in a give number of
# minutes for a dertain FPS.
def frames(minutes, fps):
    return (minutes * 60) * fps

a = frames(1, 1)
print(a)

a = frames(10, 1)
print(a)

a = frames(10, 25)
print(a)
