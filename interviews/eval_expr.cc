// 2. parse & evaluate simple arithmetic expression [Google]
// example: “3/1*2+2*1”
// improve?
int compute(string s)
{
    stack<int> eval;
    char waitop = ‘’;
    char nowip = ‘’;
    int res = 0;

    int i = 0;
for (size_t i = 0; i != s.size(); ++i) {
        if (s[i] == ‘/’ || s[i] == ‘*’) {
            nowop = s[i];
} else if (s[i] == ‘+’ || s[i] == ‘-’) {
    if (waitop != ‘’) {
        if (eval.size() > 1) {
            int y = eval.top();
            eval.pop();
            int x = eval.top();
            eval.pop()
        switch(waitop) {
        case ‘+’:
            eval.push(x + y);
            waitop = ‘’;
            break;
        case ‘-’:
            eval.push(x - y);
            waitop = ‘’;
            break;
        }
    }
    } else {
                waitop = s[i];
            }
        } else {
            eval.push(stoi(s[i]));
            if (eval.size() > 1) {
                int y = eval.top();
                eval.pop();
                int x = eval.top();
                eval.pop();
                switch(nowop) {
                case ‘/’:
                    eval.push(x / y);
                    nowop = ‘’;
                    break;
                case ‘*’:
                    eval.push(x * y);
                    nowop = ‘’;
                    break;
                }
            }
        }
    }

    return res;
}
