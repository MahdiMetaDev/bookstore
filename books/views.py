from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse

from .models import Book, Comment
from .forms import CommentForm

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books_num'] = Book.objects.all().count()
        return context
        

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    slug_field = 'slug'
    context_object_name = 'book'
    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            book = self.get_object()
            form.instance.user = request.user
            form.instance.book = book
            form.save()

            return redirect(reverse('book_detail', kwargs={
                'slug': book.slug,
            }))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context


# def book_detail_view(request, pk):
#     book = get_object_or_404(Book, pk=pk)

#     book_comments = book.comments.all()
    
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.book = book
#             new_comment.user = request.user
#             new_comment.save()
#             comment_form = CommentForm()
#     else:
#         comment_form = CommentForm()

#     return render(request, 'books/book_detail.html', context={
#         'book': book,
#         'comments': book_comments,
#         'comment_form': comment_form,
#     })


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover', 'slug', ]
    template_name = 'books/book_create.html'
    slug_field = 'slug'
    

class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover', ]
    template_name = 'books/book_update.html'
    

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('books_list')
