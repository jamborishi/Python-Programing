ry:
 n=int(raw_input("enter a number"))
 if(n>=1 and n<=100000):
                      print "\npositive value"
 elif(n>100000):
                        print "\nits beyond the limit"
 elif(n<0):
                      print "\nnegative value"
 elif(n==0):
                      print "\nzero"
 else:
                      print "\nenter valid input"
except:
                      print "\nenter valid input"
