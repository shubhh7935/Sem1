start_date=int(input("enter the start year: "))
end_date=int(input("enter the end year: "))
leap_years=[]
not_leap_years=[]
for i in range(start_date,end_date):
  if i%4==0:
    leap_years.append(i)
    i+=1
  elif i%400==0:
    leap_years.append(i)
  else:
    not_leap_years.append(i)

print("leap years are:",leap_years)
print("not leap years",not_leap_years)
  
