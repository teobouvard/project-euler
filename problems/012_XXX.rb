require 'prime'

n_divisors = 0
triangle_number = 2e163
counter = 0

while n_divisors < 500
    counter += 1
    triangle_number += counter
    factors = Prime.prime_division(triangle_number)
    n_divisors = factors.map{|e| e[1]+1}.reduce(:+).to_i
    puts n_divisors
end

puts triangle_number