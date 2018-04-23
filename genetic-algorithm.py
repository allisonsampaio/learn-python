import math
import random
import numpy

def fitness(x):
    return math.sin((math.pi * x) / 256)

def gen_pop(N):
    pop = []
    for i in range(N):
        pop.append(random.randrange(0,255))
    return pop

#acumular([1,2,3,4]) -> [1,3,6,10]
def acumular(v):
    res = []
    acum = 0
    for i in v:
        res.append(i + acum)
        acum = res[-1]
    return res

def random_select(pop, f):
    fit = map(f, pop) #Lista que vai ter o valor de fitness pra cada elemento da população
    soma = sum(fit)
    #norm = map(lambda x: x / soma, fit)
    norm = []
    for i in fit:
        norm.append(i/soma)
    acm = acumular(norm)
    
    r = random.random()
    
    for i in range(len(acm)):
        if r < acm[i]:
            break
    return pop[i]
        
    
    print fit
    print soma
    print norm
    print acm
    
def reproduzir(x, y):
    bx = format(x, '08b')
    by = format(y, '08b')
    c = random.randint(0, len(bx)-1)
    return int(bx[0:c] + by[c:len(by)],2)

def mutar(x):
    bx = format(x, '08b')
    r = random.randrange(0, len(bx))
    x = x ^ (1 << r)
    return x
    
#pop_inicial = [17, 20, 118, 79, 204, 197, 213, 44, 254, 0]
#print(pop_inicial)
#random_select(pop_inicial, fitness)

reproduzir(10,120)
mutar(10)