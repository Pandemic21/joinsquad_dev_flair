import praw
import time

USERNAME="pandemic21bot"
PASSWORD=""
r = praw.Reddit("joinsquad dev checker by /u/Pandemic21")
devs={'Pandemic21'}
r.login(USERNAME,PASSWORD,disable_warning="True")

sub = r.get_subreddit("pandemicsandbox")

k=0
print "---------------start"
for comment in praw.helpers.comment_stream(r, sub, limit=1,verbosity=1):
	for dev in devs:
		if str(comment.author) == dev:
			print str(comment.author) + " is " + str(dev)
			print comment.permalink
			s = r.get_submission(url=comment.permalink)
			r.set_flair(sub, s, flair_text="flair text!")
		else:
			print "NOT on dev list: " + str(comment.author)
print "---------------end"
