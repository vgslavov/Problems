#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

// number: 468
// title: Validate IP Address
// url: https://leetcode.com/problems/validate-ip-address/
// section: meta
// difficulty: medium
// tags: string, meta

// constraints
// queryIP consists only of English letters, digits and the characters '.' and ':'.

const int VALID_IPV4_LEN = 4;
const int VALID_IPV6_LEN = 8;

// complexity
// run-time: O(n)
// space: O(1)
bool tokenize(
    std::string str,
    const std::string& delimeter,
    std::vector<std::string>& tokens)
{
    if (str.empty()) {
        return false;
    }

    int pos = str.find(delimeter);

    while (pos != std::string::npos) {
        //std::cout << "str:" << str << std::endl;

        tokens.push_back(str.substr(0, pos));
        // delete from start to pos including delimeter
        str.erase(0, pos + delimeter.length());
        pos = str.find(delimeter);
    }

    if (tokens.empty()) {
        return false;
    }

    // always push: will catch ending delimeter
    tokens.push_back(str);

    return true;
}

// complexity
// run-time: O(n)
// space: O(1)
std::string validIPv4(const std::vector<std::string>& tokens)
{
    if (tokens.empty() || tokens.size() != VALID_IPV4_LEN) {
        std::cerr << "not enough tokens: " << tokens.size() << std::endl;
        return "Neither";
    }

    int num = 0;
    for (const auto& t : tokens) {
        //std::cout << "token:" << t << std::endl;

        // or strncmp/strlcmp, but not t[0]
        if (t.size() > 1 && t.substr(0, 1) == "0") {
            return "Neither";
        }

        size_t pos;

        try {
            num = std::stoi(t, &pos, 10);
            if (pos < t.size()) {
                std::cerr << "invalid chars in t:" << t
                            << " at pos:" << pos
                            << std::endl;
                return "Neither";
            }
        } catch (std::invalid_argument const& ex) {
            std::cerr << "invalid_argument: " << ex.what()
                        << std::endl;
            return "Neither";
        } catch (std::out_of_range const& ex) {
            std::cerr << "out_of_range: " << ex.what()
                        << std::endl;
            return "Neither";
        }

        if (num < 0 || num > 255) {
            return "Neither";
        }
    }

    return "IPv4";
}

// complexity
// run-time: O(n)
// space: O(1)
std::string validIPv6(const std::vector<std::string>& tokens)
{
    if (tokens.empty() || tokens.size() != VALID_IPV6_LEN) {
        std::cerr << "not enough tokens: " << tokens.size() << std::endl;
        return "Neither";
    }

    for (const auto& t : tokens) {
        //std::cout << "token:" << t << std::endl;

        // 4-digit hex
        if (t.size() > 4) {
            return "Neither";
        }

        size_t pos;

        try {
            int num = std::stoi(t, &pos, 16);
            if (pos < t.size()) {
                std::cerr << "invalid chars in t:" << t
                            << " at pos:" << pos
                            << std::endl;
                return "Neither";
            }
        } catch (std::invalid_argument const& ex) {
            std::cerr << "invalid_argument: " << ex.what() 
                        << std::endl;
            return "Neither";
        } catch (std::out_of_range const &ex) {
            std::cerr << "out_of_range: " << ex.what()
                        << std::endl;
            return "Neither";
        }
    }
    return "IPv6";
}

// solution: substr/find/erase + divide & conquer + try/except
// complexity
// run-time: O(n)
// space: O(1)
std::string validIPAddress(const std::string& queryIP)
{
    if (queryIP.empty()) {
        return "Neither";
    }

    std::vector<std::string> tokens;
    tokenize(queryIP, ".", tokens);

    if (tokens.size() > 1) {
        return validIPv4(tokens);
    }

    tokenize(queryIP, ":", tokens);

    if (tokens.size() > 1) {
        return validIPv6(tokens);
    }

    return "Neither";
}

// TODO: add unit tests
