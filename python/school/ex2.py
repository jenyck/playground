#!/usr/bin/env python3
##В племени Кенгуру имена детям издавна дают по строгим правилам. В имени
##кенгурёнка обязательно должен присутствовать первый слог имени мамы и первый
##слог имени папы, причём мамин слог должен быть раньше папиного. При этом
##девочкам дают имена, заканчивающиеся на “a” или “i”, а мальчикам — на “e”,
##“o” или “u”. Других гласных в языке Кенгуру нет, а слог - это пара из
##согласной буквы латиницы и одной из гласных.
##
##Однажды под Пальмой Совета обнаружили маленькую девочку. Имён родителей она
##не знала, но своё имя помнила: katerina. Список всех взрослых кенгурийцев
##содержится в текстовом файле (по одному имени в строке). Определите, сколько
##существует возможных пар "подходящих" для "Катерины" родителей.
##
##Например, если в файле имена
##seketu
##tego
##malina
##kabota
##nakuku
##возможны 2 пары родителей: kabota - tego и kabota - nakuku
##
##Сколько пар подходящих родителей для katerina можно подобрать из этого файла?

child = 'katerina'
with open('names.txt', 'r') as file1:
    lines = [line.rstrip() for line in file1]

male = []
female = []
for line in lines:
    if line[-1] in {'a', 'i'}:
        female.append(line)
    else:
        male.append(line)

for mum in female:
    if mum[0:2] in child:
        for pa in male:
            if pa[0:2] in child[child.find(mum[0:2]):]:
                print(mum, '-', pa)
