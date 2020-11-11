class node:
  def __init__(self, val, ptr):
    self.val = val
    self.ptr = ptr

def add(head, val):
  if exist(head, val):
    return head
  else:
    new_node = node(val, head)
    return new_node

def exist(head, val):
  if head is None:
    return False

  if val is head.val:
    return True
  else:
    return exist(head.ptr, val)

def remove(head, val):
  if head.val is val:
    return head.ptr

  present_node = head
  next_node = head.ptr
  while(1):
    if next_node is None:
      break
    if next_node.val is val:
      present_node.ptr = next_node.ptr
      break
    else:
      present_node = next_node
      next_node = next_node.ptr
  return head

if __name__ == "__main__":
  # init
  head = node(input("Input: "), None)

  while(1):
    val = raw_input("Input: ")
    if val is "":
      break
    head = add(head, int(val))
  
  iter_head = head
  while(1):
    if iter_head is None:
      break
    print str(iter_head.val)
    iter_head = iter_head.ptr

  while(1):
    val = raw_input("Remove: ")
    if val is "":
      break
    head = remove(head, int(val))
 
  iter_head = head
  while(1):
    if iter_head is None:
      break
    print str(iter_head.val)
    iter_head = iter_head.ptr


