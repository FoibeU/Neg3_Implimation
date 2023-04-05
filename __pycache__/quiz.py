import random
from string import ascii_lowercase

def quiz():
    NUM_QUESTIONS_PER_QUIZ = 5
    QUESTIONS = {
        "What does HTML stand for?": [
            "HyperText Markup Language",
            "HighText Markup Language", 
            "HyperTech Markup Language",
            "HighTech Markup Language",
            ],
        
        "Which HTML tag is used to link to an external CSS file?": [
        "<link>",
        "<script>",
        "<style>",
        "<css>",
        ],

        "Which HTML tag is used to define a hyperlink?": [
            "<a>", 
            "<link>", 
            "<href>", 
            "<url>",
            ],    
    
        "What is the correct way to set the font size in CSS?": [
            "font-size: 12;",
            "font-size: 12px;",
            "font-size: 12em;",
            "font-size: 12pt;",
            ],   
        
        "Which of the following is not a valid HTML element?": [
            "<paragraph>", 
            "<article>", 
            "<nav>", 
            "<section>",
            ],
        
        "What is the correct way to center an HTML element horizontally in CSS?": [
            "align: center;",
            "text-align: center;",
            "horizontal-align: center;",
            "center: center;",
            ], 

        "Which HTML tag is used to define an unordered list?": [
            "<ul>", 
            "<ol>", 
            "<li>", 
            "<list>",
            ],

        "What is the correct way to set the background color of an HTML element in CSS?": [
            "bg-color: blue;",
            "background-color: blue;",
            "color: blue;", 
            "color-bg: blue;",
            ], 

        "What is the correct HTML tag for the largest heading?": [
        "<h1>",
        "<h6>",
        "<head>", 
        "<header>",
        ],

        "Which CSS property is used to control the spacing between HTML elements?": [
        "margin", 
        "padding",
        "border", 
        "spacing", 
        ],   
    }

    num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
    questions = random.sample(list(QUESTIONS.items()), k=num_questions)

    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        print(f"{question}?")
        correct_answer = alternatives[0]
        labeled_alternatives = dict(
            zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
        )
        for label, alternative in labeled_alternatives.items():
            print(f"  {label}) {alternative}")

        while (answer_label := input("\nAnswer: ")) not in labeled_alternatives:
            print(f"You can only pick:  {', '.join(labeled_alternatives)}")

        answer = labeled_alternatives[answer_label]
        if answer == correct_answer:
            num_correct += 1
            print("Correct!")
        else:
            print(f"Sorry, The right answer is {correct_answer!r}")

    print(f"\nYou got {num_correct}/{num}\n")


    if num_correct == num:
        print("Congratulations, you got a perfect score!\nYou can now move to the next level\n")


    else:
        print("Keep practicing to improve your score")
        print("\nYou've got this💪\n")
quiz()
        
            
