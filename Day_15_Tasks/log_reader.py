'''Scenario:
A large log file needs to be processed.
Task:
● Create a generator to read file line by line
● Use loop to process logs
● Use condition to filter errors
● Count occurrences using a dictionary'''

#  Create a generator to read file line by line
def read_logs(logfile):
    with open(logfile, 'r') as file:
        for line in file:
            yield line.strip()


# Create a dictionary to count errors
error_count = {}

#  Use loop to process logs
for log in read_logs("logfile.txt"):

    #  Use condition to filter errors
    if "ERROR" in log:

        error_type = log.split("ERROR:")[-1].strip()

        #  Count occurrences using dictionary
        if error_type in error_count:
            error_count[error_type] += 1
        else:
            error_count[error_type] = 1

#  Display results
print("Error Summary:")

for error, count in error_count.items():
    print(error, ":", count)