README for:
  insertsort.py
  mergesort.py
  insertTime.py
  mergeTime.py

Josh Hughes
07 OCT 2019
CS325 Assignement 1

---------------------------------------------------------------
INSERT SORT
-------------------------------------------------------------
insertsort.py uses the insertion sort algorithm to sort a list of length n.  It will read a file, located in the same directory, named 'data.txt'.  insertsort.py will save the sorted array to a file named 'insert.txt', in the same directory.


RUNNING insertsort.py:

1. Place data.txt file in same directory as the insertsort.py script.

2. Change directory, so that the current working directory is location of wher insertsort.py is located.

3. Type the following command into the command prompt:
    "python insertsort.py" (without the quotes)


---------------------------------------------------------------
MERGE SORT
---------------------------------------------------------------
mergesort.py uses the merge sort algorithm to sort a list of length n.  It will read a file, located in the same directory, named 'data.txt'.  mergesort.py will save the sorted array to a file named 'merge.txt', in the same directory.


RUNNING mergesort.py:

1. Place data.txt file in same directory as the mergesort.py script.

2. Change directory, so that the current working directory is location of wher mergesort.py is located.

3. Type the following command into the command prompt:
    "python mergesort.py" (without the quotes)




---------------------------------------------------------------
INSERT SORT TIME
-------------------------------------------------------------
insertTime.py uses the insertion sort algorithm to sort n lists of various lengths.  It will output to the terminal the list length and the time (in seconds) that it took to sort the list. Additionally, it will save the data to .csv file in the same direcotry. 


RUNNING insertTime.py:

1. Change directory, so that the current working directory is location of wher insertTime.py is located.

2. Type the following command into the command prompt:
    "python insertTime.py" (without the quotes)


---------------------------------------------------------------
MERGE SORT TIME
---------------------------------------------------------------
mergeTime.py uses the merge sort algorithm to sort n lists of various lengths.  It will output to the terminal the list length and the time (in seconds) that it took to sort the list.  Additionally, it will save the data to .csv file in the same direcotry.



RUNNING mergeTime.py:

1. Change directory, so that the current working directory is location of wher mergesort.py is located.

2. Type the following command into the command prompt:
    "python mergeTime.py" (without the quotes)


---------------------------------------------------------------
OTHER
---------------------------------------------------------------
there two scripts used by inertsort.py and mergesort.py respectally, importing them as modules.  the code was modularized as much as possible.

scripts where written by josh hughes

sources used are:
	www.geeksforgeeks.org/merge-sort
	intro to algorithms v3

---------------------------------------------------------------
OTHER
---------------------------------------------------------------
both mergesort.py and insertsort.py depend on fileHandler.py to read in and write text tiles.  This was put into its own module so that both programs could use the one function. 

also, both mergsort.py and insertsort.py use cleanup.py to clean up the current direclty after they are ran.  this simply deletes the .pyc files at the end of running.

insertTime.py and mergeTime import in insertsort.py and mergeTime.py. this allowed the timing scripts in part 4 to use the same functions as for part 3.  

mergeTime and insertTime use also save the output to a csv file.  this was for testing purposes, i found this useful so i left it in the scripts.

mergeTime and insertTime use randomArray.py to generate random arrays of length n.  this was put into its own script so that the code could be reused between the two timing scripts.


all scripts where written by josh hughes

sources used are:
	www.geeksforgeeks.org/merge-sort
	intro to algorithms v3
