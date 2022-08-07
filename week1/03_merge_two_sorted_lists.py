
'''
Solution 1:
Time Complexity: O(n)
Space Complexity: O(1)
'''

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        result = None
        
        if ptr1 is None:
            return ptr2
        if ptr2 is None:
            return ptr1
        
        if ptr1.val <= ptr2.val:
            result = ptr1
            ptr1 = ptr1.next
        else:
            result = ptr2
            ptr2 = ptr2.next
        head = result
        
        while ptr1 is not None and ptr2 is not None:
            if ptr1.val <= ptr2.val:
                result.next = ptr1
                ptr1 = ptr1.next
                result = result.next
            else:
                result.next = ptr2
                ptr2 = ptr2.next
                result = result.next
        if ptr1 is not None:
            result.next = ptr1
        if ptr2 is not None:
            result.next = ptr2
        return head