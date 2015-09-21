#-*- coding:utf-8 -*-

from django.db import models
from django.contrib import admin

# Create your models here.
class Activity_category(models.Model):
	user_id = models.IntegerField(verbose_name=u'用户ID')
	equipment_id = models.IntegerField(verbose_name=u'设备ID')
	start_time = models.DateTimeField(verbose_name=u'开始时间')
	end_time = models.DateTimeField(verbose_name=u'结束时间')

	class Meta:
		verbose_name_plural = u'活动种类'

	def __int__(self):
		return self.user_id

class Equipment(models.Model):
	equipment_id = models.IntegerField(verbose_name=u'设备ID')
	place_id = models.IntegerField(verbose_name=u'景点ID')
	equipment_name = models.CharField(max_length=100, verbose_name=u'设备名称')
	equipment_intro = models.TextField(verbose_name=u'设备简介')
	equipment_owner = models.CharField(max_length=100, verbose_name=u'设备所属者')
	equipment_is_available = models.CharField(max_length=100, verbose_name=u'是否可用')
	equipment_lat = models.FloatField(verbose_name=u'纬度')
	equipment_lon = models.FloatField(verbose_name=u'经度')
	equipment_imagepath = models.CharField(max_length=100, verbose_name=u'图片路径')
	equipment_location = models.CharField(max_length=100, verbose_name=u'设备所在地')

	class Meta:
		verbose_name_plural = u'设备'

	def __unicode__(self):
		return self.equipment_name

class Equipment_order(models.Model):
	user_id = models.IntegerField(verbose_name=u'用户ID')
	equipment_id = models.IntegerField(verbose_name=u'设备ID')
	start_time = models.DateTimeField(verbose_name=u'开始时间')
	end_time = models.DateTimeField(verbose_name=u'结束时间')

	class Meta:
		verbose_name_plural = u'设备订单'

	def __int__(self):
		return self.user_id

class Product(models.Model):
	product_name = models.CharField(max_length=100, verbose_name=u'产品名称')
	product_type = models.IntegerField(verbose_name=u'产品类型')
	product_photo = models.CharField(max_length=100, verbose_name=u'产品图片')
	product_price = models.FloatField(verbose_name=u'产品价格')
	product_num = models.IntegerField(verbose_name=u'产品数量')
	product_introduce = models.TextField(verbose_name=u'产品介绍')

	class Meta:
		verbose_name_plural = u'产品'

	def __unicode__(self):
		return self.product_name

class Product_category(models.Model):
	type_name = models.CharField(max_length=100, verbose_name=u'类型名称')

	class Meta:
		verbose_name_plural = u'产品种类'

	def __unicode__(self):
		return self.type_name

class Scene(models.Model):
	scene_id = models.IntegerField(verbose_name=u'景点ID')
	scene_telphone = models.CharField(max_length=100, verbose_name=u'联系方式')
	scene_place = models.CharField(max_length=100, verbose_name=u'所在地')
	scene_price = models.FloatField(verbose_name=u'价格')
	scene_opentime = models.CharField(max_length=100, verbose_name=u'开放时间')
	scene_introduce = models.TextField(verbose_name=u'介绍')
	scene_activity_type = models.IntegerField(verbose_name=u'活动种类')
	scene_imagepath1 = models.CharField(max_length=100, verbose_name=u'图片1')
	scene_imagepath2 = models.CharField(max_length=1000, verbose_name=u'图片2')
	scene_videopath = models.CharField(max_length=100, verbose_name=u'视频')

	class Meta:
		verbose_name_plural = u'景点'

	def __unicode__(self):
		return self.scene_name

class Scene_comment(models.Model):
	user_id = models.IntegerField(verbose_name=u'用户ID')
	scene_id = models.IntegerField(verbose_name=u'景点ID')
	comment = models.TextField(verbose_name=u'评论')
	submit_time = models.DateTimeField(verbose_name=u'提交时间')

	class Meta:
		verbose_name_plural = u'景点评论'

	def __int__(self):
		return self.user_id

