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

bool condition(int a, int b)
{
    // define the condition for two pointers
    return a < b;
}

// Two pointers: one input, opposite ends
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

// Two pointers: one input, same direction
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

// Two pointers: two inputs, exhaust both
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

const int SOME_THRESHOLD = 10;

bool invalidCondition(int curr)
{
    return curr > SOME_THRESHOLD;
}

// Sliding window
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

// Sliding *fixed* window
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

// Build a diff array, calculate prefix sum on it
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

// Build a prefix sum: using STL
std::vector<int> prefixSumPartialSum(const std::vector<int>& v)
{
    std::vector<int> prefix(v.size()+1);
    prefix[0] = 0;
    std::partial_sum(v.begin(), v.end(), prefix.begin());
    return prefix;
}

// Build a prefix sum
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

// Build a prefix sum for range queries
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

// Query sum of range using prefix sum
int queryPrefixSum(const std::vector<int>& prefix, int left, int right)
{
    if (left == 0) {
        return prefix[right];
    }

    return prefix[right] - prefix[left - 1];
}

// recursive
int factorial(int n)
{
    // base case
    if (n <= 1) {
        return 1;
    }

    // recursive call
    return n * factorial(n-1);
}

// iterative
int factorialIterative(int n)
{
    int ans = 1;

    for (int i = 2; i <= n; ++i) {
        ans *= i;
    }

    return ans;
}

// iterative: stack
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

// Efficient string building
// v is a list of chars
std::string buildString(const std::vector<std::string>& v)
{
    return std::string(v.begin(), v.end());
}

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

// Linked list: fast and slow pointer
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

// Linked list: fast & slow k apart
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

// Linked list: dummy nodes
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

// Reversing a linked list
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

// monotonically increasing stack
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

// merge intervals
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

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int val) : val(val), left(nullptr), right(nullptr) {}
};

// Binary tree: recursive DFS (more common)
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

// Binary tree: iterative DFS (less common)
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

// Binary tree: iterative BFS (more common)
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

// Graph: build adjacency list
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

// Graph: recursive DFS
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

// Find top k elements with heap
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

// Binary search: using binary_search, return if found
bool binarySearch(const std::vector<int>& v, int target)
{
    return std::binary_search(v.begin(), v.end(), target);
}

// Binary search: using lower_bound, return if found
bool binarySearchLeft(const std::vector<int>& v, int target)
{
    int lower = *std::lower_bound(v.begin(), v.end(), target);
    if (lower != target) {
        return false;
    }

    return true;
}

// Binary search: using lower_bound, return index of element
int binarySearchLeft2(const std::vector<int>& v, int target)
{
    auto it = std::lower_bound(v.begin(), v.end(), target);
    if (it == v.end() || *it != target) {
        return -1;
    }

    return std::distance(v.begin(), it);
}

// Binary search: manual, ala lower_bound
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

// Dynamic programming: recursive top-down w/ memoization
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

// Dynamic programming: iterative bottom-up 1D
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

// TODO: Dynamic programming: iterative bottom-up 2D

// Build a trie: insert & search
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
