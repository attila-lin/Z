#!/usr/bin/env python
#-*- coding: UTF-8 -*-



import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

import utils


topic_url = "http://news-at.zhihu.com/api/3/sections"

# {"data":[{"description":"睡前宵夜，用别人的故事下酒","id":1,"name":"深夜食堂","thumbnail":"http:\/\/pic2.zhimg.com\/23d10d5d60ef82c3c0099695e991599a.jpg"},{"id":2,"thumbnail":"http:\/\/pic1.zhimg.com\/b7547d1a729507453d1d1bce5d78a294.jpg","name":"瞎扯","description":"随便扯扯，也能很有深度"},{"description":"带你逛逛全世界","id":5,"name":"知天下","thumbnail":"http:\/\/p1.zhimg.com\/0f\/b9\/0fb9932f82b328657021e714eb65f631.jpg"},{"description":"我喜欢假的","id":6,"name":"苗炜专栏","thumbnail":"http:\/\/pic4.zhimg.com\/015cbf1daf2992e67350d33bdcb8c8ff.jpg"},{"description":"来，聊聊天。","id":12,"name":"#知乎日报周末话题#","thumbnail":"http:\/\/pic1.zhimg.com\/255a460bad98c22781846463bed9463e.jpg"},{"id":9,"thumbnail":"http:\/\/pic1.zhimg.com\/4d3883ce6c02c7e7b993a806dbe5d6b0.jpg","name":"最美应用","description":"一群爱应用的理想主义者发起的开放项目"},{"id":14,"thumbnail":"http:\/\/p1.zhimg.com\/85\/9e\/859ea4167c0af1d506c7e20b0de7a84b.jpg","name":"麻省理工科技评论","description":"关注即将商业化的技术创新，分享即将资本化的技术创业。"},{"thumbnail":"http:\/\/p2.zhimg.com\/1d\/ab\/1dab78da4b87dd85a7cf5a304da594bc.jpg","description":"关注智能汽车、智能硬件和设计创意","name":"硬科技","id":8},{"thumbnail":"http:\/\/pic3.zhimg.com\/4d360740ba4b0dc677c8011d79a99bf6.jpg","description":"吃，很重要","name":"吃很重要","id":3},{"id":10,"thumbnail":"http:\/\/pic3.zhimg.com\/6e6fe4f2714713e20c8cbf3d6f7c8a1b.jpg","name":"鲜柚游戏周报","description":"回顾一周 iOS 精品游戏"},{"thumbnail":"http:\/\/pic2.zhimg.com\/f7504bcbd1ec9ba52b86ff428225b22d.jpg","description":"每周发现一款优质应用","name":"豌豆荚设计奖","id":11},{"thumbnail":"http:\/\/p3.zhimg.com\/b1\/f4\/b1f434425c0d8343571d1df357fb7818.jpg","description":"道听途说仅供参考","name":"小道消息","id":7},{"description":"精选每周 #知乎日报周末话题# 优秀评论","id":15,"name":"#周末话题优秀评论精选#","thumbnail":"http:\/\/p4.zhimg.com\/3a\/be\/3abe47457e993ccf1cad2a3ce9f88218.jpg"},{"thumbnail":"http:\/\/pic1.zhimg.com\/9032d7d8c0e4bc92194af6784dff6e2c.jpg","description":"","name":"整点儿新闻","id":16},{"thumbnail":"http:\/\/pic3.zhimg.com\/bb82881467eb3fba15087a47116e89cb.jpg","description":"","name":"饿了","id":17}]}





class Topic():
  """
  docstring for Topic
  """
  def __init__(self):
    self.topics = self.getTopics()


  def getTopics(self):
    js = utils.getList(topic_url)
    topics = []
    for item in js['data']:
      # topics[item["name"]] = item["id"]
      topics.append([item["name"], item["id"]])
    return topics
