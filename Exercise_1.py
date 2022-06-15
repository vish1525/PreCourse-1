
"""
Runtime Complexity:
1) Initializing stack takes O(1), because we are just declaring an empty array.
2) Operations such as push(), pop(), peek(), size(), isEmpty() takes O(1) runtime complexity. Because push just appends the new item to the end of the list and we dont need to 
iterate through the entire list. Same applies for pop() and peek(), we just display the last appended item in peek() and remove the top element for pop() operation.
Both operations just look at the top element and not the entire list. 
3) show() operation takes O(n) time as we need to iterate through all the elements in the stack.

Space Complexity:
1) O(n), because we store n items in the stack.
"""


class myStack:
  #Please read sample.java file before starting.
  #Kindly include Time and Space complexity at top of each file
    
     
    stack =[]
    def __init__(self):                                                                     #initialise stack array
        self.stack= []
        
         
    def isEmpty(self):
        if (len(self.stack)==0):                                                             #checks if the length of the stack is empty or not
            print("Stack is empty")
        else:
            print("Stack is not empty")                                                       
         
    def push(self, item):
        self.stack.append(item)                                                               #append item to the end of the list
        print("Item:"+item+" has been added to the stack")
         
    def pop(self):
        if len(self.stack)==0:                                                                #checks if the length of the stack is empty or not
            print("Stack Empty")
        else:
            self.stack.pop()                                                                  #if length!=0, removes the top element
        
        
    def peek(self):
        if len(self.stack)==0:
            print("Stack is Empty")
        else:
            print("The Topmost element added to stack is:"+ self.stack[len(self.stack)-1])    #if length!=0, displays the top element
        
    def size(self):
        print("The size of the stack is:"+ str(len(self.stack)))                               #size of the stack is printed out
         
    def show(self):                                                                             #items in stack is displayed here
        print("Items in Stack:")
        return self.stack
         

s = myStack()
s.push('1')
s.push('2')
s.push('3')
s.push('4')
s.push('5')
#s.push('2')
#s.push('3')
s.isEmpty()
#print(s.pop())
print(s.show())
s.size()
s.peek()
