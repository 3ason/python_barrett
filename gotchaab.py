import time 


def print_items(n): 
    for i in range(n): 
        print(i)
    for j in range(n): 
        print(j) 
    

def print_items2(a,b):
    for i in range(a): 
        print(i) 
    for j in range(b):
        print(j)


start = time.time()
print_items(10)
end = time.time() 

print(end - start) 

start = time.time() 
print_items2(100,200)
end = time.time()

print(end - start) 


