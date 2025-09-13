
#Made a function which add two number 

print("==== Add two numbers ====")
print("")

def add(x=3,y=5):
    sum = x+y
    print("Sum of two numbers: ", sum)


print("add default values: ", add())
print("add 121 and 234: ",add(121, 234))
print("add 1324 and 42346: ",add(1324,42346))
print("add 73 and 64: ",add(73, 64))

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

pop_item=stack.pop()
print("Stack: ",stack)
print("Popped item: ", pop_item)

stack.pop()
print("Stack: ",stack)




