# RedTeamTool

Name: Salomi Rao
Team: Team Bravo
Date: 15th Feb 2023

I have three distraction tools built as a part of my red team tools assignment.

# 1. Apache Stop

This is a simple Bash script that randomly stops the Apache service, (which would most likely be a scored service).

This script assumes that there is an existing apache service running.

This script has been built and tested on an Ubuntu machine. Needs to be executed with sudo.

```
    sudo chmod 777 apache_stop.sh
```

To run this, 
```
    sudo ./apache_stop.sh
```

# 2. Password Change

This is a python script that randomly prompts the user randomly to change their password.

It is just being used to distract and take time away from the Blue team members.

The username for the user in this case is "student" but can be easily changed or can include a list of users for ease of use within the competition.

This assumes you are running python3 and using a Linux based machine.

To run this, 
```
    python3 pass_change.py
```

# 3. Prompt

This is a python script that throws random pop-ups on the screen and the prompts continue to show up until the answer is "yes" to a specific question.

This assumes you are running python3.

```
    sudo apt-get update
    sudo apt-get install python3-tk
```

To run this,
```
    python3 prompt.py
```


# Execution

Each of these can be executed in the above mentioned ways, but additionally can also be executed using a C2 or by adding these the cronjobs. For use in the competition, the filenames will not remain as clear and will be changed to seem like nothing of much importance.
