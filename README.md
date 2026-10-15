# algorithm-reference

My personal notes about algorithms during self-study.

## Set up the environment

```
$ git clone https://github.com/TakamichiOsumi/python-reference.git
$ cd python-reference
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
  - [Double Dots][1]
  - [Tour][2]
  - [Sensors][3]
    Similar to BFS and applied to matrix. Set a center point and search all of the eight surrounding cells from the center.
  - [Grid Repainting][11]
  - [Maze Master][12]

- DP(dynamic programming)
  - [Frog 1][4]
  - [Prediction and Restriction][5]
  - [A16 - Dungeon 1][27]
  - [A18 - Subset Sum][29]
  - [A19 - Knapsack 1][30]

- Bit Brute Force
  - [H and V][6]
  - [ORXOR][7]

- Trig Functions
  - [Opposite][8]
    Describe some notes regarding conversion between degrees and radians. Also, about point rotation.

- Binary Search
  - [Buy an Integer][9]
  - [A12 - Printer][24]
  - [A13 - Close Pairs][25] A13's performance can be made faster to O(N) by another logic called 'Two Pointer Technique'.
  - [A14 - Four Boxes][26]

- Segment Tree
  - [Min-Max Swap][13]
  - [Range Xor Query][17]

- Disjoint Set Union (Union-Find)
  - [Friends][14]

- XOR (Exclusive or)
  - [Inc, Dec, Xor][10]

- Run-length encoding
  - [String Compression][15]
  See the reference for the Run-length function.
  - [DoubleCamelCase Sort][16]
  This is a problem similar to Run-length algorithm.

- Cumulative Sum
  - [10/90][18]
  - [38/90][20]
  - [A07 - Event Attendance][21]
  - [A08 - Two Dimensional Sum][22]
    A08 can be improved more, from the speed aspect. Refer to the A09 below.
  - [A09 - Winter in ALGO kingdom][23]
    This approach can be applied to [Range Set Insertion Query][28] too.

- Faster Power (math.power()) Calculation
  - [A29 - Power][31]

- Cycle Graph
  - [Cycle Graph][19]

[1]:re/D/Double_Dots.py
[2]:C/Tour.py
[3]:E/Sensors.py
[4]:A/Frog_1.py
[5]:re/D/Prediction_and_Restriction.py
[6]:C/H_and_V.py
[7]:re/C/ORXOR.py
[8]:re/D/Opposite.py
[9]:re/C/Buy_an_Integer.py
[10]:re/C/Inc,_Dec,_Xor.py
[11]:D/Grid_Repainting.py
[12]:re/D/Maze_Master.py
[13]:E/Min_Max_Swap.py
[14]:D/Friends.py
[15]:B/String_Compression.py
[16]:F/Double_Camel_Case.py
[17]:re/F/Range_Xor_Query.py
[18]:90/010.py
[19]:re/C/Cycle_Graph.py
[20]:90/038.py
[21]:tessoku/A07_Event_Attendance.py
[22]:tessoku/A08_Two_Dimensional_Sum.py
[23]:tessoku/re/A09_Winter_in_ALGO_kingdom.py
[24]:tessoku/re/A12_Printer.py
[25]:tessoku/A13_Close_Pairs.py
[26]:tessoku/A14_Four_Boxes.py
[27]:tessoku/A16_Dungeon_1.py
[28]:D/Range_Set_Insertion_Query.py
[29]:tessoku/re/A18_Subset_Sum.py
[30]:tessoku/A19_Knapsack_1.py
[31]:tessoku/A29_Power.py


## Minor insights for competitve programming

- Memory Limitation
  - [Remove and Append](./C/Remove_and_Append.py)

- Time Limitation
  - [Maze Master](./re/D/Maze_Master.py)
