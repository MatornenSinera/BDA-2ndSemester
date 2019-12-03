
import Data.Foldable
import Data.Monoid


data MyTree a = MyLeaf a | MyFilledNode a [MyTree a]
 deriving (Ord, Read, Show, Eq)


instance Functor MyTree where
 fmap f (MyLeaf a) = MyLeaf (f a)
 fmap f (MyFilledNode a xs) = MyFilledNode (f a) (fmap f <$> xs)


instance Foldable MyTree where
 foldr f z (MyLeaf x) = x `f` z
 foldr f z (MyFilledNode x ns) = foldr f z (x: concat (fmap toList ns))

countRoots                  :: Num a => MyTree a  -> a
countRoots (MyLeaf _) = 1
countRoots (MyFilledNode _ _) = 1

roseSize (MyLeaf _) = 1
roseSize (MyFilledNode a (t:ts)) = roseSize t + roseSize (MyFilledNode a ts)
roseSize (MyFilledNode a []) = 0

isElem :: (Eq a) => MyTree a ->  a -> Bool
isElem (MyLeaf x) y = x == y
isElem (MyFilledNode x []) y = x==y
isElem (MyFilledNode x (t:ts)) y
 | x == y = True
 | otherwise = isElem t y || isElem (MyFilledNode x ts) y

height (MyLeaf a) = 1
height (MyFilledNode x t) = 1 + maximum (map (height) t)
