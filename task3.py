list_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JZ', 10: 'QZ'}
list_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
text = input().upper()
if list_ru is text:
    print(sum([k for i in text for k, v in list_ru.items() if i in v]))
else:
    print(sum([k for i in text for k, v in list_en.items() if i in v]))
