import numpy as np
import matplotlib.pyplot as plt
from random import randint

plot_matrix = np.array(
 [
  [1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1]
 ]
)

# 5 (down), 6 (right), 7 (up)
actions_plot_matrix = np.array(
 [
  [1, 1, 1, 1, 1, 1],
  [1, 5, 6, 5, 0, 1],
  [1, 5, 7, 5, 7, 1],
  [1, 5, 7, 5, 7, 1],
  [1, 6, 7, 6, 7, 1],
  [1, 1, 1, 1, 1, 1]
 ]
)

vacuum_position_x = 1
vacuum_position_y = 1

def first_show_plot():
 initialize_plot_matrix_with_dirt()
 show_plot_with_positions()

def walking_plots():
 while is_plot_dirty():
  vacuum_walker()
  show_plot_with_positions()

  if (plot_matrix[vacuum_position_x][vacuum_position_y] == 2):
    plot_matrix[vacuum_position_x][vacuum_position_y] = 0

 show_plot_with_positions()

def vacuum_walker():
 global vacuum_position_x
 global vacuum_position_y
 action_current_index = actions_plot_matrix[vacuum_position_x][vacuum_position_y]

 if (action_current_index == 5):
  vacuum_position_x += 1
 elif (action_current_index == 7):
  vacuum_position_x -= 1
 elif (action_current_index == 6):
  vacuum_position_y += 1

def show_plot_with_positions():
 plt.imshow(plot_matrix, 'gray')
 plt.nipy_spectral()
 plt.plot(vacuum_position_x, vacuum_position_y, marker='o', color='r', ls='')
 plt.show(block=False)
 plt.pause(0.5)
 plt.clf()

def get_dirt_number():
 need_reading = True
 dirt_number = 0

 while need_reading:
  dirt_number = int(input("Type the number of dirt between 0 and 9: "))

  if (dirt_number > 8):
   print("The max number of dirt of dirt is equal to 8.")
  else:
   need_reading = False
 return dirt_number

def initialize_plot_matrix_with_dirt():
 global plot_matrix

 for _ in range(get_dirt_number()):
  dirt_position_x = randint(1, 4)
  dirt_position_y = randint(1, 4)
  plot_matrix[dirt_position_x][dirt_position_y] = 2

def is_plot_dirty():
 for row_value in range(len(plot_matrix[vacuum_position_x])):
  for column_value in range(len(plot_matrix[vacuum_position_y])):
   if (plot_matrix[row_value][column_value] == 2):
    return True
 return False

first_show_plot()
walking_plots()