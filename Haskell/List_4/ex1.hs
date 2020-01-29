import Control.Monad
import Data.Set

type A = Int
type B = Int

move :: Int -> Int -> Maybe Int
move a b
 | a+b > 2 = Nothing 
 | a+b < -2 = Nothing
 | otherwise = Just (a+b)

move_list ::  Int -> [Int]-> Maybe Int
move_list a xs = foldM move a xs 


