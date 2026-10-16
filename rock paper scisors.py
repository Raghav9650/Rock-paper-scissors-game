import random
rock=('''          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)''')
paper=('''         _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)''')
scissors=('''           _______
         ---'   ____)____
                   ______)
               __________)
            (____)
      ---.__(___)''')
n=int(input("What do you want to choose\n0=rock\n1=paper\n2=scissors"))
while (n<0 or n>2):
    print("Invalid choice")
    exit()
t=[rock,paper,scissors]
print(t[n])
computer_choice=random.randint(0,2)
while computer_choice==n:
    computer_choice=random.randint(0,2)
print("computer choice"
"\n",t[computer_choice])
if n==0 and computer_choice==2:
    print("You win!")
elif n==1 and computer_choice==0:
    print("You win!")
elif n==2 and computer_choice==1:
    print("You win!")
else:
    print('You loose!')
