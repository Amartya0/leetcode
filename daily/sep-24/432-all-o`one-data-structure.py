'''
432. All O`one Data Structure
Solved
Hard
Topics
Companies
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.

 

Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"
 

Constraints:

1 <= key.length <= 10
key consists of lowercase English letters.
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 5 * 10^4 calls will be made to inc, dec, getMaxKey, and getMinKey.
'''


# class AllOne:
#     def __init__(self):
#         self.DS = {}

#     def inc(self, key: str) -> None:
#         if key not in self.DS:
#             self.DS[key] = 1
#         else:
#             self.DS[key] += 1

#         self.DS = dict(sorted(self.DS.items(), key=lambda item: item[1]))

#     def dec(self, key: str) -> None:
#         if self.DS[key] == 1:
#             self.DS.pop(key)
#         else:
#             self.DS[key] -= 1

#         self.DS = dict(sorted(self.DS.items(), key=lambda item: item[1]))

#     def getMaxKey(self) -> str:
#         if self.DS:
#             return list(self.DS)[-1]
#         else:
#             return ""

#     def getMinKey(self) -> str:
#         if self.DS:
#             return list(self.DS)[0]
#         else:
#             return ""

class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = {}

    def _insert_node_after(self, new_node, prev_node):
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def visualize(self) -> None:
        current = self.head.next
        print("Doubly Linked List State:")
        print("HEAD", end=" <==> ")
        while current != self.tail:
            print(f"[Count: {current.count}, Keys: {
                  list(current.keys)}]", end=" <==> ")
            current = current.next
        print("TAIL")

    def inc(self, key: str) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            next_count = node.count + 1
            if node.next.count != next_count:
                new_node = Node(next_count)
                self._insert_node_after(new_node, node)
            else:
                new_node = node.next
            new_node.keys.add(key)
            self.key_to_node[key] = new_node
            node.keys.remove(key)
            if len(node.keys) == 0:
                self._remove_node(node)
        else:
            if self.head.next.count != 1:
                new_node = Node(1)
                self._insert_node_after(new_node, self.head)
            else:
                new_node = self.head.next
            new_node.keys.add(key)
            self.key_to_node[key] = new_node

    def dec(self, key: str) -> None:
        node = self.key_to_node[key]
        if node.count == 1:
            del self.key_to_node[key]
        else:
            prev_count = node.count - 1
            if node.prev.count != prev_count:
                new_node = Node(prev_count)
                self._insert_node_after(new_node, node.prev)
            else:
                new_node = node.prev
            new_node.keys.add(key)
            self.key_to_node[key] = new_node
        node.keys.remove(key)
        if len(node.keys) == 0:
            self._remove_node(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

def main():
    obj = AllOne()
    print(obj.inc("a"))
    print(obj.inc("b"))
    print(obj.inc("b"))
    print(obj.inc("b"))
    print(obj.inc("b"))
    print(obj.dec("b"))
    print(obj.dec("b"))
    print(obj.getMaxKey())
    print(obj.getMinKey())
    obj.visualize()


if __name__ == '__main__':
    main()
