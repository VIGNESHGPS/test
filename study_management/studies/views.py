import logging
from django.shortcuts import render, redirect, get_object_or_404
from .models import Study
from .forms import StudyForm

logger = logging.getLogger(__name__)

def delete_multiple_studies(request):
    try:
        if request.method == 'POST':
            study_ids = request.POST.getlist('study_ids')
            if study_ids:
                Study.objects.filter(id__in=study_ids).delete()
                return redirect('study_list')
    except Exception as e:
        logger.error(f"Error deleting multiple studies: {e}")
    return redirect('study_list')

def study_list(request):
    try:
        studies = Study.objects.all()
        return render(request, 'study_list.html', {'studies': studies})
    except Exception as e:
        logger.error(f"Error retrieving study list: {e}")
        return render(request, 'error.html')  # You can create an error template for user-friendly feedback

def add_study(request):
    try:
        if request.method == 'POST':
            form = StudyForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('study_list')
        else:
            form = StudyForm()
        return render(request, 'add_study.html', {'form': form})
    except Exception as e:
        logger.error(f"Error adding study: {e}")
        return render(request, 'error.html')

def delete_study(request, pk):
    try:
        datatodelete = get_object_or_404(Study, pk=pk)
        if request.method == 'POST':
            datatodelete.delete()
            return redirect('study_list')
        return render(request, 'delete_study.html', {'study': datatodelete})
    except Exception as e:
        logger.error(f"Error deleting study with id {pk}: {e}")
        return render(request, 'error.html')

def edit_study(request, pk):
    try:
        editbyid = get_object_or_404(Study, id=pk)

        if request.method == 'POST':
            form = StudyForm(request.POST, instance=editbyid)
            if form.is_valid():
                form.save()
                return redirect('study_list')
        else:
            form = StudyForm(instance=editbyid)

        return render(request, 'edit_study.html', {'form': form, 'study': editbyid})
    except Exception as e:
        logger.error(f"Error editing study with id {pk}: {e}")
        return render(request, 'error.html')

def view_study(request, pk):
    try:
        study = get_object_or_404(Study, id=pk)
        return render(request, 'view_study.html', {'study': study})
    except Exception as e:
        logger.error(f"Error viewing study with id {pk}: {e}")
        return render(request, 'error.html')
