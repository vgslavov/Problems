// Twitter pre-screening

#include <cctype>

int solution(const string &S) {
    long long k = 0;
    long n = S.size();
    
    if (n == 1)
        return 1;
    
    for (int i = 0; i < n; i++) {
        char ch = S[i];
        k = k ^ ch;
    }
    
    if (k == 0 || isalpha(k))
        return 1;
    else
        return 0;
}
