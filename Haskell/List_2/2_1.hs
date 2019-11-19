
map' :: (a->b) -> [a] -> [b]
map' f [] = []
map' f xs = foldr (\y ys -> (f y): ys) [] xs

filter'             :: (a -> Bool) -> [a] -> [a]
filter' p []        = []
filter' p xs        = foldr (\x xs -> if p x then x:xs else xs ) [] xs