# Import the necessary libraries. We will be using 'instaloader' and the output accounts will be stored in the csv file on your system.
# Instaloader is a library written in python that helps us to download the instagram data from your feed and from all followees of a given profile.

# pip3 install instaloader

import csv
import instaloader

# Create an instance of Instaloader.
ig = instaloader.Instaloader()

# Login into instagram using username & credentials of your account.
ig.login('@username', 'password')

# Get the profile for which you want to check the unfollowers by specifying the username. You can check for your own account and even for your friends' account.

person = 'omwtoswe'  # mention the username without '@'
profile = instaloader.Profile.from_username(ig.context, person)

# Get the list of accounts that follow you (followers) from the profile.

my_followers = []
for follower in profile.get_followers():
    username = follower.username
    my_followers.append(username)  # append in the list

# Similarly, get the list of the accounts you are following (followees).
my_following = []
for followe in profile.get_followees():
    username = followe.username
    my_following.append(username)  # append in list

# Now for account in your following list, if the account is not present in the followers list then write it in csv file.
with open('unfollowers.csv', 'w') as csvfile:  # unfollowers.csv file saved on system
    writer = csv.writer(csvfile)
    for followe in my_following:
        if followe not in my_followers:
            print(followe)
            writer.writerow([followe])
