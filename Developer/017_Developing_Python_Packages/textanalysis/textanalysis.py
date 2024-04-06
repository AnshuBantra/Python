def count_words(filepath, words_list):
  # Open the text file
  with open(filepath) as file:
    text = file.read()

  wrd_count = []

  lst = text.lower().split()
  for _ in words_list:
    wrd_count.append((_, lst.count(_)))
  return wrd_count