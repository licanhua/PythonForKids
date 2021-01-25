# Python For Kids
My son is 10 years old, and I want to assign some projects for him to start learn Python.

# Project 1: vs code IDE setup
Time allocation: 2 days
## Preparation
My son knows how to play Roblox on Windows, but never touch IDE like vs code. So I spent two minutes to show him below links, opened vs code in my laptop, then write a Helloworld python file and run the .py to let him know what's the expectation.

## Tasks
1. Download and install [vs code](https://code.visualstudio.com/)
2. Install [Python and the Python extension](https://code.visualstudio.com/docs/languages/python#_install-python-and-the-python-extension) 
3. Finish parts of [Python-tutorial](https://code.visualstudio.com/docs/python/python-tutorial) until `Configure and run the debugger`, and stop at `Install and use packages`

![Python-tutorial scope](img/PythonTutorial.jpg?raw=true "Title")

Skip things like `Data Science`, `Windows Subsystem for Linux`, `Anaconda`

4. Make a video to install vs code, python extension and create `Hello World` python file, then run it.

## Video to install vscode, python and python extension

[IDE setup video](https://www.youtube.com/watch?v=P9VmSIIO-Xc)

[My son's video](https://www.youtube.com/watch?v=_NtuZ2VwQFs)

# Project 2: Response to `input`
## Preparation
```
for i in range(1, 5):
    guessNum = input ("Please enter number :")
    if (guessNum == "5" ):
        print("Bingle!!!")
    else:
        print("wrong guess number: " + guessNum)
```

## Tasks
1. run above code in python
- enter 1, 3, 5, 10 and check the output
- what's `input` here used for

2. Based on above code, change the `guessNum` logic to:
```
    if input is 1, print "Monday"
    if input is 2, print "Tuesday"
    ...
    if input is 7, print "Sunday"
    otherwise print "I don't know"
```

# Project 3: function
## Preparation
In Python a function is defined using the def keyword.
For example:
```
def echo(message):
  print(message)

echo("I'm happy")
echo("I have " + str(100) + "$")

def guessNumber(num):
    print("Please guess number " + str(num))

guessNumber(1)
guessNumber(2)

```

In above code, `echo`, `guessNumber`, `print` and `str` are all functions.
`print` and `str` are built-in functions

## Tasks:
1. what's built-in function? can you name some of them?
2. what's str function?
3. implement below function
```
def classification(age):
    # your code here
    # if age>18 print "adult"
    # if age<=18 and age=>12 print "teen"
    # else print "kids or others" 
    pass

classification(5)  # expect "kids or others"
classification(18) # expect "teen"
classification(13)  # expect "teen"
classification(21) # expect "adult"
``` 