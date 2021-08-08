# Python List Methods

![](https://wtmatter.com/wp-content/uploads/2020/04/Python-List-Methods.png)

[Source](https://wtmatter.com/python-list-methods/#Python_List_append)

# Introducing List
A List Is a Sequence
Like a string, a list is a sequence of values. In a string, the values are characters; in a
list, they can be any type. The values in a list are called elements or sometimes items. [Source](https://www.amazon.com/Think-Python-Like-Computer-Scientist/dp/1491939362/ref=sr_1_1?dchild=1&keywords=9781491939369&linkCode=qs&qid=1628431565&s=books&sr=1-1)


### Accessing Elements in a List
<iframe width="800" height="400" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=bicycles%20%3D%20%5B'trek',%20'cannondale',%20'redline',%20'specialized'%5D%0Aprint%28bicycles%5B0%5D.title%28%29%29%0Aprint%28bicycles%5B3%5D%29%0Aprint%28bicycles%5B-1%5D%29%0Amessage%20%3D%20f%22My%20first%20bicycle%20was%20a%20%7Bbicycles%5B0%5D.title%28%29%7D.%22%0Aprint%28message%29%0A&codeDivHeight=400&codeDivWidth=350&cumulative=true&curInstr=0&heapPrimitives=true&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


# Try It Yourself
### 3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.

<iframe width="800" height="300" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=names%20%3D%20%5B'Jack',%20'Anna',%20'Eric',%20'Vanusa'%5D%0Aprint%28names%5B0%5D%29%0Aprint%28names%5B1%5D%29%0Aprint%28names%5B2%5D%29%0Aprint%28names%5B3%5D%29%0A&codeDivHeight=400&codeDivWidth=350&cumulative=true&curInstr=0&heapPrimitives=true&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

### 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

<iframe width="800" height="400" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=names%20%3D%20%5B'jack',%20'anna',%20'eric',%20'vanusa'%5D%0Amessage%20%3D%20f%22Hello%20%7Bnames%5B0%5D.title%28%29%7D,%20you%20are%20welcome!%22%0Aprint%28message%29%0Amessage%20%3D%20f%22Hello%20%7Bnames%5B1%5D.title%28%29%7D,%20you%20are%20welcome!%22%0Aprint%28message%29%0Amessage%20%3D%20f%22Hello%20%7Bnames%5B2%5D.title%28%29%7D,%20you%20are%20welcome!%22%0Aprint%28message%29%0Amessage%20%3D%20f%22Hello%20%7Bnames%5B3%5D.title%28%29%7D,%20you%20are%20welcome!%22%0Aprint%28message%29%0A&codeDivHeight=400&codeDivWidth=350&cumulative=true&curInstr=0&heapPrimitives=true&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

### 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
<iframe width="800" height="500" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=rides%20%3D%20%5B'bicycle',%20'motorcycle',%20'car',%20'boat',%20'plane'%5D%0Aprint%28f'Do%20you%20know%20how%20to%20ride%20a%20%7Brides%5B0%5D%7D%3F'%29%0Aprint%28f%22Do%20you%20know%20how%20to%20ride%20a%20%7Brides%5B1%5D%7D%3F%22%29%0Aprint%28f%22Can%20you%20drive%20a%20%7Brides%5B2%5D%7D%3F%22%29%0Aprint%28f%22Do%20you%20how%20to%20piloting%20a%20%7Brides%5B3%5D%7D%3F%22%29%0Aprint%28f%22Can%20you%20piloting%20a%20%7Brides%5B-1%5D%7D%3F%22%29%0A&codeDivHeight=400&codeDivWidth=350&cumulative=true&curInstr=0&heapPrimitives=true&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

