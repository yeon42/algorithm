# 6-1. 선택 정렬 소스코드

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]: # 앞의 원소가 크면
            min_index = j # 가장 작은 원소 탐색
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)