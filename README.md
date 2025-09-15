# Code-Practice-Study-Record

## Google Leetcode Library:
### Two Sum

- Tag: hashtable
- Intuition: use a hashtable to check complements fast
- Approach: one-pass; check complement, else store value->index
- Complexity: O(n) time, O(n) space

#### Code
```python3 []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two-pass hash table
        hashmap = {}

        # find complement idx
        for i in range(len(nums)):
            # calculate complement
            complement = target - nums[i]

            # check keys
            if complement in hashmap and complement in nums and hashmap[complement] != i:
                return [i, hashmap[complement]]
            # create a hash table value:idx
            hashmap[nums[i]] = i
```

### Add Two Numbers

- Tag: linkedlist
- Intuition: add digits with carry using a dummy head
- Approach: iterate while l1/l2/carry; sum digits, update carry, append, advance
- Complexity: O(n) time, O(n) space

#### Code
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        # check l1 extra digit, l2 extra digit, extra carry
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0 # safeguard no digit case
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            # get carry and local vlaue
            carry = columnSum//10
            newNode = ListNode(columnSum % 10)
            # update curr pointer
            curr.next = newNode
            curr = newNode
            # safeguard no digit case
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next

        
```



