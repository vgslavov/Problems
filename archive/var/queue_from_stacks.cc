class Queue {
    public:
        // enqueueing always pushes to 1st stack
        void enqueue(int val) {
            A_.push(val);
        }

        int dequeue() {
            int val;
            // B is empty, first move everything from A
            if (B_.empty()) {
                while (!A_.empty()) {
                    val = A_.top();
                    B_.push(val);
            }

            // top of B is the head of the queue
            if (!B_.empty()) {
                val = B_.top();
                B_.pop();
            } else {
                throw length_error(“empty queue”);
            }
        }

    private:
        stack<int> A_, B_;
};
