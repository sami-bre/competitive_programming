def has_cycle(head):
    nodes = {}
    while(head):
        if nodes.get(head) != None:
            return 1
        nodes[head] = 0
        head = head.next
    return 0