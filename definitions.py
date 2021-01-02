import random
import time

def inputt():
	user=input("Your turn. Choose: ")
	return user

# def inputt():
# 	while True:
# 		try:
# 			user=input("Your turn. Choose: ")
# 			return user
# 		except ValueError:
# 			clear()
# 			print("Wrong Choice")
# 			continue

def calculations(user,comp):
	if user=="R":
		if comp=="P":
			print("You Lose. Comp Wins!")
			time.sleep(3)
		else:
			print("You Win!")
			time.sleep(3)
	elif user=="P":
		if comp=="S":
			print("You Lose. Comp Wins!")
			time.sleep(3)
		else:
			print("You Win!")
			time.sleep(3)
	elif user=="S":
		if comp=="R":
			print("You Lose. Comp Wins!")
			time.sleep(3)
		else:
			print("You Win!")
			time.sleep(3)

def compare(user):
	R="R"
	P="P"
	S="S"

	avail=[R,P,S]

	comp=random.choice(avail)
	print(comp)

	if user==comp:
		print("Draw!")
		userAgain=inputt();
		compare(userAgain);
	else:
		calculations(user,comp);
