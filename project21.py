# Given an integer N and a cake which can be cut into pieces, each cut should be a straight line going from the center of the cake to its border. Also, the angle between any two cuts must be a positive integer. Two pieces are equal if their appropriate angles are equal. 
# The given cake can be cut in following three ways: 
#     • Cut the cake into N equal pieces.
#     • Cut the cake into N pieces of any size.
#     • Cut the cake into N pieces such that no two of them are equal.
n=int(input("enter the number of pieces: "))
# cake cutting into N pieces of equal size
if 360%n==0:
  print(n,"equal pieces possible")
else:
  print(n,"equal pieces are not possible")
# cake cutting into N pieces of any size
# no. of pieces=no of cuts
# so if no. of cuts can devide the care with no decimal quotient, then cake cutting of N pieces of any size would be possible
a= 360%n
if a is integer:
  print(n,"pieces possible")
else:
  print(n,"pices Not Possible")
# cake cutting into  pieces so that no two of them are equal





