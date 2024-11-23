intro_text ="""You’ve just started your first year of teaching at Riverside Middle School. It’s been a tough day, but you're determined to make it through. 

You’re teaching an eighth-grade English class, and you’ve barely gotten through the lesson before one of your more disruptive students, Ethan, begins acting out. He’s been talking loudly, making jokes at inappropriate times, and distracting the rest of the class. You’ve tried asking him to stop multiple times, but it’s not working. The class is getting restless, and the other students are starting to lose focus.
"""

intro_text_2 = """
The rest of the class is watching to see how you’ll handle the situation. You can feel the pressure mounting, and you need to act fast before things get out of hand.
"""

actions={
    "step_1":[
        "A. Raise your voice and give Ethan a stern warning in front of the class. You\’ll establish authority right away.",
        "B. Call Ethan aside for a private conversation after class to see if something\’s bothering him.",
        "C. Try to engage Ethan by asking him to contribute to the lesson. Maybe redirecting his energy will help."
        ],
    "step_1_A": [
        "A. Stay firm and continue the lesson, hoping the warning worked.", 
        "B. Apologize to Ethan privately after class to smooth things over."
        ],
    "step_1_B":[
        "A. Suggest to Ethan that you\’ll work together to improve his behavior and offer to help with his schoolwork if he needs it.",  
        "B. Express sympathy but also set clear expectations that the behavior must improve, or there will be consequences."
    ],
    "step_1_C":[
        "A. Use this momentum to turn the lesson into a more interactive activity for the class, involving Ethan and the other students.",
        "B. Allow Ethan to contribute but keep the class on track with minimal interruptions."
    ]

}
print(intro_text)

print(intro_text_2)
user_input = input("What do you choose? ")

for n in actions["step_1"]:
    print(n)

while True:
    if user_input.lower() == "stop" or user_input == "":
        break
    
    