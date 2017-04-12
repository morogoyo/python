import random
adjectives = ["creative","inovation","service","data driven","Marketing","consulting"]

for a in adjectives:
	randInt = random.randrange(0,len(adjectives))
	print("LMS is "+adjectives[randInt])

	