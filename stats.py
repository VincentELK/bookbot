def get_number_of_words(text):
     return len(text.split())

def num_of_char(text):
     char = {}
     for letter in text:
          low_letter = letter.lower() #get every char in low
          if low_letter in char:
               char[low_letter] += 1
          else:
               char[low_letter] = 1
           
     return char
def stats_num(stats):
     return stats["num"]

def sort_dictionary(dic_char):
     stat_list = []
     for key in dic_char:
          if key.isalpha():
               stat_char = {"char":key, "num": dic_char[key]}
               stat_list.append(stat_char)
     stat_list.sort(reverse=True, key=stats_num)
     return stat_list
