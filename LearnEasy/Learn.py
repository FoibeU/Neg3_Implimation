#!/usr/bin/pythn3c
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
def advanced():
    print("You will get the following subjects")
    print("Python introduction")
    print("Java Introduction")
    print("Sql Introduction")

def main():
    print("Welcome to Women in Technology Platform")
    print("Select one of the following level  in which you want to start with")
    while(True):
        print("1.Beginner Level ")
        print("2. Advanced Level")
        print("10. Exit")
        print("Enter the choice number from above")
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
                html= " HTML: \n is a markup language that defines the structure of your content.\n HTML consists of a series of elements, which you use to enclose,\n or wrap, different parts of the content to make it appear a certain way\n, or act a certain way. The enclosing tags can make a word or image hyperlink to somewhere else,\n can italicize words, can make the font bigger or smaller\n, and so on."
                print(html)
                break
        elif choice == 2:
            print("You have chosen an advanced level.");
            advanced();
            print("Are you sure you want to start as an advanced ? A or B.")
            print("A. Yes, I'm sure")
            print("B. No, I'm not sure")
            ch = input()[0]
            if ch == 'A':
                print("Wonderful, Now you can start leaen how to build simple program");
                break
        elif choice == 10:
            break
        else:
            print("You have entered an invalid choice.")
if __name__ == '__main__':
    main()

