from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
def index(request):
    return HttpResponse(
        '''
            <!doctype html>
            <h1>A new project 'Shop' has been created successfully.</h1>
            <form method=post enctype=multipart/form-data>
              <input type=file name=file>
              <input type=submit value=Upload>
            </form>
            '''

    )

#
# if request.method == 'POST':
#     form = PostForm(request.POST)
#     messages.success(request, "A new project 'Shop' has been created successfully.")
#     return redirect('posts')
# else:
#     return render(request, 'blog/post_form.html',{'form':form}')