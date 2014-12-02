int solution(vector<int> &A) {
    // write your code in C++98
    long int npass = 0;
    long int nw = 0;
    long int ne = 0;
    
    for (int i = 0; i < (int)A.size(); i++) {
        // east
        if (A[i] == 0) {
            ++ne;
        // west
        } else if (A[i] == 1) {
            ++nw;
            // pass only when west is added after east
            // # of cars passing increases by $ne
            npass += ne;
            if (npass > 1000000000)
                return -1;
        // invalid
        } else
            return -1;
    }
    return npass;
}
