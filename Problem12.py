letter = '''Dear <|Name|> ,
               You are selected!
               <|Date|>'''

print(letter.replace("<|Name|>", "Abdul").replace("<|Date|>", "12 July 2026"))