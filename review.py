def create_youtube_video(title,discription):
	vid={"title" : title,
	"discription" :discription,
	"likes" : 0,
	"dislikes" :0,
	"comments":{}}
	return vid 

def likes(youtubevideo):
	if "likes" in youtubevideo:
		youtubevideo["likes"]+=1


def dislikes(youtubevideo):
	if "dislikes" in youtubevideo:
		youtubevideo["dislikes"]+=1

def add_comment(youtubevideo ,username ,comment_text):
	youtubevideo["comments"][username]=comment_text

vid1 = create_youtube_video('ali' ,"best ta")
print(vid1)

for anything in range(495):
	likes(vid1)
dislikes(vid1)
add_comment(vid1 ,"meet" ,"y2")
print(vid1)