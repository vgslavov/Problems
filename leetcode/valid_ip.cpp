#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

// number: 468
// section: meta
// difficulty: medium
// tags: string, meta

// constraints
// queryIP consists only of English letters, digits and the characters '.' and ':'.

const int VALID_IPV4_LEN = 4;
const int VALID_IPV6_LEN = 8;

bool tokenize(
    std::string str,
    const std::string& delimeter,
    std::vector<std::string>& tokens)
{
    if (str.empty()) {
        return false;
    }

    while (!str.empty()) {
        tokens.push_back(str.substr(0, str.find(delimeter)));
        str.erase(0, str.find(delimeter) + delimeter.length());
    }

    return true;
}

// complexity
// run-time: O(n)
// space: O(1)
std::string validIPv4(const std::vector<std::string>& tokens) {
    if (tokens.empty() || tokens.size() != VALID_IPV4_LEN) {
        return "Neither";
    }

    int num = 0;
    for (const auto& t : tokens) {
        try {
            num = std::stoi(t, nullptr, 10);
        } catch (std::invalid_argument const& ex) {
            std::cout << "invalid_argument: " << ex.what()
                        << std::endl;
            return "Neither";
        } catch (std::out_of_range const& ex) {
            std::cout << "out_of_range: " << ex.what()
                        << std::endl;
            return "Neither";
        }

        if (num < 0 || num > 255) {
            return "Neither";
        }

        // TODO: check if it starts with 0
    }

    return "IPv4";
}

// complexity
// run-time: O(n)
// space: O(1)
std::string validIPv6(const std::vector<std::string>& tokens)
{
    if (tokens.empty() || tokens.size() != VALID_IPV6_LEN) {
        return "Neither";
    }

    int num = 0;

    for (const auto& t : tokens) {
        try {
            num = std::stoi(t, nullptr, 16);
        } catch (std::invalid_argument const& ex) {
            std::cout << "invalid_argument: " << ex.what()
                      << std::endl;
            return "Neither";
        } catch (std::out_of_range const& ex) {
            std::cout << "out_of_range: " << ex.what()
                      << std::endl;
            return "Neither";
        }
    }

    return "IPv6";
}

// solution: Pythonic split + divide & conquer + try/except
// complexity
// run-time: O(n)
// space: O(1)
std::string validIPAddress(std::string queryIP)
{
    if (queryIP.empty()) {
        return "Neither";
    }

    std::vector<std::string> tokens;
    if (tokenize(queryIP, ".", tokens)) {
        return "Neither";
    }

    if (tokens.size() > 1) {
        return validIPv4(tokens);
    }

    if (tokenize(queryIP, ":", tokens)) {
        return "Neither";
    }

    if (tokens.size() > 1) {
        return validIPv6(tokens);
    }

    return "Neither";
}

// TODO: add unit tests
