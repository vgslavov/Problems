% given a binary tree and an integer corresponding to a level in the tree, print the contents of the nodes in that level of the tree from left to right

% Find intersection of two arrays and how to handle duplicates

% Design the classes required to represent a deck of cards and write functions to shuffle and deal cards

const int SUITS = 4; //This is the number of different suits (should be 4)
const int VALUES = 13; //This is the number of individual values that a card can have (should be 13)
const int RANDOM_SWITCHES = 25; //This is the number of times that a pair of cards is switched in the shuffle function.
enum cardSuit {SPADE, CLUB, HEART, DIAMOND};
struct card{
        cardSuit suit;
        int value;
}

#include "stdafx.h" //needed for the Windows display
#include "globals.h" //include the global constants we set
#include <cstdlib> //the standard c library
#include <time.h> //used when seeding the rand() function
#include <string>

using namespace std;
#include "card.h" //include our card structure.

//Declare any global variables (the multi-dimensional array of cards) here.
card myCardArray[SUITS][VALUES];

//Our prototypes for the functions.
void initDeck();
void getCard(char cardString[], int row, int column);
void shuffleCards();
bool compareCards(char cardString[], int row, int column);

void initDeck()
{
    //For each of the card structs in your multidimensional array,
    //You need to set it's suit and value. Initially you should organize the cards
    //by having each suit on its own row, and have the cards in order by value on each row.
    for(int i = 0; i < VALUES; i++){
        myCardArray[0][i].suit = SPADE;
        myCardArray[0][i].value = i+1;
        myCardArray[1][i].suit = CLUB;
        myCardArray[1][i].value = i+1;
        myCardArray[2][i].suit = HEART;
        myCardArray[2][i].value = i+1;
        myCardArray[3][i].suit = DIAMOND;
        myCardArray[3][i].value = i+1;
    }

    //You do not need to modify the below call. It will seed your rand() function used in the shuffleCards function with the current time.
    srand((unsigned int)time(NULL));
}

void getCard(char cardString[], int row, int column)
{

    if(myCardArray[row][column].suit == SPADE){
        cardString[0]= 'S';
    }
    else if(myCardArray[row][column].suit == CLUB){
        cardString[0]= 'C';
    }
    else if(myCardArray[row][column].suit == HEART){
        cardString[0] = 'H';
    }
    else {
        cardString[0] = 'D';
    }

    if(myCardArray[row][column].value == 1)
        cardString[1] ='A';
    else if(myCardArray[row][column].value == 2)
        cardString[1] = '2';
    else if(myCardArray[row][column].value == 3)
        cardString[1] = '3';
    else if(myCardArray[row][column].value == 4)
        cardString[1] = '4';
    else if(myCardArray[row][column].value == 5)
        cardString[1] = '5';
    else if(myCardArray[row][column].value == 6)
        cardString[1] = '6';
    else if(myCardArray[row][column].value == 7)
        cardString[1] = '7';
    else if(myCardArray[row][column].value == 8)
        cardString[1] = '8';
    else if(myCardArray[row][column].value == 9)
        cardString[1] = '9';
    else if(myCardArray[row][column].value == 10)
        cardString[1] = 'T';
    else if(myCardArray[row][column].value == 11)
        cardString[1] ='J';
    else if(myCardArray[row][column].value == 12)
        cardString[1] = 'Q';
    else if(myCardArray[row][column].value == 13)
        cardString[1] = 'K';

    cardString[2] = '\0';

    //Look at the card located at the passed in row and column and generate
    //a 2 character long character array in cardString[] that represents the card.
    //If you return a valid character array, you will see the card on the screen,
    //if not you will see the back of a card.
}

bool compareCards(char cardString[], int row, int column)
{
    //compare the card located at the passed in row and column to the
    //card represented in cardString[]. If they are the same, return true.
    //HINT: Look up the strcmp() function.
    int result;
    char myCard[20];
    getCard(myCard, row, column);
    result = strcmp(cardString,myCard);
    if(result == 0){
        return true;
    }
    else{
        return false;
    }

}

void shuffleCards()
{
    //pick 2 cards at random and swap their locations. Do this RANDOM_SWITCHES number
    //of times.

    for(int i = 0; i < RANDOM_SWITCHES; i++){
        swap(myCardArray[rand()%4][rand()%13], myCardArray[rand()%4][rand()%13]);
    }

}

% Given an array of integers write a function to return the product of the value of the largest integer and its frequency

public class Problem1 {

