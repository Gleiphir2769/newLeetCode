# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_num = ListNode(0)
        head_p = list_num
        while True:
            tsum = l1.val + l2.val
            if list_num.val + tsum < 10:
                list_num.val = list_num.val + tsum
                list_num.next = ListNode(0)
            else:
                list_num.val = list_num.val + tsum - 10
                list_num.next = ListNode(1)
            if l1.next is None and l2.next is None:
                if list_num.next.val == 0:
                    list_num.next = None
                return head_p
            elif l1.next is None:
                l1.next = ListNode(0)
            elif l2.next is None:
                l2.next = ListNode(0)
            list_num = list_num.next
            l1 = l1.next
            l2 = l2.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    # l2.next.next = ListNode(4)

    solution = Solution()
    l3 = solution.addTwoNumbers(l1, l2)

    while l3:
        print(l3.val)
        l3 = l3.next
