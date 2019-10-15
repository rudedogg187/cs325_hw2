

#getMajority(lst, p, q):
  

def majority(lst, p, r):
 if p == r:
   return lst[p]


 if p < r: 
   q = (p + r) / 2
   

   lel = majority(lst, p, q)
   rel = majority(lst, p + 1, r)


   if lel == rel:
     return lel
  



 
 




lst = [1, 2, 1, 1, 3, 5, 7, 1]


print majority(lst, 0, len(lst) - 1)
