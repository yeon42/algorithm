// 백준 13414번

#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int main() {
    int K, L, arr[500010];
    map<int, int> m;
    
    cin >> K >> L;

    for (int i=0; i<L; i++) {
        cin >> arr[i]; // 학번
        m[arr[i]] = i; // 학번과 인덱스 저장
    }
    
    int cnt = 0;
    for (int i=0; i<L; i++) {
        if (cnt >= K) break;
        if (m[arr[i]] == i) {
            cout << arr[i] << '\n';
            cnt ++;
        }
    }

    return 0;
}