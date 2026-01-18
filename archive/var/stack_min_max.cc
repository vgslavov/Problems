// store pairs of value and current min on same stack:
// space: +O(n)
// time: O(1)

// use 2nd stack and store pairs of current min and a ref. counter (supports duplicates)
// time: O(1)
// space: worst O(n), when pushing ascending numbers, best O(1)
class Stack {
    public:
        bool empty() {
            return s_.empty();
        }

        int max() {
            if (!maxs_.empty())
                return maxs_.top().first;
        }

        int min() {
            if (!mins_.empty())
                return mins_.top().first;
        }

        int pop() {
            if (s_.empty())
                throw length_error(“empty stack”)

            val = s_.top();
            s_.pop();

            // max
            if (val == maxs_.top().first) {
                if (!--maxs_.top().second)
                    maxs_.pop();
            // min
            } else if (val == mins_.top().first) {
                if (!--mins_.top().second)
                    mins_.pop();
            }

            return val;
        }

        void push(int val) {
            s_.push(val);

            // max
            if (!maxs_.empty()) {
                // bigger than current max
                if (val > maxs_.top().first) {
                    maxs_.push(val, 1);
                // increase ref. counter
                } else if (val == maxs_.top().first) {
                    ++maxs_.top().second;
                }
            } else {
                maxs_.push(val, 1);
            }

            // min
            if (!mins_.empty()) {
                // smaller than current min
                if (val < mins_.top().first) {
                    mins_.push(val, 1);
                } else if (val == mins_.top().first) {
                    ++mins_.top().second;
                }
            } else {
                mins_.push(val, 1);
            }
        }

    private:
        stack<int> s_;
        stack<pair<int, int> > mins_;
        stack<pair<int, int> > maxs_;
};
