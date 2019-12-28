#include <iostream>
#include <vector>

using namespace std;

int next_prime(vector<int> previous_primes){
    int candidate = previous_primes.back() + 2;
    bool prime_found = false;
    while (!prime_found){
        prime_found = true;
        for (int i : previous_primes){
            if (candidate % i == 0){
                prime_found = false;
                candidate += 2;
                break;
            }
        }
    }
    return candidate;
}

int main(){
    int LIMIT = 2e6;
    vector<int> primes = {2, 3};
    int biggest_prime = primes.back();
    long sum = 5;
    while (biggest_prime < LIMIT){
        biggest_prime = next_prime(primes);
        if (biggest_prime < LIMIT){
            primes.push_back(biggest_prime);
            sum += biggest_prime;
        }
    }
    cout << sum << endl;
    return 0;
}