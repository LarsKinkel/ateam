# The A-Team (with A for 'Algorithm')
## A solving algorithm for the Rush Hour game
Rush hour is a sliding block logic puzzle, invented by Nob Yoshigahara in the 1970s. Classically, the game consists of a 6x6 grid with up to 16 vehicles (12 cars and 4 trucks) with each a different color. Vehicles can only be moved along a straigt line on the grid, but cannot rotate. The goal of the game is to get the red car out through the exit of the board on the right, by moving the other vehicles out of its way.

This repository contains a Python implementation of the board game Rush Hour. There are 7 different starting positions, of which 3 are a 6x6 grid, 3 are a 9x9 grid and 1 12x12 grid. Cars are a 2x1 size and trucks are 3x1. Once the vehicles are positioned in their starting position, they cannot rotate, but only move forwards and backwards.

We also implemented an algorithm to find the fastest way of solving the puzzle. We implemented a:
<ul>
    <li>Random solve algorithm</li>
    <li>Breadth First Search algorithm (BFS)</li>
    <li>Depth First Search algorithm (DFS)</li>
</ul>
After constructing those algorithms we applied some heuristics on the BFS algorithm
to make it less time and memory consuming to get a solution for games 4-7.

## Set up
This codebase is written in Python 3.8.10. In requirements.txt all the packages that are needed to run this code are listed. You can easily install these packages via:
<pre><code>pip install -r requirements.txt</code></pre>

## Use
You can actually run the program by typing the following in the terminal:
<pre><code>python3 main.py</code></pre>

In main.py, we wrote code to solve a game from 1-7 with either one of the algorithms.
A comment line states which algorithm can be found directly underneath it. Firstly, for the random algorithm, one can adjust the number of solutions you want to get and which puzzle you want to solve. As output, the program will return you the number of moves each solution has cost, which solution was the fastest and automatically generate and show a histogram with this data.

After this random algorithm we get to the BFS algorithm. The BFS and DFS algorithms require a bit less user input, one only has to give the number of the game that he/she wants to solve in the setupgrid() function, and the algorithm will try to solve the game. Be aware that with the regular BFS and DFS algorithms, games 4-7 can cause memory issues.

We wanted to make use of some heuristics to try to improve the results we collected with the BFS algorithm, so below the DFS algorithm in main.py, one can find three BFS algorithms with different heuristics applied (called BFS_H_algorithm). Only thing needed as user input is change the game one wants to solve.

## Structure
In the next part we will shortly explain the most important directories and files of this project:
<ul>
    <li><strong>/Code</strong>: contains all the code of the project</li>
    <li><strong>/Code/Algorithms</strong>: contains all the code for the different algorithms</li>
    <li><strong>/Code/Classes</strong>: contains the necessary classes for this project</li>
    <li><strong>/gameboards</strong>: here are game 1-7 as input csv format </li>
    <li><strong>/Results</strong>: contains the outputfiles and animations + robust results</li>
</ul>

In the main folder, 'main.py' contains all the info for running the algorithms. Furthermore, helpers.py contains functions that are not used as method of a class.

The DFS algorithm is made with use of inheritance of the BFS algorithm, since we only have to change one method in order to go from BFS to DFS. The BFS_H_algorithm is also very similar to the BFS algorithm, but since we adjusted a few things in the '__init__' and in the solve() method, we chose to write this algorithm on itself without making use of inheritance.

## Results
We were able to solve game 1-3 with the standard BFS algorithm, this means that our solutions for game 1-3 are the solutions with the least possible amount of moves.
Unfortunately, game 4-7 caused time and memory issues when solving with BFS. Therefore we applied the heuristic functions. Heuristic 3 (Manhattan Distance) was the heuristic that gave us the most optimal solution for game 4-6. The solutions are quite good compared to the best random solutions that we acquired. For game 7, we were not able to find a solution with another algorithm than the random algorithm.

Below we show a table of the best results for the games, most important are the least amount of moves that we found, if two algorithms found the same least amount of moves, we ordered them on how many iterations were needed to get to the solution.

| Game        | Moves to solution | Iterations | Algorithm for best solution    |
| ----------- |:-----------------:|:---------- |:------------------------------ |
| 1           | 35                | 2562       | Breadth First Search           |
| 2           | 29                | 23680      | Breadth First Search           |
| 3           | 83                | 51572      | Breadth First Search H1        |
| 4           | 74                | 14298      | Breadth First Search H3 (MHD)  |
| 5           | 85                | 3041       | Breadth First Search           |
| 6           | 65                | 20286      | Breadth First Search           |
| 7           | 7948              | 7948       | Random Algorithms              |

The information in this table comes from a xls file where we kept track of all the results. This file can be found in the <strong>/Results</strong> folder.

## Authors
<ul>
    <li>Jio Macaya</li>
    <li>Laura Outhuis</li>
    <li>Lars Kinkel</li>
</ul>

## Acknowlegdements
We would like to thank our course coordinators, Quinten van der Post and Wouter Vrielink, to provide us with the necessary knowledge we needed to complete our assignment. We would also like to thank our mentors, Lars Veefkind and Yvette Schroder, who guided and advised us greatly during the making of this project.
