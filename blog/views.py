from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import NameForm, DupaForm, PepekForm
from .models import Post, Catego, Question, Choice
# from .forms import CategoForm, PostForm



def index(request):
    posts = Post.objects.all()[:3]
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def posts(request):
    posts = Post.objects.order_by('created_on')
    context = {'posts': posts}
    return render(request, 'blog/posts.html', context)


def categories(request):
    kategorie = Catego.objects.all()
    context = {'categories': kategorie}
    return render(request, 'blog/categories.html', context)

# def test(request):
#     return render(request, 'blog/gdxg.html')


def catego(request, catego_id):
    catego = Catego.objects.get(id=catego_id)
    posts = catego.post_set.order_by('-created_on')
    for p1 in posts:
        if len(p1.text) > 50:
            p1.text = p1.text[:50] + '...'
    context = {'catego': catego, 'posts': posts}
    return render(request, 'blog/catego.html', context)


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.order_by('created_on')
    context = {'post': post, 'comments': comments}
    return render(request, 'blog/post.html', context)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'blog/detail.html'

class ResultsView(generic.DeleteView):
    model = Question
    template_name = 'blog/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'blog/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('blog:results', args=(question_id,)))



class IndexView(generic.ListView):
    template_name = 'blog/index2.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]



def new_catego(request):
    if request.method != 'POST':
        # No data submited creat a blank form
        form = DupaForm()
    else:
        # POST data submited; process data.
        form = DupaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:catego'))

    context = {'form': form}
    return render(request, 'blog/new_catego.html', context)


def new_post(request, catego_id):
    catego = Catego.objects.get(id=catego_id)

    if request.method != 'POST':
        # no data submited, creat a blank .
        form = PepekForm()
    else:
        # post submited, process data.
        form = PepekForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.catego = catego
            new_post.save()
            return HttpResponseRedirect(reverse('blog:catego',
                                        args=[catego_id]))

    context = {'catego': catego, 'form': form}
    return render(request, 'blog/new_post.html', context)


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'blog/name.html', {'form': form})
