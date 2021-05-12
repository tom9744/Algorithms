# 11399 : ATM

people = int(input())
times_needed = list(map(int, input().split()))
waiting_time = 0
time_taken = []

times_needed.sort()

for time in times_needed:
    time_taken.append(time + waiting_time)
    waiting_time += time

print(sum(time_taken))