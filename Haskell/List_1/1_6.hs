ecd myList = eliminateDups myList
 where
  eliminateDups []		= []
  eliminateDups [x] 	   = [x]
  eliminateDups (x:xx:xs) 
   | x == xx = eliminateDups (x:xs) 
   | otherwise = x : eliminateDups (xx:xs)

