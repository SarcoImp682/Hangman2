# The following code is needed for us to check your answer, do not modify it, please.
students = json.loads(input())
Belov = students['Belov']
Smith = students['Smith']
Sarada = students['Sarada']

# Your code here. Work with the variables 'Belov', 'Smith', and 'Sarada'
all_classes = set(Belov)
all_classes.update(set(Smith))
all_classes.update(set(Sarada))
print(len(all_classes))
