def func(head, val):
    temp = head
    prev = None
    while(temp!=None and temp.data==val):
        head = temp.next
        temp = head
    while(temp!=None):
        while(temp!=None and temp.val!=val):
            prev = temp
            temp = temp.next
        if temp==None:
            return head
        prev.next = temp.next
        temp = prev.next
    return head
