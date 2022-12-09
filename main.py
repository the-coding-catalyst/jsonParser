from test import *
for test in testCases:
    string = json.dumps(test)
    isArray = string[0] == "["
    result = jsonParser(string, isArray)
    result = result[0] if isArray else result
    # To check whether giving correct results
    print(json.loads(string) == result)
    print("---------------------")
    print(json.loads(string))
    print("-------------------")
    print(result)