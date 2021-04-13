"""list = [1,56,2,8,9,7,58]
a = int(input("Choose Number:"))
for i in list:
    if(i%a)==0:
        print(i)"""


##################################
"""dec = 344
print("The decimal value :",dec,"is:")
print(bin(dec), "in binary.")
print(oct(dec), "In octal.")
print(hex(dec), "in Hexadecimal.")"""
###################################

"""c='p'
print("The ASCII value of p :", ord(c))"""
###################################
"""def computeHCF (x,y):

   if x>y:
        smaller = y
    else:
        smaller = x
    for i in range (1, smaller + 1):
        if((x%i==0) & (y%i==0)):
            hcf = i
    return hcf
print(computeHCF(12,16))"""
def computeLcm (x,y):
          if x>y:
               greater = x
          else:
              greater = y
          while(True):
             if((greater%x==0) & (greater%y==0)):
                   lcm = greater
                   break
             greater+=1
          return lcm
print(computeLcm(12,16))





