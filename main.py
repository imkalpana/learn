
#Made a function which add two number 

print("==== Add two numbers ====")
print("")

def add(x=3,y=5):
    sum = x+y
    print(f"Sum of two numbers {x}, {y}: ", sum)


add()
add(121, 234)
add(1324,42346)
add(73, 64)

#Made a stack 

print("")
print("==== Stack ====")
print("")

stack=[]

print("Stack: ",stack)

#Add fruits' name in the stack

stack.append("Apple")
stack.append("Banana")
stack.append("Orange")
stack.append("Stawberry")
stack.append("Blueberry")

print("Stack: ",stack)

#Remove an items one by one from stack

pop_item=stack.pop(-1)
print("Stack: ",stack)
print("Popped item: ", pop_item)

stack.pop(-1)
print("Stack: ", stack)


#Made a queue

print("")
print("==== Queues ====")
print("")

queue=[]
print("Queue: ", queue)

#Add Numbers in queue

queue.append(4)
queue.append(2)
queue.append(7)
queue.append(1)
queue.append(8)

print("Queue: ", queue)


#Remove element from queue

pop_element=queue.pop(0)
print("Queue: ", queue)
print("Popped element: ", pop_element)

queue.pop(0)
print("Queue: ", queue)



#Implementing liner search
print("")
print("==== Liner_Search ====")
print("")

def liner_search(arr=[2,4,6,2,8,5,2,9,3,5,1,7], val=1):
    count=0
    for i in arr:
        if i==val:
            print( "Found!")
            break
        else:
            print("Not Found!")

        count+=1
    print(f"Found in {count} iterate")

liner_search()



#Implementing binary search
print("")
print("==== Binary_Search ====")
print("")

def binary_search(arr=[2,5,7,8,9,13,24,46,78,85,87], val=9):
    count=0
    left=0
    right=len(arr)-1
    while left<=right:
        mid= (left+right)//2
        count+=1
        if arr[mid] == val:
            print(f"Element is present at {mid} index")
            print(f"Found in {count} iterate")
            break

        elif arr[mid] < val:
            left = mid + 1

        else:
            right = mid -1

    print("Targeted Value is not found!")


binary_search()