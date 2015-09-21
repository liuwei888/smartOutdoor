from django.contrib import admin
from outdoor.models import *

# Register your models here.

class Activity_categoryAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'equipment_id', 'start_time', 'end_time')
	ordering = ('user_id', )
	search_fields = ('user_id', )

class EquipmentAdmin(admin.ModelAdmin):
	list_display = ('equipment_id', 'place_id', 'equipment_name', 'equipment_intro', 'equipment_owner', 'equipment_is_available', 'equipment_lat', 'equipment_lon', 'equipment_imagepath', 'equipment_location')
	ordering = ('equipment_name', )
	search_fields = ('equipment_name', )

class Equipment_orderAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'equipment_id', 'start_time', 'end_time')
	ordering = ('user_id', )
	search_fields = ('user_id', )

class ProductAdmin(admin.ModelAdmin):
	list_display = ('product_name', 'product_type', 'product_photo', 'product_price', 'product_num', 'product_introduce')
	ordering = ('product_name', )
	search_fields = ('product_name', )

class Product_categoryAdmin(admin.ModelAdmin):
	list_display = ('type_name', )
	ordering = ('type_name', )
	search_fields = ('type_name', )

class SceneAdmin(admin.ModelAdmin):
	list_display = ('scene_id', 'scene_telphone', 'scene_place', 'scene_price', 'scene_opentime', 'scene_introduce', 'scene_activity_type', 'scene_imagepath1', 'scene_imagepath2', 'scene_videopath',)
	ordering = ('scene_id', )
	search_fields = ('scene_name', )
	
class Scene_commentAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'scene_id', 'comment', 'submit_time', )
	ordering = ('user_id', )
	search_fields = ('user_id', )

class UserAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'username', 'password', 'sex', 'age', 'email', 'telphone', 'bankcard_num', 'user_type', 'user_score', 'user_level', )
	ordering = ('username', )
	search_fields = ('username', )

class MerchantAdmin(admin.ModelAdmin):
	list_display = ('merchant_login_name', 'merchant_company_name', 'merchant_email', 'merchant_intro', 'merchant_address', 'merchant_telphone', )
	ordering = ('merchant_login_name', )
	search_fields = ('merchant_login_name', )

class Scene_itemAdmin(admin.ModelAdmin):
	list_display = ('scene_name','scene_keyword', 'scene_score', 'scene_comment_num', 'scene_price', 'scene_imagepath', 'scene_category', 'scene_lon', 'scene_lat', 'scene_city')
	ordering = ('scene_name', )
	search_fields = ('scene_name', )

class Place_categoryAdmin(admin.ModelAdmin):
	list_display = ('place_id','place_name')
	ordering = ('place_name', )
	search_fields = ('place_name', )

class Scene_markiconAdmin(admin.ModelAdmin):
	list_display = ('scene_id','scene_icon')
	ordering = ('scene_id', )
	search_fields = ('scene_id', )

class User_albumAdmin(admin.ModelAdmin):
	list_display = ('user_id','album_name', 'photo_path', 'photo_describe', 'photo_mapping')
	ordering = ('user_id', )
	search_fields = ('user_id', )

class User_videoAdmin(admin.ModelAdmin):
	list_display = ('user_id','video_name', 'video_path', 'video_describe', 'video_thumb')
	ordering = ('user_id', )
	search_fields = ('user_id', )

class User_orderAdmin(admin.ModelAdmin):
	list_display = ('user_id','equipment_id', 'order_time', 'order_remark', 'number', 'state', 'equipment_price')
	ordering = ('user_id', )
	search_fields = ('user_id', )

admin.site.register(Activity_category, Activity_categoryAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Equipment_order, Equipment_orderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Product_category, Product_categoryAdmin)
admin.site.register(Scene, SceneAdmin)
admin.site.register(Scene_comment, Scene_commentAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Merchant, MerchantAdmin)
admin.site.register(Scene_item, Scene_itemAdmin)
admin.site.register(Place_category, Place_categoryAdmin)
admin.site.register(Scene_markicon, Scene_markiconAdmin)
admin.site.register(User_album, User_albumAdmin)
admin.site.register(User_video, User_videoAdmin)
#admin.site.register(User_order, User_orderAdmin)
