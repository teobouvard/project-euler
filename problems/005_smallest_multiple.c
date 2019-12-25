#include <stdio.h>
#include <stdbool.h>

bool divisible(int n){
    for (int i = 1; i < 21; ++i){
        if (n % i != 0) {
            return false;
        }
    }
    return true;
}

void main(){
    int smallest = 1;
    while (!divisible(smallest)) ++smallest;
    printf("%d\n", smallest);
}