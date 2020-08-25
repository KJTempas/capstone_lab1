
classes = []

class_name = input('Type the name of the class. Press Enter to quit.  ')

while class_name: #means something was entered; empty strings are False
    classes.append(class_name.title()) #make it title case and add to the classes list
    class_name = input('Type the name of the class. Press Enter to quit.  ')

print('The classes you are taking are:')
print(classes)
for c in classes:
   print(c)
# alternate method - will give numbers along with data 
for index, c in enumerate(classes):
    print(f'{index+1} {c}')