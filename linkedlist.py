

class ListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList: #sort things in ascending order [1,2,3,4]
    def __init__(self):
        self._head = None 
        
    def add(self, value):
        #inserts value at its correct position in the list.
        node = ListNode(value) #ListNode(value, None) for 1st add
        if (self._head is None) or (value < self._head.value):
            node.next = self._head #looks like ListNode(value, None)
            self._head = node #ListNode(value, ListNode(value2))
            return
        
        current_head = self._head

        while (current_head.next is not None) and (current_head.next.value < value):
            current_head = current_head.next

        node.next = current_head.next
        current_head.next = node
        
    def count(self):
        #returns the number of values in the list.
        count = 0
        current_head = self._head
        while current_head is not None:
            count += 1
            current_head = current_head.next
        return count
    
    def get(self,index):
        # returns the value stored at index. 
        # If index is invalid, it raises an IndexError.
        current_head = self._head
        current_index = 0

        if index < 0: 
            index += self.count() #[1,2,3]what if index = -7?
        if index < 0 or index >= self.count():
             raise IndexError("Index out of range. Absolute value of index > count()")

        while current_head is not None:
                if current_index == index:
                    return current_head.value
                else:
                    current_index += 1
                    current_head = current_head.next              
    
    def head(self):
        # returns the first ListNode in the list, or None if 
        # the list is empty.
        if self._head is not None:
            return self._head
        else:
            return None
        
    def print(self, reverse = False):
         #prints the values stored in the list, separated with commas
         #  and spaces and enclosed in square brackets, with a newline 
         # after the closing bracket. If reverse is False 
         # (or not specified), it prints the list in it's natural 
         # (ascending) order:
        
        current_head = self._head #create copy of list
        real_list = []
        while current_head is not None:
            real_list.append(current_head.value)
            current_head = current_head.next

        if reverse == True:
            sorted_list_True = sorted(real_list, reverse = True)
            print(f"[{', '.join(map(str,sorted_list_True))}]", end='\n')

        else: #reverse == False
            sorted_list_False = sorted(real_list, reverse = False)
            print(f"[{', '.join(map(str,sorted_list_False))}]", end='\n')
        
    def remove(self, index):
        #removes the value stored at index and returns 
        # that value. If index is invalid, it raises an IndexError.
        current_head = self._head
        current_index = 0

        if index < 0: #checks for valid index
            index += self.count()
        if index < 0 or index >= self.count():
             raise IndexError("Index out of range. Absolute value of index > count()")
            
        if index == 0: #if the index is at the head of the list
            removed_value = current_head.value
            self._head = self._head.next
            return removed_value
            
        while current_head is not None: #need to remove the value at the given index
            if current_index == (index - 1):
                if current_head.next is not None:
                    removed_value = current_head.next.value
                    current_head.next = current_head.next.next 
                    return removed_value
                else:
                    raise IndexError("Index out of range.")  
            current_index += 1
            current_head = current_head.next
                
        
    def remove_all(self, value):
        # removes all copies of value from the list.
        #  It returns the number of values that were removed.
        current_head = self._head
        removed_count = 0
        previous_head = None
        
        while current_head is not None: #need to remove the value at the given index
            if current_head.value == value:
                removed_count += 1
                if previous_head is None:
                    self._head = current_head.next
                else:
                    previous_head.next = current_head.next
                    
            else: 
                previous_head = current_head
            current_head = current_head.next    
        return removed_count    


# test = LinkedList()
# test.add(5)
# test.add(6)
# print(test.head())
# test.add(7)
# test.add(9)
# test.count()
# test.get(-1)

# test.print(reverse = True)
# test.head()
# #if __name__ == '__main__ :
