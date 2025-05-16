#include <algorithm>
#include <queue>
#include <vector>

// difficulty: easy
// section: sorting
// tags: citadel

// constraints
// sort semi-sorted data
// can't fit in memory

struct Data {
    int timestamp;
    char* buf;
    int size;
};

class DataReader {
public:
    bool get(Data* d);
};

class DataWriter {

public:
    bool put(const Data& d);
};

// solution: brute-force
// run-time: O(n*log n)
// space: O(n)
void sort1()
{
    DataReader reader;
    Data data;
    std::vector<Data> output;

    while (reader.get(&data)) {
        output.push_back(data);
    }

    std::sort(output.begin(), output.end());

    DataWriter writer;

    for (const auto& d: output) {
        writer.put(d);
    }
}

const int MAX_SIZE = 1000;

// solution: min priority queue
// run-time: O(log n)
// space: O(k)
void sort2()
{
    Data data;
    DataReader reader;
    DataWriter writer;
    std::priority_queue<Data, std::vector<Data>, std::greater<Data>> queue;
    int k = MAX_SIZE;

    while (reader.get(&data)) {
        if (queue.size() > k) {
            while (queue.size()) {
                if (data.timestamp < queue.top().timestamp) {
                    break;
                }
                writer.put(queue.top());
                queue.pop();
            }
        }

        queue.push(data);
    }
}

// solution: external sort
// run-time: O(n*log n)
// space: O(1)
// TODO
void sort3()
{
}
