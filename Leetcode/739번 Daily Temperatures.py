def dailyTemperatures(self, T: List[int]) -> List[int]:
  stack = []
  day = [0] * len(T)

  for i, cur in enumerate(T):
    while stack and T[stack[-1]] < cur:
      x = stack.pop()
      day[x] = i - x
    stack.append(i)
  
  return day

    
    
