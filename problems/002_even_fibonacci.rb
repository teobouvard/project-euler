# https://projecteuler.net/problem=2

limit = 4e6
sum = 0
a = 1
b = 2

while a < limit
  if a.even?
    sum += a
  end
  a, b = b, a + b
end

puts sum


