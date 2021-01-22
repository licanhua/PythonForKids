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

[IDE setup Video](https://www.youtube.com/watch?v=P9VmSIIO-Xc)


# Project: Response to `input`
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