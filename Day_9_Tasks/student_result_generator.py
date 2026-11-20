'''A school system calculates student results differently depending on available data.
Create a Result class where a method can calculate the result using either two
subjects or three subjects'''


class Result:
    def calculate(self, s1, s2, s3=0):
        total = s1 + s2 + s3
        print("Total Marks:", total,"\n")


# Creating object
r = Result()

# Calculating result using two subjects
print("Two Subjects:")
r.calculate(80, 90)

# Calculating result using three subjects
print("Three Subjects:")
r.calculate(80, 90, 85)
