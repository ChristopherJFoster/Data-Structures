Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?

   Since we always append the element to the end of the queue's storage list, the time and space complexities are each `O(1)`.

2. What is the runtime complexity of `dequeue`?

   (I think:)
   Since we always pop the first element of the queue's storage list, the time and space complexities are each `O(1)`.

   (But maybe:)
   Since each element after the first in the queue's storage list will have to be shifted when the first element is popped, the time complexity is `O(n)`, where n is the number of elements in the list. The space complexity is `O(1)`.

3) What is the runtime complexity of `len`?

   The time and space complexities are each `O(1)`.

## Binary Search Tree

1. What is the runtime complexity of `insert`?

   If the tree were well-balanced, the time and space complexities would each be `O(log n)`. In the worst-case scenario, however, the tree is maximally unbalanced—all children are left-hand nodes, or they're all right-hand nodes, and the inserted value belongs at the lowest level. In this case, the space and time complexities are each `O(n)`.

2. What is the runtime complexity of `contains`?

   The same analysis of `insert` applies to `contains`: `O(log n)` (time and space) if the tree is more-or-less balanced, `O(n)` (time and space) if the tree is maximally unbalanced.

3. What is the runtime complexity of `get_max`?

   `O(log n)` time complexity if the tree is balanced, `O(n)` time complexity if the tree is maximally unbalanced.

## Heap

1. What is the runtime complexity of `_bubble_up`?

   The time complexity is `O(log n)`, where `n` is the number of elements in the heap. Since additional elements are always added to the rightmost open leaf of the lowest level of the heap (i.e., the end of list), the tree cannot be more than slightly unbalanced. As such, at most `log n` comparisions will need to be made to bubble up an element to its proper place in the heap.

   The space complexity of `_bubble_up` is also O(log n), where `n` is the number of elements in the heap. `_bubble_up` recursively calls itself, but at most it will do so `log n` times.

2. What is the runtime complexity of `_sift_down`?

   Like `_bubble_up`, the time and space complexities of `_sift_down` are each `O(log n)`, and for the same reasons.

3. What is the runtime complexity of `insert`?

   Since `insert` adds a new element to the end of the heap's storage list (a O(1) operation) and then calls `_bubble_up` on the index of that element, the runtime complexity is the same as that of `_bubble_up`: the time and space complexities are each `O(log n)`

4) What is the runtime complexity of `delete`?

   Since `delete` swaps the first and last elements of the heap's storage list (a O(1) operation), then deletes the last element (a O(1) operation), then calls `_sift_down` on the first element, the runtime complexity is the same as that of `_sift_down`: the time and space complexities are each `O(log n)`

5) What is the runtime complexity of `get_max`?

   Since the maximum value in a max_heap is always the first element, the time and space complexities of `get_max` are each `O(1)`.

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

   (I think:)
   The time and space complexities are each `O(1)`.

2. What is the runtime complexity of `ListNode.insert_before`?

   (I think:)
   The time and space complexities are each `O(1)`.

3. What is the runtime complexity of `ListNode.delete`?

   (I think:)
   The time and space complexities are each `O(1)`.

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

   The time and space complexities are each `O(1)`.

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

   The time and space complexities are each `O(1)`.

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

   The time and space complexities are each `O(1)`.

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

   The time and space complexities are each `O(1)`.

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

   (I think:)
   The time and space complexities are each `O(1)`.

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

   (I think:)
   The time and space complexities are each `O(1)`.

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    (I think:)
    The time and space complexities are each `O(1)`.

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    (I think:)
    Since the time and space complexities of `DoublyLinkedList.delete` are each `O(1)`, the worst-case runtime of `Array.splice` could only hope to perform as well as `DoublyLinkedList.delete`, but will usually perform worse.
