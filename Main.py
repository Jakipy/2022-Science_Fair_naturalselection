import random
from re import L
import string
from numpy import square
import pygame
import matplotlib.pyplot as plt
import numpy
pygame.init()
organism_info = () # row,col,group,color
divided_parents_group = []
matrix = [[0 for i in range(50)] for i in range(50)]
avg_score_parents = []
generation = 0
random_row = 0
random_col = 0
food_location_collection = []
food_location = []
real_height = 600
width = 500
height = 500
dimension = 50
square_size = height/dimension # in this case it is 10, 500/50 = 10
screen = pygame.display.set_mode((width,real_height))
white = (200, 200, 200)
red = (255,   51,   51)
green = (51,255,153) #forest green color
yellow = (255,255,0)
sky_blue = (51,255,255)
p1 = ''
p2 = ''
p = ''
population = 10
parents = [] # collection of possible solution
x = 9 # length of chromosome
crossover_point = random.randint(0,x)
if x%2 == 0:
    crossover_point = x/2
else:
    crossover_point = x/2 + 0.5
print(crossover_point)
# generating 100 parents, go into fitness score function
def generate_parent(x):
    
    global parents,population
    letters = string.digits
    for i in range(population):

        result_str = ''.join(random.choice(letters) for i in range(x))
        parents.append(result_str)
    print("parents",parents)

def pick_parents(population,parents):
    global p1,p2
    male = random.randint(0,population)
    female = random.randint(0,population)
    p1 = parents[male]
    p2 = parents[female]
    return male,p1,female,p2


def single_corssover(parent1,parent2,x,crossover_point,parents):
   child1 = parent1[0:crossover_point] + parent2[crossover_point:x]
   child2 = parent2[crossover_point:x] + parent1[0:crossover_point]
   parents.append(child1)
   parents.append(child2)
   return child1,child2

#print(single_corssover("123456","654321",6,random.randint(1,6)))

def two_crossover(parent1,parent2,x,parents):
    # two different crossover point
    crossover_point1 = random.randint(1,x)
    crossover_point2 = random.randint(1,x)
    point1 = max(crossover_point1,crossover_point2)
    point2 = min(crossover_point1,crossover_point2)
    # assume point1 != point2 fix it later
    child1 = p1[0:point2] + p2[point2:point1] + p1[point1:x]
    print(p1[0:point2],p2[point2:point1],p1[point1:x])
    child2 = p2[0:point2] + p1[point2:point1] + p2[point1:x]
    print(p2[0:point2],p1[point2:point1],p2[point1:x])
    parents.append(child1)
    parents.append(child2)
    return child1,child2,point1,point2


#print("call pick_parents function",pick_parents(population,parents))
#print("parent1 and parent2",p1,p2)

#child = crossover(crossover_point)
#print("two point crossover",child.two_point_crossover())
#call_mutation = mutation()
#print("mutation_sub",call_mutation.sub())

def avg_fitness_score(parents,avg_score_parents):
    sum = 0
    for i in range(len(parents)):
        for j in (parents[i]):
            sum = sum + int(j)
        avg_score_parents.append(sum/x)

    print("avagre score parents",avg_score_parents)

def drawGrid():
    # the greed has a coordinate for (0,0) to (490,490)
    blockSize = int(square_size) #Set the size of the grid block
    for x in range(0, width, blockSize):
        for y in range(0, width, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, white, rect, 1)

def draw_organism():
    global random_row,random_col
    food_location_collection = []
    food_location = []
   
    for i in range(population):
        random_food_r = random.randint(1,49) * int(square_size)
        random_food_c = random.randint(1,49) * int(square_size)
        pygame.draw.rect(screen,red,pygame.Rect(random_food_c,random_food_r,int(square_size),int(square_size)))
        food_location.append(random_food_r)
        food_location.append(random_food_c)
        food_location_collection.append(food_location)
        food_location = [] # you have to reset the food_location list since it act as temporary storage
        
    print("location",food_location_collection) 


def group_animals(avg_score_parents):
    temp = []
    global divided_parents_group
   
    for i in avg_score_parents:
        if i > 0 and i <= 25:
            temp = ["D","white"]
            divided_parents_group.append(temp)
            temp = []
        elif i > 25 and i <= 50:
            temp = ["C","yellow"]
            divided_parents_group.append(temp)
            temp = []
        elif i > 50 and i <= 75:
            temp = ["B","sky_blue"]
            divided_parents_group.append(temp)
            temp = []
        elif i > 75:
            temp = ["A","red"]
            divided_parents_group.append(temp)
            temp = []

    

    print("divided_parents_group", divided_parents_group)
 
def reproduce(parents):
    a = random.randint(1,2)
    if a == 1:
        two_crossover(parents[random.randint(1,len(parents))],parents[random.randint(1,len(parents))],x,parents)
    else:
        single_corssover(parents[random.randint(1,len(parents))],parents[random.randint(1,len(parents))],x,random.ranint(1,x),parents)
    
def graphing(avg_score_parents):
    global generation
    plt.plot(avg_score_parents)
    plt.ylabel("fitness_score")
    plt.xlabel("generation")
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.show()

running = True
generate_parent(x)
avg_fitness_score(parents,avg_score_parents)
group_animals(avg_score_parents)
draw_organism()
while True:
    reproduce(parents)
    graphing(avg_score_parents)
    drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
               

pygame.display.update()
