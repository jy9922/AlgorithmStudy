def removeDuplicateLetters(s):
    for char in set(s):
      suffix = s[s.index(char):]
      if set(s) == set(suffix):
        return char + removeDuplicateLetters(suffix.replace(char, ''))
    return ''


def removeDuplicateLetters2(s):
  counter, seen, stack = collections.Counter(s), set(), []

  for char in s:
    counter[char] -= 1
    if char in seen:
      continue

    while stack and char < stack[-1] and counter[stack[-1]] > 0:
      seen.remove(stack.pop())
      
    stack.append(char)
    seen.add(char)

  return ''.join(stack)
