#include <map>
#include <stack>

int solution(const string &S) {
    map<char, char> matched;
    stack<char> pushed;
    
    matched[']'] = '[';
    matched[')'] = '(';
    matched['}'] = '{';
    
    for (int i = 0; i < (int)S.size(); i++) {
        // to avoid const char errors
        char ch = S[i];
        // as long as it's an opening bracket, keep pushing
        if (ch == '[' || ch == '(' || ch == '{') {
            pushed.push(ch);
        } else {
            // more chars in string but stack is empty (missing opening bracket(s))
            if (pushed.empty()) {
                return 0;
            // there is a matching opening bracket on top of stack
            // pop it!
            } else if (matched[ch] == pushed.top()) {
                pushed.pop();
            // there is no matching opening bracket on top of stack
            } else {
                return 0;   
            }
        }
    }
    if (pushed.empty())
        return 1;
    // there are left overs
    else {
        return 0;
    }
}
