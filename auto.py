import os
import subprocess
import time

# Specify the path to the "website" folder
website_path = r'C:\Users\might\Downloads\test-upload-repo'

# Store the initial modification times for each file
initial_mod_times = {item: os.path.getmtime(os.path.join(website_path, item)) for item in os.listdir(website_path) if os.path.isfile(os.path.join(website_path, item))}

while True:
    # Check the current modification times for each file
    current_mod_times = {item: os.path.getmtime(os.path.join(website_path, item)) for item in os.listdir(website_path) if os.path.isfile(os.path.join(website_path, item))}

    # Compare with the initial modification times
    if current_mod_times != initial_mod_times:
        print("Changes detected in files inside the directory!")

        # Change to the "website" directory
        os.chdir(website_path)

        # Run git add .
        subprocess.run(["git", "add", "."])

        # Run git commit -m " "
        subprocess.run(["git", "commit", "-m", "Auto commit"])

        # Run git push -u origin master
        subprocess.run(["git", "push", "-u", "origin", "master"])

        print("Git commands executed successfully.")

        # Update the initial modification times
        initial_mod_times = current_mod_times

    # Wait for a short interval before checking again (e.g., 1 second)
    time.sleep(1)
