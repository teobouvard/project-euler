#include <stdio.h>
#include <math.h>

unsigned int count_divisors(unsigned long n){
    unsigned int n_divisors = 0;
    for (unsigned long i = 1; i <= n; i++) {
        if (n % i == 0){
            int k = 0;
            n_divisors++;
        }
    }
    return n_divisors;
}

void main(){
    unsigned long triangle_number = 0;
    unsigned long counter = 0;
    unsigned int n_divisors = 0;
    while (n_divisors < 500) {
        counter++;
        triangle_number += counter;
        n_divisors = count_divisors(triangle_number);
        //printf("%lu\n", triangle_number);
    }
    printf("%lu\n", triangle_number);
}