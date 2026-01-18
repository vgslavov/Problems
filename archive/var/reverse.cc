using namespace std;

// rotate: in-place
void rotate_array(vector<int> *A, int i)
{
    // A is ptr, so use ->
    int i %= A->size();

    // reverse whole array
    reverse(A->begin(), A->end());

    // reverse 1st i elements
    reverse(A->begin(), A->begin() + i);

    // reverse the rest
    reverse(A->begin() + i, A->end());
}

// string: in-place
string reverse_str(string instr)
{
    int end = instr.length() - 1;
    char tmp;

    for (int i = 0; i < instr.length(); i++) {
        tmp = instr[i];
        instr[i] = instr[end];
        instr[end] = tmp;
        --end;
    }
}

// string: in-place using pointers
void reverse_strp(char *instr)
{
    // empty string
    if (instr == NULL)
        return;

    // go to end of string
    char *end = instr;
    while (*end) {
        ++end;
    }
    // go back one (was pointing to NULL)
    --end;

    // swap end with beginning until ptrs cross
    char tmp;
    while (instr < end) {
        tmp = *instr;
        *instr++ = *end;
        *end-- = tmp;
    }
}

// sentence: in-place, 2 passes
void reverse_words(string *input)
{
    // 1st reverse whole string
    reverse(input->begin(), input->end());

    // then reverse each word:
    size_t start = 0, end;
    // search for the next space (starting after already processed words),
    // check if end of string (npos) reached
    while ((end = input->find(“ “, start)) != string::npos) {
        // one word only
        reverse(input->begin() + start, input->begin() + end);
        // skip space (TODO: assuming 1 space?)
        start = end + 1;
    }
    // reverse last word
    reverse(input->begin() + start, input->end());
}

// sentence: in-place, 1 pass
// TODO: very messy!

// int
// TEST: 0, -1, 1, 534
int reverse_int(int num)
{
    bool isneg = false;

    if (num < 0) {
        isneg = true;
        num = -num;
    }

    int rev = 0;
    while (num != 0) {
        rev = rev * 10 + num % 10;
        num /= 10;
    }

    if (isneg)
        rev = -rev;

    return rev;
}

// bits: XOR (O(n))
unsigned int swap_bits(unsigned int x, unsigned int i, unsigned int j)
{
    unsigned int ibit = ((x >> i) & 1);
    unsigned int jbit = ((x >> i) & 1);

    // XOR i-th and j-th bits
    // if (ibit ^ jbit)
    // or check if bits differ (signedness doesn’t matter: shifted bits ANDed with 0s)
    if (((x >> i) & 1) != ((x >> j) &1)) {
        // toggle i-th and j-th bits:
        // 1st set i-th and j-th bit, then XOR itself with that (XOR with 1 toggles a bit)
        x ^= ((1U << i) | (1U << j));
    }
    return x;
}

unsigned int reverse_bits(unsigned int num) {
    unsigned int n = sizeof(num) * 8;

    // swap half of the bits (LSB) with the other half (MSB)
    for (unsigned int i = 0; i < n/2; i++) {
        num = swap_bits(num, i, n-i-1);
    }
    return num;
}

// bits: divide & conquer (O(logn))

// list: recursive
// O(n) time, O(n) space (on function call stack)
// TODO: study
Node *reverse_list(Node *head)
{
    // base case
    if (!head || !head->next)
        return head;

    Node *new_head = reverse_list(head->next);
    // why?
    head->next->next = head;
    head->next = NULL;
    return new_head;
}

// list: recursive
// O(n) time, O(n) space (on function call stack)
// TODO: study
void reverse_list(Node *&p)
{
    if (!p)
        return;

    Node *rest = p->next;
    if (!rest)
        return;

    reverse(rest);
    p->next->next = p;
    p->next = NULL;
    p = rest;
}

// list: recursive
// O(n) time, O(n) space (on function call stack)
void reverse_list(Node *&head)
{
    // attn: no need to use & when calling!
    head = reverse_list_helper(head, NULL);
}

Node *reverse_list_helper(Node *head, Node *prev)
{
    Node *p;

    // base case
    if (head->next == NULL) {
        // conect last node to prev!
        head->next = prev;
        return head;
    } else {
        p = reverse_list(head->next, head);
        // reverse ptr!
        head->next = prev;
        return p;
    }
}

// list: iterative
// O(n) time, O(1) space
//void reverse_list(Node *&head)
void reverse_list(Node **head)
{
    Node *cur = *head;
    Node *pre = NULL;

    while (*head) {
        *head = (*head)->next;
        cur->next = pre;
        pre = cur;
        cur = cur->next;
    }
}
