# Round A1 for Google Code Jam 2017
This code was done as a practice, and not during a competition.

## Problem A. Alphabet Cake
You are catering a party for some children, and you are serving them a cake in the shape of a grid with R rows and C columns. Your assistant has started to decorate the cake by writing every child's initial in icing on exactly one cell of the cake. Each cell contains at most one initial, and since no two children share the same initial, no initial appears more than once on the cake.

Each child wants a single rectangular (grid-aligned) piece of cake that has their initial and no other child's initial(s). Can you find a way to assign every blank cell of the cake to one child, such that this goal is accomplished? It is guaranteed that this is always possible. There is no need to split the cake evenly among the children, and one or more of them may even get a 1-by-1 piece; this will be a valuable life lesson about unfairness.

### Practice Details
Time Spent: 1.25h (7:35p - 8:50p)  
Date: 10/10/2017  
Details: I tried to create a greedy algorithm which visited each initial and tried to expand as much as possible, and then proceeding to the next initial. I made the incorrect assumption that because we were dealing with a grid, we wouldn't run into the grid-lock case where this greedy method doesn't work. This happens when all of the spaces around a blank section are expanded as much as possible, and can't expand into the blank pieces, as exemplified in large.out. I also considered doing the opposite and trying to find the closest initial to fill each blank square.
Complexity: Time: O(n^3), Space: O(n^3)  
Result: Partial Completion  

All problem statements, input data and contest analyses are licensed under the Creative Commons Attribution License. Copyright 2008-2017 Google
