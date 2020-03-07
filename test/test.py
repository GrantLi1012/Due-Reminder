import json
import os

person = {"name": "Boo",
"languages": ["English", "Fench"],
"married": True,
"age": 33
}


with open('example.txt', 'rb+') as outfile:
    outfile.seek(-1, os.SEEK_END)
    outfile.truncate()
    outfile.close()

with open('example.txt', 'a+') as outfile1:
    outfile1.write(",\n")
    outfile1.write(json.dumps(person))
    outfile1.write("]")
    outfile1.close()

with open('example.txt') as outfile2:
    data = json.load(outfile2)
    print(data[0]["name"])
    outfile1.close()



