#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
#Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
#Function Description
#Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
#timeConversion has the following parameter(s):
#s: a string representing time in  hour format
#Input Format
#A single string  containing a time in -hour clock format (i.e.:  or ), where  and .
#Constraints
#All input times are valid
#Output Format
#Convert and print the given time in -hour format, where .
#Sample Input 0
#07:05:45PM
#Sample Output 0
#19:05:45
#___________________________________________________________________________________
#Solution
#___________________________________________________________________________________


s1=input('Enter time in 12 hour format \n')
print(s1)
x=0
for i in range(0,len(s1)): 
 if(i==0 and i+1==1):
     hh=s1[i]+s1[i+1]
     i=2
 elif(i==3 and i+1==4):
     mm=s1[i]+s1[i+1]
     i=5
 elif(i==6 and i+1==7):
     ss=s1[i]+s1[i+1]
 elif(i==8):
     if(s1[i]=='P' or s1[i]=='p'):
         x=1

if(x==1):
    if(hh=='12'):
      print(hh+':'+mm+':'+ss)
    else:    
     hh1=int(hh)+12
     print(str(hh1)+':'+mm+':'+ss)
    
else:
    if(hh=='12'):
      hh2=int(hh)-12
      print(str(hh2)+'0:'+mm+':'+ss)
    else:  
      print(hh+':'+mm+':'+ss)