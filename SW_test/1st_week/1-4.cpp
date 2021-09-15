// 프로그래머스 42576번

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    
    string answer = " ";

    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());

    for (int i=0; i<completion.size(); i++) {
        if (participant[i] != completion[i])
            return participant[i];
    }
    return participant[participant.size()-1];
}

int main() {
    vector<string> participant;
    vector<string> completion;

    int N;
    cin >> N;

    string str;
    for (int i=0; i<N; i++) {
        cin >> str;
        participant.push_back(str);
    }
    for (int i=0; i<N-1; i++) {
        cin >> str;
        completion.push_back(str);
    }

    string answer = solution(participant, completion);
    cout << answer << '\n';

    return 0;
}