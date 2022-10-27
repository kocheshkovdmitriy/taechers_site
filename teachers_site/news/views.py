from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View, generic
from .models import New, Commit
from .forms import NewForm, CommitForm
from django.contrib.auth import authenticate

def new_list(request):
    news = New.objects.all()
    return render(request, "news/news_list.html", {'news': news})

class NewsDetailView(generic.DetailView):
    model = New
    template_name = 'news/news_detail.html'


class NewFormView(View):
    def get(self, request):

        new_form = NewForm()
        return render(request, 'news/edit_new.html', context={'new_form': new_form})

    def post(self, request):
        new_form = NewForm(request.POST)
        if new_form.is_valid():
            New.objects.create(**new_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'news/edit_new.html', context={'new_form': new_form})

class NewEditView(View):
    def get(self, request, pk):
        new = New.objects.get(id=pk)
        new_form = NewForm(instance=new)
        return render(request, 'news/edit_new.html', context={'new_form': new_form, 'pk': pk})

    def post(self, request, pk):
        new = New.objects.get(id=pk)
        new_form = NewForm(request.POST, instance=new)
        if new_form.is_valid():
            new_form.save()
        return render(request, 'news/edit_new.html', context={'new_form': new_form, 'pk': pk})


class CommitFormView(View):
    def get(self, request, pk):
        new = New.objects.get(id=pk)
        commit_form = CommitForm(initial={'new': new})
        return render(request, 'news/create_commit.html', context={'commit_form': commit_form,
                                                                       'pk': pk})

    def post(self, request, pk):
        new = New.objects.get(id=pk)
        commit_form = CommitForm(request.POST, initial={'new': new})
        if commit_form.is_valid():
            commit = Commit(**commit_form.cleaned_data)
            if request.user.is_authenticated:
                commit.user = request.user
                commit.user_name = request.user.first_name
            commit.save()
            return HttpResponseRedirect(f'/news/{pk}')
        return render(request, 'news/create_commit.html', context={'commit_form': commit_form,
                                                                       'pk': pk})