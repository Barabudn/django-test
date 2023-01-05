from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('-date')  #[:2] ограничить количество записей на странице
    return render(request, 'news/news_home.html', {'news': news})



class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/news-delete.html'
    success_url = '/news/'


def test(request):
    return render(request, 'testapp/test.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена неверно'



    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }


    return render(request, 'news/create.html', data)
