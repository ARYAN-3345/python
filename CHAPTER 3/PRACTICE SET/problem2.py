name = input("Enter your name ")
print(f"Dear {name}\nYou're selected!\n29th April 2025")


letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 

print(letter.replace("<|Name|>","Aryan Jaiswal").replace("<|Date|>","29th April 2050"))