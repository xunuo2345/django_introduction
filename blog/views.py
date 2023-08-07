from django.shortcuts import render

from django.http import HttpResponse
from django.core.paginator import Paginator

# Create your views here.

from blog.models import Article

#首先定义一个函数
def hello_world(request):
    #request参数就是http请求的对象
    #不能直接级进行返回字符串 应该封装成为一个httpresponse进行返回
    return HttpResponse("Hello World")

#实现博客数据的返回
#返回博客的文章内容
def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date

    return_str = 'title: %s, brief_content: %s,' \
                 'content: %s, article_id: %s, publish_date: %s' % (title,
                                                                    brief_content,
                                                                    content,
                                                                    article_id,
                                                                    publish_date)

    return HttpResponse(return_str)

def get_index_page(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1

    all_article = Article.objects.all()
    item_per_page = 3
    paginator = Paginator(all_article, item_per_page)
    page_article_list = paginator.get_page(page)

    top10_article_list = __get_top10_article_list()
    page_num = paginator.num_pages

    return render(request, 'blog/index.html',
                  {
                      'page_article_list': page_article_list,  # 页面文章列表
                      'top10_article_list': top10_article_list,  # top10文章列表
                      'page_num': range(1, page_num + 1),  # 分页数量
                      'curr_page': page,  # 当前页面index
                      'previous_page': 1 if (page - 1) == 0 else (page - 1),  # 前一页index
                      'next_page': page_num if (page + 1) > page_num else page + 1  # 后一页index
                  })

#实现文章详情页面的跳转
def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    previous_article = None
    next_article = None
    curr_article = None
    for index, item in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1

        if item.article_id == article_id:
            curr_article = item
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break

        # 渲染页面
    return render(request, 'blog/detail.html',
                  {
                      'curr_article': curr_article,
                      'section_list': curr_article.content.split('\n'),
                      'next_article': next_article,
                      'previous_article': previous_article
                  })

def __get_top10_article_list():
    top10_article = Article.objects.order_by('publish_date')[:10]
    return top10_article


def __get_paginator(item):
    item_per_page = 3
    paginator = Paginator(item, item_per_page)
    return paginator