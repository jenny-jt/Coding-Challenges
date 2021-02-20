List of Problems for Interview Prep

### Strings
1. Non-repeating Character
Given a string, return the first non-repeating char in a string
Example 1: “cabc” -> a
Example 2: “abc” -> a
Example 2: “bacab” -> c

* Constant time solution: using hash map/set and DLL


### Arrays 
2. Subset Sum
Given array of numbers, return a subset that adds up to target value
Example 1: [3,34,4,12,5,2], 9
{3, 34 , 4 , 12 , 5 , 2} sum=9 True 

* more optimized than brute force solution


### Graphs
3. For a really fun exercise think about the differences between cyclical and acyclical graphs.
Question: Thinking about google maps, what kind of graph are roads.
Answer: roads are cyclic graphs. otherwise they wouldnt be connected, and we wouldnt be able to 
travel successfully between pt A and pt B


### Trees
4. Define a tree structure - start with a tree with two nodes.
For an extra challenge, ask yourself how the implementation would
change if there are more than two branches per node. An example of this would be a Trie.
These are very useful for autocomplete and the like

5. Write a function that returns the lowest common ancestor of two nodes (the lowest node in T that has both n1 and n2 as descendants)

6. Write a function that returns the lowest common ancestor of a list of nodes (the lowest node in T that has both n1 and n2 as descendants)

7. Escape Room Keypads
You are attempting to solve a puzzle in an Escape room with your team where you need to
open a door to get to the next stage. There are several doors, each with a different keypad 
on it. The keypads each have 7 keys, containing 7 distinct letters.

Each kepad looks like this:

The instructions state that one of the keypads will open the correct door leading to the next
stage of the game. Your job is to find a word that unlocks the correct keypad. 

After struggling for some time, the Escape room leader gave you a clue, that the first letter
of the keypad is guaranteed to be in the word that opens the door. We will call this letter the
"key" letter. The goal of this exercise is to come up with as many words as possible that your
team can test out on the keypads and find the correct combination to go to the next stage of the
game. How many owrds from the input wordlist canyou make out of the letters in each keypad?

What you know:
The correct combination will be a valid english word
The words are at least 5 letters long, with no maximum length
The key letter will be in the correct answer
The words do not contain any letters outside the seven letters on the keypad
The letters may be reused, including the "key" letters

For our purposes, we will express each set of keypad letters as string of length 7, where the 
first letter

Constraints:
both wordlist and keypad letters will be in all capital letters
all words in wordlist are length 5 or greater
every sequence of keypad letters will consist of 7 distinct letters

Example 1
input: ['APPLE', 'PLEAS', 'PLEASE'] 
keypads: ['AELWXYZ', 'AELPXYZ', 'AELPSXY', 'SAELPRT', 'XAEBKSY'] 
expected output: [0, 1, 3, 2, 0]
