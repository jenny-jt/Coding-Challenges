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
