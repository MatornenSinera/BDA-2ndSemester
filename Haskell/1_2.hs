revs l =  rev l []
  where
    rev []     a = a
    rev (x:xs) a = rev xs (x:a)


