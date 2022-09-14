import requests
import re

'''  图片爬取
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0'
}

url1 = 'https://photo.16pic.com/00/93/57/16pic_9357910_b.png'

resp = requests.get(url=url1, headers=headers)


#json text content(二进制数据)
image_data = resp.content

with open("demo.jpg", "wb") as fp:
    fp.write(image_data)
'''


''' 正则解析
'''
s = '''
<li>
            <div class="item">
                <div class="pic">
                    <em class="">3</em>
                    <a href="https://movie.douban.com/subject/1292720/">
                        <img width="100" alt="阿甘正传" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2372307693.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1292720/" class="">
                            <span class="title">阿甘正传</span>
                                    <span class="title">&nbsp;/&nbsp;Forrest Gump</span>
                                <span class="other">&nbsp;/&nbsp;福雷斯特·冈普</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 罗伯特·泽米吉斯 Robert Zemeckis&nbsp;&nbsp;&nbsp;主演: 汤姆·汉克斯 Tom Hanks / ...<br>
                            1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;剧情 爱情
                        </p>

                        
                        <div class="star">
                                <span class="rating5-t"></span>
                                <span class="rating_num" property="v:average">9.5</span>
                                <span property="v:best" content="10.0"></span>
                                <span>2018815人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">一部美国近现代史。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
'''

iter1 = re.compile(r'<li>.*?<span class="title">(?P<movie_title>.*?)</span>.*?'
                   r'<br>'
                   )

result = iter1.finditer(s)

for i in result:
    print(i.groups('book_menu'))

