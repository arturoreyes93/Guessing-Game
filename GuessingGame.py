#  File: GuessingGame.py

#  Description: guesses a number between 100 and 1 in less than 7 tries

#  Student Name: Arturo Reyes Munoz

#  Student UT EID: ar48836

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 04/11

#  Date Last Modified: 04/11


def main():

	print('Think of a number between 1 and 100 inclusive.\nAnd I will guess what it is in 7 tries or less.\n ')

	ready = str(input('Are you ready? (y/n) : '))

	while ready != 'y' and ready != 'n':

		ready = input('Are you ready? (y/n) : ')

	if ready =='n':
		print('Bye')
		return 

	elif ready =='y':

		guess = 1
		correct = 2

		lo=0
		hi=100

		while guess!=8 or correct!=0:

			mid=(hi+lo)//2

			print(' ')

			print('Guess '+str(guess)+' The number you thought was '+str(mid))
			correct=eval(input('Enter 1 if my guess was high, -1 if low, and 0 if correct: '))

			if correct==-1:

				lo=mid+1


			elif correct==1:

				hi=mid-1

			elif correct==0:
				print(' ')
				print("Thank you for playing the Guessing Game.")

				return 
			
			guess+=1

			if guess==8:
				print(' ')
				print('Either you guessed a number out of range or you had an incorrect entry.')

				return 


				
main()







