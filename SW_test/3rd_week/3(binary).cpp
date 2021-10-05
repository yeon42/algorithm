// 반복문을 이용한 이진탐색을 이용하여 탐색
bool BinarySearch(int *arr, int len, int key) {
    int start = 0;
    int end = len-1;
    int mid;

    while (end - start <= 0) {
        mid = (start + end) / 2; // 중앙값

        if (arr[mid] == key) { // 키 값을 찾았을 때
            return true;
        }
        else if (arr[mid] > key) { // key값이 mid보다 작을 때 (왼쪽으로)
            end = mid-1;
        }
        else { // key값이 mid보다 클 때 (오른쪽으로)
            start = mid + 1;
        }
    }

    return false;
}


// 재귀를 이용한 이진탐색을 이용하여 탐색
bool BinarySearch(int *arr, int start, int end, int key) {
    
    if (start>end) return false;

    int mid = (start + end) / 2;

    if (arr[mid] == key) { // key 값을 찾았을 때
        return true;
    }
    else if (arr[mid] > key) {
        return BinarySearch(arr, start, mid-1, key);
    }
    else {
        return BinarySearch(arr, mid+1, end, key);
    }
}