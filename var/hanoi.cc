using namespace std;

// n: # of pegs
// TODO: study and understand
void hanoi(int n)
{
    vector<stack<int> > pegs(3);

    // init peg 0
    for (int i = n; i > 0; i--) {
        pegs[0].push(i);
    }

    // from 0 to 1 using 2
    transfer(n, pegs, 0, 1, 2);
}

void transfer(int n, vector<stack<int> > &pegs, int from, int to, int use)
{
    if (n > 0) {
        // from 0 to 2 using 1
        transfer(n-1, pegs, from, use, to);

        // move top of 0 to 1
        pegs[to].push(pegs[from].top());
        pegs[from].pop();

        cout << “Move from peg “ << from << “ to peg “ << to << endl;

        // from 2 to 1 using 0
        transfer(n-1, pegs, use, to, from);
    }
}

