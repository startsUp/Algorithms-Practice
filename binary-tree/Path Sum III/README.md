[EASY] 
# Path Sum III
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.


## Solution
Maintain a stack of possible values that add up to the sum. When a new node is reached update all the paths and see if values reaches 0, meaning a path sums to the given *sum* value. Pop the root value and update the path when both trees are checked.
```
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.valStack = []
        self.count = 0
        self.dfs(root, sum)
        return self.count
    
    def dfs(self, root: TreeNode, sum: int):
        if(root is None):
            return
        for i in range(len(self.valStack)):
            self.valStack[i] = self.valStack[i] - root.val
            if(self.valStack[i] == 0):
                self.count+=1
        if(sum-root.val == 0):
            self.count+=1
        self.valStack.append(sum-root.val)
        self.dfs(root.left, sum)
        self.dfs(root.right, sum)
        self.valStack.pop()
        for i in range(len(self.valStack)):
            self.valStack[i]+=root.val

```