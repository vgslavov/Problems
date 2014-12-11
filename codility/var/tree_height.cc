// 100%
#include <algorithm>
int solution(tree * T) {
    // we are done!
    if (T->l == NULL && T->r == NULL)
        return 0;
    // right-skewed tree
    else if (T->l == NULL)
        return 1 + solution(T->r);
    // left-skewed tree
    else if (T->r == NULL)
        return 1 + solution(T->l);
    else
        return 1 + max(solution(T->l), solution(T->r));
}

// 44%
#include <algorithm>
int solution(tree * T) {
    if (T->l == NULL || T->r == NULL) return 0;
    
    return 1 + max(solution(T->l), solution(T->r));
}
