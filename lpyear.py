def is_leap(year):
   
    if (year % 4 == 0):
        return True
    return False

def check_leap_year(years):
    leap_years = [year for year in years if is_leap(year)]
    return leap_years


years = list(map(int, input("Enter the years : ").split()))
leap_years = check_leap_year(years)
print(f"Leap years from the list are: {leap_years}")
