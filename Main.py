import random
import string
from numpy import square
import pygame

pygame.init()
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
red = (255,   0,   0)
green = (34,139,34) #forest green color
yellow = (255,255,0)
p1 = ''
p2 = ''
p = ''
population = 100
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
    return parents, len(parents)

def pick_parents(population,parents):
    global p1,p2
    male = random.randint(0,population)
    female = random.randint(0,population)
    p1 = parents[male]
    p2 = parents[female]
    return male,p1,female,p2

class crossover():
    global p1,p2,x
    def __init__ (self,crossover_point,child1 = '',child2=''):
        self.p1 = p1
        self.p2 = p2
        self.crossover_point = crossover_point
        self.child1= child1
        self.child2 = child2
    
    def single_crossover(self):
        self.child1 = p1[0:self.crossover_point] + p2[self.crossover_point:x]
        self.child2 = p2[self.crossover_point:x] + p1[0:self.crossover_point]
        return self.child1,self.child2,len(self.child1),len(self.child2)

    def two_point_crossover(self):
        # two different crossover point
        crossover_point1 = random.randint(1,x)
        crossover_point2 = random.randint(1,x)
        point1 = max(crossover_point1,crossover_point2)
        point2 = min(crossover_point1,crossover_point2)
        # assume point1 != point2 fix it later
        self.child1 = p1[0:point2] + p2[point2:point1] + p1[point1:x]
        print(p1[0:point2],p2[point2:point1],p1[point1:x])
        self.child2 = p2[0:point2] + p1[point2:point1] + p2[point1:x]
        print(p2[0:point2],p1[point2:point1],p2[point1:x])
        return self.child1,self.child2,point1,point2

class mutation(crossover):
    global x
    def __init__(self):
        super().__init__(self)
    def sub(self):
        sub_point = random.randint(1,x)
        to_replace = random.choice(string.digits)
        print("children to be mutated",self.child1,self.child2)
        self.child1 = self.child1[:sub_point] + str(to_replace) + self.child1[sub_point+1:]
        self.child2 = self.child2[:sub_point] + str(to_replace) + self.child2[sub_point+1:]
        
        return sub_point,to_replace,self.child1,self.child2

def fitness_score():
    pass

print(generate_parent(x))
print("call pick_parents function",pick_parents(population,parents))
print("parent1 and parent2",p1,p2)

child = crossover(crossover_point)
print("two point crossover",child.two_point_crossover())
call_mutation = mutation()
print("mutation_sub",call_mutation.sub())

def drawGrid():
    # the greed has a coordinate for (0,0) to (490,490)
    blockSize = int(square_size) #Set the size of the grid block
    for x in range(0, width, blockSize):
        for y in range(0, width, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, white, rect, 1)

def draw_organism():
    global random_row,random_col,food_location_collection,food_location
    #colors = ["red","blue","yellow","orange","green","white"] # this color is for debuggin purpose later make sure to remove this color list and unite organism with one color. 
    for i in range(6):
        random_r =random.randint(1,49) * int(square_size)
        random_c = random.randint(1,49) * int(square_size)
        food_location = [random_r,random_c,]
        food_location_collection.append(food_location)
        pygame.draw.rect(screen,white,pygame.Rect(random_r,random_c,int(square_size),int(square_size)))
        #pygame.draw.rect(screen,yellow,pygame.Rect(1,1,int(square_size),int(square_size))) #also for debugging purpose

    return food_location
def move_organism(food_location_collection,square_size,dimension):
    print(food_location_collection)
    organism_x_val = 0
    organism_y_val = 0
    
    will_move = []
    will_move_collection = []
    for x in range(len(food_location_collection)):
        for y in range(0,2):
            if y == 0:
                organism_x_val = dimension*10 - food_location_collection[x][y]
            else:
                organism_y_val = dimension*10 - food_location_collection[x][y]

        if organism_x_val/10 == 49:
            if organism_y_val/10 == 49: 
                will_move = [0,0]
                will_move_collection.append(will_move)
            else:
                will_move = [0,random.randint(organism_y_val/10,49)*int(square_size)]
                will_move_collection.append(will_move)
        else:
            if organism_y_val/10 == 49:
                will_move = [random.randint(organism_x_val/10,49)*int(square_size),0]
                will_move_collection.append(will_move)

            else:
                will_move = [random.randint(organism_x_val/10,49)*int(square_size),random.randint(organism_y_val/10,49)*int(square_size)]
                will_move_collection.append(will_move)

        
    print(will_move_collection)

    for x in range(len(will_move_collection)):
        pygame.draw.rect(screen,green,pygame.Rect(will_move_collection[x][0],will_move_collection[x][1],int(square_size),int(square_size)))


       
       

            
    
    print(will_move_collection)
    
running = True
draw_organism()
move_organism(food_location_collection,square_size,dimension)
while True:
    
        drawGrid()
        
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
               

        pygame.display.update()
