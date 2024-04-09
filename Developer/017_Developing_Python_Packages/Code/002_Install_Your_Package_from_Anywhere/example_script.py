import impyrial

result = impyrial.length.convert_unit(10, 'in', 'yd')
print(result)
result = impyrial.weight.convert_unit(2, 'lb', 'oz')
print(result)

impyrial.weight.hello()