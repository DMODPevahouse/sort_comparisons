# Sort Comparisons

## Description
The purpose of this project was to use 5 different sorting algorithms, 4 quick sorts of differing implementations and a
natural merge sort, and compare them against each other to see how they perform. The algorithms were tested on
~30 different input files of varying sizes, some as small as 50 others as large as 60,000. The results were then
analyzed to see which algorithm performed the best in which cases. There are two different output files listed in the
output directory. One is a text file that contains the sorted values of the files smaller then 50, and the other is a 
csv file that was used to create the graphs in the report. The csv file also includes all of the timing, comparisons,
and swaps for each algorithm. 

Helpful information:

ll = the natural merge sort
qs = the quick sort using first pivot
qsi100 = the quick sort using first pivot and insertion sort for n < 100
qsi50 = the quick sort using first pivot and insertion sort for n < 50
qsm = the quick sort using median pivot

## Running This project

> Note: This program was written in Python 3.11
> Note: This program was written in Pycharm 2022.2.1
> Results may vary if you are using a different version of Python or Pycharm
> The source code can be found in the src folder

1. Download and install Python on your computer
2. Open up a terminal
3. Navigate to the directory containing the README.md
4. Run the program as a module: `python -m src -h`. This will print the help message.
5. Run the program as a module (with real inputs): `python -m src <some_input_directory> <some_output_csv> <some_output_txt>`
   a. IE: `python3 -m src rour_directory\inputs\ your_directory\outputs\output.csv your_directory\outputs\output.txt`
> Note: The input file can also be a directory for automated testing, just give a directory
> WARNING -- All files in the directory will need to be .txt files, or the program not operate on them



## This project's usage:

```commandline
usage: python -m src in_file out_file

positional arguments:
    in_file     The input file or directory
    out_file_list    The output file
    out_file_csv    The output file for the csv
```

## Sample Input and Output

The required input files are in the directory inputs within the project, resting in the inputs directory:



As for outputs, any output file will be created in the directory outputs within the project
and you will be able to name it whatever you want, the program will create it, resting in the output directory:
 
For your convenience, one is already created below
IE: D:\this_is\your_directory_path\here\outputs\output.txt


When using the function you will need to use the full path to the input and output files
in order for it to be recognized

## Acceptable Input

The acceptable input for this program is a directory of .dat files. If the files are not in .dat format, nothing will be 
read but an error will not be given, the outputs would just be empty. Within those .dat files, the acceptable input is
a list of integers. They can be seperated by spaces or by new lines. The program will read the integers and sort them
using the 5 different sorting algorithms. The output will be a csv file that contains the timing, comparisons, and swaps
for each algorithm, and a text file that contains the sorted values of the files smaller then 50. As long as a file has
only integers and is in the .dat format it will be read.
