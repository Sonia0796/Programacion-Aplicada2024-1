#diccionarios
thisdict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)


thisdict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict["brand"])

thisdict = {
    "brand ": "ford",
    "model" : "Mustang ",
    "year" : 1964,
    "year" : 2020
}
print(thisdict)

print(len(thisdict))

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year":1964,
    "colors":["red", "While", "blue"]
}

thisdict = dict( name = "John", age = 36, country = "Norway")
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year":1964

}
x = thisdict["model"]
print(x)

y= thisdict.get("model")
print(y)

z=thisdict.keys()
print(z)

car = {
    "brand": "Ford",
    "model":"Mustang",
    "year":1964
}

x = car.keys()
print(x)

car["color"] = "white"
print(x)

x=thisdict.values()
print(x)

car = {
    "brand" : "Ford",
    "model" : "mustang",
    "year":1964
}

x = car.values()
print(x)

car["year"] = 2020
print(x)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}

x = car.values()
print(x)

car["color"] = "red"
print(x)

x = thisdict.items()
print(x)

car = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()
print (x)

car["year"] = 2020
print(x)

car = {
    "brand": "ford",
    "model": "mustang",
    "year" : 1964
}

x = car.items()
print(x)

car["color"] = "red"
print(x)

thisdict = {
    "brand": "Ford",
    "model" : "Mustang",
    "year": 1964
}

if "model" in thisdict:
    print("yes, model is the keys in the thisdict dictionary")


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "motor": "",
    "year": 1964
}

thisdict["year"] = 2018
print(thisdict)