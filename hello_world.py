# Import datetime module to get today's date
from datetime import date

# Take user input for name
name = input("Enter your name: ")

# Take user input for internship role
role = input("Enter your internship role: ")

# Get today's date
today_date = date.today()

# Print the output using variables
print("Name:", name)
print("Internship Role:", role)
print("Today's Date:", today_date)
