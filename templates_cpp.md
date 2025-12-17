# Algorithm Templates (C++)

## Table of Contents

- [Sources](#sources)
- [Includes](#includes)
- [Template Class Example](#template-class-example)
- [Two Pointers](#two-pointers)
  - [One Input, Opposite Ends](#two-pointers-one-input-opposite-ends)
  - [One Input, Same Direction](#two-pointers-one-input-same-direction)
  - [Two Inputs, Exhaust Both](#two-pointers-two-inputs-exhaust-both)
- [Divide & Conquer](#divide--conquer)
  - [Recursive Stable Merge Sort](#divide--conquer-recursive-stable-merge-sort)
- [Deduplication](#deduplication)
  - [Three Sum](#deduplication-three-sum)
- [Sliding Window](#sliding-window)
  - [Sliding Window](#sliding-window-1)
  - [Sliding Fixed Window](#sliding-fixed-window)
- [Prefix Sum](#prefix-sum)
  - [Build a Diff Array](#build-a-diff-array-calculate-prefix-sum-on-it)
  - [Build a Prefix Sum: Using STL](#build-a-prefix-sum-using-stl)
  - [Build a Prefix Sum](#build-a-prefix-sum)
  - [Build a Prefix Sum for Range Queries](#build-a-prefix-sum-for-range-queries)
  - [Query Sum of Range Using Prefix Sum](#query-sum-of-range-using-prefix-sum)
- [Factorial](#factorial)
  - [Recursive](#recursive)
  - [Iterative](#iterative)
  - [Iterative: Stack](#iterative-stack)
- [String Building](#string-building)
  - [Efficient String Building](#efficient-string-building)
- [Linked Lists](#linked-lists)
  - [Definition for Singly-Linked List](#definition-for-singly-linked-list)
  - [Fast and Slow Pointer](#linked-list-fast-and-slow-pointer)
  - [Fast & Slow K Apart](#linked-list-fast--slow-k-apart)
  - [Dummy Nodes](#linked-list-dummy-nodes)
  - [Reversing a Linked List](#reversing-a-linked-list)
- [Monotonic Stack](#monotonic-stack)
  - [Monotonically Increasing Stack](#monotonically-increasing-stack)
- [Intervals](#intervals)
  - [Merge Intervals](#merge-intervals)
- [Binary Trees](#binary-trees)
  - [Recursive DFS (More Common)](#binary-tree-recursive-dfs-more-common)
  - [Iterative DFS (Less Common)](#binary-tree-iterative-dfs-less-common)
  - [Iterative BFS (More Common)](#binary-tree-iterative-bfs-more-common)
- [Graphs](#graphs)
  - [Build Adjacency List](#graph-build-adjacency-list)
  - [Recursive DFS](#graph-recursive-dfs)
- [Heaps](#heaps)
  - [Find Top K Elements with Heap](#find-top-k-elements-with-heap)
- [Binary Search](#binary-search)
  - [Using binary_search, Return If Found](#binary-search-using-binary_search-return-if-found)
  - [Using lower_bound, Return If Found](#binary-search-using-lower_bound-return-if-found)
  - [Using lower_bound, Return Index of Element](#binary-search-using-lower_bound-return-index-of-element)
  - [Manual, ala lower_bound](#binary-search-manual-ala-lower_bound)
- [Backtracking](#backtracking)
  - [Backtracking](#backtracking-1)
- [Dynamic Programming](#dynamic-programming)
  - [Recursive Top-Down w/ Memoization](#dynamic-programming-recursive-top-down-w-memoization)
  - [Iterative Bottom-Up 1D](#dynamic-programming-iterative-bottom-up-1d)
- [Tries](#tries)
  - [Build a Trie: Insert & Search](#build-a-trie-insert--search)

---

## Sources

- [LeetCode: Code Templates](https://leetcode.com/explore/interview/card/cheatsheets/720/resources/4723/)
- [AlgoMonster: Templates](https://algo.monster/templates)
- [NeetCode](https://neetcode.io/)

---

## Includes

```cpp
#include <algorithm>
#include <cstddef>
#include <deque>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>
```

---

## Template Class Example

Example template class demonstrating copy/move semantics, exception safety, and RAII principles.

```cpp
namespace notstd {

template <typename T>
class Example {
public:
    // default ctor
    Example() = default;

    // ctor
    Example(int size)
    : d_size(size) {}

    // dtor
    ~Example() noexcept
    {
        // can delete nullptr
        delete d_buf;
    }

    // support copying
    // copy ctor
    Example(const Example& rhs) = default;

    // copy assignment op
    // exception safety: strong guarantee
    Example& operator=(const Example& rhs)
    {
        // don't check, occasional self-assign is cheaper
        //if (this == &rhs) return *this;
        auto tmp = rhs;
        std::swap(tmp);
        // or?
        //this->swap(rhs);
        return *this;
    }

    // support moving
    // move ctor
    // exception safety: ?
    Example(Example&& rhs) noexcept
    : d_size(rhs.d_size)
    , d_buf(rhs.d_buf)
    {
        // leave moved *from* in valid state
        rhs.d_size = 0;
        rhs.d_buf = nullptr;
    }

    // move assignment op
    // exception safety: ?
    Example& operator=(Example&& rhs) noexcept
    {
        // have to check self-assign!
        if (this == &rhs) return *this;

        d_size = rhs.d_size;
        rhs.d_size = 0;

        d_buf = rhs.d_buf;
        rhs.d_buf = nullptr;

        return *this;
    }

    // member swap: don't throw!
    void swap(Example& rhs) noexcept
    {
        std::swap(d_buf, rhs.d_buf);
        std::swap(d_size, rhs.d_size);
    }

private:
    // default member init
    int d_size = 0;
    T* d_buf = nullptr;
};

// non-member cmp op
template <typename T>
bool operator==(const Example<T>& rhs, const Example<T>& lhs) noexcept
{
    return rhs.d_size == lhs.d_size &&
           rhs.d_buf == lhs.d_buf;
}

// non-member swap
template <typename T>
void swap(Example<T>& rhs, Example<T>& lhs)
{
    rhs.swap(lhs);
}
```

---

## Two Pointers

### Two Pointers: One Input, Opposite Ends

```cpp
bool condition(int a, int b)
{
    // define the condition for two pointers
    return a < b;
}

int twoPointersOpposite(const std::vector<int>& v)
{
    int ans = 0;
    int left = 0;
    int right = v.size()-1;

    while (left < right) {
        if (condition(v[left], v[right])) {
            ++left;
        } else {
            --right;
        }
    }

    return ans;
}
```

### Two Pointers: One Input, Same Direction

```cpp
int twoPointersSame(const std::vector<int>& v)
{
    int fast = 0;
    int slow = 0;
    int ans = 0;

    while (fast < v.size()) {
        // do logic

        // slow pointer only moves if condition is true
        if (condition(v[slow], v[fast])) {
            ++slow;
        }

        // fast pointer *always* moves forward
        ++fast;
    }

    return ans;
}
```

### Two Pointers: Two Inputs, Exhaust Both

```cpp
int twoPointers(const std::vector<int>& v1, const std::vector<int>& v2)
{
    int i = 0;
    int j = 0;
    int ans = 0;

    while (i < v1.size() && j < v2.size()) {
        // do some logic here
        if (condition(v1[i], v2[j])) {
            ++i;
        } else {
            ++j;
        }
    }

    while (i < v1.size()) {
        // do logic
        ++i;
    }

    while (j < v2.size()) {
        // do logic
        ++j;
    }

    return ans;
}
```

---

## Divide & Conquer

### Divide & Conquer: Recursive Stable Merge Sort

```cpp
std::vector<int> merge(const std::vector<int>& nums, int left_i, int right_i)
{
    // base case
    if (nums.size() < 2) {
        return nums;
    }

    // 1. divide: split array into 2
    size_t mid = nums.size() / 2;
    std::vector<int> left = merge(nums, left_i, mid-1);
    std::vector<int> right = merge(nums, mid, right_i);

    // 2. merge: combine
    int l = 0;
    int r = 0;
    std::vector<int> ans;

    while (l < left.size() && r < right.size()) {
        if (left[l] <= right[r]) {
            ans.push_back(left[l]);
            ++l;
        } else {
            ans.push_back(right[r]);
            ++r;
        }
    }

    // add remaining
    while (l < left.size()) {
        ans.push_back(left[l]);
        ++l;
    }

    while (r < right.size()) {
        ans.push_back(right[r]);
        ++r;
    }

    return ans;
}

std::vector<int> mergeSort(const std::vector<int>& nums)
{
    return merge(nums, 0, nums.size());
}
```

---

## Deduplication

### Deduplication: Three Sum

```cpp
void twoSum(const std::vector<int>& nums, int target, int left, int right)
{}

void threeSum(const std::vector<int>& nums, int target)
{
    std::sort(nums.begin(), nums.end());

    for (size_t i = 0; i != nums.size(); ++i) {
        // optimization: skip duplicates
        if (i > 0 && nums[i-1] == nums[i]) {
            continue;
        }

        // restrict search interval
        twoSum(nums, target-nums[i], i+1, nums.size()-1);
    }
}
```

---

## Sliding Window

### Sliding Window

```cpp
const int SOME_THRESHOLD = 10;

bool invalidCondition(int curr)
{
    return curr > SOME_THRESHOLD;
}

int slidingWindowLongest(const std::vector<int>& v)
{
    int ans = 0;
    int left = 0;
    int winSum = 0;

    for (int right = 0; right != v.size(); ++right) {
        winSum += v[right];

        // update left until window is valid again
        while (invalidCondition(winSum)) {
            winSum -= v[left];
            ++left;
        }

        // window is guaranteed to be valid here
        ans = std::max(ans, right - left + 1);

    }

    return ans;
}

bool validCondition(int curr)
{
    return curr >= SOME_THRESHOLD;
}

int slidingWindowShortest(const std::vector<int>& v)
{
    int left = 0;
    int winSum = 0;
    int ans = v.size();

    for (int right = 0; right != v.size(); ++right) {
        winSum += v[right];

        while (validCondition(winSum)) {
            // window is guaranteed to be valid here
            ans = std::min(ans, right-left+1);

            winSum -= v[left];
            ++left;
        }
    }

    return ans;
}
```

### Sliding Fixed Window

```cpp
int slidingWindowFixed(const std::vector<int>& v, int k)
{
    int ans = 0;
    int winSum = 0;

    // 1st window
    //for (size_t i = 0; i < v.size() && i < k; ++i)
    for (size_t i = 0; std::min(k, static_cast<int>(v.size())); ++i) {
        ans += v[i];
    }

    // start at k
    for (int right = k; right != v.size(); ++right) {
        int left = right - k;
        winSum -= v[left];
        winSum += v[right];
        ans = std::max(ans, winSum);
    }

    return ans;
}
```

---

## Prefix Sum

### Build a Diff Array, Calculate Prefix Sum on It

```cpp
std::vector<int> diffArray(
    const std::vector<int>& v,
    const std::vector<std::vector<int>>& shifts)
{
    std::vector<int> diff(v.size());

    for (const auto& range : shifts) {
        int start = range[0];
        int end = range[1];

        diff[start] += 1;

        // if inclusive
        if (end + 1 < diff.size()) {
            diff[end + 1] -= 1;
        }
    }

    return diff;
}
```

### Build a Prefix Sum: Using STL

```cpp
std::vector<int> prefixSumPartialSum(const std::vector<int>& v)
{
    std::vector<int> prefix(v.size()+1);
    prefix[0] = 0;
    std::partial_sum(v.begin(), v.end(), prefix.begin());
    return prefix;
}
```

### Build a Prefix Sum

```cpp
std::vector<int> prefixSum(const std::vector<int>& v)
{
    std::vector<int> prefix{v[0]};
    // or preallocate
    //std::vector<int> prefix(v.size());

    // start at 1!
    for (size_t i = 1; i != v.size(); ++i) {
        prefix.push_back(prefix[i-1] + v[i]);
        //prefix[i] = prefix[i-1] + v[i];
    }

    return prefix;
}
```

### Build a Prefix Sum for Range Queries

```cpp
int prefixSumRange(
    const std::vector<int>& v,
    int left,
    int right)
{
    std::vector<int> prefix{0, v[0]};

    for (size_t i = 1; i != v.size(); ++i) {
        prefix.push_back(prefix[i-1] + v[i]);
    }

    return prefix[right + 1] - prefix[left];
}
```

### Query Sum of Range Using Prefix Sum

```cpp
int queryPrefixSum(const std::vector<int>& prefix, int left, int right)
{
    if (left == 0) {
        return prefix[right];
    }

    return prefix[right] - prefix[left - 1];
}
```

---

## Factorial

### Recursive

```cpp
int factorial(int n)
{
    // base case
    if (n <= 1) {
        return 1;
    }

    // recursive call
    return n * factorial(n-1);
}
```

### Iterative

```cpp
int factorialIterative(int n)
{
    int ans = 1;

    for (int i = 2; i <= n; ++i) {
        ans *= i;
    }

    return ans;
}
```

### Iterative: Stack

```cpp
int factorialStack(int n)
{
    std::stack<int> s;
    int ans = 1;

    // push each call to a stack
    // top of stack is base case
    while (n > 0) {
        s.push(n);
        n -= 1;
    }

    // pop and use return value until stack is empty
    while (!s.empty()) {
        ans *= s.top();
        s.pop();
    }

    return ans;
}
```

---

## String Building

### Efficient String Building

```cpp
// v is a list of chars
std::string buildString(const std::vector<std::string>& v)
{
    return std::string(v.begin(), v.end());
}
```

---

## Linked Lists

### Definition for Singly-Linked List

```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};
```

### Linked List: Fast and Slow Pointer

```cpp
int fastSlowPtr(ListNode* head)
{
    ListNode* slow = head;
    ListNode* fast = head;
    int ans = 0;

    while (fast != nullptr && fast->next != nullptr) {
        // do logic
        slow = slow->next;
        fast = fast->next->next;
    }

    return ans;
}
```

### Linked List: Fast & Slow K Apart

```cpp
ListNode* fastSlowPtr(ListNode* head, int k)
{
    ListNode* slow = head;
    ListNode* fast = head;

    while (fast != nullptr && k != 0) {
        fast = fast->next;
        --k;
    }

    while (fast != nullptr) {
        // do logic
        slow = slow->next;
        fast = fast->next;
    }

    return slow;
}
```

### Linked List: Dummy Nodes

```cpp
ListNode* dummyNodes(ListNode* head)
{
    ListNode* dummy = new ListNode(0, head);
    ListNode* fast = head;
    ListNode* slow = head;

    // move fast pointer k ahead

    while (fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next;
    }

    // do something

    return dummy->next;
}
```

### Reversing a Linked List

```cpp
ListNode* reverseList(ListNode* head)
{
    ListNode* curr = head;
    ListNode* prev = nullptr;

    while (curr != nullptr) {
        ListNode* next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    return prev;
}
```

---

## Monotonic Stack

### Monotonically Increasing Stack

```cpp
std::vector<int> monotonicallyIncreasing(const std::vector<int>& nums)
{
    // can use vector instead of stack
    std::vector<int> stack;

    for (const auto& n : nums) {
        // for monotonically decreasing, just flip the > to <
        while (!stack.empty() && stack.back() > n) {
            // do logic
            stack.pop_back();
        }

        stack.push_back(n);
    }

    return stack;
}
```

---

## Intervals

### Merge Intervals

```cpp
std::vector<std::vector<int>> mergeIntervals(std::vector<std::vector<int>> intervals)
{
    std::sort(intervals.begin(), intervals.end());
    std::vector<std::vector<int>> ans;

    for (const auto& start_end : intervals) {
        // merge
        if (!ans.empty() && start_end[0] <= ans.back()[1]) {
            ans.back()[1] = std::max(ans.back()[1], start_end[1]);
        } else {
            ans.push_back(start_end);
        }
    }

    return ans;
}
```

---

## Binary Trees

### Binary Tree: Recursive DFS (More Common)

```cpp
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int val) : val(val), left(nullptr), right(nullptr) {}
};

int dfs(TreeNode* root)
{
    if (!root) {
        return 0;
    }

    // do something with ans
    int ans = 0;

    std::cout << "pre order: " << root->val << std::endl;

    dfs(root->left);

    // sorted order
    std::cout << "in order: " << root->val << std::endl;

    dfs(root->right);

    std::cout << "post order: " << root->val << std::endl;

    return ans;
}
```

### Binary Tree: Iterative DFS (Less Common)

```cpp
int dfs(TreeNode* root)
{
    std::stack<TreeNode *> s;
    int ans = 0;

    while (!s.empty()) {
        TreeNode* node_p = s.top();
        s.pop();

        // do logic
        if (node_p->left) {
            s.push(node_p->left);
        }

        if (node_p->right) {
            s.push(node_p->right);
        }
    }

    return ans;
}
```

### Binary Tree: Iterative BFS (More Common)

```cpp
int bfs(TreeNode* root)
{
    std::queue<TreeNode *> level;
    level.push(root);
    int ans = 0;

    while (!level.empty()) {
        int size = level.size();
        // do logic for current level

        while (size) {
            // front of queue is leftmost
            TreeNode* node_p = level.front();
            // pop *front* of queue
            level.pop();

            // do logic
            if (node_p->left) {
                // back of queue is rightmost
                level.push(node_p->left);
            }

            if (node_p->right) {
                level.push(node_p->right);
            }

            // don't forget to decrement size
            --size;
        }
    }

    return ans;
}
```

---

## Graphs

### Graph: Build Adjacency List

```cpp
std::unordered_map<int, std::vector<int>> adjacencyList(
    const std::vector<std::vector<int>>& edges)
{
    std::unordered_map<int, std::vector<int>> graph;

    for (const auto& e : edges) {
        graph[e[0]].push_back(e[1]);
        // undirected graph
        graph[e[1]].push_back(e[0]);
    }

    return graph;
}
```

### Graph: Recursive DFS

```cpp
int dfs(int node,
        const std::unordered_map<int, std::vector<int>>& graph,
        std::vector<bool>& seen)
{
    // base case
    if (seen[node]) {
        return 0;
    }

    seen[node] = true;

    // do logic

    for (const auto& neighbor : graph[node]) {
        dfs(neighbor, graph, seen);
    }

    return 0;
}
```

---

## Heaps

### Find Top K Elements with Heap

```cpp
std::vector<int> findTopk(const std::vector<int>& v, int k)
{
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
    //std::priority_queue<int> maxHeap;

    for (const auto& num : v) {
        // do some logic to push onto heap according to problem's criteria
        //minHeap.push(std::tuple<int, int>(CRITERIA, num));
        minHeap.push(num);

        if (minHeap.size() > k) {
            minHeap.pop();
        }
    }

    std::vector<int> ans;
    while (!minHeap.empty()) {
        ans.emplace_back(std::move(minHeap.top()));
        minHeap.pop();
    }

    return ans;
}
```

---

## Binary Search

### Binary Search: Using binary_search, Return If Found

```cpp
bool binarySearch(const std::vector<int>& v, int target)
{
    return std::binary_search(v.begin(), v.end(), target);
}
```

### Binary Search: Using lower_bound, Return If Found

```cpp
bool binarySearchLeft(const std::vector<int>& v, int target)
{
    int lower = *std::lower_bound(v.begin(), v.end(), target);
    if (lower != target) {
        return false;
    }

    return true;
}
```

### Binary Search: Using lower_bound, Return Index of Element

```cpp
int binarySearchLeft2(const std::vector<int>& v, int target)
{
    auto it = std::lower_bound(v.begin(), v.end(), target);
    if (it == v.end() || *it != target) {
        return -1;
    }

    return std::distance(v.begin(), it);
}
```

### Binary Search: Manual, ala lower_bound

```cpp
int binarySearch(const std::vector<int>& v, int target)
{
    int left = 0;
    int right = v.size()-1;

    while (left <= right) {
        int mid = left + (right-left)/2;

        if (v[mid] == target) {
            return mid;
        } else if (v[mid] > target) {
            right = mid-1;
        } else {
            left = mid+1;
        }
    }

    // left is the insertion point
    return left;
}
```

---

## Backtracking

### Backtracking

```cpp
void backtrack(curr)
{
    // base case
    if (BASE_CASE) {
        // modify the answer
        return;
    }

    // do logic

    for (const auto& choice : CHOICES) {
        // make choice
        backtrack();
        // undo choice
    }
}
```

---

## Dynamic Programming

### Dynamic Programming: Recursive Top-Down w/ Memoization

```cpp
int dp(int STATE, const std::vector<int>& v, std::map<int, STATE>& memo)
{
    // base cases
    if (BASE_CASE) {
        return 0;
    }

    // check cache
    auto it = memo.find(STATE);
    if (it != memo.end()) {
        return memo[STATE];
    }

    // recurrence relation
    memo[STATE] = RECURRENCE_RELATION(STATE);

    return memo[STATE];
}

int fn(const std::vector<int>& v)
{
    std::map<int, STATE> memo;
    return dp(STATE_FOR_WHOLE_INPUT, memo);
}
```

### Dynamic Programming: Iterative Bottom-Up 1D

```cpp
int fn(const std::vector<int>& v)
{
    // init
    std::vector<int> dp(v.size());

    // set base case(s)
    dp[0] = BASE_CASE;

    for (size_t i = 2; i != v.size(); ++i) {
        // define recurrence relation
        dp[STATE] = RECURRENCE_RELATION(STATE)
    }

    return dp[v.size()-1];
}
```

**TODO:** Dynamic programming: iterative bottom-up 2D

---

## Tries

### Build a Trie: Insert & Search

```cpp
class Trie {
public:
    using ChildrenMap = std::map<char, Trie>;

    void insert(const std::string& word) {
        Trie* node = this;

        for (const auto& c: word) {
            ChildrenMap& children = node->d_children;
            auto it = children.find(c);
            if (it == children.end()) {
                children[c] = Trie();
            }

            node = &children[c];
        }
    }

    bool search(const std::string& word) {
        Trie* node = this;

        for (const auto& c: word) {
            ChildrenMap& children = node->d_children;
            const auto cit = children.find(c);
            if (cit == children.end()) {
                return false;
            }

            node = &children[c];
        }

        return true;
    }

private:
    ChildrenMap d_children;
};

} // notstd namespace
```
