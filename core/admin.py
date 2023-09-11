from django.contrib import admin
from .models import Product,Order,Pages,MaintenceMode , ProductImages
from django.contrib.auth.models import User , Group
from .forms import ProductForm

# Register your models here.


class Pagesadmin(admin.ModelAdmin):
    def has_add_permission(self, request):

        if Pages.objects.count()<1:
            return True 
        else:
            return False

admin.site.register(Pages,Pagesadmin)
admin.site.register(MaintenceMode)
admin.site.unregister(User)
admin.site.unregister(Group)







@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name',)
    add_form_template = 'admin/post_form.html'
    change_form_template = 'admin/post_form.html'

    def get_form(self, request, obj=None, **kwargs):
        try:
            instance = kwargs['instance']
            return ProductForm(instance=instance)
        except KeyError:
            return ProductForm

    def add_view(self, request, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context['form'] = self.get_form(request)
        return super(PostAdmin, self).add_view(request, form_url=form_url, extra_context=extra_context)
    
    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = extra_context or {}
        post = Product.objects.get(id=object_id)
        extra_context["form"] = self.get_form(instance=post, request=request)
        return super(PostAdmin, self).change_view(request, object_id, form_url=form_url, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        obj.save()
        pictures = request.FILES.getlist('pictures')
        for picture in pictures:
            ProductImages.objects.create(product=obj, pics=picture)
        return super().save_model(request, obj, form, change)