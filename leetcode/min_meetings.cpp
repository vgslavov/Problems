#include <algorithm>
#include <queue>
#include <vector>

// number: 253
// title: Meeting Rooms II
// url: https://leetcode.com/problems/meeting-rooms-ii/
// section: meta
// difficulty: medium
// tags: array, two pointers, greedy, sorting, heap, prefix sum, citadel

// constraints
// 1 <= intervals.length <= 10^4
// 0 <= starti < endi <= 10^6

// solution: min heap
// complexity
// run-time: O(n log n)
// space: O(n)
int minMeetingRooms(std::vector<std::vector<int>>& intervals)
{
    if (intervals.empty()) {
        return 0;
    }

    // sort by start time
    std::sort(intervals.begin(), intervals.end());

    // min heap for storing *end* times of concurrent meetings
    std::priority_queue<int, std::vector<int>, std::greater<int>> rooms;
    // add end time of 1st meeting
    rooms.push(intervals[0][1]);

    for (size_t i = 1; i != intervals.size(); ++i) {
        const auto& start_end = intervals[i];
        // next meeting starts after earliest ends
        if (rooms.top() <= start_end[0]) {
            rooms.pop();
        }

        // add meeting end time
        rooms.push(start_end[1]);
    }

    return rooms.size();
}

// TODO: add unit tests