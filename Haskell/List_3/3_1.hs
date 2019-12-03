module Main where


data MyTree a = MyLeaf a | MyFilledNode  (MyTree a) a (MyTree a)
 deriving (Ord, Read, Show, Eq)



main :: IO ()
main  =
   do
      putStrLn "Begin program"
 
      let aMyTree = MyFilledNode  (MyFilledNode  (MyLeaf 1) 3 (MyLeaf 1)) 5 (MyFilledNode (MyLeaf 1) 2 (MyLeaf 1))
      print aMyTree
      print (sumMyTree aMyTree)
 
      let bMyTree = MyFilledNode  (MyFilledNode (MyLeaf "b") "s" (MyLeaf "b")) "r" (MyFilledNode (MyLeaf "b") "a" (MyLeaf "b"))
      print bMyTree
 
      putStrLn "End program"


sumMyTree                       :: Num a => MyTree a  -> a
sumMyTree (MyLeaf a)         = a
sumMyTree (MyFilledNode t1 n t2) = n + sumMyTree t1 + sumMyTree t2

fold :: (a -> a -> a) -> MyTree a -> a
fold f (MyLeaf n) = n
fold f (MyFilledNode l n r) = f n m 
 where
  m = f (fold f r) (fold f l)

countRoots                  :: Num a => MyTree a  -> a
countRoots (MyLeaf _) = 1
countRoots (MyFilledNode x _ y) = 1


countLeaves               :: Num a => MyTree a  -> a
countLeaves   (MyLeaf _) = 1
countLeaves   (MyFilledNode x _ y) = 0 + countLeaves x + countLeaves y

isElem :: (Eq a) => MyTree a ->  a -> Bool
isElem (MyLeaf x) y = x == y
isElem (MyFilledNode l n r) y
 | n == y = True
 | otherwise = isElem l y || isElem r y

height (MyLeaf a) = 1
height (MyFilledNode l n r) = 1 + (max (height (l)) (height (r)))