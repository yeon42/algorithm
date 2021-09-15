// 1 ~ N까지의 합 구하기

#include <iostream>
using namespace std;

int sum_func(int i) {
    if (i==1)
        return 1;
    else
        return i + sum_func(i-1);
}

int main() {
    int n;
    cin >> n;
    cout << sum_func(n) << '\n';
}