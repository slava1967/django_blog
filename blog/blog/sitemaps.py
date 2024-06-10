from django.contrib.sitemaps import Sitemap

from main.models import Category, Post


class CategorySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Category.objects.all()


class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=Post.ACTIVE)

    def lastmod(self, obj):
        return obj.created_at


sitemaps = {
    "categories": CategorySitemap,
    "posts": PostSitemap
}
