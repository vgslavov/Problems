// using a stack
int eval(string s)
{
    stack<int> eval_stack;
    // convert to stringstream because of getline
    stringstream ss(s);
    string sym;
    int x, y;

    while (getline(ss, sym, ‘,’)) {
        // is it an operator?
        if (sym == ‘-’ || sym == ‘+’ || sym == ‘*’ || sym == ‘/’) {
if (!eval_stack.empty()) {
        y = eval_stack.top();
        eval_stack.pop();
        if (!eval_stack.empty()) {
            x = eval_stack.top();
            eval_stack.pop();
        }
    } else {
        throw length_error(“stack empty”);
    }
    switch (sym.front()) {
            case ‘-’:
                eval_stack.push(x - y);
                break;
            case ‘+’:
                eval_stack.push(x + y);
                break;
            case ‘*’:
                eval_stack.push(x * y);
                break;
            case ‘/’:
                eval_stack.push(x / y);
                break;
            }
        // or a number?
} else if (isdigit(sym[0])) {
            eval_stack.push(stoi(sym));
        } else {
            throw type_error(“invalid input”);
        }
    }
    return eval_stack.top();
}
