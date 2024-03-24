from django.contrib import admin
from django.db.models import Count
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from digishop.apps.catalog.models import Category, ProductClass, Option, ProductAttribute, ProductRecommendations, \
    Product, ProductAttributeValue, ProductImage


# Register your models here.

class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)


admin.site.register(Option)


class ProductAttributeInline(admin.StackedInline):
    model = ProductAttribute
    extra = 2


class AttributeCountFilter(admin.SimpleListFilter):
    title = 'Attribute Count'
    parameter_name = 'attribute_count'

    def lookups(self, request, model_admin):
        return [
            ('more_2', 'More 2 Attributes'),
            ('less_2', 'Less 2 Attributes')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'more_2':
            return queryset.annotate(attribute_count=Count('attributes')).filter(attribute_count__gt=2)
        if self.value() == 'less_2':
            return queryset.annotate(attribute_count=Count('attributes')).filter(attribute_count__lte=2)


@admin.register(ProductClass)
class ProductClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'require_shipping', 'track_stock', 'attribute_count')
    list_filter = ('require_shipping', 'track_stock', AttributeCountFilter)
    inlines = [ProductAttributeInline]
    actions = ['enable_track_stock', 'disable_track_stock']
    prepopulated_fields = {'slug': ('title',)}

    def attribute_count(self, obj):
        return obj.attributes.count()

    def enable_track_stock(self, request, queryset):
        queryset.update(track_stock=True)

    def disable_track_stock(self, request, queryset):
        queryset.update(track_stock=False)


class ProductRecommendedInline(admin.StackedInline):
    model = ProductRecommendations
    extra = 2
    fk_name = 'primary'


class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    extra = 2


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 2


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    inlines = [ProductAttributeValueInline, ProductImageInline, ProductRecommendedInline]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
