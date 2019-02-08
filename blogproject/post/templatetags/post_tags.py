from post.models import Post
from django import template
register=template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('post/latest_posts123.html')
def show_latest_posts():
    latest_posts=Post.objects.order_by('-publish')[:3]
    return {'latest_posts':latest_posts}

from django.db.models import Count
@register.assignment_tag
def most_comments_post(count=4):
    return Post.objects.annotate(most_comment=Count('comments')).order_by('-most_comment')[:count]
