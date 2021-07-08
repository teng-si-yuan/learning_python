def fibonacci_sequence(count):
      x = 0
      y = 1
      i = 2
      a = []
      a.append(x)
      a.append(y)
      while i < count:
            z = x + y
            x = y
            y = z
            i = i + 1
            a.append(y)
      if count == 0:
            return([])
      if count == 1:
            return([0])
      return(a)
print(fibonacci_sequence(10))
