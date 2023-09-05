import numpy as np
import matplotlib.pyplot as plt
from random import randint

def show_plot(plot_matrix):
 global posAPAx
 global posAPAy

 plt.imshow(plot_matrix, 'gray')
 plt.nipy_spectral()
 plt.plot([posAPAy],[posAPAx], marker='o', color='r', ls='')
 plt.show(block=False)
 plt.pause(0.5)
 plt.clf()

def get_dirt_number():
 need_reading = True
 dirt_number = 0

 while need_reading:
   dirt_number = int(input("Type the number of dirt between 1 and 8: "))

   if (dirt_number > 8):
    print("The max number of dirt of dirt is equal to 8.")
   else:
    need_reading = False
 return dirt_number

def initialize_plot_matrix():
 plot_matrix = np.array(
  [
   [1,1,1,1,1,1],
   [1,0,0,0,0,1],
   [1,0,0,0,0,1],
   [1,0,0,0,0,1],
   [1,0,0,0,0,1],
   [1,1,1,1,1,1]
  ]
 )

 for x in range(get_dirt_number()):
  x = randint(1, 4)
  y = randint(1, 4)
  plot_matrix[x, y] = 2

 return plot_matrix

posAPAx = 1
posAPAy = 1

show_plot(initialize_plot_matrix())
