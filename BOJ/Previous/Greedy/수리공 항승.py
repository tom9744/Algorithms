# 1449 : 수리공 항승
#
# 테이프 하나로 가릴 수 있는 범위를 저장하기 위한 변수 start, end 를 선언한다.
# 위치가 담긴 배열을 오름차순 정렬하고, 가장 첫번째 위치로 첫 start 와 end 값을 구한다.
# 배열의 원소들을 탐색하면서 테이프로 가려지는 범위를 벗어나면 새로운 start, end 계산 후 count 증가.

leaks, tape_length = map(int, input().split())
locations = list(map(int, input().split()))
locations.sort()

count = 1
start = locations[0] - 0.5
end = start + tape_length

for location in locations:
    if start < location < end:
        continue
    else:
        start = location - 0.5
        end = start + tape_length
        count += 1

print(count)