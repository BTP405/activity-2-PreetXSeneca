import time
#Approach 1
start = time.time()
def doubleL(n):
    res = []
    for i in range(n): res.append(i * 2)
    return res

for i in doubleL(10): 
    print(i, end=' : ')
end = time.time()
duration = end -start 
print(f"\nTime taken by approach 1: {duration:.6f}\n")

#Approach 2
start = time.time()
for x in [n * 2 for n in range(10)]:
    print(x, end=' : ')
end = time.time()
duration = end -start 
print(f"\nTime taken by approach 2: {duration:.6f}\n")



#Approach 3
start = time.time()
def doubleG(n):
        for i in range(n):
            yield i * 2

for i in doubleG(10):
        print(i, end=' : ')
end = time.time()
duration = end -start 
print(f"\nTime taken by approach 1: {duration:.6f}\n")
