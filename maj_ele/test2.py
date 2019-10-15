def CompareElements(Array, left_element, right_element):
  if left_element == right_element:
    return left_element

  majority = int( len(Array) / 2 ) + 1

  left_count = 0
  right_count = 0

  for element in Array:
    if element == left_element:
      left_count += 1

    if element == right_element:
      right_count += 1
 
    if left_count >= majority:
      return left_element

    if right_count >= majority:
      return right_element
  
  return "No Majority Element Exists"        
 

def MajorityElement(Array):
  length = len(Array)
  if length == 1:
    return Array[0]

  mid_index = int( length / 2 )
  #print(Array)
  left_element = MajorityElement(Array[0: mid_index])
  right_element = MajorityElement(Array[mid_index: length])
  #print(left_element, right_element)
  #print ("------------")


  return CompareElements(Array, left_element, right_element)

 

  

 

 

 

lst = [1, 2, 4, 1, 2, 2, 8, 1, 2, 2] 

print (MajorityElement(lst))