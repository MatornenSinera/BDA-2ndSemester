sumOfFactInv' num sil sum counter
    | num == counter = sum
    | otherwise = sumOfFactInv' num (sil*counter) (sum+1/sil) (counter+1)

sumOfFact num
 | num==0 = 1
 | otherwise = sumOfFactInv' num 1 0 1

 -- sumOfFactInv' stores three variables -
 -- Sil - which keeps current value of factorial
 -- Sum - which adds everytime inverted value of sil
 -- Coutner - which keeps track of everystep of the way.
 -- Program achives high values of approximation within small time margin.
