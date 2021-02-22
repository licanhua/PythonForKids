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

# Project 4: Guess Number
## Preparation
generate random number

```
import random
number = random.randint(1, 8)
print(number)
```

## Tasks
1. search randint. what's the correct answer to generate random number between 0 and 9(includes 0 and 9), randint(0, 9), or random.randint(0, 10)?
2. generate the random number which >=0 and <9, then ask user to input a number. if the number matches with the random number, print correct. if it's less than random number, print "too small", otherwise print "too big".
Complete below code:

```
import random
number = random.randint(?, ?)
for i in range(0, 10):
    guessNumber = input()
    ...

```

# Project 5: Find the biggest number from the dictionary, list, or tuple
## Preparation

There are two ways to check if a variable is tuple: use `type` or `isinstance`

```
test_tup = (4, 5, 6)
if (type(test_tup) is tuple):
    print("it's tuple")

if (isinstance(test_tup, tuple)):
    print("it's tuple too");
```

## Task
ages: the ages of all students in a classroom. it can be list, tuple, int. For example

`ages = [5,4,5,6,4]`
or
`ages = (5,4,5,6,4)`
or
`ages = 6`

Your tasks:
1. find the max number in the ages. in above, max is 6
2. if the input is list, print `max is 6 in list of ages`.
if the input is tuple, print `max is 6 in tuple of ages`
if the input is int, print `type is not supported`

```
def PrintMax(ages):
    ...

```

## Test cases
```
ages = (4,4,6,5,2)
printMax(ages)

ages = [1,2,3,4,5]
printMax(ages)

ages = 1
printMax(ages)
```

# Project 6: sell skis
## Preparation

List Methods

|Method   |Description   |
|---|---|
|append   |Adds an element at the end of the list   |
|remove   |Removes the item with the specified value   |
|len(list)| returns the number of elements in the list |
|   |   |


```
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.append('added item');
print "List : ", aList
aList.remove('xyz');
print "List : ", aList
aList.remove('abc');
print "List : ", aList
```

## Task
You are the owner of a ski store, and you sell the skis in store, also accept reservation if there is no ski available.

Given you have two lists:
```
availableSkis = [100, 120, 125, 130]
reservation = []
```

availableSkis means the list of skis which is available to sell. 100 and 120 means the size of the ski

```
availableSkis = [100, 120, 125, 130]
reservation = []

while (len(availableSkis) > 0)
{
    # use input to ask customer which size of ski he want
    # if the size is in availableSkis, sell it to him, and remove it from availableSkis
    # else ask his name and append it to reservation. For example, if his name is Nemo, and the size is 120, then append ['Nemo', 100] to reservation
}

print(reservation)
```


