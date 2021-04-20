import pygame
import Node
import math, random

pygame.init()

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A*STAR Pathfinding")

SIZE = 50
SCALE = WIDTH // SIZE 

def close():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run=False
      pygame.quit()
      quit()
# graph
def h(x, y, x1, y1):
  # return eulidean distance
  return math.sqrt((x - x1) ** 2 + (y - y1) ** 2)

def show_graph(graph):
  for x in range(SIZE):
    for y in range(SIZE):
      graph[x][y].draw(screen, SCALE)
  pygame.display.update()
  
def backtrack(tmp):
  dist = 0
  while tmp.previous is not None:
    tmp.path = True
    tmp = tmp.previous
    dist += 1
  tmp.path = True
    
def setup(graph, SIZE, start, end):
  wait = True
  move_start, move_end = False, False
  while wait:
    close()
    pygame.event.get()
    if pygame.mouse.get_pressed()[0]:
      mouse_x, mouse_y = pygame.mouse.get_pos()
      mouse_x = mouse_x // SCALE
      mouse_y = mouse_y // SCALE
      
      if mouse_x == start.x and mouse_y == start.y:
        move_start = True
      if mouse_x == end.x and mouse_y == end.y:
        move_end = True
      
      if move_start:
        start.path = False
        start.g = float('inf')
        start.h = float('inf')
        start.f = float('inf')
        
        start = graph[mouse_x][mouse_y]
        start.path = True
        start.g = 0
        start.h = h(start.x, start.y, end.x, end.y)
        start.f = start.g + start.h
        
      elif move_end:
        end.path = False
        end = graph[mouse_x][mouse_y]
        end.path = True
      else:
        graph[mouse_x][mouse_y].block = True
        for x, y in graph[mouse_x][mouse_y].get_neighbours(SIZE)[:3]:
          graph[x][y].block = True
      
    else:
      move_start, move_end = False, False
    show_graph(graph)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
      wait = False
      
  return start, end
    
    
def main():
  start = (1, 1)
  end = (SIZE - 2, SIZE - 2)

  graph = [[Node.Node(x, y) for y in range(SIZE)] for x in range(SIZE)] 
  
  start = graph[start[0]][start[1]]
  end = graph[end[0]][end[1]]
  start.path = True
  start.g = 0
  start.h = h(start.x, start.y, end.x, end.y)
  start.f = start.g + start.h
  end.path = True
  
  stop = False
  start, end = setup(graph, SIZE, start, end)
  curr = start
  

  while True:     
    if not stop:
      for x, y in curr.get_neighbours(SIZE):
        if graph[x][y].visited == False and graph[x][y].block == False:
          tmp_g = curr.g + h(curr.x, curr.y, x, y) 
          if tmp_g < graph[x][y].g:
            graph[x][y].previous = curr
            graph[x][y].g = tmp_g
            graph[x][y].h = h(x, y, end.x, end.y)
            graph[x][y].f = graph[x][y].g + graph[x][y].h
      
      curr.visited = True        
      backtrack(curr)
      
      if curr == end:
        stop = True
        
    show_graph(graph)
    close()
    if not stop: 
      # check all unvisited nodes and choose the one with lowest f-score to be next curr      
      min_f = float('inf')
      for x in range(SIZE):
        for y in range(SIZE):
          if x != end.x or y != end.y:
            graph[x][y].path = False
            #print(x,y)
          if graph[x][y].visited == False and graph[x][y].block == False and graph[x][y].f < min_f:
            curr = graph[x][y]
            min_f = graph[x][y].f
        
      if min_f == float('inf'):
        stop = True
        print('NO SOLUTION')
    
        
  
main()