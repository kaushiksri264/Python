# Dictonary - Data is stored in form of pairs(Key Value Pairs) - mutable and duplicate keys not allowed
info = {
    "key" : "value",
    "name" : "Sri",
    "learning" : "coding",
    "age" : 25,
    "is_adult" : True,
    "marks" : [94.5,97.9,10.0,98],
    "grades" : ("A","A","A","A"),
    "courses" : {
        "py" : False,
        "java" :  True,
        "Ts" : True

    }
}
# print(type(info))
# print(info["name"])
# print(info["courses"]["java"])
# print(info.keys())
# print(list(info.keys()))
# print(list(info.values()))
# print(info.items())
# print(info.get("courses"))
# print(info.update({"CGPA" : 97}))
# print(info)
info["courses"].update({"js" : True})
print(info)