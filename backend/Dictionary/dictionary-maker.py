# читаем файл в список
def read2list(file):
    # открываем файл в режиме чтения utf-8
    file = open(file, 'r', encoding='utf-8')

    # читаем все строки и удаляем переводы строк
    lines = file.readlines()
    lines = [line.rstrip('\n') for line in lines]

    file.close()

    return lines 

# читаем файл функцией read2list
lines = read2list('10000.txt')

# создаём список из популярных пятибуквенных слов
five_symb_popular = []
for line in lines:
         if len(line) == 5:
                five_symb_popular.append(line)

print("из 10 000 самых популярных слов", len(five_symb_popular), "пятибуквенных") 
                
# удаляем дубли, если такие есть
for line in five_symb_popular:
         if five_symb_popular.count(line) > 1:
                five_symb_popular.remove(line);
                print("нашли дубль слова", line, "удаляем")

print("после удаления дублей в списке", len(five_symb_popular), "слов")                
                               

# читаем файл функцией read2list
lines = read2list('russian_nouns.txt')

# делаем список пятибуквенных существительных
five_symb_nouns = []
for line in lines:
         if len(line) == 5:
                five_symb_nouns.append(line)

print("в списке всех существительных", len(five_symb_nouns), "пятибуквенных")

# удаляем дубли, если есть
for line in five_symb_nouns:
         if five_symb_nouns.count(line) > 1:
                five_symb_nouns.remove(line);
                print("нашли дубль слова", line, "удаляем")

print("после удаления дублей в списке", len(five_symb_nouns), "существительных из 5 букв")

# сохраняем список в файл
saved_file = open("All_words.txt", "w")
for line in five_symb_nouns_popular:
    saved_file.write('%s\n' %line)
saved_file.close()

# создаём список популярнвх пятибуквенных слов, которые являются существительными
five_symb_nouns_popular = []
for line in five_symb_popular:
         if line in five_symb_nouns:
                five_symb_nouns_popular.append(line)

print("в топ 10 000 попало", len(five_symb_nouns_popular), "пятибуквенных существительных")

saved_file = open("Secret_words.txt", "w")
for line in five_symb_nouns_popular:
    saved_file.write('%s\n' %line)
saved_file.close()