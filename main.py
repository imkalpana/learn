
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


