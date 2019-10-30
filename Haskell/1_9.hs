sublists :: [a] -> [[a]]
sublists [] = [[]]
sublists (x:xs) = [x:sublist | sublist <- sublists xs] ++ sublists xs