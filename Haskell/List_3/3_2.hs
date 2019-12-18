
import Data.Foldable
import Data.Monoid


data MyTree a = MyLeaf a | MyFilledNode a [MyTree a]
 deriving (Ord, Read, Show, Eq)

instance Functor MyTree where
 fmap f (MyLeaf a) = MyLeaf (f a)
 fmap f (MyFilledNode a xs) = MyFilledNode (f a) (fmap f <$> xs)
 -- FMAP - Function applied for every element of a tree. 

countRoots                  :: Num a => MyTree a  -> a
countRoots (MyLeaf _) = 1
countRoots (MyFilledNode _ _) = 1
-- Previous Version - where there is only one root for entire tree.


leavesCount (MyLeaf _) = 1
leavesCount (MyFilledNode a (t:ts)) = leavesCount t + leavesCount (MyFilledNode a ts)
leavesCount (MyFilledNode a []) = 0

-- Counting Leaves - every leaf is assigned a "1", every node - "0"

rootsCount2 (MyLeaf _) = 0
rootsCount2 (MyFilledNode a (t:ts)) = rootsCount2 t + rootsCount2 (MyFilledNode a ts)
rootsCount2 (MyFilledNode a []) = 1

-- Counting Not Leaves - every leaf is assigned a "0", every node - "1"

myTreeFoldList :: (a -> b -> b) -> b -> [MyTree a] -> b
myTreeFoldList f z (x:[]) = foldMyTree f z x
myTreeFoldList f z [] = z
myTreeFoldList f z xs = myTreeFoldList f (foldMyTree f z (last xs)) (init xs)


foldMyTree :: (a -> b -> b) -> b -> MyTree a -> b
foldMyTree f z (MyLeaf a) = f a z
foldMyTree f z (MyFilledNode x xs) = foldMech
    where
        foldMech = myTreeFoldList f rightmostEl (init xs)
        rightmostEl = f x (foldMyTree f z (last xs))

--Folding RoseTree - for a leaf we apply function to the value
--For branch - using additional funcion that folds lists - firstly to the rightmost element of lowest possible level, then going up one level.
--Upon applying function to higher instance, we apply same function to every possible lower branch/leaf - from right to left (last element of the remaining things inside a [MyTreeList]) 


isElem :: (Eq a) => MyTree a ->  a -> Bool
isElem (MyLeaf x) y = x == y
isElem (MyFilledNode x []) y = x==y
isElem (MyFilledNode x (t:ts)) y
 | x == y = True
 | otherwise = isElem t y || isElem (MyFilledNode x ts) y

--For every element inside a tree, we check is x==y. If yes - we don't really care about the rest, so outcome will be true. 

height (MyLeaf a) = 1
height (MyFilledNode x t) = 1 + maximum (map (height) t)
--Every element gets assigned a 1, with added maximum of height function mapped upon remaining branches.