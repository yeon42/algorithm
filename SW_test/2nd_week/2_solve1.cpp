// 카카오 신입 공채 1차 코딩테스트
// 1. 비밀 지도 (난이도: 하)

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    vector<string> arr;

    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            if (arr1[i]%2 || arr2[i]%2) { // 둘 다 1이면 #
                arr.push_back("#");
            } else {
                arr.push_back(" ");
            }
            arr1[i] = arr1[i] / 2;
            arr2[i] = arr2[i] / 2;
        }

        answer.push_back(arr[n-1]);
        for (int j=n-2; j>=0; j--) { // 순서 반대로 저장
            answer[i] += arr[j];
        }
        arr.clear();
    }
    return answer;
}

int main() {
    int n;
    cin >> n;
    
    vector <int> arr1;
    vector <int> arr2;
    vector <string> res;

    int nn;
    for (int i=0; i<n; i++) {
        cin >> nn;
        arr1.push_back(nn);
    }

    for (int i=0; i<n; i++) {
        cin >> nn;
        arr2.push_back(nn);
    }

    res = solution(n, arr1, arr2);
    for (int i=0; i<n; i++) {
        cout << res[i] << '\n';
    }


}