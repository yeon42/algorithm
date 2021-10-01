// 백준 1181번

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool sorting(string v1, string v2) {
    if (v1.size() == v2.size())
        return v1 < v2;
    return v1.size() < v2.size();
}

int main() {
    int N;
    cin >> N;

    vector <string> vec;

    for (int i=0; i<N; i++) {
        string s; cin >> s;
        if (find(vec.begin(), vec.end(), s) == vec.end())
            vec.push_back(s);
    }

    sort(vec.begin(), vec.end(), sorting);

    for (int i=0; i<vec.size(); i++) {
        cout << vec[i] << '\n';
    }
}