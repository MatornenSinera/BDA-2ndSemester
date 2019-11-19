{-# LANGUAGE FlexibleContexts #-}
prime list = modest list [] 0
 where
  modest [] ys a = a
  modest xs ys a = foldr (\z zs -> if divis z == 1 then (+ 1) ys else ( +0 ) ys) a xs 

divis s = diiv s sqrt' . s [0]
 where
 diiv s 0 [x] = x  
 diiv s d xs
  | s `mod` d == 0 = diiv s d-1 [xs+1]
  | otherwise = diiv s d-1 [xs]

sqrt' s = floor . sqrt . s