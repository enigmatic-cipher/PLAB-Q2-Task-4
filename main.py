"""
Given a string as input. Print patterns according to following set of test cases.
Input-> "trisect"
Output->
t 
t# 
t#i 
t#i# 
t#i#e 
t#i#e# 
t#i#e#t
"""

st = "trisect"
ln = len(st)
st_1 = ""
for i in range(0,ln):
  ch = st[i]
  if (i%2==0):
    st_1 = st_1 + ch
  else:
    st_1 = st_1 + "#"
print(st)
  