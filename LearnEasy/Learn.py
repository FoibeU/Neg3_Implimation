#!/usr/bin/python3
# Define a dictionary of information about each language
language_info = {
    "Python": "Python is a high-level programming language...",
    "Java": "Java is a popular programming language...",
    "JavaScript": "JavaScript is a programming language...",
    "C++": "C++ is a general-purpose programming language...",
    "Ruby": "Ruby is a dynamic, object-oriented programming language...",
    "Swift": "Swift is a powerful and intuitive programming language..."
}

def beginner():
    print("You will get the following subjects")
    print("Introductions to CSS")
    print("HTML Introduction")
    print("RWD Introductioni")

def intermediate():
    print("You will get the following subjects")
    print("Python introduction")
    print("C++ Introduction")

def advanced():
    print("You will get the following subjects")
    print("Java Introduction")
    print("Sql Introduction")

def main():
    print("Welcome to Women in Technology Platform👩‍💻\n This is a platform where you get to learn and improve your basics of programming and its Languages\n Without much I do, lets get to it.")
    print(" Which level will you like to begin with, Select 1,2,3 or 10): ")
    while(True):
        print("1.Beginner Level ")
        print("2.Intermediate Level ")
        print("3. Advanced Level")
        print("10. Exit")
        print("Level: ")
        choice = int(input())
        if choice == 1:
            print("You have chosen Beginner Level.");
            beginner();
            print("Are you sure you want to start as  a beginner ? A or B.")
            print("A. Yes, I'm sure")
            print("B. No, I'm not sure")
            ch = input()[0]
            if ch == 'A':
                print("Wonderful, Now you can start learning the basics of web\n" );
            if ch == "A":
                html= " HTML: \n is a markup language that defines the structure of your content.\n HTML consists of a series of elements, which you use to enclose,\n or wrap, different parts of the content to make it appear a certain way,\n or act a certain way. The enclosing tags can make a word or image hyperlink to somewhere else,\n can italicize words, can make the font bigger or smaller,\n HTML is the foundation of the web, and learning it is essential for anyone interested in web development.\n ..."
                css= "CSS: \n CSS stands for Cascading Style Sheets. \nIt is a style sheet language used to describe the presentation of a document written in a markup language such as HTML.In simpler terms, CSS is used to style and format the visual appearance of web pages, including layout, colors, fonts, and other design elements. \nCSS allows web developers to separate the design of a website from its content, making it easier to maintain and update the site's look and feel.\nCSS works by applying rules to HTML elements using selectors. The rules define how the elements should be displayed, such as setting the background color or font size. Multiple CSS rules can be applied to the same HTML element, and the rules are applied in a specific order, which is known as the 'cascading' aspect of CSS.\n Overall, CSS is an essential tool for web developers to create visually appealing and user-friendly websites."
                print(html)
                print(css)
                break
        elif choice == 3:
            print("You have chosen an advanced level.");
            advanced();
            print("Are you sure you want to start as an advanced ? A or B.")
            print("A. Yes, I'm sure")
            print("B. No, I'm not sure")
            ch = input()[0]
            if ch == 'A':
                print("Wonderful, Now you can continue building on your programming skills");
                break
        elif choice == 2:
            print("You have chosen intermediate level.");
            intermediate();
            print("Are you sure you want to start as an Intermediate ? A or B.")
            print("A. Yes, I'm sure")
            print("B. No, I'm not sure")
            ch = input()[0]
            if ch == 'A':
                print("Wonderful, Now you can start learning how to build on your basic programming skills");
                break

        elif choice == 10:    
            break
        else:
            print("You have entered an invalid choice.")
if __name__ == '__main__':
    main()

       
