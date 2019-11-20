calculatePrimes list = (length $ filter (isPrime) list)

isPrime n = if f n == 2 then True else False
     where f n = foldl (\count x -> if n `mod` x == 0 then count + 1 else count) 0 [1..n]

-- calculatePrimes substitutes every number from the list into a binary value, depending on whether the number is prime
-- isPrime checks if for every x, amount of divisors from 1 to x is equal to 2. 
-- borderline examples (0, 1) are not included when checked for with function isPrime