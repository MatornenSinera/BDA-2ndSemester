mutacja [] =[[]]
mutacja lista = [a:x | a<-lista, x<-(mutacja $ filter (\x -> x/=a) lista)]


