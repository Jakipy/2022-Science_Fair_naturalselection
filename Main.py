import random
from re import M
import string
from telnetlib import STATUS
# parent
# temp
# temp with child 
# temp with child -> new parent
parents = []
population = 10
generation = 10 #repeating process 100 times 100 generation
evolution = [] # this will be two dimensional list

x = 10 # should be divisible by 5 
def generate_parent(x):
    
    global parents,population
    letters = string.digits
    for i in range(population): # generating 10 organism 

        result_str = ''.join(random.choice(letters) for i in range(x))
        parents.append(result_str) #storing the genetic information on the list called parent
    

    #print("initial parents population",parents)
  
    evolution.append(parents)

def t_selection(parents): # this function will select k candiates from the parents.
    # in each generation 6 candidates will be choosen. which means t_selection will be excecuted 6 times per generation
    k = int(len(parents)/5) # choose 20% of population
    temp = [] # selected k indiviual genes
    score = [] # scores for selected k indivual genes
    m = 0
    
    r = random.randint(1,len(parents)-k)
    temp = parents[r:r+k] # choosing a section of the parent with k indivual candidates
    for i in range(len(temp)):
        v = evaluation(temp[i])
        if v > m:
            m = v
            m_index = i

    c = temp[m_index]
    return c # c is the choosen candidate 
            
def evaluation(x):
    s = 0
    v = 0 # fitness score of the gene
    for i in range(len(x)):
        s += int(x[i])
    v = s/len(x)
    v = int(v)
    return v
                
# crossover
def single_crossover(temp,status):
    status = random.randint(1,2)
    x = len(temp)
    cp = random.randint(0,x)
    for i in range(int(x/2)):
        a = temp[i]
        b = temp[i+1]
        child = a[0:cp] + b[cp:10]
        temp.append(child)
    if status == 1:
        pass
    else:
        pass
        #substitution(temp)
    return temp,status
        


def twopoint_crossover(temp,status):
    status = random.randint(1,2) # have some probelem (produce more children)
    x = len(temp)
    one = random.randint(0,x)
    two = random.randint(0,x)
    n = 0
    m = 0
    if one > two:
        n = one
        m = two
    elif one < two:
        n = two
        m = one
    else:
        two = random.randint(0,x)
    for i in range(int(x/2)):
        a = temp[i]
        b = temp[i+1]
        child = a[0:m] + b[m:n] + a[n:10]
        temp.append(child)

    if status == 1:
        pass
    else:
        pass
       # substitution(temp)

    return temp,status


# mutation

def substitution(temp):
     # need more research
    print("this is mutation")
    digits = string.digits # assigning 
    i = random.randint(0,len(temp)-1)
    t = temp[i]
    d1 = random.randint(0,len(t))
    d2 = random.choice(digits)
    d2 = str(d2)
    t[d1] = d2
    
      

    return temp
            
    

 

def main(generation):
    status = ""
    global x,parents
    generate_parent(x)
    temp = []
    for i in range(generation):
        n = random.randint(0,1)
        temp = [t_selection(parents) for i in range(6)] # evalution and selection
        if n == 1: # crossover and mutation
            single_crossover(temp,status)
            print("generation",i,temp,"\n","status = one")
        else:
            twopoint_crossover(temp,status)
            print("generation",i,temp,"\n","status = two")

        #substitution(temp)
        #print("generation",i,temp,"\n","status = ",status)
    print()
    evolution.append(temp)
    parents = temp
    temp.clear()
    
main(generation)
