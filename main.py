def main():
  book_path = ("books/frankenstein.txt")
  book_text = get_book(book_path)
  num_words = get_num_words(book_text)
  char_dict = count_letters(book_text)
  chars_sorted_list = convert_dict(char_dict)

  # PRINT REPORT
  print(f"--- Begin report of ${book_path} ---")
  print(f"{num_words} words found in the document")
  print()

  for char in chars_sorted_list:
    print(f"The {char['char']} character was found {char['num']} times")
  
  print("--- End report ---")

def get_book(path):
  with open(path) as b:
    return b.read()

def get_num_words(book):
  words = book.split()
  return len(words)

def count_letters(text):
  chars = {}
  for i in text:
    lowered = i.lower()
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1
  return chars

def sort_on(x):
  return x["num"]

def convert_dict(dict):
  char_list = []
  for i in dict:
    if i.isalpha():
      char_list.append({"char": i, "num": dict[i]})
  char_list.sort(reverse=True, key=sort_on)
  return char_list

main()