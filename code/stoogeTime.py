import timeit
import stoogesort
import cleanup
import randomArray
#import testLogger

testName = "Insert"
logName = "sort_tests.csv"

minVal = 0
maxVal = 10000
strtN = 300
nIncr = 200
tests = 10


tstLst = randomArray.lstOfLsts(minVal, maxVal, strtN, nIncr, tests)

results = []
i = 0
for tst in tstLst:
  n = len(tst)
  strt = timeit.default_timer()
  print("test: {}\nn: {}".format(i, n))
  stoogesort.stoogeSort( tst, 0, len(tst) - 1 )

  end = timeit.default_timer()
  t = end - strt 
  print("t: {}\n".format(t) )

  
  result = [testName, n, t]
  results.append(result)

  i += 1

#testLogger.addLogData(logName, results)

cleanup.pyc()





