import random
import string

p1 = ''
p2 = ''
x = random.randint(0,20)
def generate_parent(x):
    global p1,p2
    for i in range(x):
        temp1 = str(random.randint(0,1))
        p1 = p1 + temp1
    for i in range(x):
        temp2 = str(random.randint(0,1))
        p2 = p2 + temp2

    return(p1,p2)

class crossover():
    global p1,p2,x
    def __init__ (self,crossover_point,):
        self.p1 = p1
        self.p2 = p2
        self.crossover_point = crossover_point
        
        #return crossover_point
    
    def single_crossover(self):
        child1 = ''
        child2 = ''
        self.child = child1
        self.child = child2
        self.child1 = p1[0:self.crossover_point] + p2[self.crossover_point:x]
        self.child2 = p2[0:self.crossover_point] + p1[self.crossover_point:x]
        return self.child1,self.child2

    def mutation(self):
        #return self.child1,self.child2
        pass
        

print(generate_parent(15))

child = crossover(x)
#print(child.single_crossover())
print(child.single_crossover())

