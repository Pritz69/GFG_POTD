#Function to find the data of nth node from the end of a linked list
def getNthFromLast(head,n):
    #code here
    count = 0
    t = head
    while t is not None:
        count += 1
        t = t.next
    
    # Base case if given n is greater than size
    if n > count:
        return -1
    
    # Get the nth node from the back
    n = count - n
    t = head
    
    # Use the count variable to reach n
    count = 0
    while count != n:
        count += 1
        t = t.next
    
    return t.data
