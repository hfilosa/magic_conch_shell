import urllib2, google, bs4, re

q="who played superman"
r=google.search(q,num=10,start=0,stop=10)
l=[]
for result in r:
    l.append(result)

#print l[0]

def get_pages(l):
    n = 0
    while n < len(l):
        url = urllib2.urlopen(l[n])
        page = url.read()
        soup = bs4.BeautifulSoup(page,'html')
        raw = soup.get_text()
        n = n+1
        #print raw
    return raw

def find_name(s):
    exp = "[A-Z][a-z]+ [A-Z][a-z]+"
    result = re.findall(exp,s)
    return result

#print find_name(raw)

def find_champ(l):
    for item in l:
        champ = ""
        champnum = 0
        current = l.count(item)
        if  current > champnum:
            champnum = current
            champ = item
    return champ

pages = get_pages(l)
names = find_name(pages)
print find_champ(names)