    public static void main(String a[])
    {
        new Problem1().maxInteger();

    }
    void maxInteger()
    {
        int []a = {3,5,1,2};
        int i,freq=1,max=0;
        int min=9999,max_diff=0;
        for(i=0;i<a.length;i++)
        {
            if(max<a[i])
            { freq=0;
                max=a[i];
            }
            if(max==a[i])
            freq++;
        }

        System.out.println(max*freq + " is the result");
}

% To find and return the common node of two linked lists merged into a 'Y' shape.

1. add each element's address (of the smallest list)and push it to the hash table.
2. start walking second list.
3. get element compar eits address with hash table if match is found in hash table, return
4. if list is not exhausted, go to step 2.
5. return NULL

Hashtable is complete overkill. The point is to realize that the two linked lists have the same tail. That means if you traverse them with the same index but from the right you will eventually find the first similar node. It's almost as easy if the problem said the two linked lists had the same prefix, find the first node on which they split. Here you walk them with the same index from the left.

% To return the 'm' smallest numbers from a file of 'n' numbers

I will create a min heap with the given numbers and extract 'm' minimums from the heap which will get stored into the resultant array

O((M+N)log N)?

it's O(n+m*log n), since you can construct the min heap bottom-up and that only takes O(n)?

Why don't we just sort the array and return the first m numbers? Takes O(nlogn) for sorting and O(m) to return the first m numbers.

% How does malloc work in C? How does deadlock prevention work in operating systems?

% Design classes for Kindle Fire 'shelves'

% How do you find if two values in an array sum to a given value? Make it as efficient as possible.

assume two arrays to be A and B of sizes m and n respectively.
assume the given sum as S;

step 1: sort array B using Quick sort /*Worst case complexity is O(nlogn)*/
step 2: for (i=0 ; i<A.length; i++) /*loop runs for n times in the worst case*/
             {
                  v=S-A[i];
                  if(Binary_Search(B, v)) // Binary search time complexity at runtime is O(logm)
                      return true;
             }
             return false;

SO the worst case complexity is O(nlogn + O(mlogn));

public void findValues(int[] a, int k)
HashMap<Integer, Integer> map = new HashMap<Integer,Integer>();

for (i=0; i < a.size(); i++) {
    map.put(a[i], a[i]);
}

for (i=0; i < a.size(); i++) {
    if (map.get(k-a[i]) != null ) {
          System.out.println(a[i] + " " + k - a[i]);
    }
}

% Write a program that reverses the words in a sentence.

I used a stack, pushing words onto it as I reached spaces.

public static String reverseSentence(String a){
    StringBuilder result = new StringBuilder();
    Stack<String> stack = new Stack<String>();
    String[] temp;
    temp = a.split(" ");
    for (String s : temp){
        stack.push(s);
    }
    while(!stack.empty()){
        result.append(stack.pop() + " ");
    }
    return result.toString();
    }

<?php
        // O(n) times
    function reverse1($word)
    {
        $result = "";
        for ($index = strlen($word)-1; $index>=0; $index--)
        {
            $result[strlen($word)-1 - $index] = $word[$index];
        }
        return implode("", $result);
    }
    // O(n/2) times = O(n) times
    function reverse2($word)
    {
        $temp = "";
        if(strlen($word)%2 == 1)
            $stop = strlen($word)/2;
        else
            $stop = strlen($word)/2-1;
        for ($index = 0; $index<=$stop; $index++)
        {
            $temp = $word[$index];
            $word[$index] = $word[strlen($word)-1 - $index];
            $word[strlen($word)-1 - $index] = $temp;
        }
        return $word;
    }
?>

% Write a program that sees if two binary trees are equal.

I utilized a depth-first traversal method, comparing the data within each node and recursively checking the left, then right child.

How if we use in-order traversal? If my understanding is correct, two binary trees are equal if they contain the same elements (although at different positions in the tree)

% What is the difference between an array and a linked list? When might you use either data structure?

% What is the difference between an array and a linked list? When might you use either data structure?

% Design a parking lot

% Describe data structures (Trees, Linked Lists, Sets)

% Given two nodes that are in a binary search tree (this is guaranteed) find the shortest traversal path between them

I found the path to each node from the root, and stored that path in an array. The shortest path would then be the path from the end of one array (which contains a one of the nodes), up to the 'pivot point' of the array, and then from the 'pivot point' of the next array, to the node. You merge the two arrays at the 'pivot point' and the result is the shortest path.

That was my solution. it works, but I didn't have time to look into any special cases, debugging, optimization, etc. I'm sure there is a much simpler/efficient way.

Dijkstra's Algorithm came to mind, but I couldn't remember it in detail off of the top of my head at that moment.

"The shortest path would be from a node to the common ancestor (of the two nodes) to the other node -- right?"

Yes, that's correct.

% Return the index of the first repeated character of a string.

This one was easy. Walk through string array with for loop, add each char to a java Set data structure. the add() method in a Java set returns false if the object is already in the set. When 'false' happens, break out of loop and return the current index. return -1 otherwise.

I'm not sure if there is a way to do this without using a temporary data structure, but this is O(n) in worst case time complexity, so it's pretty good.

public static void main(String[] args) {
        // Return the index of the first repeated character of a string.

        String s = "abdcbm";

        boolean[] map = new boolean[28];
        for (int i = 0; i < s.length(); i++) {
            if (!map[s.charAt(i) - 'a']) {
                map[s.charAt(i) - 'a'] = true;
            } else {
                System.out.println(i);
                break;
            }
        }

    }

% Find out if the array has repeated numbers in it. (make it more time efficient)

Create a hash map for the array which maps every number to its frequency. If there exists an element with frequency > 1 => there is repetition!

map<int,int>frequency; // map

% Reverse a singly linked list

Traverse the list once to find a pointer to the tail node. Traverse the list again and insert the current node directly after the tail node you originally found. Stop when you reach the tail node. Then, set the tail to the head.

Use a stack. add each node to the stack. once you reach the tail, pop the stack and assign tail->next to the popped node. do it until stack is empty

% in an array of characters find the character that is repeated the most

Correct me if I'm wrong, but is priority queue really the best way? I think efficiency ends up being O(nlogn) for PQ...inserting n elements into the queue (insert is O(logn)) then peeking. Using a hash table, it takes O(n) to insert the n elements and O(n) to find the max, resulting in O(n) efficiency.

Okay actually building a heap is O(n) not O(nlogn). So both techniques take O(n). Priority queue might be a little better since it only requires one scan and peek is O(1), whereas the hash table method requires two scans through the array.

% Print the BST in level order

Basic idea: perform a breadth first traversal of the tree. Every time you dequeue a node, print it. This will give a level order print in linear time.

% Write a function to serialize a binary tree

I just stored the tree in an array with the index corresponding to its position in the tree.

% Write the code to reverse a string

void reverseString(char *str)
{
   int i=0;
   int j=strlen(str)-1;
   char temp;

   while(i<=j)
   {
       temp = str[i];
       str[i] = str[j];
       str[j] = temp;
       i++;
       j--;
   }
}

This is an O(n) operation.. linear time.
just exchange first and last terms and keep moving to the middle.

% Find the maximum subset sum in an array of numbers. Discuss complexity. 
http://en.wikipedia.org/wiki/Maximum_subarray_problem

% Find the max ;length palindrome in an input string.
http://stevekrenzel.com/articles/longest-palnidrome

Here's a code with O(n2) complexity

#include<stdio.h>
#include<conio.h>
#include<string.h>

void ispal(char*,int,int*);

void longpal(char *str)
{
   int longest[2]={0};
   int i=0;

   for(;i<strlen(str)-1;i++)
      ispal(str,i,longest);

   printf("\nLongest Palindrome: ");
   for(i=longest[0];i<=longest[1];i++)
    printf("%c",str[i]);
}

void ispal(char *str, int i, int *longest)
{
  int j=i;
  while(i>=0&&j<=strlen(str)-1)
  {
     if(str[i]==str[j])
     {
    if((j-i)>(longest[1]-longest[0]))
    {
       longest[0]=i;
       longest[1]=j;
    }
     }
     i--;
     j++;
  }
}

void main()
{
   char *str;
   scanf("%s",str);
   longpal(str);
   getch();
}

% Write a function to get the most repeated word in a string.

I started droning about tokenizing words and storing them in an array and then switched to a hash table when all it really needed was to sort all the words using strcmp and maintain a count for each word and return the word with the maximum count.

% Given the head pointers to two linked lists of unknown length, find the node of intersection if they do intersect.

% Write a program to find the square root of a double.

use binary search to narrow down the search space and keep multiplying the answer in each iteration by itself to check if it is equal to the double given. If it is lesser, move up the lower bound, else move down the upper bound.

http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method

% Write a function that takes in an array and repeats an integer that appears the most.

you can go through the array adding all the key-value pairs (number and times) to a hashmap and then access the hashmap in constant time. O(n).

% Compare and Book and a Three Ring Binder using data structures and classes

A book is like an array. You can very easily look up based on index (page number), however it is hard to insert (you'd have to cut out pages, put one in, and put pages back in). A binder has a more difficult lookup, but insertions are easy (like an unsorted list)

% Design and implement an algorithm to determine if a binary tree is symmetric.

% Test whether a binary tree is symmetrical in both data and shape

% Given an array of integers, all but one of which appears an even number of times, find the one integer which appears an odd number of times. Upon completion, asked to improve the algorithm in terms of both time and space, eventually asked to do it in O(n) time and constant space.

xor the entire array, all the integers which appear an even number of times will cancel eachother out

int[] theArray = new int[]{1, 1, 2, 2, 3, 3, 3, 4, 4, 10, 10, 10, 10, 10, 11, 11, 12, 12};
        Map<Integer, Integer> theMap = new HashMap<Integer, Integer>();

        for (int i = 0; i < theArray.length; i++) {
            if(theMap.containsKey(theArray[i])) {
                theMap.put(theArray[i], theMap.get(theArray[i]) + 1);
            } else {
                theMap.put(theArray[i], 1);
            }
        }

        Set<Integer> mapKeys = theMap.keySet();
        for(int keyInt : mapKeys) {
            if(theMap.get(keyInt) % 2 != 0) {
                System.out.println(keyInt + " occurs odd number of times");
            }
        }
    }

% difference between an abstract class and interface

% find the intersection of two arrays	

% find the first unrepeated character in a string

We can use a LinkedHashMap which preserves the order of insertion. After one full scan and storing the counts (if need be), the first item in the hash map with frequency 1 will be the first unrepeated character

% Given an integer array, one element occurs odd number of times and all others have even occurrences. Find the element with odd occurrences.

(The answer they want): Build a hash table that maps to each element. Each has entry holds a boolean. It turns to true if it got accessed odd times. O(n)
You might be asked about collision resolution which you can talk about chaining and open addressing.

(other answer): sort O(nlogn) iterate through the list find the number O(n). overall O(nlogn)

% find duplicate in a circular linked list 

% Given N petrol pumps in a circular road, distance b/w adjacent petrol pumps and amount of petrol with vehicle capacity . Find a petrol pump where we should start so that we can cover entire road Expected Complexity O(n)

% Given a linked list , swap alternate nodes of linked list . For eq: 1 2 3 4 will become 2 1 4 3 and 1 2 3 4 5 6 will become 2 1 4 3 6 5 

I made a function to swap two nodes of link list and applied it to first two nodes , then next two nodes and so on recursively .

% If you get an array of integers, find the only integer that is repeated for an odd number of times.

Hashmaps

XOR all the numbers

% Describe how hashtables work, and traversals for trees both recursive and non recursive

% Linear sorting (radix sort, counting sort)

% Given thousand lists, find the longest common sublist

% How would you traverse through a binary search tree and print out each element in order?

Use a queue and store all the current node's children in the queue. Loop until the queue is empty.

No, the interviewer did not mean inorder traversal. You have to print the elements in order as in the root first then its left element and then its right element, then the left elements right element, ect. I thought recursion would work at first too, but it doesn't because you will need to recurse all the way through either the left or right node and that's not correct. You basically have to go to the left then the right and then the left again to get its children. This can't be done using a stack either because you would get the wrong order. This problem is similar to BFS (breadth first search) - its pretty much that exact problem and that's why a queue is used.

% Find the numbers in an array that appear an odd number of times.

I used a hashtable and stored all the values into it with a key and value, value being the number of times it appears. Then I looped through the hashtable checked if mod(value) == 1 or 0. If 1 (odd) then save the key it into an array

If you are given that there's only one element duplicated an odd number of times, you can simply XOR all the elements together. The resulting value is the element that was repeated an odd # of times.

This works because A XOR A = 0.

There could be several values that are have an odd number of duplicates. Using XOR wouldn't work because you would get a weird XOR combination of all the odd number of duplicates. Nice thinking though; your approach was very interesting and outside the box

Make a hashmap.

Iterate through the array.
If the element is in the hashmap, remove it.
If it's not in the hashmap, add it.

Now the only elements in the hashmap are ones that appeared an odd number of times.

% Design a stack with min(stack) operation in constant time

The idea is to have a "current minimum" variable that you update on push. The trick is to save this current minimum with the node on push, so that once you pop you get the old "current minimum".

Using temporary variable is OKAY.
But if pop operation is performed on curr minimum,it would be O(n) to update the new minimum

% Print common elements between two arrays

% Write the code for the preorder traversal of a tree.

% Write a program to sort two arrays and merge them

Approach similar to merge sort

% You got some baby bottle samples. You would like to know the max height you can drop it without breaking the bottle. Let set the unit as 1 foot. And the highest height you can reach is at N feet. So how would you find the (max) safe height?

It's a binary search problem. Find n/2. Try it. If broken, repeat same process for 1~(n/2-1). The time complexity is O(log n). Then explain my pseudo codes.

% You got only ONE baby bottle sample. You would like to know the max height you can drop it without breaking the bottle. Let set the unit as 1 foot. And the highest height you can reach is at N feet. So how would you find the (max) safe height?

Do a linear search. Time complexity is O(N). Only need ONE bottle.

Drop the bottle start from down i.,e from 1 foot and traverse upwards in increments of 1 until height reaches N. (LInear search) .

% (following the previous one) You got only TWO baby bottle sample. You would like to know the max height you can drop it without breaking the bottle. Let set the unit as 1 foot. And the highest height you can reach is at N feet. So how would you find the (max) safe height? (This is the one I think is kind of brain-teaser one.)

% Given two int arrays, write a function which returns their intersection as an int array; analyze the time/space complexity of your function.

% Write code to do a k-way merge of sorted lists

% Given a 5x5 board containing random characters, find all words that can be formed from consecutive adjacent (diagonals count) characters.

% Given a list of n elements...every element has a duplicate except one...Find that lone number?

I think the best method is to create a hash table with all entries.. this is an O(n) operation.
hash_map <int,int>.. i.e key and frequency of occurrence...

so creating the map is O(n) and then searching for the element with frequency=1 is again O(n). Thus summing up to O(2n) which is nothing but O(n) time complexity.

Create a temporary variable k = 0. Loop through the array bitwise XORing array elements with k. Since XOR is commutative and associative, the total will be the single element XORed with all the other elements each XORed with its duplicate. All the duplicates cancel to zero, and the XOR of the single element with 0 is the single element. So return k. This is also O(n), but does not require the memory used by a hash table.

#include<stdio.h>
#include<conio.h>

void main()
{
 int list[7]={1,2,3,4,1,3,2};
 int k=0,i;

 for(i=0;i<7;i++)
 {
   k=k^list[i];
 }
 printf("No duplicate: %d",k);
 getch();
}

% The input to a function is an array of n elements.Output of that function is also an array where each element is product of all elements in the input array except the one with same index. Input ::::: 1 2 3 4 Output ::::: 2*3*4 1*3*4 1*2*4 1*2*3

Either run two loops nested and carry out operations ==> O(n^2)

or multiply every element at first, which is O(n) and then divide each element by the product to find individual answers ==> O(n)

Total time complexity => O(2n) ==> O(n)

Create the Output array such that the value in every position 'i' is n! / i. The time complexity will be O(n)

% How would you all values from the nodes of a given binary tree into a string and then deserialize the string and put it back in the binary tree?

% Given a list of strings how would you find the prefix of each string? What is the complexity? How will you sort the string?

% Consider a simple array. What is the time complexity to insert, search, delete an element?

