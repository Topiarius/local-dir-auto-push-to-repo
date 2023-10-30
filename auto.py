import os
import time
import subprocess

# Specify the path to the "website" folder
website_path = r'C:\Users\might\Downloads\test-upload-repo'

# Store the initial modification time
initial_mod_time = os.path.getmtime(website_path)

while True:
    # Check the current modification time
    current_mod_time = os.path.getmtime(website_path)

    # Compare with the initial modification time
    if current_mod_time != initial_mod_time:
        print("Website folder has been modified!")

        # Change to the "website" directory
        os.chdir(website_path)

        # Run git add .
        subprocess.run(["git", "add", "."])

        # Run git commit -m " "
        subprocess.run(["git", "commit", "-m", "Auto commit"])

        # Run git push -u origin master
        subprocess.run(["git", "push", "-u", "origin", "master"])

        print("Git commands executed successfully.")

        # Update the initial modification time
        initial_mod_time = current_mod_time

    # Wait for a short interval before checking again (e.g., 1 second)
    time.sleep(1)