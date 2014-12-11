// 100%
int solution(const string &S) {
    long long open_count = 0;
    
    for (int i = 0; i < (int)S.size(); i++) {
        char ch = S[i];
        
        if (ch == '(')
            ++open_count;
        else {
            // no more opening p.
            if (open_count == 0)
                return 0;
            else
                --open_count;
        }
    }
    if (open_count > 0)
        return 0;
    else
        return 1;
}
