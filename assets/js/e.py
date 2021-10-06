from tqdm import tqdm
from random import uniform
l = []

for x in tqdm(range(1000000)):
    t = 0
    i = 0
    while t <= 1:
        t += uniform(0, 1) 
        i += 1
    l.append(i)

print(sum(l) / 1000000)