import random
import subprocess


probability = 0.2

while True:
	if random.random() < probability:
		user = "student"

	print("Change your password")
	print(f"sudo passwd {user}")

	subprocess.call(["sudo", "passwd", user])
