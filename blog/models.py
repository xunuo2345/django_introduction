from django.db import models

# Create your models here.

#进行文章模型的定义
#此外还需要进行模型的迁移 将模型的定义保存到数据库里面
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    #文章id
    title = models.TextField()
    #文章标题
    brief_content = models.TextField()
    #文章预览
    content = models.TextField()
    #内容
    publish_date = models.DateField(auto_now=True)
    #发布日期，如果没有指定文章的发布日期就以当前的时间作为发布日期

    def __str__(self):
        #返回文章的title
        return self.title
