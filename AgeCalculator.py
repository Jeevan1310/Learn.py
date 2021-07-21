from datetime import datetime, date
  
born=input("Enter your date of birth  in  the format(DD/MM/YYYY) :")
print("Your  date of birth is  ",born)
  
born = datetime.strptime(born, "%d/%m/%Y").date()
  
today = date.today()
print("Yeah It is true!")
print("You are",
      today.year - born.year - ((today.month,
                                          today.day) < (born.month,
                                                        born.day)),"years,",today.month - born.month -((today.year,
                                                                    today.day) < (born.year,born.day)),"month and",(today.day - born.day or born.day - today.day) -((today.month,
                                                                                     today.year) < (born.month,born.year)),"days old")