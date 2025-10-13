import pickle

d = {"stu1": {"Name": "John", "Age": "21", "ID": 28 },
    "stu2": {"Name": "Jenny", "Age": "22", "ID": 23 },

     }

with open("myUsers.dat", "wb") as file1:
    pickle.dump(d, file1)
file1.close()

with open("myUsers.dat", "rb") as file2:
    myDictionary = pickle.load(file2)

print(myDictionary["stu1"]["Name"])

i = 1
for x in myDictionary:
    var = "stu"+str(i)
    print(myDictionary[var]["Name"])
    i += 1