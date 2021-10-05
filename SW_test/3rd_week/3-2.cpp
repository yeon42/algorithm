#include <iostream>
using namespace std;

int main() {
    int arr[9] = {0};

    for (int i=0; i<9; i++) {
        cin >> arr[i];
    }

    int max = arr[0];
    int index;
    for (int i=0; i<9; i++) {
        if (arr[i] > max) {
            max = arr[i];
            index = i+1;
        }
    }

    cout << max << '\n' << index << '\n';


}