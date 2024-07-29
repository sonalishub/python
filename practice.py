char_list=input("enter any string: ")

my_list=list(char_list)
print(my_list)
if (len(char_list)>=3):
  first_char=my_list.pop(0)
  my_list.append(first_char)
  print(my_list)
  my_list.append("abc")
  print(my_list)
  my_list.insert(0,"xyb")
  print(my_list)
  string=''.join(my_list)
  print(f"this is the coded string {string}")
elif (len(char_list)<=2):
  my_list=list(char_list)
  my_list.reverse()
  print(my_list)   
  string=''.join(my_list)
  print(f"this is the coded string:{string}")  

  # decode 
print("the program will decode the string back to original")
decode_list=string
# print(decode_list)
# decode_list=list(decode_list)
print(decode_list)
if (len(decode_list)>=3):
    # print(decode_list[3:])
    sliced_string=decode_list[3:-3]
    print(f"this is removed string from the end {sliced_string}")
    final_list=list(sliced_string)
    print(final_list)
    save_pop=final_list.pop(-1)
    final_list.insert(0,save_pop)
    print(final_list)
    join_list=''.join(final_list)
    print(join_list)

  
elif (len(decode_list)<=2):
    my_list=list(decode_list)
    my_list.reverse()
    final_string=''.join(decode_list)
    print(final_string)
