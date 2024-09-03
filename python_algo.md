# Python Data Structure & Algorithms + Leetcode Exercises 

$: section 
* big idea 
- idea within idea 
! specific point
? question I have 

## Section 1.1 [Overview] 
* Big O measures how efficient your code is 
    ? Given the constraint that we want to be efficient when removing the last idea in a list, 
    should we choose a singly linked list or a doubly linked list? 
* Reasons of Big O importance 
    1) Important Topic
    2) Helps makes decision on what data structure to use in code 
    3) Coding Interview 
* Classes & Pointers
    * every DS is using a class in this course 
    * Pointers trip up a lot of student
        - Fallacy of where the head & tail are. 
            * head and tails aren't the nodes but are variables that points that pointer to node.       
        (x) is a node 
        (1) -> (2) -> (3) , head -> (1) and tail -> (3) 
    * difference of pointer vs. variable 

+ Summary 
    Big O is measure of performance and can be used to decide what data structure to use, example of singly linked list vs doubly linked list 


## Section 1.2 [Coding Environment] 
* he runs vertical terminal which i think you can do with :split and :vsplit  



# Section 2 Big O 

## Section 2.3 [Big O: Intro ] 

Big O
- a way of comparing code 1 and code 2 
    * is it by 
        * readability? 
        * conciseness?
        * no, mathematically on how on efficient they run 

What is Big O?
* time of code to run (is it by standard time like stopwatching and measuring)? 
    * obviously not, what if one computer is faster and the other one is slower 
* We measure by *Time Complexity* 
    - measured in number of operations 
* Space Complexity is also a measure of performance 
    - have to consider preserving memory space as a priority vs time. 


## Section 2.4[Big O: Worst Case] 

* ω(Omega), Theta(θ), Omicron(O) 

* What are these used for? 

* example: Let's say you have a list w/ 7 items & I'm going to build a for loop to iterate through to find # 
    
[1 , 2 , 3 , 4, 5, 6, 7, 8, 9]
Omega(omega)  Theta(avg case)   Omnicron(worse case) 



## Section 2.5 [Big O: O(n)]

* example to type a backtick do shift + esc 
```python 
def print_items(n): 
    for i in range(n): 
        print(i) 
print_items(10) 


```
* example of something that is O(n), passed number n & it ran n times. 
* so if this was on graph it would y = x, if y was number of operations and x is size of input relative to algorithm 


## Section 2.6 [Big O: Drop Constants] 
* simplification 

* so what if we change the previous code to this? 
```python 
def print_items(n) : 
    for i in range(n): 
        print(i)
    for j in range(n):
        print(j) 
print_items(10) 
```
* this ran 2n times as do we n + n for the two separate for loops 
* O(2n) => O(n) 
* O(100n) => O(n) 


## Section 2.7[Big O: O(n^2)] 

```python 
def print_items(n): 
    for i in range(n):
        for j in range(n): 
            print(i,j) 
print_items(10)

# 10x10 = 100 items printed out. 
```

* n * n = n^2 number of operations 
* (VISUALIZE) it's just a parabola(only the right side) on the graph, a lot less efficient from the time complexity standpoint 



## Section 2.8[Big O: Drop Non-Dominants]
* another simplications techniques 

```python 
def print_items(n): 
    for i iin range(n): 
        for j in range(n): 
            print(i,j) 
    for k in range(n): 
         print(k) 
```

* so the time complexity is O(n^2) + O(n) => O(n^2 + n) 
* as a percentage of the total operation that stand alone n is insignificant 

* O(n^2 + n) => O(n^2) 


## Section 2.9[Big O:O(1)]

```python 
def_add_items(n): 
    return n + n + n   vs  return n + n 
        O(2)?                   O(1) 
O(1) is constant line, as n increases, the number of operation stays the same 
```

* so on a graph it's just Y = constant 



## Section 2.10 [Big O: O(log n)]

list [1,2,3,4,5,6,7,8]

+ How can we find "1" efficiently 

1. Search first half & the second half 
    [1|2|3|4]    [5|6|7|8]
2. Repeat 
    [1|2]       [3|4] 
3. again 
    [1]

* took a total of 3 steps to find 1 in 8 item list 
    * now why is it 8? 
        * 2^3 = 8 
            * therefore ...log base 2(8) = 3 
    * so if we have a list have a billion items it will take 
        * log2(1,073,741,824) = 31 
            * if list has a billion items, only needs 31 times to find 1 
    * thus time complexity of binary search is log2(n) 


