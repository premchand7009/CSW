
month_days = {
    "january": 31,
    "february": 28,   
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}


month = input("Enter the name of a month: ").strip().lower()


if month not in month_days:
    print("Error: Invalid month name. Please enter a valid month (e.g., January).")
else:
    
    if month == "february":
        year = int(input("Enter a year: "))
        
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days = 29
        else:
            days = 28
        print(f"February {year} has {days} days.")
    else:
        
        days = month_days[month]
        
        print(f"{month.capitalize()} has {days} days.")
