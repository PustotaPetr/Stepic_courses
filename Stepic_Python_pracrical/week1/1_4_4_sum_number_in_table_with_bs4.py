# В файле https://stepik.org/media/attachments/lesson/209723/3.html находится
# одна таблица. Просуммируйте все числа в ней и введите в качестве ответа
# одно число - эту сумму. Для доступа к ячейкам используйте возможности
# BeautifulSoup.

from urllib.request import urlopen
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/209723/5.html')  # скачиваем файл
html = resp.read().decode('utf8')  # считываем содержимое
soup = BeautifulSoup(html, 'html.parser')  # делаем суп

s = 0
for td in soup.find_all('td'):
    s += int(td.get_text())

print('Кол-во элементов', len(soup.find_all('td')))
print('Сумма элементов', str(s))
