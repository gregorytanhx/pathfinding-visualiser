import pygame, random
class Node:
  def __init__(self, x, y):
      self.x = x
      self.y = y
      self.h = float('inf')
      self.g = float('inf')
      self.f = float('inf')
      self.block = False
      self.visited = False
      self.previous = None
      self.path = False

  def mouse_click(self, mouse_x, mouse_y, scale):
      if mouse_x > self.x * scale and mouse_x < self.x * scale + scale - 1:
        if mouse_y > self.y * scale and mouse_y < self.y * scale + scale - 1:
            self.block = True
                     
  def get_neighbours(self, SIZE):
    neighbours = []
    # east
    if self.x < SIZE - 1: 
      neighbours.append((self.x+1, self.y))
    # south east
    if self.x < SIZE - 1 and self.y < SIZE - 1:
      neighbours.append((self.x+1, self.y+1))
    #south
    if self.y < SIZE - 1:
      neighbours.append((self.x, self.y+1))
    # south west
    if self.x > 0 and self.y < SIZE - 1:
      neighbours.append((self.x-1, self.y+1))
    # west
    if self.x > 0: 
      neighbours.append((self.x-1, self.y))
    # north west
    if self.x > 0 and self.y > 0: 
      neighbours.append((self.x-1, self.y-1))
    # north
    if self.y > 0:
      neighbours.append((self.x, self.y-1))
    # north east
    if self.x < SIZE - 1 and self.y > 0:
      neighbours.append((self.x+1, self.y-1))
            
    return neighbours
    
  def draw(self, screen, scale):
    if self.path:
      color = (255, 0, 0)
    elif self.visited: 
      color = (0, 0, 255)
    elif self.block:
      color = (0, 0, 0)
    else:
      color = (255, 255, 255)
    pygame.draw.rect(screen, color, (self.x * scale, self.y * scale, scale - 1, scale - 1))