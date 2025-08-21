def alter(s):
  r = ""
  while len(s) > 1:
    r = r + s[1] + s[0]
    s = s[2:]
  return r+s

def scramble_word(s):
  if len(s) >= 2:
    return (s[0] + alter(s[1:-1]) + s[-1])
  else:
    return s

def scramble_text(s):
  r = []
  for w in s.split():
    r.append(scramble_word(w))
  return " ".join(r)

unscramble_text = scramble_text
