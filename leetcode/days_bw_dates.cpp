#include <cstdlib>
#include <iostream>
#include <map>

// number: 1360
// section: assessments
// difficulty: easy
// tags: math, string, meta, optiver

// constraints
// The given dates are valid dates between the years 1971 and 2100.

// solution: manual
// complexity
// run-time: O(n)?
// space: O(1)
const int START_YEAR = 1900;
const int START_MONTH = 1;
const int START_DAY = 1;
// TODO: make const
std::map<int,int> DAYS_PER_MONTH = {
    {1, 31},
    {2, 28},
    {3, 31},
    {4, 30},
    {5, 31},
    {6, 30},
    {7, 31},
    {8, 31},
    {9, 30},
    {10, 31},
    {11, 30},
    {12, 31}
};

bool isLeap(int year)
{
    // not a multiple of 4
    if (year % 4) {
        return false;
    }

    // multiple of 100 but not 400
    if (!(year % 100) && year % 400) {
        return false;
    }

    // a leap year!
    return true;
}

int str2int(std::string& date)
{
    static std::string delimiter("-");
    int token = std::stoi(date.substr(0, date.find(delimiter)));
    date.erase(0, date.find(delimiter) + delimiter.length());

    return token;
}

int daysSinceStart(std::string date)
{
    int totalDays = 0;
    int year = str2int(date);
    int month = str2int(date);
    int day = str2int(date);

    //std::cout << "year:" << year
    //          << ", month:" << month
    //          << ", day:" << day
    //          << std::endl;

    // years: not inclusive
    for (int i = START_YEAR; i != year; ++i) {
        if (isLeap(i)) {
            totalDays += 366;
        } else {
            totalDays += 365;
        }
    }

    //std::cout << "totalDays:" << totalDays << std::endl;

    // months: not inclusive
    for (int i = 1; i != month; ++i) {
        if (i == 2 && isLeap(year)) {
            totalDays += 1;
        }

        totalDays += DAYS_PER_MONTH[i];
    }

    //std::cout << "totalDays:" << totalDays << std::endl;

    // days
    totalDays += day;

    //std::cout << "totalDays:" << totalDays << std::endl;

    return totalDays;
}

int daysBetweenDates(const std::string& date1, const std::string& date2)
{
    return std::abs(daysSinceStart(date1)-daysSinceStart(date2));
}

// TODO: add unit tests
