score = 0
max_attempts = 3

attempt = 0
while attempt < max_attempts:
    print("1. What is the capital of France?")
    print("A) London")
    print("B) Berlin")
    print("C) Paris")
    print("D) Madrid")
    user = input("Your answer: -- ")
    if user.lower() == "c":
        print("Correct Answer")
        score += 1
        break
    else:
        print("Try another one")
        attempt += 1
if attempt == max_attempts:
    print("No more attempts left for this question.")
print("-" * 30)

attempt = 0
while attempt < max_attempts:
    print("2. Which planet is known as the Red Planet?")
    print("A) Earth")
    print("B) Mars")
    print("C) Jupiter")
    print("D) Venus")
    user = input("Your answer: -- ")
    if user.lower() == "b":
        print("Correct Answer")
        score += 1
        break
    else:
        print("Try again")
        attempt += 1
if attempt == max_attempts:
    print("No more attempts left for this question.")
print("-" * 30)

attempt = 0
while attempt < max_attempts:
    print("3. What is 5 + 7?")
    print("A) 10")
    print("B) 12")
    print("C) 14")
    print("D) 11")
    user = input("Your answer: -- ")
    if user.lower() == "b":
        print("Congratulations")
        score += 1
        break
    else:
        print("Try again")
        attempt += 1
if attempt == max_attempts:
    print("No more attempts left for this question.")
print("-" * 30)

attempt = 0
while attempt < max_attempts:
    print("4. Which animal is known as the King of the Jungle?")
    print("A) Tiger")
    print("B) Lion")
    print("C) Elephant")
    print("D) Cheetah")
    user = input("Your answer: -- ")
    if user.lower() == "b":
        print("Good job")
        score += 1
        break
    else:
        print("Try again")
        attempt += 1
if attempt == max_attempts:
    print("No more attempts left for this question.")
print("-" * 30)

attempt = 0
while attempt < max_attempts:
    print("5. What color do you get when you mix red and white?")
    print("A) Pink")
    print("B) Purple")
    print("C) Orange")
    print("D) Brown")
    user = input("Your answer: -- ")
    if user.lower() == "a":
        print("Correct Answer")
        score += 1
        break
    else:
        print("Try again")
        attempt += 1
if attempt == max_attempts:
    print("No more attempts left for this question.")
print("-" * 30)

print(f"Your final score is: {score} out of 5")
print("-" * 30)
