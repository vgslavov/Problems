// 100%
// x^x = 0; 0^x = x
int solution(vector<int> &A) {
    int n = A.size();
    int xor_sum = 0;
    
    for (int i = 0; i < n; i++) {
        xor_sum = xor_sum ^ A[i] ^ (i+1);
    }
    return xor_sum ^ (n+1);
}