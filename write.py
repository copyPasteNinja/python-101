

# my_file = open("script.py", "a")
# my_file.write("""
# Well Well Well :)
# Isn't this a purprise?
# """)

# my_file.close()

# my_file = open("script.py")
# print(my_file.read())


# String you want to replace
search_text = "surprise"
  
# string you want to replace with
replace_text = "replaced"
  
with open('script.py', 'r') as my_file:
  
    data = my_file.read()
    data = data.replace(search_text, replace_text)
    print(data)

with open('script.py', 'w') as file:
    file.write(data)
  
print("Text replaced")