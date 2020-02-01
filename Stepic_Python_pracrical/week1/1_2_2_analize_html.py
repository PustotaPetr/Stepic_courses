# Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит статью
# с Википедии про язык Python. В этой статье есть теги code, которыми
# выделяются конструкции на языке Python. Вам нужно найти все строки,
# содержащиеся между тегами <code> и </code> и найти те строки, которые
# встречаются чаще всего и вывести их в алфавитном порядке, разделяя пробелами.


from urllib.request import urlopen
import re
from collections import Counter


html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").\
    read().decode('utf-8')

pattern = '<code>(.*?)</code>'
code_list = Counter(re.findall(pattern, html))

print(len(code_list))
print(code_list.most_common())
print(*[x[0] for x in list(filter(lambda y: y[1] ==
        code_list.most_common(1)[0][1], code_list.most_common()))])
