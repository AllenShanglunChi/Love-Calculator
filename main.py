# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# print(type("allen".count('a')))

combinedName = name1 + name2
lowerCaseName = combinedName.lower()
t = lowerCaseName.count('t')
r = lowerCaseName.count('r')
u = lowerCaseName.count('u')
e = lowerCaseName.count('e')

true = t + r + u + e

l = lowerCaseName.count('l')
o = lowerCaseName.count('o')
v = lowerCaseName.count('v')
e = lowerCaseName.count('e')

love = l + o + v + e

scoreStr = str(true) + str(love)

score = int(scoreStr)

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}, I have a bad feeling about this...") 