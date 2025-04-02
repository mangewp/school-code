import pickle

pb = {"mom": "555-1234", "dad": "555-5678"}
print (pb)
print (pb["mom"])

for key in pb:
    print(key)
    
for key in pb:
    print(key, pb[key])

outputFile = open("phonebook.dat", "wb")
pickle.dump(pb, outputFile)
outputFile.close

inputFile = open("phonebook.dat", "rb")
pb = pickle.load(inputFile)
inputFile.close()
print(pb)