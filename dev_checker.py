import praw
import time


def read_devs_file(f_path):
	f = open(f_path, 'r')
	devs=[]
	for dev in f:
		devs.append(dev.strip())
		gen_log('Added dev: "' + dev.strip() + '"')
	return devs

def gen_log(data):
	f = open(LOGFILE, 'a')
	datetime =  str(time.strftime("%Y/%m/%d")) + " " + str(time.strftime("%H:%M:%S"))
	f.write(datetime + ": " + data + "\n")
	f.close()
	print datetime + ": " + data


# MAIN ###########################################################################
USERNAME=""
PASSWORD=""
LOGFILE='dev_checker.log'
DEVSFILE='c:\users\caldw\desktop\devs.txt'
SUBREDDIT='pandemicsandbox'
FLAIR_ADDITION=" | Dev Response"

devs=read_devs_file(DEVSFILE)

r = praw.Reddit("joinsquad dev checker by /u/Pandemic21")
r.login(USERNAME,PASSWORD,disable_warning="True")
sub = r.get_subreddit(SUBREDDIT)


#get new comments
for comment in praw.helpers.comment_stream(r, sub, limit=1,verbosity=1):
	#check comment author against dev list
	for dev in devs:
		if str(comment.author) == dev:
			gen_log(str(comment.author) + " is a dev")
			gen_log(comment.permalink)
			#get submission dev just commented in
			s = r.get_submission(url=comment.permalink)
			
			#if the post has already been flaired "| Dev Response" don't reflair it
			if "| Dev Response" in s.link_flair_text:
				gen_log(str(s.id) + " already flaired")
				break
				
			new_flair_text = s.link_flair_text + FLAIR_ADDITION
			r.set_flair(sub, s, flair_text=new_flair_text, flair_css_class=s.link_flair_css_class)
