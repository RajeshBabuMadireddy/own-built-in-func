n=int(input("enter ur first num:"))
x=int(input("enter ur second num:"))
class Own:
    def func(self,n,x):
        
        if n==0 and x==0:
            return n*x
        elif n==0 and x>=1:
            return n*x
        elif n>=1 and x>=1:
            return n**x    
        elif n<=-1 and x%2==0:
            return n**x
        elif n<=-1 and x%2!=0:
            return -n**x
res=Own()
print(res.func(n,x))                         


