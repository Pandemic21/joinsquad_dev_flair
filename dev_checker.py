import praw
import time

USERNAME="pandemic21bot"
PASSWORD=""
r = praw.Reddit("joinsquad dev checker by /u/Pandemic21")
devs={'homfri'}
#r.login(USERNAME,PASSWORD,disable_warning="True")

sub = r.get_subreddit("joinsquad")

k=0
print "---------------start"
for comment in praw.helpers.comment_stream(r, sub, limit=5,verbosity=1):
	for dev in devs:
		if str(comment.author) == dev:
			print str(comment.author) + " is " + str(dev)
			print comment.permalink
			s = r.get_submission(url=comment.permalink))
		else:
			print "NOT on dev list: " + str(comment.author)
print "---------------end"
