import urllib.request
def read_text():
	quotes = open("/home/varis/environments/mail")
	contents = quotes.read()
	print(contents)
	quotes.close()
	check(contents)

def check(text):
	with urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text) as url:
		output = url.read()
	print(output)
	connection.close()
read_text()
