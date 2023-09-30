#check if an array is a palindrome
def palindrome(arr):
  #create pointers
  L = 0
  R = len(arr) -1

  while L < R:#break loop when pointers cross
    if arr[L] != arr[R]:
      return False
    L += 1 # increment
    R -= 1 # decrement

  return True #output

print(palindrome([1,2,3,3,2,1]))
