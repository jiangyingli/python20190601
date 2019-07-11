# https://www.fifa.com/worldcup/players/player/312252/
import requests
from bs4 import BeautifulSoup

num = 1


def get_html(url):
    html = ""
    try:
        html = requests.get(url)
        html.encoding = html.apparent_encoding
    except Exception as e:
        print("error!")
        print(e)
    return html.text


def parse_data(html, num):
    soup = BeautifulSoup(html, "html.parser")
    datas = ['年龄','身高','国家队出场次数','进球次数']
    results = soup.find_all("div", attrs={"class": "fi-p__profile-number__number"})
    print("result len is :",len(results))
    if len(results) == 0:
        return 0
    else:
        for num in range(len(results)):
            print(datas[num],results[num].string.strip())

if __name__ == '__main__':
    player_num = 229397

    while player_num <= 229997:
        #url = "https://www.fifa.com/worldcup/players/player/" + str(player_num) + "/"
        url = "https://www.fifa.com/worldcup/_libraries/players/player/"+str(player_num)+"/_player-profile-data"
        html = get_html(url)
        print(url)
        flag = parse_data(html,num)
        if flag == 0:
            pass
        else:
            num = num + 1
        player_num = player_num+1
