string = input('Enter a string: \n')
charecter = input('Enter target character: \n')
result = ''

for index in string:
    if(index != charecter):
        result = result + index
print('Output: ', result)