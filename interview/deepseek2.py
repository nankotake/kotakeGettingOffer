# 说明下列代码返回结果
def decorator(func):
  def wrapper(*args, **kwargs):
    return f"[{func(*args, **kwargs)}]"
  return wrapper
  
@decorator
def greet(name):
  return f"Hello, {name}"

result = greet("Hello World")

print(result)

# 3. 现在有一个区间数组，每个区间之间不重叠，一行代码算出总长
arr = [(1,2),(3,4)]

segments = [(1,2), (3,4)]
print(sum(b-a for a,b in segments))  # 输出: 2



sum(b-a for a,b in (lambda s: [(s[0][0], max(y[1] for y in s if y[0]<=s[0][0]<=y[1] or y[0]<=s[-1][1]<=y[1]))] + [(y[0], max(z[1] for z in s if z[0]<=y[0]<=z[1] or z[0]<=y[1]<=z[1])) for y in s if y[0]>s[s.index(y)-1][1]] if s else [])(sorted(segments)))
from functools import reduce
sum(b-a for a,b in reduce(lambda r,x: r+[x] if not r or x[0]>r[-1][1] else r[:-1]+[(r[-1][0],max(r[-1][1],x[1]))], sorted(segments), []))
