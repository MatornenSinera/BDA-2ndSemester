func :: Eq a => [a] -> [[a]]
func = foldr f []
  where f x []        = [[x]]
        f x (b@(b1:_):bs)
          | x == b1    = (x:b):bs
          | otherwise = [x]:b:bs