* O(n log n) algorithm examples: mergesort, quicksort, most efficient you can make a sorting algorithm n  


## Section 2.11 [Big O: Different Terms for Inputs] 
    - gotcha question? 

```python 
def print_items(n): 
    for i in range(n):
        print(i)
    for j in range(n): 
        print(j)

# this code on top vs. this code at bottom 

def print_items2(a,b): 
    for i in range(a): 
        print(i) 
    for j in range(b): 

```

* cannot say O(2n) for second example, have to state it as O(a+b) 
if it was 
```python 
for i in range(a):
    for j in range(b): 
        print(i,j)
```
* then the time complexity would be O(a*b) 



## Section 2.12[Big O: Lists] 
* built in data structure 

* list -> [11,3,23,7] 
    *      0  1 2  3 , indexes 

* Okay what is the time complexity for adding and removing? how does reindexing affect this? 

mylist.append(17) 
[11,3,23,7,17] 
mylist.pop() 
[11,3,23,7] 

* O(1) adding & removing, no reindexing necessary 

* however, if we do 
mylist.pop(0) 
    * if first element is popped, reindexing needs to happen, shifting down the line as the 
    index from index 1 and beyond is wrong, same is true for mylist.insert(0,11) 
    * [,3,23,7]
        * have to shift 3 down to index 0 and 23 to index 1 and etc etc. 
    * thus this shift needs to take O(n) time 
* this is the difference in the adding/removal of head vs. tail 



* okay now what happens if we try to insert in the middle? 
> mylist.insert(1,'Hi') 
[11, 'Hi', 3, 23, 7] 
  0   1    1   2  3    <---- no longer correct, so it needs reindexing 

* Why is it not O(1/2n) for insertion 
    - worse case not avg case 
    - constants are removed 

* Search by value: O(n) 
* Search by index: O(1) 



## Section 2.13 [Big O:Wrap-Up]

* visualize O(n^2), O(n) , O(log n), and O(1) 
* Say n = 100 
    * O(n^2) = 10,000 , O(n) = 100, O(log n) = 7, O(1) = constant 
* Say n = 1000 
    * O(1) = constant, O(log n ) = 10, O(n) = 1000, O(n^2) = 1,000,000, very inefficient 
    compared to others, in programming try your best to make O(n) 

* O(n^2) - is usually loop within loop 
* O(n)   - proportional 
* O(log n) - divide and conquer 
* O(1)     - constant 


* bigocheatsheet.com 
    - chart on what is consdiered efficient or inefficient 
* also below 
    - have common data structure and their operations with time complexity analysis as well as space complexity 

* Space Complexity 
    - Quicksort and Mergesort are Time: O(n log(n)) but 
                                  Space:O(log(n)) and O(n), not the best however 
    - Bubble, Insertion, Selection  Time:O(n^2) 
                                    Space:O(1) 
    * bubble insertion, selection is primitive sorting algorithms but space complexity is good. 
        - in best case secnarios, Bubble, Insertion is more efficient than quicksort of merge sort      
            * like when you already have already or mostly sorted data 
               - why is quicksort terrible or worse in these scenarios? maybe it does some type of action that is still necessary but costs a lot even if it's sorted? 



# Section 3: Classes & Pointers 

## 3.14 [Classes] 

* every data structure we will create is created using Classes 
+ What is a class? 
    - analogy: cookie cutter 
    - built in cookie cutter where you can create a int, string 
    - class is your own datatype 


* this below is a constructor and self references a specific instance 
```python 
class Cookie: 
    def __init__(self,color):
        self.color = color 

    def get_color(self):        # if all it has is itself, no arguments passed on  
        return self.color 

    def set_color(self,color):
        self.color = color 

cookie_one = Cookie('green') 
cookie_two = Cookie('blue')


print('Cookie one is ', cookie_one.get_color()) 
print('Cookie two is ', cookie_two.get_color()) 

cookie_one.set_color('yellow') 

print('\nCookie one is now',cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color()) 

```


* okay how would we use classes on a high level 

```python 

class LinkedList:                           # always capital  
    def __init__(self,value):               # constructor 

    def append(self,value):                 # header lines only? 

    def pop(self): 

    def prepend(self, value): 

    def insert(self, index, value): 

    def remove(self,index): 
```


## 3.15 [Pointers] 

* what are pointers and do they work differently with different data types? 

