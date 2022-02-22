import random
import string
import pygame

pygame.init()
random_row = 0
random_col = 0
width = 500
height = 500
dimension = 50
square_size = height/dimension
screen = pygame.display.set_mode((width,height))
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
    blockSize = int(square_size) #Set the size of the grid block
    for x in range(0, width, blockSize):
        for y in range(0, width, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, white, rect, 1)

def draw_organism():
    global random_row,random_col
    food_location_collection = []
    food_location = []

    for i in range(20):
        random_food_r =random.randint(1,50) * int(square_size)
        random_food_c = random.randint(1,50) * int(square_size)
        food_location.append(random_food_r)
        food_location.append(random_food_c)
        food_location_collection.append(food_location)
        pygame.draw.rect(screen,green,pygame.Rect(random_food_c,random_food_r,int(square_size),int(square_size)))
        pygame.draw.rect(screen,yellow,pygame.Rect(1,1,int(square_size),int(square_size)))

    return food_location
def move_organism(speed):
    pass

running = True
draw_organism()

while True:
        drawGrid()
        
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
               

        pygame.display.update()
