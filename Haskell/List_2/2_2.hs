
areyouonthesquare list = squarehammer list 0
squarehammer [] a = a
squarehammer xs a = foldr (\y ys -> if y `mod` 2 == 0 then (+ y*y) ys else (+0) ys) a xs


