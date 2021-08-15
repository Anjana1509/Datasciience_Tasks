 
def register():
 #create username   
 
 from typing import Pattern
 import re
Pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
Pattern1= '^[@]\w+[.]\w{2,3}$'
Pattern2= '^[a-z0-9]+[\._]?[a-z0-9]+[@][.]\w{2,3}$'
username = input("Create Username:")
if(re.search(Pattern1, username)):
    print("it should not start with special characters and numbers") 
    register()  
elif(re.search(Pattern2, username)):
    print("there should not be any . immediate next to @")
    register()
elif(re.search(Pattern, username)):
    print("username created")

register()  
def access():
  pass  
           
 #password validation   
import re
Password =input("Create Password:")
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?& ])[A-Za-z\d@$!#%*?&]{5,16}$"
match_re = re.compile(reg)
result = re.search(match_re, Password)
if result:
   print("Valid Password")  
elif result!=match_re:
    print("invalid password")  
    register()      
else:
   
   
  register()

   



  
                


    










 
     

    

