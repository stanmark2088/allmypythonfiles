def check_leap_year(year):
    if year % 4 == 0:
      return str(year) + " is a leap year"
    else:
      return str(year) + " is not a leap year"

year_to_check = 2021  # creezi o variabila pe care o inserezi in check_leap_year
returned_value = check_leap_year(year_to_check)  # creezi returned value calculezi functia cu variabila definita inautru
print(returned_value)