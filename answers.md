# CMPS 2200 Assignment 3
## Answers

**Name:**___Maria Chen______________________


Place all written answers from `assignment-03.md` here for easier grading.






- **b.**
- Suppose n is the length of the input string. In the iterative method, each judgment depends on the previous x, so there is no way to parallelize. Recursive n layers, the running time of each layer is O(1), so the time complexity of work is O(n), and the time complexity of span is also O(n)
  work:O(n)
  span:O(n)




- **d.**
- Suppose n is the length of the input string. The title assumes that all paren_map operations are parallel, so the overhead of the first for loop is O(1). For the scan function, in an efficient implementation, W(n) = W( n/2) + n, so W(n)∈O(n), S(n) = S(n/2) + O(1), so S(n)∈O(lgn).
Work: O(n)
Span: O(log2(n))





- **f.**
Suppose n is the length of the input string. At each recursion, two recursive subtasks are generated, so the overall time complexity is T(n) = 2*T(n/2) + c, and the height of the tree is O(log2(n)). So the time complexity of work is O(n), and the time complexity of span is O(log2(n))
work: O(n)
span: O(log2(n))
