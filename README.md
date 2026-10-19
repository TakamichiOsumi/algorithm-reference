# algorithm-reference

My personal notes about algorithms during self-study.

## Set up the environment

```
$ git clone https://github.com/TakamichiOsumi/algorithm-reference.git
$ cd algorithm-reference
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Optionally, prepare the snippets in different repo.
```
$ git clone https://github.com/TakamichiOsumi/Env.git
$ cp Env/.emacs ~/.emacs
$ mkdir -p ~/.emacs.d/snippets/python-mode
$ cp Env/snippets/python-mode/* ~/.emacs.d/snippets/python-mode
```

## During a competition, run an offline reference

Execute 'python3' to start the console. Load the reference file.
This enables key shortcuts such as Cntrl-a and Cntrl-d and quicker
reference of the offline library manuals.
```
>>> import reference
...
>>> help(string)
```

## Run the last edited script in the current directory

```
$ `git rev-parse --show-toplevel`/execute_latest.sh
```

This enables the same interface of script execution wherever the
current directory is.

## Notes

Tested on only Mac OS X.

## Algorithms

- BFS(breadth-first search)
  - [Double Dots](re/D/Double_Dots.py)
  - [Tour](C/Tour.py)
  - [Sensors](E/Sensors.py)
    Similar to BFS and applied to matrix. Set a center point and search all of the eight surrounding cells from the center.
  - [Grid Repainting](D/Grid_Repainting.py)
  - [Maze Master](re/D/Maze_Master.py)

- DP(dynamic programming)
  - [Frog 1](A/Frog_1.py)
  - [Prediction and Restriction](re/D/Prediction_and_Restriction.py)
  - [A16 - Dungeon 1](tessoku/A16_Dungeon_1.py)
  - [A18 - Subset Sum](tessoku/re/A18_Subset_Sum.py)
  - [A19 - Knapsack 1](tessoku/A19_Knapsack_1.py)
  - [A32 - Game 1](tessoku/re/A32_Game_1.py)

- Bit Brute Force
  - [H and V](C/H_and_V.py)
  - [ORXOR](re/C/ORXOR.py)

- Trig Functions
  - [Opposite](re/D/Opposite.py)
    Describe some notes regarding conversion between degrees and radians. Also, about point rotation.

- Binary Search
  - [Buy an Integer](re/C/Buy_an_Integer.py)
  - [A12 - Printer](tessoku/re/A12_Printer.py)
  - [A13 - Close Pairs](tessoku/A13_Close_Pairs.py) A13's performance can be made faster to O(N) by another logic called 'Two Pointer Technique'.
  - [A14 - Four Boxes](tessoku/A14_Four_Boxes.py)

- Segment Tree
  - [Min-Max Swap](E/Min_Max_Swap.py)
  - [Range Xor Query](re/F/Range_Xor_Query.py)

- Disjoint Set Union (Union-Find)
  - [Friends](D/Friends.py)

- XOR (Exclusive or)
  - [Inc, Dec, Xor](re/C/Inc,_Dec,_Xor.py)

- Run-length encoding
  - [String Compression](B/String_Compression.py)
  See the reference for the Run-length function.
  - [DoubleCamelCase Sort](F/Double_Camel_Case.py)
  This is a problem similar to Run-length algorithm.

- Cumulative Sum
  - [10/90](90/010.py)
  - [38/90](90/038.py)
  - [A07 - Event Attendance](tessoku/A07_Event_Attendance.py)
  - [A08 - Two Dimensional Sum](tessoku/A08_Two_Dimensional_Sum.py)
    A08 can be improved more, from the speed aspect. Refer to the A09 below.
  - [A09 - Winter in ALGO kingdom](tessoku/re/A09_Winter_in_ALGO_kingdom.py)
    This approach can be applied to [Range Set Insertion Query](D/Range_Set_Insertion_Query.py) too.

- Faster Power (math.power()) Calculation
  - [A29 - Power](tessoku/A29_Power.py)

- Greedy Algorithm
  - [A39 - Interval Scheduling Problem](tessoku/re/A39_Interval_Scheduling_Problem.py)
    As the name indicates, this is a problem for interval scheduling.

- Cycle Graph
  - [Cycle Graph](re/C/Cycle_Graph.py)

## Minor insights for competitve programming

- Memory Limitation
  - [Remove and Append](./C/Remove_and_Append.py)

- Time Limitation
  - [Maze Master](./re/D/Maze_Master.py)
