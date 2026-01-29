# Dynamic Programming Summary

## What is Dynamic Programming?

```
Dynamic Programming = Recursion + Memoization
```

DP is an optimization technique for recursive problems that have:
- **Optimal substructure**: Optimal solution can be built from optimal solutions of subproblems
- **Overlapping subproblems**: Same subproblems are solved multiple times

## When to Use DP

Look for these problem patterns:
- **Min cost** to do something
- **Max profit** from some action
- **Number of ways** to achieve a goal
- **Longest possible** sequence/subsequence
- **Is it possible** to reach a state

## Two Approaches

### 1. Top-Down (Memoization)
- Start from the final state, recurse down to base cases
- Cache results to avoid recomputation
- Easier to write and understand
- Uses recursion

```python
from functools import cache

@cache
def dp(state):
    if BASE_CASE:
        return BASE_VALUE
    return RECURRENCE_RELATION(state)
```

Or with manual memoization:
```python
def dp(state):
    if BASE_CASE:
        return BASE_VALUE
    if state in memo:
        return memo[state]
    memo[state] = RECURRENCE_RELATION(state)
    return memo[state]

memo = {}
```

### 2. Bottom-Up (Tabulation)
- Start from base cases, build up to final answer
- Uses iteration with nested loops (one per state variable)
- Faster execution, less memory overhead
- Start *after* base case

```python
def solve(arr):
    n = len(arr)
    dp = [0] * n

    # Base case(s)
    dp[0] = arr[0]

    # Build up from base case
    for i in range(1, n):
        dp[i] = RECURRENCE_RELATION(i)

    return dp[n-1]
```

## Strategy for Solving DP Problems

1. **Start with recursive backtracking** - Write the brute force solution
2. **Add memoization** - Convert to top-down DP
3. **Convert to bottom-up** - Remove recursion for better performance
4. **Optimize space** - Often can reduce from O(n) to O(1) if only need previous states

## Common DP Patterns

### Pattern 1: Linear Sequence (1D DP)

**State**: Single index tracking position in sequence
**Structure**: `dp[i]` depends on previous states like `dp[i-1]`, `dp[i-2]`

**Examples**:
- Fibonacci: `dp[i] = dp[i-1] + dp[i-2]`
- Climbing Stairs: `dp[i] = dp[i-1] + dp[i-2]`
- House Robber: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`

```python
# House Robber (LeetCode #198)
def rob(nums):
    @cache
    def dp(i):
        if i == 0:
            return nums[0]
        elif i == 1:
            return max(nums[0], nums[1])
        return max(dp(i-1), dp(i-2) + nums[i])
    return dp(len(nums)-1)
```

### Pattern 2: Two Sequence/Substring (2D DP)

**State**: Two indices (i, j) for positions in two sequences or substring boundaries
**Structure**: `dp[i][j]` compares characters, decides to include or skip

**Examples**:
- Longest Common Subsequence
- Edit Distance
- Maximum Length Repeated Subarray

```python
# Longest Common Subsequence (LeetCode #1143)
def lcs(text1, text2):
    @cache
    def dp(i, j):
        if i == len(text1) or j == len(text2):
            return 0
        # Match: advance both
        if text1[i] == text2[j]:
            return 1 + dp(i+1, j+1)
        # No match: try both options
        return max(dp(i, j+1), dp(i+1, j))
    return dp(0, 0)
```

### Pattern 3: State Machine DP

**State**: Multiple possible states with transitions between them
**Structure**: Track which state you're in and transition based on decisions

**Examples**:
- Best Time to Buy/Sell Stock with Cooldown
- Best Time to Buy/Sell Stock with Transaction Fee

```python
# Stock with Cooldown (LeetCode #309)
def max_profit(prices):
    reset = 0           # Initial/after cooldown
    sold = -math.inf    # Just sold
    held = -math.inf    # Holding stock

    # Transitions: reset -buy-> held -sell-> sold -rest-> reset
    for p in prices:
        pre_sold = sold
        sold = held + p              # Sell: held -> sold
        held = max(held, reset - p)  # Buy: reset -> held, or hold
        reset = max(reset, pre_sold) # Cooldown: sold -> reset

    return max(reset, sold)
```

### Pattern 4: Kadane's Algorithm (Subarray)

**State**: Track current subarray sum and global maximum
**Structure**: Either extend current subarray or start fresh

```python
# Maximum Subarray (LeetCode #53)
def max_subarray(nums):
    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
```

## Multidimensional DP

| Dimensions | State Variables | Example |
|------------|-----------------|---------|
| 1D | Index `i` | Fibonacci, Climbing Stairs |
| 2D | Two indices `(i, j)` | LCS, Edit Distance |
| 3D | + Constraint (e.g., `k` transactions) | Stock with K transactions |
| 4D | + Boolean status | Stock with cooldown |
| 5D | + Bitmask for visited/seen | Traveling Salesman |

## Complexity Analysis

- **Time**: `O(n * F)` where:
  - `n` = number of possible states
  - `F` = computation per state
- **Space**: Usually equal to time complexity, but can often be optimized

## Memoization Techniques

| Method | When to Use | Performance |
|--------|-------------|-------------|
| `@functools.cache` | Top-down, Python | Convenient, automatic |
| `dict` memo | Top-down, any language | Flexible, sparse states |
| Array/list | Bottom-up | Faster, more memory |

## Common DP Problems by Category

### Easy (1D Linear)
- Fibonacci Number (#509)
- Climbing Stairs (#70)
- Min Cost Climbing Stairs (#746)

### Medium (1D with Decisions)
- House Robber (#198)
- Maximum Subarray (#53)
- Best Time to Buy/Sell Stock (#121, #122)

### Medium (2D Subsequence)
- Longest Common Subsequence (#1143)
- Palindromic Substrings (#647)
- Longest Palindromic Substring (#5)

### Medium (State Machine)
- Best Time to Buy/Sell Stock with Cooldown (#309)
- Best Time to Buy/Sell Stock with Transaction Fee (#714)

## Tips and Gotchas

1. **Start simple**: Always start with the recursive solution first
2. **Identify the state**: What variables fully describe a subproblem?
3. **Find the recurrence**: How does the current state relate to previous states?
4. **Handle base cases**: What are the smallest subproblems?
5. **Space optimization**: If only using `dp[i-1]` and `dp[i-2]`, use two variables instead of an array
6. **Bottom-up direction**: Sometimes easier to fill from end to start (e.g., LCS)
7. **Off-by-one errors**: Be careful with array sizing and loop bounds

## Quick Reference

```
Don't know where to start? → Use DFS + memoization

Problem asks for "minimum/maximum"? → Consider DP

Problem asks for "number of ways"? → Consider DP

Problem involves subsequence/substring? → Consider 2D DP

Problem has multiple states (hold/sell/cooldown)? → State machine DP

Want to optimize top-down to bottom-up? →
  1. Identify state variables → loop indices
  2. Identify base cases → initial values
  3. Identify recurrence → loop body
```
