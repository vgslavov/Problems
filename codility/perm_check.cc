// 100%
int solution(vector<int> &A) {
    vector<long long> C(A.size(), 0);
    
    for (int i = 0; i < (int)A.size(); i++) {
        if (A[i] > A.size() || A[i] < 1)
            return 0;
        else {
            // perm seq is 1 to N!
            if (C[A[i]-1] != 0)
                return 0;
            else
                C[A[i]-1] += 1;
        }
    }
    return 1;
}

// 77%
//#include <iostream>
int solution(vector<int> &A) {
    // write your code in C++98
    vector<long long> C(A.size(), 0);
    
    for (int i = 0; i < (int)A.size(); i++) {
        // perm seq is 1 to N!
        if (A[i] > 0)
            C[A[i]-1] += 1;
        //else
        //    cout << "skipping " << A[i] << endl;
    }
    
    for (int i = 0; i < (int)C.size(); i++) {
        //cout << C[i] << endl;
        if (C[i] != 1)
            return 0;
    }
    return 1;
}
