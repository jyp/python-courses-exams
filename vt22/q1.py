
def query():
    month = input("Current month?").lower()
    day = input("Day of the week?").lower()
    if month in ["march", "june", "september","december"] and day == "monday":
        hfm = input("Is that the first holiday-free Monday?").lower()
        return hfm == "yes"
    else:
        return False

if query():
    print("Test the VMA at 15:00!")
else:
    print("No testing today")
