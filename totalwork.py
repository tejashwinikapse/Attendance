import sys

total_days = int(sys.argv[1])
present_days = int(sys.argv[2])

attendance = (present_days / total_days) * 100

print("Attendance percentage of student is:", attendance, "%")