func :: Eq a => [a] -> [[a]]
func = foldr f []
  where f x []        = [[x]]
        f x (b@(b1:_):bs)
          | x == b1    = (x:b):bs
          | otherwise = [x]:b:bs

count myList = [ (head i, length $ i) | i<- func myList]

func2 :: (a, Int) -> [a]
func2 (a, b) = take b (repeat a)

countReversed myList = concat [func2 i | i<- myList] 



