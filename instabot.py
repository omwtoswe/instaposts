#this script is just for education purpose only, please use it at your own risk
#instagram is blocking bots and the profiles using bots. use it at your own risk
#this script unfollows the followers who do not follow you
#installation
#pip install instapy
from instapy import InstaPy
session = InstaPy(username="YOURUSERNAME", password="YOURPASSWORD",headless_browser=False, #<- Insert your username and password 
                  want_check_browser=False)
session.login()
session.set_quota_supervisor(enabled=True,
                               sleep_after=["unfollows", "server_calls"],
                               sleepyhead=True,
                               stochastic_flow=True,
                               notify_me=True,
                               peak_unfollows_hourly=20,
                               peak_unfollows_daily=250,
                               peak_server_calls_hourly=200,
                               peak_server_calls_daily=2500)
session.set_dont_unfollow_active_users(enabled=True, posts=1)                              
session.unfollow_users(amount = 200, nonFollowers=True, style="FIFO")  #<- Update the amount to your desired list

"""unfollows 200 people, but only people who do not follow you, in the order of First In, First Out (FIFO)"""
session.end()
