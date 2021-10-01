/*

- map을 이용해 (알파벳, 인덱스) 쌍 저장
 ex) m[A]=1, m[B]=2, ..., m[Z]=26

- 앞에서부터 차례대로 문자열의 일부분을 확인할 때 map의 기능을 이용해
  해당 알파벳 문자열, 즉 key 값이 map에 있는 경우, 없는 경우를 나누었다.
- 있다면 인덱스를 출력하고 + 길이를 하나 늘려 위 과정 반복
- 없다면 map에 새로운 (알파벳, 인덱스) 쌍으로 저장해 위 과정 반복

*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int main() {
    string msg;
    cin >> msg;

    vector <int> answer;
    map <string, int> m;
    int index;

    string temp = "";
    for (int i=1; i<=26; i++) {
        temp += 'A' + i - 1;
        m[temp] = i;
        temp = "";
    }

    int i=0, k=27;
    temp = msg[0];

    while(i < msg.size()) {
        if (m.find(temp) != m.end()) { // map에 있다면
            index = m[temp]; // 인덱스 저장

            if (i == msg.size()-1) { // 맨 마지막 단어
                answer.push_back(index);
                break;
            }
            i++;
            temp += msg[i]; // 다음 단어까지 추가

        }
        else { // map에 없다면
            answer.push_back(index); // 이전의 index 추가
            m[temp] = k;
            k++;
            temp = msg[i];
        }
    }

    for (int i=0; i<answer.size(); i++) {
        cout << answer[i] << ' ';
    }

    return 0;

}