while(True):
     print("****************************************************************")
     print("Choose which action u want to perform")
     print("1.) Add Birthday")
     print("2.) Display Added Birthdays")
     print("3.) Exit")
     print("Enter from above numbers: ")
     a=int(input())
     noglo=0
     my_dict = {}
     if(a==1):
         print("How many bday u want to add")
         no=int(input())
         noglo=no
         for i in range(1,no+1):
              b=input("Enter the name of person: ")
              c=int(input("Enter the year of bday: "))
              my_dict={b:c}

     elif(a==2):
              print(my_dict)


     if(a==3):
         exit(0)
     print("****************************************************************")