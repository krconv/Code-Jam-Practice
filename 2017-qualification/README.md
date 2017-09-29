# Qualification Round for Google Code Jam 2017
This code was done as a practice, and not during a competition.

## Problem A. Oversided Pancake Flipper
Last year, the Infinite House of Pancakes introduced a new kind of pancake. It has a happy face made of chocolate chips on one side (the "happy side"), and nothing on the other side (the "blank side").

You are the head cook on duty. The pancakes are cooked in a single row over a hot surface. As part of its infinite efforts to maximize efficiency, the House has recently given you an oversized pancake flipper that flips exactly K consecutive pancakes. That is, in that range of K pancakes, it changes every happy-side pancake to a blank-side pancake, and vice versa; it does not change the left-to-right order of those pancakes.

You cannot flip fewer than K pancakes at a time with the flipper, even at the ends of the row (since there are raised borders on both sides of the cooking surface). For example, you can flip the first K pancakes, but not the first K - 1 pancakes.

Your apprentice cook, who is still learning the job, just used the old-fashioned single-pancake flipper to flip some individual pancakes and then ran to the restroom with it, right before the time when customers come to visit the kitchen. You only have the oversized pancake flipper left, and you need to use it quickly to leave all the cooking pancakes happy side up, so that the customers leave feeling happy with their visit.

Given the current state of the pancakes, calculate the minimum number of uses of the oversized pancake flipper needed to leave all pancakes happy side up, or state that there is no way to do it.

### Practice Details
Time Spent: 1.25h (8:45a - 10:00a)  
Date: 9/27/2017  
Details: Created a brute force solution which searches in a BFS fashion for all pancakes flipped. This solution solved the small dataset but cannot solve the large one.  
Complexity: Time: O(n^3), Space: O(n^3)  
Result: Partial Completion  

## Problem B. Tidy Numbers
Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, her pencils are sorted from shortest to longest and her computers from oldest to newest. One day, when practicing her counting skills, she noticed that some integers, when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order. Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to N. What was the last tidy number she counted?

### Practice Details
Time Spent: 40m (9:35p - 10:15p)  
Date: 9/28/2017  
Details: Created a program which looks at two numbers at a time, compares them, and moves back and forth on the input digits to do what it needs. It moves from the most-significant digit (left to right) and continues until it finds a problem; then it turns around where it is and finds the least-significant digit back in the direction it came from (right to left) that can be decremented without causing another problem; then it makes the rest of the digits '9'.
Complexity: Time: O(n), Space: O(1)  
Result: Full Completion  


All problem statements, input data and contest analyses are licensed under the Creative Commons Attribution License. Copyright 2008-2017 Google
