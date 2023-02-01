# The A-Team (with A for 'Algorithm')
## A solving algorithm for the Rush Hour game 
Rush hour is a sliding block logic puzzle, invented by Nob Yoshigahara in the 1970s. Classically, the game consists of a 6x6 grid with up to 16 vehicles (12 cars and 4 trucks) with each a different color. Vehicles can only be moved along a straigt line on the grid, but cannot rotate. The goal of the game is to get the red car out through the exit of the board on the right, by moving the other vehicles out of its way. 

This repository contains a Python implementation of the board game Rush Hour. There are 7 different starting positions, of which 3 are a 6x6 grid, 3 are a 9x9 grid and 1 12x12 grid. Cars are a 2x1 size and trucks are 3x1. Once the vehicles are positioned in their starting position, they cannot rotate, but only move forwards and backwards.

We also implemented an algorithm to find the fastest way of solving the puzzle. We implemented a:
<ul>
    <li>Breadth First Search algorithm (BFS)</li>
    <li>Depth First Search algorithm (DFS)</li>
    <li>Random solve algorithm</li>
</ul>

## Set up
This codebase is written in Python 3.8.10. In requirements.txt all the packages that are needed to run this code are listed. You can easily install these packages via:
<pre><code>pip install -r requirements.txt</code></pre>

## Use
You can actually run the program by typing the following in the terminal:
<pre><code>python3 main.py</code></pre>
In main.py you can also adjust the number of solutions you want to get and which puzzle you want to solve. As output, the program will return you the number of moves each solution has cost, which solution was the fastest and automatically generate and show a histogram with this data.

In main.py there are also scripts to get a solution running the BFS, DFS, and BFS with three different kinds of heuristics applied. 

## Structure
In the next part we will shortly explain the most important directories and files of this project:
<ul>
    <li><strong>/Code</strong>: contains all the code of the project</li>
    <ul>
    <li><strong>/Code/Algorithms</strong>: contains all the code for the different algorithms</li>
    <li><strong>/Code/Classes</strong>: contains the necessary classes for this project</li>
    </ul>
</ul>

## Authors
<ul>
    <li>Jio Macaya</li>
    <li>Laura Outhuis</li>
    <li>Lars Kinkel</li>
</ul>

## Acknowlegdements
We would like to thank our course coordinators, Quinten van der Post and Wouter Vrielink, to provide us with the necessary knowledge we needed to complete our assignment. We would also like to thank our mentors, Lars Veefkind and Yvette Schorder, who guided and advised us greatly during the making of this project.
