
map' :: (a->b) -> [a] -> [b]
map' f [] = []
map' f xs = foldr (\y ys -> (f y): ys) [] xs

filter'             :: (a -> Bool) -> [a] -> [a]
filter' p []        = []
filter' p xs        = foldr (\x xs -> if p x then x:xs else xs ) [] xs

-- Implementation of Map' and Filter' functions:
-- Map'
-- For every element from xs, lambda function applies function f, and appends it to empty array
-- Filter'
-- For every element from xs, lambda function checks if it returns true when checked with expression p (i.e. - <2)
-- Sufficient results are appended to empty array.