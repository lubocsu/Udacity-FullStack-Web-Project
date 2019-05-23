import urllib.request as request
import requests
import urllib.parse
def read_text():
    f = open("C:\\Users\\lubo\\Desktop\\python入门\\udacity\\全栈工程师\\02ProfanityEditor-MiniProject\\movie_quotes.txt")
    check_profanity(f.read())
    f.close()
def check_profanity(text):

    proxies = {
        'https': 'https://127.0.0.1:1080',
        'http': 'http://127.0.0.1:1080'
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    full_url = "http://www.wdylike.appspot.com/?q=" + urllib.parse.quote(text)
    opener = request.build_opener(request.ProxyHandler(proxies))
    request.install_opener(opener)
    req = request.Request(full_url, headers=headers)
    response = request.urlopen(req).read().decode()
    if 'false' in response :
        print("No Profanity")
    else:
        print("Profanity found")
read_text()




