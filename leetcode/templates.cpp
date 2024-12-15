#include <algorithm>
#include <deque>
#include <iostream>
#include <iterator>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <tuple>
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
    ~Example()
    {
        if (d_buf) {
            delete d_buf;
        }
    }

    // support copying
    // copy ctor
    Example(const Example& rhs) = default;

    // copy assignment op
    // exception safety: strong guarantee
    Example& operator=(const Example& rhs)
    {
        // don't check self-assignment, copy is cheaper
        //if (this == &rhs) return *this;
        auto tmp = rhs;
        std::swap(tmp);
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
        d_buf = std::move(rhs.d_buf);
        rhs.d_buf = nullptr;
        return *this;
    }

private:
    // default member init
    int d_size = 0;
    T* d_buf = nullptr;
};

// non-member
template <typename T>
bool operator==(const Example& a, const Example& b)
{
    return a.d_size == b.d_size && a.d_buf == b.d_buf;
}

// Two pointers: one input, opposite ends
int fn(const std::vector<int>& v)
{
    int ans = 0;
    int left = 0;
    int right = v.size()-1;

    while (left < right) {
        if (CONDITION) {
            ++left;
        } else {
            --right;
        }
    }

    return ans;
}

// Two pointers: two inputs, exhaust both
int fn(const std::vector<int>& v1, const std::vector<int>& v2)
{
    int i = 0;
    int j = 0;
    int ans = 0;

    while (i < v1.size() && j < v2.size()) {
        // do some logic here
        if (CONDITION) {
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

// Sliding window
int fn(const std::vector<int>& v)
{
    int ans = 0;
    int left = 0;
    int curr = 0;

    for (int right = 0; right != v.size(); ++right) {
        // do logic here to add v[right] to curr

        while (WINDOW_CONDITION_BROKEN) {
            // remove v[left] from curr
            ++left;
        }

        // update ans

    }

    return ans;
}

// Sliding *fixed* window
int fn(const std::vector<int>& v, int k)
{
    int ans = 0;
    int curr = 0;

    for (int i = 0; i < v.size() && i < k; ++i) {
        // do logic here to add v[i] to curr
    }

    // update ans

    for (int i = 0; i < std::min(k, v.size()) ; ++i) {
        // add v[i] & remove v[i-k] from curr

        // update ans

    }

    return ans;
}

// Build a prefix sum
std::vector<int> fn(const std::vector<int>& v)
{
    std::vector<int> prefix{v[0]};

    for (int i = 1; i != v.size(); ++i) {
        prefix.push_back(prefix[i-1] + v[i]);
    }

    return prefix;
}

// Efficient string building
// v is a list of chars
std::string fn(const std::vector<std::string>& v)
{
    std::string s(v.begin(), v.end());
    return s;
}

// TODO: linked lists

struct Tree {
    int val;
    Tree* left;
    Tree* right;
};

// Binary tree: recursive DFS (more common)
int dfs(Tree* root)
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
int dfs(Tree* root)
{
    std::stack<Tree> s;
    int ans = 0;

    while (!s.empty()) {
        Tree node = s.top();
        s.pop();

        // do logic
        if (node.left) {
            s.push(node.left);
        }

        if (node.right) {
            s.push(node.right);
        }
    }

    return ans;
}

// Binary tree: iterative BFS (more common)
int bfs(Tree* root)
{
    std::deque<Tree*> queue{root};
    int ans = 0;

    while (!queue.empty()) {
        int size = queue.size();
        // do logic for current level

        while (!size) {
            Tree* node_p = queue.front();
            queue.pop_front();

            // do logic
            if (node_p->left) {
                queue.push_back(node_p->left);
            }

            if (node_p->right) {
                queue.push_back(node_p->right);
            }

            --size;
        }
    }

    return ans;
}

// Find top k elements with heap
std::vector<int> fn(const std::vector<int>& v, int k)
{
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;

    for (const auto& num : v) {
        // do some logic to push onto heap according to problem's criteria
        //minHeap.push(std::tuple(CRITERIA, num));
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
bool fn(const std::vector<int>& v, int target)
{
    return std::binary_search(v.begin(), v.end(), target);
}

// Binary search: using lower_bound, return if found
bool fn(const std::vector<int>& v, int target)
{
    int lower = *std::lower_bound(v.begin(), v.end(), target);
    if (lower != target) {
        return false;
    }

    return true;
}

// Binary search: using lower_bound, return index of element
int fn(const std::vector<int>& v, int target)
{
    auto it = std::lower_bound(v.begin(), v.end(), target);
    if (it == v.end() || *it != target) {
        return -1;
    }

    return std::distance(v.begin(), it);
}

// Binary search: manual, ala lower_bound
int fn(const std::vector<int>& v, int target)
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

// TODO: Backtracing

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

    for (int i = 2; i != v.size(); ++i) {
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
        Trie* curr = this;

        for (const auto& c: word) {
            ChildrenMap& children = curr->children();
            auto it = children.find(c);
            if (it == children.end()) {
                children[c] = Trie();
            }

            curr = &curr->children()[c];
        }
    }

    bool search(const std::string& word) {
        Trie* curr = this;

        for (const auto& c: word) {
            ChildrenMap& children = curr->children();
            const auto cit = children.find(c);
            if (cit == children.end()) {
                return false;
            }

            curr = &curr->children()[c];
        }

        return true;
    }

    // TODO: don't expose children?
    ChildrenMap& children() { return d_children; }
private:
    ChildrenMap d_children;
};

} // notstd namespace
