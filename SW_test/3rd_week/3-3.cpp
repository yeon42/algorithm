// 이진 탐색

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, k;
    cin >> n;

    int arr[1000001] = {0};
    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }

    cin >> k;

    int max = arr[0];
    for (int i=0; i<n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    if (k>max) cout << n+1 << endl;
    else {
        for (int i=0; i<n; i++) {
            if (arr[i] >= k) {
                cout << i+1 << endl;
                break;
            }
        }
    }

    // cout << binary_search(arr, arr+n, k);
}