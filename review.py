class SLNode:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None # points to the next node in the least

class SList:
    def __init__(self) -> None:
        self.head = None # will eventually point to the next node in the list
    
    def add_to_front(self, val):
        new_node = SLNode(val) # create new node
        new_node.next = self.head # points to what will be the next node in the list
        self.head = new_node # places new node at the top of the list
        return self
    
    def add_to_back(self, val):
        if self.head == None:
            self. add_to_front()
            return self
        new_node = SLNode(val) # creates new node
        runner = self.head # need a runner to run through the list
        while runner.next != None: # result is runner node will be last item in list
            runner = runner.next
        
        runner.next = new_node
        return self

    def remove_from_front(self):
        if self.head == None: # don't mess with an empty list
            print("*** Empty List ***")
            return self
        value = self.head.value # capture value to return before removing node
        self.head = self.head.next # removes first node from list
        return value
    
    def remove_from_back(self):
        if self.head == None:
            print("*** Empty List ***")
            return self
        if self.head.next == None: # if only one node in list, remove_front
            value = self.remove_from_front()
            return value
        runner = self.head # set runner to run through list
        while runner.next != None: #loop results in runner being the last node in the list
            current_node = runner # allows access to penultimate node
            runner = runner.next
        value = runner.value # capture last node's value before it gets deleted
        current_node.next = None # removes final node
        return value

    def remove_val(self, val):
        if self.head.value == val: # remove if first node in the list
            self.remove_from_front()
            return self
        runner = self.head # need a runner to iterate through the list
        while runner.next != None:
            current_node = runner # captures current node
            runner = runner.next # captures next node

            if runner.value == val: # find if middle nodes match value
                runner = runner.next
                current_node.next = runner # skips node where value matches
                break
        if current_node.value == val: # if final node value matches val, delete it
            self.remove_from_back()
        return self
    
    def insert_at(self, val, num):
        if num == 0:
            self.add_to_front(val)
            return self
        runner = self.head # runner to run through the list
        list_length = 0
        while runner.next != None:
            list_length += 1 # keeps track of node list "index"

            if list_length == num: # insert node at requested index
                new_node = SLNode(val)
                new_node.next = runner.next
                runner.next = new_node
            runner = runner.next

        if num >= list_length: # add node to the end, allows for a number too large for the list
            self.add_to_back(val)
        return self

        

    def display_list(self):
        runner = self.head # need runner to run through the nodes in the list
        while runner != None:
            print(runner.value)
            runner = runner.next # advances to the next node
        return self
    
new_list = SList()
new_list.add_to_front('Hello').add_to_front('goodbye').add_to_back('friend')
new_list.insert_at("turd",2).display_list()