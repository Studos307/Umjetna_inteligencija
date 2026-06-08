from time import*
import sys

N = int(input('Unesite broj misionara N = '))
M = int(input('Unesite broj kanibala M = '))
K = int(input('Unesite broj misionara K = '))
L = int(input('Unesite broj misionara L = '))

start = (N, M, 1)
goal = (0, 0, 0)

problem    = lambda m, c: 0 < m < c
no_problem = lambda m, c: not problem(m, c) and not problem(N - m, M - c)

def next_states(state):
    m, c, b = state
    if b == 1:
        return { (m - mb, c - cb, 0) for mb in range(m + 1)
                                 for cb in range(c + 1)
                                 if K <= mb + cb <= L and no_problem(m - mb, c - cb) and (mb >= cb or mb == 0) 
                }
    else:
        return { (m + mb, c + cb, 1) for mb in range(N - m + 1)
                                 for cb in range(M - c + 1)
                                 if K <= mb + cb <= L and no_problem(m + mb, c + cb) and (mb >= cb or mb == 0)
                }

def path_to(state, Parent):
    p = Parent.get(state)
    if p == state:
        return [state]
    return path_to(p, Parent) + [state]


def bfs(start, goal, next_states):
    Frontier = [ start ]
    Visited  = set()
    Parent   = { start: start }
    sumaF = sys.getsizeof(Frontier)
    sumaV = sys.getsizeof(Visited)
    sumaP = sys.getsizeof(Parent)
    while len(Frontier) > 0:
        s = Frontier.pop(0)
        if s == goal:
            print('Ukupna potrošnja:', sumaF + sumaV + sumaP)
            print('Posebno Frontier:', sumaF)
            print('Posebno Visited:', sumaV)
            print('Posebno Parent:', sumaP)
            print()
            return path_to(goal, Parent)
        if s not in Visited:
            Visited.add(s)
            sumaV += sys.getsizeof(s)
            for ns in next_states(s):
                if ns not in Visited:
                    Frontier.append(ns)
                    Parent[ns] = s
                    sumaF += sys.getsizeof(ns)
                    sumaP = sys.getsizeof(Parent)
    print('Ukupna potrošnja:', sumaF + sumaV + sumaP)
    print('Posebno Frontier:', sumaF)
    print('Posebno Visited:', sumaV)
    print('Posebno Parent:', sumaP)
    print()
        
def dfs(start, goal, next_states):
    Frontier = [ start ]
    Visited  = set()
    Parent   = { start: start }
    sumaF = sys.getsizeof(Frontier)
    sumaV = sys.getsizeof(Visited)
    sumaP = sys.getsizeof(Parent)
    while len(Frontier) > 0:
        s = Frontier.pop()
        if s == goal:
            print('Ukupna potrošnja:', sumaF + sumaV + sumaP)
            print('Posebno Frontier:', sumaF)
            print('Posebno Visited:', sumaV)
            print('Posebno Parent:', sumaP)
            print()
            return path_to(goal, Parent)
        if s not in Visited:
            Visited.add(s)
            sumaV += sys.getsizeof(s)
            for ns in next_states(s):
                if ns not in Visited:
                    Frontier.append(ns)
                    Parent[ns] = s
                    sumaF += sys.getsizeof(ns)
                    sumaP = sys.getsizeof(Parent)      
    print('Ukupna potrošnja:', sumaF + sumaV + sumaP)
    print('Posebno Frontier:', sumaF)
    print('Posebno Visited:', sumaV)
    print('Posebno Parent:', sumaP)
    print()

def bfs2(start, goal, next_states):
    Frontier = { start }
    Visited  = set()
    Parent   = { start: start }
    sumaNF = 0
    sumaF = sys.getsizeof(Frontier)
    sumaV = sys.getsizeof(Visited)
    sumaP = sys.getsizeof(Parent)
    while len(Frontier) > 0:
        NewFrontier = set()
        sumaNF = sys.getsizeof(NewFrontier)
        for s in Frontier:
            for ns in next_states(s):
                if ns not in Visited and ns not in Frontier: 
                    NewFrontier.add(ns)
                    sumaNF += sys.getsizeof(ns)
                    Parent[ns] = s
                    sumaP = sys.getsizeof(Parent) 
                    if ns == goal:
                        print('Ukupna potrošnja:', sumaNF + sumaF + sumaV + sumaP)
                        print('Posebno New Frontier:', sumaNF)
                        print('Posebno Frontier:', sumaF)
                        print('Posebno Visited:', sumaV)
                        print('Posebno Parent:', sumaP)
                        print()
                        return path_to(goal, Parent)
        Visited |= Frontier
        Frontier = NewFrontier
        sumaV = sys.getsizeof(Visited)
        sumaF += sys.getsizeof(Frontier)
    print('Ukupna potrošnja:', sumaNF + sumaF + sumaV + sumaP)
    print('Posebno New Frontier:', sumaNF)
    print('Posebno Frontier:', sumaF)
    print('Posebno Visited:', sumaV)
    print('Posebno Parent:', sumaP)
    print()



Path1 = bfs(start, goal, next_states)
Path2 = dfs(start, goal, next_states)
Path3 = bfs2(start, goal, next_states)

print()

if Path1 == None or Path2 == None or Path3 == None: print('Nema rješenja')
else:

    print('Broj koraka rješenja metodom bfs (ili bfs2) iznosi:', len(Path1) - 1) 
    print('Koraci:\n', Path1)
    print()
    print('Broj koraka rješenja metodom dfs iznosi:', len(Path2) - 1) 
    print('Koraci:\n', Path2)
    print()
    


