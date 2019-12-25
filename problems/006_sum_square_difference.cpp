#include <iostream>
using namespace std;

int main(){
    int sum_square = 0;
    int square_sum = 0;

    for (int i = 0; i < 101; i++){
        square_sum += i;
        sum_square += i*i;
    }

    int difference = square_sum*square_sum - sum_square;
    cout << difference << endl;

    return 0;
}