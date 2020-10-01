# import numpy as np
# from PIL import Image

# img1 = Image.open('1.png').convert('RGBA')
# img2 = Image.open('2.png').convert('RGBA')

# arr1 = np.array(img1)
# arr2 = np.array(img2)

# # record the original shape
# shape1 = np.matrix(arr1.ravel())
# shape2 = np.matrix(arr2.ravel())
# print(shape1[0][0][0])
# print(shape2[0][0][0])


from scipy import misc
from PIL import Image
arr1 = misc.imread('1.png')
arr2 = misc.imread('2.png')
# print(arr1[20, 30])
# print(arr2[20, 30])

diff = [ [0]*900 for i in [0]*900]

def isDiff(a, b):
#   print(','.join(str(a)))
#   print(','.join(str(b)))
#   print(abs(int(a[0]) - int(b[0])))
#   print(abs(int(a[1]) - int(b[1])))
#   print(abs(int(a[2]) - int(b[2])))
  if abs(int(a[0]) - int(b[0])) < 20 and abs(int(a[1]) - int(b[1])) < 20 and abs(int(a[2]) - int(b[2])) < 20:
  # distance = pow(int(a[0]) - int(b[0]), 2) + pow(int(a[1]) - int(b[1]), 2) + pow(int(a[2]) - int(b[2]), 2)
  # if distance < 300:
    return False
  else:
    return True

for x in range(0, 900):
  for y in range(0, 900):
    if isDiff(arr1[x][y], arr2[x][y]):
      diff[x][y] = (0, 0, 0, 255)
      # diff[x][y] = "0"
    else:
      diff[x][y] = (255, 255, 255, 255)
      # diff[x][y] = "1"

# sum = 0
# for x in range(0, 900):
#   print(''.join(diff[x]))

flat = [j for sub in diff for j in sub]
im = Image.new("RGBA", (900, 900))
im.putdata(flat)
im.save('diff.png')

# for x in range(0, 900):
#   for y in range(0, 900):
#     if diff[x][y] == 1:
#       print(x)
#       print(y)