* num1 = 11 
  num2 = num1 

    - when we do this we create the integer 11 somewhere in memory, we point variable num1 to that integer 
    - what happens on the code num2 = num1? 
                num1 -> 11 
                num2 -> 11 or?? does it point to the same value 11 that num1 points to? 
                    * like basically does it create its separate 11 or use the same one? 

* test in vscode 
```python 
num1 = 11 
num2 = num1 
print("First Run")
print('num1 = ', num1) 
print('num2 = ', num2)

print("\nnum1 points to:", id(num1)) 
print("num2 points to:", id(num2)) 
# id(var) gives me the address of where var is stored 

```

Output
Before num2 value is updated: 
num1 = 11 
num2 = 11 

num1 points to: 140727958956656
num2 points to: 140727958956656

* so we find out from running this code that they are pointing to the same 11 in memory. (same address) 

* now what happens when we set num2 = 22 
what happens does 
num1 = num2 = 22 or does num1 = 11 and num2 = 22  


```python
num2 = 22 
print("\nAfter num2 value is updated:" ) 
print("num1 = ", num1) 
print("num2 = ", num2) 

print("\nnum1 points to:", id(num1)) 
print("num2 points to: ", id(num2)) 
```

Output 
After num2 value is updated: 
num1 = 11 
num2 = 22 

num1 points to: 140710779218544
num2 points to: 140710779218896 
 
- so the behavior we find out is that num1 = 11 and num2 = 22, original 11 does not get changed 
- the reason this happens is because integers are immutable, they cannot be changed, once 11 is put into a place in memory, you cannot change that number11. You can point num1 to different integer that is stored somewhere else, which you can't actually change the number 11 once you create it. 


### let's look at a different datatype that works differently vs. integer 

```python 
dict1 = {
    'value':11
}
dict2 = dict1 
```

* What happens?
    * new creation of an additional dictionary that is identical someplace else in memory or 
     and have dictionary two point at it? 
* so they point to the same dictionary, same behavior as integer. 

* What happens if dict2['value'] = 22, overwrite or new dictionary in memory? 


* vscode time :) 

```python 
dict1 = {
    'value':11 
}
dict2 = dict1 

print("Before value is updated:") 
print("dict1 =", dict1)
print("dict2 =", dict2) 

print("\ndict1 points to:", id(dict1)) 
print("dict2 points to:", id(dict2))

dict2['value'] = 22 

print("\nAfter value is updated:") 
print("dict1 =", dict1) 
print("dict2 =", dict2) 

print("\ndict1 points to:", id(dict1)) 
print("dict2 points to:", id(dict2)) 

```

* Output 
Before value is updated:
dict1 = {'value': 11}
dict2 = {'value': 11}

dict1 points to: 2084208831232
dict2 points to: 2084208831232

After value is updated:
dict1 = {'value': 22}
dict2 = {'value': 22}

dict1 points to: 2084208831232
dict2 points to: 2084208831232


* after value is updated, both dictionary 1 and 2 point to the same address, different behavior vs integer. 

* thus we know that dictionaries are mutable. 

* why is this important for a data structures and algorithms course? 
    * example when we have a linked list, the nodes in a linked list are going to operate 
    very much like a dictionary. 
        * if you have two variable that point to the same node, you can change the value of that    node  
        * value changing doesn't change the variables pointing to the same node 


### 2 separate concepts 

* so we have 3 dictionaries 
dict1 -> dict2 -> { 'value': 22 }
dict3 -> {'value':33 }
- let's set dict2 = dict3 
dict2 -> dict3 -> {'value':33 }
- we are changing where the dictionary point to 
- linked list concept, we might want to move head to point to a new node 
    * we just need to set head to be equal to something else pointing at that 

* another concept 
- what if we do dict1 = dict2 
        * so now all dictionary points to value 33 and nothing points to value 22 anymore 
* so what happens to that original value 22 dictionary as there's nothing no longer pointing to it, thus no way to access 
    - Python will remove that dictionary through a process called garbage collection 






# Section 4: Linked Lists 




## 4.16 [Linked List:Intro] 

* start with list to explain the differences between a linked list and list 
- linked list does not have indexes 
- list is in a contiguous place in memory
    - with a linked list, all of the nodes are going to be spread all over the place 
- linked list is PURPLE CIRCLES 
- also with linked list we have variable called head, head points to the first node in list 
- also we have tail point to the last item 
    * each node in the list points to the next to the next, last one points to none 
-  list are contiguous which is why we can use index and access indexes O of one, because we map each one of these indexes to a specific address in memory. 














