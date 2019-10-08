#who wants to be a millionare

def millionare():
    print("Which of the following mythical creatures breathes fire?")
    answer = input("A. Unicorn, B.Centaur, C.Dragon, D.Pegasus")
    if answer == "c":
        print("Congrats! You won $100")
    else:
        print("You lost")
    print("Which of these phrases is often used to describe a trusted aide?")
    answer = input("A. Right - hand man, B. Left - leg lady, C. Torso buddy, D. Left - eye Lopes")
    if answer == "a":
        print("Congrats! You won $200")
    else:
        print("You lost")
    print("A sauna is a room that people generally visit to do what?")
    answer = input("A. Sleep, B. Eat, C. Sweat, D. Fall in love.")
    if answer == "c":
        print("Congrats! You won $300")
    else:
        print("You lost")

millionare()


