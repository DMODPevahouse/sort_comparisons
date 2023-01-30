# ----- Script Creator
# ----- David Pevahouse
# ----- Date
# ----- 12/05/2022
# ----- Purpose ------
# The purpose of main is to set up the function, and call it
#
#
# ----- Description ------
# We do this by reading in the argument of the commandline to handle what the input
# and output files are. Then we call the function that will handle the rest of the
# program. We will report the success, or lack therof, of the program to the user
# by printing to the output file. The program will also handle a directory full of files
# and sort them all.


# from src import pre_to_post within function
# Helps read in filepaths
from data_objects import create_array, create_linked_list
from quick_sorts import recursive_quick_insertion_sort, recursive_median_of_three_quick_sort, recursive_first_pivot_sort
from natural_merge_sort import natural_merge_sort
from printing_def import print_linked_list, print_array
from pathlib import Path
import sys
# Imported to read argument from command line
import argparse
# Only imported to report back how long it took the function to run
import time
# when the function starts
start_time = time.time()
sys.setrecursionlimit(500000)
# Using argparse to read in command line arguments
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("in_file", type=str, help="Input File Pathname")
arg_parser.add_argument("out_file_csv", type=str, help="Output File Pathname")
arg_parser.add_argument("out_file_list", type=str, help="Output File Pathname")
args = arg_parser.parse_args()

in_file = Path(args.in_file)
output_list = Path(args.out_file_list)
output_csv = Path(args.out_file_csv)
# Count for how many prefix's have been tested
expression_count = 0
# Creates the output file
with open(output_list, 'w') as new_file:
    pass
with open(output_csv, 'w') as new_file1:
    pass
# opens the file or directory, creates the linked list and array, sorts and reports time
# results to the output file
if in_file.exists():
    if in_file.is_dir():
        in_dir = in_file
        in_dir1 = in_file
        output_file = open(output_csv, 'a')
        output_file.write("File,Type,time,comparisons,exchanges\n")
        for file in in_dir.glob("*.dat"):
            ll = create_linked_list(file)
            a = create_array(file)
            output_file = open(output_csv, 'a')
            sort_ll_time = time.time()
            sorted_ll, e1, c1 = natural_merge_sort(ll, int(0), int(0))
            end_sort_ll_time = time.time()
            qs_a_time = time.time()
            qs_sorted_a, e2, c2 = recursive_first_pivot_sort(a, int(0), int(0))
            end_qs_a_time = time.time()
            qsi100_a_time = time.time()
            qsi100_sorted_a, e3, c3 = recursive_quick_insertion_sort(a, 100, 0, 0)
            end_qsi100_a_time = time.time()
            qsi50_a_time = time.time()
            qsi50_sorted_a, e4,c4 = recursive_quick_insertion_sort(a, 50, 0, 0)
            end_qsi50_a_time = time.time()
            qsm_a_time = time.time()
            qsm_sorted_a, e5, c5 = recursive_median_of_three_quick_sort(a, 0, 0)
            end_qsm_a_time = time.time()
            output_file.write(str(file) + ", ll," + str(end_sort_ll_time - sort_ll_time) + "," + str(c1) + "," + str(e1) + "\n")
            output_file.write(str(file) + ", qs," + str(end_qs_a_time - qs_a_time) + "," + str(c2) + "," + str(e2) + "\n")
            output_file.write(str(file) + ", qs100," + str(end_qsi100_a_time - qsi100_a_time) + "," + str(c3) + "," + str(e3) + "\n")
            output_file.write(str(file) + ", qs50," + str(end_qsi50_a_time - qsi50_a_time) + "," + str(c4) + "," + str(e4) + "\n")
            output_file.write(str(file) + ", qsm," + str(end_qsm_a_time - qsm_a_time) + "," + str(c5) + "," + str(e5) + "\n")
            output_file.close()
        for file1 in in_dir1.glob("*50.dat"):
            ll = create_linked_list(file1)
            a = create_array(file1)
            output_file1 = open(output_list, 'a')
            sort_ll_time = time.time()
            sorted_ll, e1, c1 = natural_merge_sort(ll, int(0), int(0))
            end_sort_ll_time = time.time()
            qs_a_time = time.time()
            qs_sorted_a, e2, c2 = recursive_first_pivot_sort(a, int(0), int(0))
            end_qs_a_time = time.time()
            qsi100_a_time = time.time()
            qsi100_sorted_a, e3, c3 = recursive_quick_insertion_sort(a, 100, 0, 0)
            end_qsi100_a_time = time.time()
            qsi50_a_time = time.time()
            qsi50_sorted_a, e4, c4 = recursive_quick_insertion_sort(a, 50, 0, 0)
            end_qsi50_a_time = time.time()
            qsm_a_time = time.time()
            qsm_sorted_a, e5, c5 = recursive_median_of_three_quick_sort(a, 0, 0)
            end_qsm_a_time = time.time()
            output_file1.write("\nLinked list merge sort time: " + str(end_sort_ll_time - sort_ll_time) + "\n")
            printing_ll = sorted_ll
            print_linked_list(printing_ll, output_file1)
            output_file1.write("\nLinked list merge sort is the above\n")
            output_file1.write("Done in " + str(e1) + " exchanges and " + str(c1) + " comparisons" + "\n")
            output_file1 = open(output_list, 'a')
            output_file1.write("\nArray quick sort time using first item: " + str(end_qs_a_time - qs_a_time) + "\n")
            print_array(qs_sorted_a, output_file1)
            output_file1.write("\nQuick sort using first item is the above\n")
            output_file1.write("Done in " + str(e2) + " exchanges and " + str(c2) + " comparisons" + "\n")
            output_file1 = open(output_list, 'a')
            output_file1.write(
                "\nArray quick sort time using 100 partition size: " + str(end_qsi100_a_time - qsi100_a_time) + "\n")
            print_array(qs_sorted_a, output_file1)
            output_file1.write("\nQuick sort using first item is the above\n")
            output_file1.write("Done in " + str(e3) + " exchanges and " + str(c3) + " comparisons" + "\n")
            output_file1 = open(output_list, 'a')
            output_file1.write(
                "\nArray quick sort time using 50 partition size: " + str(end_qsi50_a_time - qsi50_a_time) + "\n")
            print_array(qs_sorted_a, output_file1)
            output_file1.write("\nQuick sort using first item is the above\n")
            output_file1.write("Done in " + str(e4) + " exchanges and " + str(c4) + " comparisons" + "\n")
            output_file1 = open(output_list, 'a')
            output_file1.write(
                "\nArray quick sort time using median of 3 pivot: " + str(end_qsm_a_time - qsm_a_time) + "\n")
            print_array(qs_sorted_a, output_file1)
            output_file1.write("\nQuick sort using first item is the above\n")
            output_file1.write("Done in " + str(e5) + " exchanges and " + str(c5) + " comparisons" + "\n")

    elif in_file.is_file():
        print("Please insert a directory instead of a file that includes .dat files")
else:
    print("Please insert an existing directory that includes .dat files")
# determines how long the function took to run, opening the file
# reporting the runtime by writing to the file, then closing the file
end_time = time.time()
execution_time = end_time - start_time
output_file = open(output_list, 'a')
output_file.write("\nTime it took to execute: " + str(execution_time) + "\n")
output_file.close()