class User(models.Model):
	user_id = models.IntegerField(verbose_name=u'用户ID')
	username = models.CharField(max_length=100, verbose_name=u'用户名')
	password = models.CharField(max_length=100, verbose_name=u'密码')
	sex = models.CharField(max_length=100, verbose_name=u'性别')
	age = models.IntegerField(verbose_name=u'年龄')
	email = models.CharField(max_length=100, verbose_name=u'邮箱')
	telphone = models.CharField(max_length=100, verbose_name=u'电话')
	bankcard_num = models.CharField(max_length=100, verbose_name=u'银行卡号')
	user_type = models.IntegerField(verbose_name=u'用户类别')
	user_score = models.IntegerField(verbose_name=u'用户积分')
	user_level = models.IntegerField(verbose_name=u'用户等级')

	class Meta:
		verbose_name_plural = u'用户'

	def __unicode__(self):
		return self.username

class Merchant(models.Model):
	merchant_login_name = models.CharField(max_length=100, verbose_name=u'商户登录名')
	merchant_company_name = models.CharField(max_length=100, verbose_name=u'商户公司名')
	merchant_password = models.CharField(max_length=100, verbose_name=u'商户密码')
	merchant_email = models.CharField(max_length=100, verbose_name=u'邮箱')
	merchant_intro = models.TextField(verbose_name=u'简介')
	merchant_address = models.CharField(max_length=100, verbose_name=u'商户地址')
	merchant_telphone = models.CharField(max_length=100, verbose_name=u'联系方式')

	class Meta:
		verbose_name_plural = u'商户'
		
	def __unicode__(self):
		return self.merchant_login_name

class Scene_item(models.Model):
	scene_name = models.CharField(max_length=100, verbose_name=u'景点名称')
	scene_keyword = models.CharField(max_length=100, verbose_name=u'关键字')
	scene_score = models.FloatField(max_length=100, verbose_name=u'评分')
	scene_comment_num = models.CharField(max_length=100, verbose_name=u'评论数')
	scene_price = models.CharField(max_length=100, verbose_name=u'价格')
	scene_imagepath = models.CharField(max_length=100, verbose_name=u'图片路径')
	scene_category = models.IntegerField(verbose_name=u'景点类别')
	scene_lon = models.FloatField(verbose_name=u'经度')
	scene_lat = models.FloatField(verbose_name=u'纬度')
	scene_city = models.CharField(max_length=100, verbose_name=u'所在城市')

	class Meta:
		verbose_name_plural = u'景点条目'

	def __unicode__(self):
		return self.scene_name 

class Place_category(models.Model):
	place_id = models.IntegerField(verbose_name=u'场所ID')
	place_name = models.CharField(max_length=100, verbose_name=u'场所名称')

	class Meta:
		verbose_name_plural = u'场所类别'

	def __int__(self):
		return self.place_id 

class Scene_markicon(models.Model):
	scene_id = models.IntegerField(verbose_name=u'景点ID')
	scene_icon = models.CharField(max_length=100, verbose_name=u'景点图标')

	class Meta:
		verbose_name_plural = u'景点标注'

	def __int__(self):
		return self.scene_id 

class User_album(models.Model):
	user_id = models.IntegerField(verbose_name=u'用户ID')
	album_name = models.CharField(max_length=100, verbose_name=u'相册名称')
	photo_path = models.CharField(max_length=100, verbose_name=u'相片路径')
	photo_describe = models.CharField(max_length=100, verbose_name=u'相片描述')
	photo_mapping = models.CharField(max_length=100, verbose_name=u'映射')

	class Meta:
		verbose_name_plural = u'照片'

	def __int__(self):
		return self.user_id 

class User_video(models.Model):
	user_id = models.IntegerField(verbose_name=u'用户ID')
	video_name = models.CharField(max_length=100, verbose_name=u'视频名称')
	video_path = models.CharField(max_length=100, verbose_name=u'视频路径')
	video_describe = models.CharField(max_length=100, verbose_name=u'视频描述')
	video_thumb = models.CharField(max_length=100, verbose_name=u'缩略图')

	class Meta:
		verbose_name_plural = u'视频'

	def __int__(self):
		return self.user_id 

class User_order(models.Model):
	user_id = models.IntegerField(verbose_name=u'用户ID')
	equipment_id = models.IntegerField(verbose_name=u'设备ID')
	order_time = models.CharField(max_length=100, verbose_name=u'订单时间')
	order_remark = models.CharField(max_length=100, verbose_name=u'备注')
	number = models.IntegerField(verbose_name=u'数量')
	state = models.CharField(max_length=100, verbose_name=u'状态')
	equipment_name = models.CharField(max_length=100, verbose_name=u'设备名')
	equipment_price = models.FloatField(verbose_name=u'设备价格')

	class Meta:
		verbose_name_plural = u'订单'

	def __int__(self):
		return self.user_id 
