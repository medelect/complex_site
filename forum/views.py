from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import ForumUser, ForumPost, ForumComment
from django.utils import timezone
from django.views import generic
from .forms import ForumUserForm

def index(request):
    return render(request, 'forum/index.html')

def color(request, clr):
    return HttpResponse('<h1><p style="color:#%s;">Color Text</p></h1>' % clr)

def posts(request):
    latest_post_list = ForumPost.objects.order_by('-date_create')[:5]
    template = loader.get_template('forum/posts.html')
    context = RequestContext(request,
                             {'latest_post_list': latest_post_list,}
                             )
    return HttpResponse(template.render(context))

def posts2(request):
    latest_post_list = ForumPost.objects.order_by('-date_create')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'forum/posts.html', context)

def post_vs_comments(request, pid = 0):
    print(request.path,'|',request.path_info)
    
    name_warn = 'none'
    if request.method == 'POST':
        name_warn = save_comment(request)

    post  = ForumPost.objects.get(id = pid)
    comments = ForumComment.objects.filter(post = pid)
    context = {'post': post, 'comments':comments, 'nm_wrn':name_warn}
    return render(request, 'forum/psto.html', context)

def dlp(nm):
    return HttpResponse('<p style="color:#f00;font-size:3em;'+
                        'font-weight:bold;text-align:center;'+
                        '">In developing, func is: %s </p>' % nm)

def save_comment(request):
    try:
        usr = ForumUser.objects.get(nick=request.POST['n_name'])
    except (KeyError, ForumUser.DoesNotExist):
        return 'block'
    ppp =  ForumPost.objects.get(id=request.POST['pst_id'])
    if usr.nick not in [i.nick for i in ForumUser.objects.all()]:
        return 'block'
    else:
        text = request.POST['com_text']
        tmp=ForumComment(user = usr,
            post = ppp,
            comment = text,
            date_create = timezone.now())
        tmp.save()
    
def start(request):
    return render(request, 'forum/start.html')

def input_post(request):
    return dlp('input_post')

class ForumCommentView(generic.ListView):
    template_name = 'forum/comments.html'
    context_object_name = 'ForumComment'
#    model = Comment

    def get_queryset(self):
        """Return all comments for post"""
        print(self.args,'|',self.kwargs)
        return ForumComment.objects.filter(post=self.kwargs['pst_id'])


def get_user(request):
    if request.method == 'POST':
        form = ForumUserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'forum/start.html')
    else:
        form = ForumUserForm()
    return render(request, 'forum/user.html', {'form':form})    


