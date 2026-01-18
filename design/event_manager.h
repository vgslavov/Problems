#include <string>
#include <unordered_map>
#include <vector>

class EventManager {
public:
    EventManager()
    {
        d_prefixSums.push_back(0);
    }

    ~EventManager() = default;

    void addEvent(const std::string& id, double weight)
    {
        d_prefixSums.push_back(d_prefixSums.back()+weight);
        d_idToSeq[id] = ++d_lastIndex;
    }

    double averageWeight(size_t k)
    {
        if (k == 0) return 0.0;

        size_t numEvents = d_prefixSums.size()-1;
        if (numEvents == 0) return 0.0;

        size_t eventsToAverage = std::min(k, numEvents);
        size_t startIndex = d_prefixSums.size() - eventsToAverage - 1;

        return (d_prefixSums.back()-d_prefixSums[startIndex])/eventsToAverage;
    }

private:
    // example:
    // index:  0, 1, 2, 3, 4
    // weight: 0, 5, 2, 3, 2
    // sum:    0, 5, 7,10,12
    std::vector<double> d_prefixSums;
    size_t d_lastIndex = 0;

    // key: event id, value: sequence number
    std::unordered_map<std::string, size_t> d_idToSeq;
};