data = open('data.txt', 'r').readlines()
intData = [int(val) for val in data]
#print(sum(intData)) 
value = 0
listWithAddedValues = []
#sum items in a list until a duplicate value occurs
for i in intData: 
    value += i
    listWithAddedValues.append(value)
    #print(listWithAddedValues)
def find_duplicates(listWithAddedValues):
    n = len(listWithAddedValues)
    for i in range(n):
        for j in range(i+1, n): 
            if(listWithAddedValues[i] == listWithAddedValues[j]):
                print('This is the value: ' , listWithAddedValues[i]) 
                return listWithAddedValues[i]
            else: 
                print('you suck ')



























#listWithPositiveValues = [] 
#listWithNegativeValues = []
#for num, val in enumerate(data, start=1):
#    if(val.__contains__('+')): 
#       listWithPositiveValues.append(val)
#    else: 
#       listWithNegativeValues.append(val)
#listWithPositiveValues = [int(i) for i in listWithPositiveValues] 
#listWithNegativeValues = [int(i) for i in listWithNegativeValues] 
#print(sum(listWithPositiveValues + listWithNegativeValues)) 

#for num, val in enumerate(data, start=1):
#   if(val.__contains__('+')):
#      listWithPositiveValues = [].append(float(val))
#     print(listWithPositiveValues)
#else:
#   listWithNegativeValues = [].append(float(val)) 