# https://projecteuler.net/problem=3

require 'prime'

factorization = Prime.prime_division(600851475143)

puts factorization.last.first


