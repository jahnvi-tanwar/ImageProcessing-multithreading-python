# imageProcessing-multithreading-python
Grayscale conversion of multiple images using openCV. Completing the task faster with multithreading in python.

# Key Concept
Multithreading - Multithreading is defined as the ability of a processor to execute multiple threads concurrently.

# Task Performed

- For this experiment blocks of 100, 200, 300, 400 and 500 image files were taken as input.
- rgb_to_grayscale() function defined in gray_scale.py and multithreading_gray_scale.py was used to convert image in bgr format to grayscale using cvtColor() function of openCV module.
- In gray_scale.py program task was formed sequentially but in multithreading_gray_scale.py the same task was performed with multithreading. To create threads ThreadPoolExecutor (from concurrent.futures module) was used. 
- In main.py program task is performed multiple times varying number of threads each time. This is done to find the optimal number of threads which will perform the task in less time.
- plot_thread.py file is used to plot number of thread vs time graph which is result of main.py program (Report/report).
- plot_graph.py file is used to plot  number of files vs time double line graph comparing the result of task performed with multithreading and without multithreading.

# Observations

Table 1: Comparing execution time of task with varying number of threads

Number of Active Threads | Time Taken (s)
-------------------------|--------------
1 | 806.7504532
2 | 544.4976104000001
3 | 548.5975074
4 | 545.6509420000002
5 | 552.1994285999999
6 | 360.4934754000001
7 | 366.9670584999999
8 | 364.5329006000002
9 | 364.0383883000004
10 | 363.9121553999994
11 | 366.98776720000023
12 | 364.5366519999998
13 | 364.0464326000001
14 | 362.63782359999914
15 | 364.70052849999956
16 | 364.47398650000014
17 | 362.6452294999999
18 | 361.66494629999943
19 | 361.17374199999995
20 | 361.59370090000084

Graph 1:

![alt text](https://github.com/jahnvi-tanwar/ImageProcessing-multithreading-python/blob/coder/Report/run1.png)

Optimal Number of threads = 6

Table 2: Comparing execution time of capitalizing file text with multithreading and without multithreading while increasing the number of files by 100 

Number of threads used = 13

Number of Files | Time Taken Without Multithreading (s) | Time Taken With Multithreading (s)
--------------- | ---------------------------------|-----------------------------------
100  | 32.69129072803762 | 15.775374412536621
200  | 96.38587993835710 | 35.1330668926239
300  | 161.58046132345781| 68.54701542854309
400  | 260.4525678123675 | 108.12210512161255
500  | 259.7357916341918 | 136.66275644302368

Graph 2:

![alt text](https://github.com/jahnvi-tanwar/ImageProcessing-multithreading-python/blob/coder/Compare/Figure_1.png)

# Findings:

From graph 2 it is evident that the task performed using multithtreading takes less time. 
<br/>Percent decrease in time : 55.34 %


