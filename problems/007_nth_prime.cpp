#include <iostream>
#include <math.h>

using namespace std;

bool is_prime(int n){
    int limit = sqrt(n) + 1;
    for (int i = 3; i <= limit; i += 2){
        if (n % i == 0) return false;
    }
    return true;
}

int main(){
    int prime_counter = 2;
    int test_number = 5;

    while (prime_counter < 10001){
        if (is_prime(test_number)){
            ++prime_counter;
            //cout << test_number << " is prime" << endl;
        }
        test_number += 2;
    }
    test_number -= 2;

    cout << test_number << endl;

    return 0;
}