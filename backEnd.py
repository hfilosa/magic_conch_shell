import urllib2, google, bs4, re

def search(query):
    """
    return result of google search
    
    :param query: a string
    
    :retval: array of first 10 google results from search
    """
    result=google.search(query,num=10,start=0,stop=10)
    links=[]
    for link in result:
        links.append(link)
    return links

def get_page(link):
    """
    return contents of web page at link
    
    :param link: a string
    
    :retval: string of page contents
    """
    url = urllib2.urlopen(link)
    page = url.read()
    soup = bs4.BeautifulSoup(page,'html')
    raw = soup.get_text()
    return raw

def search_page(text,query):
    """
    return occurences of desired information in a text
    
    :param text: a string
    :param query: a string. Will be searched to determine what we are looking for
    
    :retval: dictionary: Keys are names/locations/dates, their values are how often they occur in the text
    """
    #Determine if this is a who,where or when query
    if re.search("(W|w)ho",query):
        exp = "[A-Z][a-z]+ [A-Z][a-z]+"
    elif re.search("(W|w)hen",query):
        exp="A regex for dates"
    elif re.search("(W|w)here",query):
        exp="A regex for places"
    else:
        raise SystemExit(0)
    result = re.finditer(exp,text)
    ans = {}
    for match in result:
        name=match.group(0)
        if name in ans:
            ans[name]+=1;
        else:
            ans[name]=1;
    return ans
            
def find_max(dic):
    """
    return the data value that occurs most frequently in the dictionary
    
    :param dic: a dictionary with strings as keys, their values as ints
    
    :retval: The value that occurs the most. Unclear which value it returns if two keys share the same value
    """
    print dic
    occurences=list(dic.values())
    data=list(dic.keys())
    print max(occurences)
    return data[occurences.index(max(occurences))]

def find_answer(query):
    """
    return the internet's answer to the query
    
    :param query: a string
    
    :retval: The answer that appears most often in the first 10 links of the google search of the question
    """
    links=search(query)
    master_results={}
    for link in links:
        names=search_page(get_page(link),query)
        for name in names:
            if name in master_results:
                master_results[name]+=1;
            else:
                master_results[name]=1;
    return find_max(master_results)

print find_answer("Who invented the lightbulb?")

