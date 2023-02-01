from typing import Optional
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
  nodeList = []
  while head!=None:
    nodeList.append(head)
    head = head.next
  return nodeList[len(nodeList)//2]