import random
import string
# initia; population 
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

#0000000010101010


# object oriented program bulit crossover function
