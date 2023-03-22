class SLNode:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None

class SList:
    def __init__(self) -> None:
        self.head = None
    
    def check_for_nodes(self): # check for empty list
        if self.head == None:
            print('*** Empty List ***')
            return False
        else:
            return True
        
    def add_to_front(self, val):
        new_node = SLNode(val) # create a new node
        new_node.next = self.head # set new node next  to current head
        self.head = new_node # move new node into self.head
        return self

    def add_to_back(self, val):
        new_node = SLNode(val) # create a new node to add to the list

        runner = self.head # create a runner to iterate through the list
        while runner.next != None:
            runner = runner.next # takes us to the last node
        runner.next = new_node
        return self
    
    def remove_first(self):
        if self.check_for_nodes() is False:
            return self
        
        rem_val = self.head.value # record value to return
        self.head = self.head.next # change head to the next node in line, deleting first node
        return rem_val
    
    def remove_last(self):
        if self.check_for_nodes() is False:
            return self
        
        if self.head.next == None: # in case there's only one item in the list
            return self.remove_first()
        runner = self.head
        while runner.next != None: # iterate to last node, recording penultimate node on the way
            current_node = runner
            runner = runner.next
        ret_val = runner.value # record value to return before it's deleted
        current_node.next = None # deletes last node
        return ret_val
    
    def remove_value(self, val): # removes node with this value
        if self.check_for_nodes() is False:
            return self
        
        if self.head.value == val: # check to see if value is first in the list
            self.remove_first()
            return self
        
        runner = self.head # set up a runner to iterate the list
        while runner.next != None:
            current_node = runner # keep current node before looking at next node
            runner = runner.next
            if runner.value == val:
                current_node.next = runner.next
                return self
        
        if runner.next == None and runner.value == val: # check to see if last value matches val
            self.remove_last()
            return self
        else:
            print("Value not found") # notify user if nothing happens to the list
            return self
        
    def insert_at(self, val, n):
        if n == 0: # if n is 0, insert in front
            self.add_to_front(val)
        elif n >= self.length(): # if n is the length of the list, insert last
            self.add_to_back(val)
        else: # else insert at n   
            i = 1
            runner = self.head # runner to loop through nodes
            while runner.next != None:
                if i == n:
                    new_node = SLNode(val)
                    new_node.next = runner.next
                    runner.next = new_node
                    return self
                i += 1
                runner = runner.next
            return self

        return self

    
    def display_list(self):
        if self.head == None:
            print('*** Empty list ***')
            return
        runner = self.head # runner to iterate through the list
        while runner != None:
            print(runner.value) # display current value
            runner = runner.next # move iterator to next node
        print(f"Length: {self.length()}")
        return self
    
    def length(self): # returns length of the list
        length = 0 # counter for number of nodes
        runner = self.head # runner to loop through nodes
        while runner != None:
            length += 1 # adds 1 for every instance of a node
            runner = runner.next
        return length



new_list = SList()
new_list.add_to_front("hello").display_list().add_to_back("good").add_to_back("friend").display_list().insert_at("very",2).display_list()
new_list.remove_value("hello")
new_list.display_list()



