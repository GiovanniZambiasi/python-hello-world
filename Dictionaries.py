myDictionary = {"Key1":"Value1", "Key2":"Value2"}   # Key/value pairs specified with notation Key:Value
print(myDictionary)
print(myDictionary["Key1"])

d = {"K1":123, "K2":[0,1,2], "K3":{"Key":1}}    # Dictionaries can hold various types

print(d.keys())     # Returns a list of all keys
print(d.values())   # Returns a list of all values
print(d.items())    # Returns a list of key,value tuples