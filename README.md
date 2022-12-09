
How to run the code:
- Run main.py file, it will execute jsonParser.py file for all test cases in test.py.


A json can have following forms:
- Simple json object.
- Simple json array.
- Json array inside json array.
- Json object inside json object.
- Json array inside json object.
- Json object inside json array.


How code is working?
- The code is based on recursion. The logic is to find key and values in case of simple json object or value in case of simple json arrays. If we find any nesting, recursion will come into the picture.
- The code will first check whether current given string is json object or array.
- It will go further in string and search for key and values accordingly.
- Basicaly we are looking for ":" as a separator for key and values. 
- We have method for finding both key and value. The values can be simple values or any other json object or array.
- In case we find json array or object as values we will call our method again recursively.
- To find out what exactly needs to be called recursively, i have used stack.
- Values can be simple string, null, true, false, integer, decimal values etc. and it will be validated accordingly.


Limitation:
- The code works fine with complex nested json stings but it can fail when we have special characters as a value of a key. As i am using special charcters itselfs such as "{", "}", ":", "[" and "]" for parsing, it may not properly parse it when these are present inside values.
