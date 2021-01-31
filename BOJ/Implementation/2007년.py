import sys

month, day = map(int, sys.stdin.readline().rstrip().split())
num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

days_passed = 0

for idx in range(month - 1):
    days_passed += num_of_days[idx]

days_passed += day - 1

print(week[days_passed % 7])