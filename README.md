# pathfinder-A-star-algorithm-

A* achieve optimality and completeness, two valuable property of search algorithms.

When a search algorithm has the property of optimality, it means it is guaranteed to find the best possible solution. When a search algorithm has the property of completeness, it means that if a solution to a given problem exists, the algorithm is guaranteed to find it.

Now to understand how A* works, first we need to understand a few terminologies:

Node (also called State) — All potential position or stops with a unique identification
Transition — The act of moving between states or nodes.
Starting Node — Whereto start searching
Goal Node — The target to stop searching.
Search Space — A collection of nodes, like all board positions of a board game
Cost — Numerical value (say distance, time, or financial expense) for the path from a node to another node.
g(n) — this represents the exact cost of the path from the starting node to any node n
h(n) — this represents the heuristic estimated cost from node n to the goal node.
f(n) — lowest cost in the neighboring node n

Each time A* enters a node, it calculates the cost, f(n)(n being the neighboring node), to travel to all of the neighboring nodes, and then enters the node with the lowest value of f(n).
These values we calculate using the following formula:
f(n) = g(n) + h(n)


#Making grid using pygame

With the important concepts of Object Orientated programming and then take you through the process of creating a class based fun game, using pygame. Like i jst simply created a window as menu
for the use of my grid and A star algorithm here.

#Learned from this!

I was surely excited about this when i was trying to figure this out in my own way getting along with this algorithm but after sometime it worked out well with pygame, i used a way of object oriented programming for this pygame Menu thing here, which 
i have never did before, so it really inspire me and changed my way of looking things in my code more broadly!


#Hello!
This is all my written code, Did you see an error in a post? Please submit a pull request. Thank you. 
