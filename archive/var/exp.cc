// 3. exponent op. w/o overflow [Google]
// constraints: 0 < x < 10 and 0 < y < 100
// limitations: overflows
int powerxy(int x, int y)
{
    int r = x;

    for (size_t i = 1; i != y; ++i) {
        r *= x;
    }

    return r;
}

// doesn’t overflow
int powerxy2(int x, int y)
{
    std::vector<int> r;
    r.push_back(x);

    for (size_t i = 1; i != y; ++i) {
        r = vectimesx(r, x);
    }

    int res;
    if (r.back())
        res = r.back();
    else
        res = -1;

    for (size_t i = r.size() - 1; i > 0; --i) {
        res += r[i] * 10;
    }
    return res;
}

std::vector<int> vectimesx(std::vector<int> &r, int x)
{
    std::deque<int> deq;
    int n = 0;
    int carry = 0;

    for (size_t i = r.size(); i > 0; --i) {
        int m = r[i] * x;
        while (m) {
            int d = m % 10;
            if (carry) {
                deq.push_front(d*carry);
                carry = 0;
            } else {
                deq.push_front(d);
            }
            m /= 10;
            ++n;
        }
        // there is a carry digit
        if (n > 1) {
            carry = deq.front();
            deq.pop_front();
        }
        n = 0;
    }

    // too much copying?
    std::vector <int> vec;
    std::copy(deq.begin(), deq.end(), std::back_inserter(vec));
    return vec;
}
