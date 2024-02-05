#!/usr/bin/python3
MyClass = __import__('8-my_class').MyClass
#class_to_json = __import__('8-class_to_json').class_to_json
to_json_string = __import__('3-to_json_string').to_json_string

m = MyClass("John")
m.number = 89
print(type(m))
print(m)

n = {1,2}
print(type(n))
print(n)
mj = to_json_string(n.__dict__)
print(type(mj))
print(mj)
