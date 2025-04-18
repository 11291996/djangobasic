from forums.models import Forum, Comment

from django.views import View
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from forums.forms import CommentForm
from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

class ForumListView(OwnerListView):
    model = Forum
    template_name = "forums/list.html"

class ForumDetailView(OwnerDetailView):
    model = Forum
    template_name = "forums/detail.html"
    def get(self, request, pk) :
        #get primary key of the forum from url
        x = Forum.objects.get(id=pk)
        #get all comments for the forum
        comments = Comment.objects.filter(forum=x).order_by('-updated_at')
        #our form to add a comment
        comment_form = CommentForm()
        context = { 'forum' : x, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)

class ForumCreateView(OwnerCreateView):
    model = Forum
    fields = ['title', 'text']
    template_name = "forums/form.html"

class ForumUpdateView(OwnerUpdateView):
    model = Forum
    fields = ['title', 'text']
    template_name = "forums/form.html"

class ForumDeleteView(OwnerDeleteView):
    model = Forum
    template_name = "forums/delete.html"

#gets the comment from detail.html and saves it to the database
#must be logged in to comment
class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Forum, id=pk)
        #our created model
        comment = Comment(text=request.POST['comment'], owner=request.user, forum=f)
        comment.save()
        return redirect(reverse('forums:forum_detail', args=[pk]))

#deletes the comment from the database
class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "forums/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        forum = self.object.forum
        return reverse('forums:forum_detail', args=[forum.id])


