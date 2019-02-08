from django.shortcuts import render,get_object_or_404
from post.models import Post,Comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from post.forms import CommentForm

# Create your views here.
from taggit.models import Tag
def post_list_view(request,tag_slug=None):
    post_list=Post.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])
    paginator=Paginator(post_list,3)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'post/post_list.html',{'post_list':post_list,'tag':tag})

#from django.views.generic import ListView
#class Postlistview(ListView):
#    model=Post
#    paginate_by=2
from post.forms import Emailsendview
from django.core.mail import send_mail

def Email_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method=='POST':
        form=Emailsendview(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject="Your Account hacked"
            post_url=request.build_absolute_uri(post.get_absolute_url())
            message="Your mail got hacked and I have your entire information with me, \ncheck your details in the below link \n{} you don't have any choice otherthan to surender me.\n Get ready dude".format(post_url)
            send_mail(subject,message,'hackpd739@gmail.com',[cd['to']])
            sent=True
    else:
        form=Emailsendview()
    return render(request,'post/sharepost.html',{'post':post,'form':form,'sent':sent})

def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day,)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else:
        form=CommentForm()
    return render(request,'post/post_detail.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments
    })
