from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import File
from .forms import FileForm

@login_required
def file_list(request):
    files = File.objects.filter(user=request.user)
    return render(request, 'files/file_list.html', {'files': files})

@login_required
def upload_file(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user
            file.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'files/upload_file.html', {'form': form})

@login_required
def delete_file(request, pk):
    file = get_object_or_404(File, pk=pk, user=request.user)
    file.delete()
    return redirect('file_list')

@login_required
def edit_file(request, pk):
    file = get_object_or_404(File, pk=pk, user=request.user)
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm(instance=file)
    return render(request, 'files/edit_file.html', {'form': form, 'file': file})
