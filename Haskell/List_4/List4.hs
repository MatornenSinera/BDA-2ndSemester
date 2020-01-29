import Control.Monad
import Data.Set 

-- Ex 1
f x = [x+1, x+2]

g x = [2*x, 3*x]

-- Task 1
type Move = Int
type Pos = Int

move :: Move -> Pos -> Maybe Pos
move move pos 
    | abs(pos+move) < 3 = Just (pos+move)
    | otherwise = Nothing

move_list :: [Move] -> Pos -> Maybe Pos
move_list xs pos = foldM move pos xs

-- Task 2
dice_outcomes = [1..6] >>= \k6 -> [1..20] >>= \k20 -> return (k6, k20)

dice_outcomes2 :: [(Int,Int)]  
dice_outcomes2 = do  
    k6 <- [1..6]  
    k20 <- [1..20]  
    return (k6,k20) 

-- Task 3
type Position = (Int, Int)
type Board = (Int, Int)

move_knight :: Board -> Position -> [Position]
move_knight (n,k) (x,y) = do
    (x',y') <- [(x+1,y+2),(x+2,y+1),(x+1,y-2),(x-2,y+1),(x-1,y+2),(x+2,y-1),(x-1,y-2),(x-2,y-1)]
    guard (x' `elem` [1..n] && y' `elem` [1..k])
    return (x',y')

mkUniq :: Ord a => [a] -> [a]
mkUniq = toList . fromList

move_n_times :: Board -> Position -> Int -> [Position]
move_n_times board pos n = mkUniq (foldM (\a _ -> move_knight board a) pos [1..n])