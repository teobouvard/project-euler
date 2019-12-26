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
    return 0;
}