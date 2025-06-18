#include <queue>
#include <vector>

// number: 339
// title: Nested List Weight Sum
// url: https://leetcode.com/problems/nested-list-weight-sum/
// section: meta
// difficulty: medium
// tags: dfs, bfs

// constraints
// 1 <= nestedList.length <= 50
// The values of the integers in the nested list is in the range [-100, 100].
// The maximum depth of any integer is less than or equal to 50.

 // This is the interface that allows for creating nested lists.
 // You should not implement it, or speculate about its implementation
 class NestedInteger {
   public:
     // Constructor initializes an empty nested list.
     NestedInteger();
 
     // Constructor initializes a single integer.
     NestedInteger(int value);
 
     // Return true if this NestedInteger holds a single integer, rather than a nested list.
     bool isInteger() const;
 
     // Return the single integer that this NestedInteger holds, if it holds a single integer
     // The result is undefined if this NestedInteger holds a nested list
     int getInteger() const;
 
     // Set this NestedInteger to hold a single integer.
     void setInteger(int value);
 
     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
     void add(const NestedInteger &ni);
 
     // Return the nested list that this NestedInteger holds, if it holds a nested list
     // The result is undefined if this NestedInteger holds a single integer
     const std::vector<NestedInteger> &getList() const;
 };

int dfs(const std::vector<NestedInteger>& nestedList, int depth)
{
    int ans = 0;

    for (const auto& nested : nestedList) {
        if (nested.isInteger()) {
            ans += nested.getInteger() * depth;
        } else {
            ans += dfs(nested.getList(), depth+1);
        }
    }

    return ans;
}

// solution: Leetcode recursive dfs
// complexity:
// run-time: O(n)
// space: O(n)
int depthSum(const std::vector<NestedInteger>& nestedList)
{
    return dfs(nestedList, 1);
}

 // solution: Leetcode iterative bfs using queue/deque
 // complexity:
 // run-time: O(n)
 // space: O(n)
int depthSum2(const std::vector<NestedInteger>& nestedList)
{
    int depth = 1;
    int ans = 0;
    std::queue<NestedInteger> queue;

    // add to queue
    for (const auto & nested: nestedList) {
        queue.push(nested);
    }

    while (!queue.empty()) {
        int size = queue.size();

        while (size) {
            NestedInteger nested = queue.front();
            queue.pop();

            if (nested.isInteger()) {
                ans += nested.getInteger() * depth;
            } else {
                for (const auto & n : nested.getList()) {
                    queue.push(n);
                }
            }
            --size;
        }
        ++depth;
    }

    return ans;
}