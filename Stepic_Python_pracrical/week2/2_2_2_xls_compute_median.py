import xlrd
import statistics
rb = xlrd.open_workbook('salaries.xlsx')
sheet = rb.sheet_by_index(0)
fm = []
for rownum in range(1, sheet.nrows):
    row = sheet.row_values(rownum)
    fm.append((row[0], statistics.median(row[1:])))
#    print(row)
#    print(statistics.median(row[1:]))
#    for c_el in row:
#        print(c_el)
print(sorted(fm, key=lambda x: x[1], reverse=True)[0][0], end=' ')

fm = []
for colnum in range(1, sheet.ncols):
    col = sheet.col_values(colnum)
    fm.append((col[0], statistics.mean(col[1:])))


print(sorted(fm, key=lambda x: x[1], reverse=True)[0][0])
