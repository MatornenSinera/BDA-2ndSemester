
square list = squarehammer list 0
squarehammer [] a = a
squarehammer xs a = foldr (\y ys -> if y `mod` 2 == 0 then (+ y*y) ys else (+0) ys) a xs

-- For every element from list xs, we check if element y is even. If so - we add y*y to parameter a.

