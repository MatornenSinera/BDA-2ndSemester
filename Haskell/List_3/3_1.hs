
data MyTree a = MyLeaf a | MyFilledNode  (MyTree a) a (MyTree a)
 deriving (Ord, Read, Show, Eq)



sumMyTree                       :: Num a => MyTree a  -> a
sumMyTree (MyLeaf a)         = a
sumMyTree (MyFilledNode t1 n t2) = n + sumMyTree t1 + sumMyTree t2
 -- Sum - Function applied for every element of a tree. 


fold :: (a -> a -> a) -> MyTree a -> a
fold f (MyLeaf n) = n
fold f (MyFilledNode l n r) = f n m 
 where
  m = f (fold f r) (fold f l)
-- Binary Fold - Do everything on the right leg of a branch, then left, then go back for a level above.

countRoots                  :: Num a => MyTree a  -> a
countRoots    (MyLeaf _) = 0
countRoots    (MyFilledNode x _ y) = 1 + countRoots x + countRoots y

-- Counting Not Leaves - every leaf is assigned a "0", every node - "1"

countLeaves               :: Num a => MyTree a  -> a
countLeaves   (MyLeaf _) = 1
countLeaves   (MyFilledNode x _ y) = 0 + countLeaves x + countLeaves y

-- Counting Leaves - every leaf is assigned a "1", every node - "0"

isElem :: (Eq a) => MyTree a ->  a -> Bool
isElem (MyLeaf x) y = x == y
isElem (MyFilledNode l n r) y
 | n == y = True
 | otherwise = isElem l y || isElem r y
--For every element inside a tree, we check is x==y. If yes - we don't really care about the rest, so outcome will be true. 

height (MyLeaf a) = 1
height (MyFilledNode l n r) = 1 + (max (height (l)) (height (r)))
--Every element gets assigned a 1, with added maximum of height function mapped upon remaining branches.