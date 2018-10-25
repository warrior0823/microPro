# coding: utf-8

from flask import Flask
import flask

app = Flask(__name__)  # type: Flask
app.debug = True

# 电影
movies = [
    {
        'id': '34532',
        'title': u'胖子行动队',
        'thumbnail': u'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2526215398.webp',
        'rating': u'7.6',
        'comment_count': 39450,
        'authors': u'宝贝儿 / 李成敏 Clara Lee / 文章 Zhang Wen'
    },
    {
        'id': '394558',
        'title': u'李茶的姑妈',
        'thumbnail': u'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2533384240.webp',
        'rating': u'6.3',
        'comment_count': 38409,
        'authors': u'钱晨光 / 吴瑾蓉 / 黄才伦'
    },
    {
        'id': '26921827',
        'title': u'找到你',
        'thumbnail': u'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2534471408.webp',
        'rating': u'4.3',
        'comment_count': 682,
        'authors': u'姚晨 / 马伊琍 / 袁文康'
    },
    {
        'id': '26287884',
        'title': u'悲伤逆流成河',
        'thumbnail': u'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2529701498.webp',
        'rating': u'7.5',
        'comment_count': 33060,
        'authors': u'赵英博 / 任敏 / 辛云来'
    },
    {
        'id': '26287884',
        'title': u'嗝嗝老师',
        'thumbnail': u'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535365481.webp',
        'rating': u'7.5',
        'comment_count': 33060,
        'authors': u'拉妮·玛克赫吉 / 内拉吉·卡比 / 萨钦'
    }
]

# 电视剧
tvs = [
    {
        'id': '235434',
        'title': u'如懿传',
        'thumbnail': u'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2460165077.jpg',
        'rating': u'7.4',
        'comment_count': 49328,
        'authors': u'拉妮·玛克赫吉 / 内拉吉·卡比 / 萨钦'
    },
    {
        'id': '48373095',
        'title': u'奇葩说第五季',
        'thumbnail': u'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2534020405.jpg',
        'rating': u'8.4',
        'comment_count': 2483,
        'authors': u'伊藤沙莉 / 中川大志 / 上原实矩 / 森绘梨佳 / 樱田通 /'
    },

    {
        'id': '27005982',
        'title': u'最亲爱的你',
        'thumbnail': u'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2508399162.jpg',
        'rating': u'7.6',
        'comment_count': 25532,
        'authors': u'杰西·普莱蒙 / 莫莉·香侬 / 布莱德利·惠特福德 / Maude Apatow / 麦迪逊·贝蒂 /'
    },
    {
        'id': '30290917',
        'title': u'我们无法成为野兽',
        'thumbnail': u'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2537556934.jpg',
        'rating': u'3.7',
        'comment_count': 8493,
        'authors': u'钟汉良 / 杨颖 / 甘婷婷 / 孙艺洲 / 亓航 /'
    },
    {
        'id': '292843',
        'title': u'奇遇人生',
        'thumbnail': u'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2533929218.jpg',
        'rating': u'8.2',
        'comment_count': 23456,
        'authors': u'托马斯·哈登·丘奇 / 泰伦斯·霍华德 / 波伊德·霍布鲁克 / 瑞斯·维克菲尔德 / 马尔洛·托马斯 /'
    }
]


@app.route('/')
def hello_world():
    context = {
        "movies": movies,
        "tvs": tvs
    }
    return flask.render_template('index.html', **context)


# @app.route('/list/<int:category>')
# def itemList(category):
#     # 如果category等于1：返回电影
#     # 如果category等于2：返回电视剧
#     # 否则返回空数组
#     items = []
#     if category == 1:
#         items = movies
#     elif category == 2:
#         items == tvs
#     else:
#         items = []
#
#     return flask.render_template('moreList.html', items=items)


if __name__ == '__main__':
    app.run()
