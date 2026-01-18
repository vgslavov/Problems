// b7,b6,b5,b4,b3,b2,b1,b0
// MSB                  LSB(righ-most)

x ^ x = 0
0 ^ x = x
2^16: 1 << 16, 1 * 2^16
2^p: 1 << p, 1 * 2^p
x >> 16: x / 2^16, x’s 16 MSBs

// two’s complement
// flip each bit and add 1
~x + 1

// XOR: swap vars
a = a ^ b
b = a ^ b
a = a ^ b

// odd or even: test 1st bit
// odd numbers have least significant (right-most) bit equal to 1 (e.g. number 1)
// AND erases all high-order bits and leaves bit b0 the same
if ((x & 1) == 0)
    cout << “even”
else
    cout << “odd”

// test n-th bit
// shift n bits to left in 1, then eliminate/erase all bits other than n-th bit
// non-zero value means bit was set in x
if (x & (1 << n))
    cout << n << “-th bit is set”
else
    cout << n << “-th bit is not set”

// set n-th bit
// shift n bits to left in 1, then preserve all bits except for n-th bit
// OR any value (0 or 1) with 1 equals 1
y = x | (1 << n)

// unset n-th bit
// turn on all bits except n-th, then eliminate n-th bit
y = x & ~(1 << n)

// toggle n-th bit
// XOR any value with 1 (n-th bit) flips it
y = x ^ (1 << n)

// turn off right-most bit
y = x & (x - 1)

// extract lowest set bit (all others are cleared)
y = x & ~(x - 1)
