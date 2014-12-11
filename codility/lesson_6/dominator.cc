// 100%
int solution(const vector<int> &A) {
    int n = A.size();
    int candidate = -1;
    int leader_index = -1;
    int candidate_count = 0;
    int candidate_value = 0;
    int candidate_index = -1;

    for (int i = 0; i < n; i++) {
        if (candidate_count == 0) {
            ++candidate_count;
            candidate_value = A[i];
        } else {
            if (candidate_value != A[i])
                --candidate_count;
            else
                ++candidate_count;
        }
    }
    
    // defaults to -1
    if (candidate_count > 0)
        candidate = candidate_value;
    
    candidate_count = 0;
    for (int i = 0; i < n; i++) {
        if (A[i] == candidate) {
            ++candidate_count;
            candidate_index = i;
        }
    }
    
    // defaults to -1
    if (candidate_count > n/2)
        leader_index = candidate_index;
    
    return leader_index;
}