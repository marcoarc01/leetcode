"""

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cabeca = ListNode(0)
        atual = cabeca
        addUm = 0

        while l1 is not None or l2 is not None or addUm != 0:
            valor1 = l1.val if l1 is not None else 0
            valor2 = l2.val if l2 is not None else 0

            soma = valor1 + valor2 + addUm
            valor = soma % 10
            addUm = soma // 10

            newNode = ListNode(valor)
            atual.next = newNode
            atual = atual.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        resultado = cabeca.next
        cabeca.next = None
        return resultado
                