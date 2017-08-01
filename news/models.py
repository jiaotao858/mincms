# -*- coding:utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField

@python_2_unicode_compatible
class Column(models.Model):  #栏目
    name = models.CharField('栏目名称',max_length=256)
    slug = models.CharField('栏目网站',max_length=256,db_index=True)
    intro = models.TextField('栏目简介',default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']

@python_2_unicode_compatible
class Article(models.Model):  #文章
    column = models.ManyToManyField(Column,verbose_name='归属栏目')
    title = models.CharField('标题',max_length=256)
    slug = models.CharField('网址',max_length=256,db_index=True)
    author = models.ForeignKey('auth.User',blank=True,null=True,verbose_name='作者')
    #使用富文本编辑器
    content = UEditorField('内容',height=300,width=1000,
                           default=u'',blank=True,
                           imagePath='uploads/images/',toolbars='besttome',
                           filePath='uploads/files/')
    published = models.BooleanField('正式发布',default=True)
    pub_date = models.DateTimeField('发布时间',auto_now_add=True,editable=True)
    update_time = models.DateTimeField('更新时间',auto_now_add=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '教程'
        verbose_name_plural = '教程'



