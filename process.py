# Opens the "um-server-01.txt" by returning
# a fijle object so that the program can
# read from and write to the data file
log_file = open("um-server-01.txt")

# Defining a function called sales_reports
# that takes in one parameter called log_file
def sales_reports(log_file):
    # A for loop with a local variable called
    # line, which will loop through each line
    # in the data file assigned to the 
    # the variable called log_file
    for line in log_file:
        # Removes trailing spaces
        line = line.rstrip()
        # Creating a variable called 'day'
        # which will contain the first 3 characters
        # in the line
        day = line[0:3]
        # If statement, which checks for the day variable
        if day == "Tue":
            # Prints the line
            print(line)

# Calling the sales_report function and passing
# in the file opened on line 4
sales_reports(log_file)
