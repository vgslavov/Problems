// find k closest stars: selection algorithm

// find k closest stars: max-heap of k elements
// time: O(n logk) time
// space: O(k) space
vector<Star> find_k_closest(istringstream &sin, int k)
{
    priority_queue<Star, vector<Star> > max_heap;
    string line;

    // get first k stars
    // getline: separate input (istringstream) into lines
    while (getline(sin, line)) {
        // parse line (format: ID, x, y, z)
        stringstream line_stream(line);
        string buf;

        // get ID
        getline(line_stream, ‘,’);
        int ID = stoi(buf);

        // store x, y, z
        array<double, 3> data;
        for (int i = 0; i < 3; i++) {
            getline(line_stream, buf, ‘,’);
            data[i] = stod(buf);
        }

        // init star
        Star s{ID, data[0], data[1], data[2]};

        // put star in heap
        // heap is full, figure out what to remove
        if (max_heap.size() == k) {
            // compare top of heap with new star
            Star far_star = max_heap.top();
            // star is closer than current farthest one
            if (s < far_star) {
                max_heap.pop();
                max_heap.push(s);
            }
            // skip star (it’s farther from farthest seen so far)
        // heap is not full
        } else {
            max_heap.push(s);
        }
    }

    // pop stars from heap and push in vector
    vector<Star> closest;
    while (!max_heap.empty()) {
        closest.push_back(max_heap.top());
        max_heap.pop();
    }
    return closest;
}

class Star {
    public:
        // distance from Star to Earth: why?
        double distance() const
        {
            return sqrt(x_ * x_ + y_ * y_ + z_ * z_);
        }

        bool operator<(const Star &s) const
        {
            return distance() < s.distance();
        }

        int ID_;
        double x_, y_, z_;
};
