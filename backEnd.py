import urllib2, google, bs4, re

q="who played superman"
r=google.search(q,num=10,start=0,stop=10)
l=[]
for result in r:
    l.append(result)

print l[0]

url = urllib2.urlopen(l[0])
page = url.read()
soup = bs4.BeautifulSoup(page,'html')
raw = soup.get_text()
print raw
