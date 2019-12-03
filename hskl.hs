list n  = [1 .. n]
factorial n = foldl (*) 1 [1..n]
approximation = foldl(\x y -> x+(1/(factorial y))) 1
main = print $ (approximation (list 200))