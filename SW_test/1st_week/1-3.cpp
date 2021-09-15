// 문자열 변환 (소문자 -> 대문자)

#include <iostream>
#include <string.h>
using namespace std;

int main() {
    string str;
    cin >> str;

    for (int i=0; i<str.size(); i++) {
        if (str[i] >= 'a' && str[i] <= 'z')
            str[i] = toupper(str[i]);
            // str[i] = str[i] - 'a' + 'A';
    }

    cout << str << '\n';

}