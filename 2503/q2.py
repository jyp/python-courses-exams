
def rotate_group(m,i,j):
  save = m[i][j]
  m[i][j] = m[i+1][j]
  m[i+1][j] = m[i+1][j+1]
  m[i+1][j+1] = m[i][j+1]
  m[i+1][j+1] = m[i][j+1]
  m[i][j+1] = save
def is_group_complete(m,i,j):
  return (i >=0 and j >=0) or # optional in this implementation
         (i <= len(m)-2 and j <= len(m[0])-2)
def occ(m,i,j):
  return int(m[i][j] != None)
def is_single_group(m,i,j):
  return (occ(m,i,j) + occ(m,i+1,j) + occ(m,i+1,j+1) + occ(m,i,j+1)) == 1
def iteration(n,m):
  odd = n % 2
  for i in range(len(m)):
    for j in range(len(m[0])):
      if i%2==odd and j%2==odd:
        if is_group_complete(m,i,j) and is_single_group(m,i,j):
          rotate_group(m,i,j)

###########################
## Test # (and Graphical demo)

import graphics, random, tkinter

size = 200
win = graphics.GraphWin("single rotation",size,size)

# start with empty matrix
m = list ([None] * size for i in range(0,size))

# put some data about the middle
rand_size = 10
for i in range(size//2, size//2+rand_size):
    for j in range(size//2, size//2+rand_size):
        if random.randint(0,3) == 0:
            m[i][j] = tuple([random.randint(20,255) for i in range(0,3)])

# iterate and show what happens
pic = tkinter.PhotoImage(width=size,height=size)
for iter in range(1000):
    print(iter)
    iteration(iter,m)
    img_data=" ".join(("{"+" ".join(('#%02x%02x%02x' % (m[i][j] or (0,0,0)) for i in range(size)))+"}" for j in range(size)))
    pic.put(img_data,(0,0,size,size))
    i = win.create_image(0, 0, image = pic, anchor=tkinter.NW)
    graphics.update()

