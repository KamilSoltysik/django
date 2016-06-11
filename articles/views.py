from django.shortcuts import render
from django.utils import timezone
from .models import Post,User
from .forms import PostForm, UserForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from reportlab.pdfgen import canvas
from django.http import HttpResponse


def pdf(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="pdfexport.pdf"'
	pdf = canvas.Canvas(response)
	pdf.drawString(10,820, "Wykaz osób piszacych artykuly")
	i=0
	users = User.objects.all().order_by("-name")
	pdf.setFont('Verdana', 12)
	for user in users:
		pdf.drawString(50, 750+i, user.name)
		i=i+20
	pdf.showPage()

	pdf.save()
	return response
	
def post_list(request):
	posts = Post.objects.all().order_by('published_date')
	users = User.objects.all().order_by("-nickname")
	return render(request, 'post_list.html', {'posts': posts, 'users': users})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	users = User.objects.all().order_by("-nickname")
	return render(request, 'post_detail.html', {'post': post, 'users': users})
	
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			created_date =timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'post_new.html', {'form': form})
	
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'post_edit.html', {'form': form})
	
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('articles.views.post_list')
	
def users(request):
	users = User.objects.all().order_by("-nickname")
	return render(request, 'users.html', {'users': users})
	

	
def user_detail(request, pk):
	user = get_object_or_404(User, pk=pk)
	return render(request, 'user_detail.html', {'user': user})
	
	
def user_new(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('users')
	else:
		form = UserForm()
	return render(request, 'user_new.html', {'form': form})
	
	
	
def user_edit(request, pk):
	post = get_object_or_404(User, pk=pk)
	if request.method == "POST":
		form2 = UserForm(request.POST, instance=post)
		if form2.is_valid():
			post = form2.save(commit=False)
			post.save()
			return redirect('users')
	else:
		form2 = UserForm(instance=post)
	return render(request, 'user_edit.html', {'form2': form2})
	


def user_remove(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('articles.views.users')