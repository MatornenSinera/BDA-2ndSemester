euler 1 = 1
euler a = length $ filter (coprime a) [1..a-1]
 where coprime a b = gcd a b == 1

divisors l = [n | n <-[1..(l)], l `rem` n == 0]
eulist l = [euler i | i <- divisors l]
eulistsum l = sum (eulist l)

