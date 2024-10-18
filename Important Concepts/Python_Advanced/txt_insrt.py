def chars_between(start: str, end: str, idx: int) -> str:
  start_ord, end_ord = ord(start), ord(end)
  add = 1 if start_ord <= end_ord else -1
  lst = map(chr, range(start_ord+add, end_ord, add))
  lst = [start]+[*lst]+[end] if idx==0 else [*lst]+[end]
  return ''.join(lst)

# print(chars_between('h', 'a', 1))

words = ['be', 'hat', 'tree', 'house', 'planet', 'freedom', 'elephant', 'discovery', 'magnificent']
new_words = []
for word in words:
  string = ''
  for idx in range(word_len:=len(word)):
    if idx < word_len-1:
      string += chars_between(word[idx], word[idx+1], idx)
    else: break
      
  new_words.append(string)

for idx in range(len(words)):
  print(words[idx], new_words[idx])