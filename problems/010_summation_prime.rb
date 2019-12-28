require 'prime'

LIMIT = 2e6
sum = 0
Prime.each(ubound=LIMIT) do |prime|
    sum += prime
end

puts sum