import json

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def nextChar(string, idx):
    while idx < len(string):
        if string[idx] != " ":
            return idx, string[idx]
        idx += 1

def findKeyOrValue(string, index, forKey):
    result = ""
    count = 0
    idx = index
    if forKey:
        while count < 2 and index < len(string):
            if count == 1:
                result = string[index] + result if forKey else result + string[index]
            if string[index] == '"':
                count += 1
            index = index- 1 if forKey else index + 1
    else:
        while idx < len(string) and string[idx] not in ["[", "{", ":", ",", "]", "}"]:
            if string[idx] == " ":
                _, char = nextChar(string, idx)
                if char in ["[", "{", ":", ",", "]", "}"]:
                    break
            result += string[idx]
            idx += 1
        result += " "
    return result

def findNextIndex(string, idx):
    stack = [string[idx]]
    result = string[idx]
    idx += 1
    while stack and idx < len(string):
        result += string[idx]
        if string[idx] in ("[", "{"):
            stack.append(string[idx])
        if stack[-1] == "[" and string[idx] == "]":
            stack.pop()
        elif stack[-1] == "{" and string[idx] == "}":
            stack.pop()
        if len(stack) != 0:
            idx += 1
            
    return idx, result

def jsonParser(string, isArray):
#     print(string)
    if isArray:
        result = []
        idx = 0
        addingChars = False
        while idx < len(string):
#             print(string, idx)
            if string[idx] == "[":
                idx, newString = findNextIndex(string, idx)
#                 print(newString, idx)
                result.append(jsonParser(newString[1:-1], True))
            elif string[idx] == "{":
                idx, newString = findNextIndex(string, idx)
                result.append(jsonParser(newString[1:-1], False))
            else:
                if string[idx] == '"':
                    if addingChars is True:
                        result.append(temp)
                    addingChars = not addingChars
                    temp = ""
                    idx += 1
                    continue
                if addingChars is True:
                    temp += string[idx]
            idx += 1
        return result
                
    result, idx = {}, 0
    while idx < len(string):
        
        if string[idx] == ":":
            key = findKeyOrValue(string, idx, True)
            idx, char = nextChar(string, idx+1)
            if char not in ("[", "{"):
#                 print(key, string[idx+1]==" ")
                value = findKeyOrValue(string, idx, False)[:-1]
                if value.isdigit():
                    value = int(value)
                elif isfloat(value):
                    value = float(value)
                elif value == "true":
                    value = True
                elif value == "false":
                    value = False
                elif value == "null":
                    value = None
                else:
                    value = value[1:-1]
                result[key[1:]] = value
            elif char == "{":
                idx, newString = findNextIndex(string, idx)
                tempRes = jsonParser(newString[1:-1], False)
                result[key[1:]] = tempRes
            else:
                idx, newString = findNextIndex(string, idx)
                result[key[1:]] = jsonParser(newString[1:-1], True)
        idx += 1
    return result
