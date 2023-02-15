# Importing all the necesary modules
import random
import subprocess

'''
This script generates a random number between 0 and 1 at 
each iteration of the loop, and if the number is less than 
the probability (0.2), it sets the user to "student". It 
then prints a prompt to change the password, and constructs
the command to change the password using the "sudo" and 
"passwd" commands with the user obtained above. Finally, it 
executes the command to change the password using the 
"subprocess.call" function of the "subprocess" module. The 
loop runs infinitely, prompting the user to change their 
password randomly with a 20% chance.
'''

# Probablitiy that the password prompt will be shown
probability = 0.2

# Assigning user for the password change
user = "student"

# Continous loop
while True:
	# Check whether the user needs to be prompted
	# Generate a random number between 0 and 1, and if it is less than the probability
	if random.random() < probability:
		# Display message for user
		print("It is considered good practice to change your password.")
		print(f"sudo passwd {user}")

		# Prompts the user to change their password
		# Executing the password change command using the subprocess.call function from the subprocess module
		subprocess.call(["sudo", "passwd", user])