 it's constant time to look up an element at an index. Insert and delete are dependent on implementation, most languages require you to re-size or make a new array, so it's n/a for the most part. And search (if you mean find an element with value x) is O(n) (at worst).

% Design a Parking Garage using Object oriented concepts

% In linux, a folder consists of 10000 files and some files contain US phone numbers. What would you do to display the names of files containing US phone numbers?

find . -type f -print | xargs grep -l "[0-9]\{3\}-[0-9]\{3\}-[0-9]\{4\}"

% How the browser acquires IP address of the website that you entered in the address bar? Explain in details. Then after that how does the browser process the IP address to get the contents of the URL?

DNS to get the IP address (DNS will most likely do a recursive lookup for your address, or intermediate cache might fetch you the ip if it was common something like google)

Once the DNS fetched IP, opens an HTTP connection with the IP which will fetch the required pages. Most likely it will be using persistent fetching to get pages within a single TCP connection. Also, it will have to open another HTTP connection if some are provided by external content providers like Akamai.

% Given an array of numbers where each number has a duplicate except one, write a program to return the lone number.

Solution 1
Use a bit map for all possible numbers.
Initialize it with all 0.
traverse the array and XOR the corresponding bit for each number.
in the final bit map, the bit with 1 corresponds to the lone number. O(n)
 Solution 2
Sort the array, then traverse it. O(n log n), but less memory.

u can just XOR all the numbers..the result is the lone number

% Find if a linked list has a cycle in it.

You can define two pointers, slow and fast. Make both of them start from the head. Advance the fast two items at a time and the slow one item at a time. If the link list is acyclic, the fast pointer will reach a NULL. If the link-list is cyclic, you will get to a point where either "fast = slow" or "fast->next = slow". This algorithm is O(n).