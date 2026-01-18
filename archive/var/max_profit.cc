//using namespace std;

// brute force: O(n^2)
int find_max_profit_slow(const vector<int> startprice)
{
    float max_profit = 0;
    int len = startprice.size();

    for (int i = 0; i < len; i++) {
        for (int j = i+1; j < len; j++) {
            max_profit = max(max_profit, startprice[j] - startprice[i]);
        }
    }
    return max_profit;
}

// divide & conquer: O(n logn)
// sort?

// O(n)
// greedy?
// TODO: check for small # of prices
int find_max-profit-fast(const vector<int> startprice)
{
    // set min_price! (otherwise it will never get changed)
    float min_price = (float)numeric_limits<int>::max();
    float max_profit = 0;
    int len = startprice.size();

    for (int i = 0; i < len; i++) {
        // 1st: max
        max_profit = max(max_profit, startprice[i] - min_price);
        // then: min (for next iteration)
        min_price = min(min_price, startprice[i]);
    }
    return max_profit;
}
