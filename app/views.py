from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import Student
# Create your views here.
def home(request):
    return render(request, 'home.html')


def StudentView(request):

    if request.method == "POST":
        name = request.POST.get('name')
        place = request.POST.get('place')
        image = request.FILES.get('image')


        # ❌ 1. Check empty upload
        if not image:
            # messages.error(request, "Please select an image")
            return redirect("upload")

        # ❌ 2. File size limit (5MB example)
        if image.size > 5 * 1024 * 1024:
            # messages.error(request, "Image must be under 5MB")
            return redirect("upload")

        # ✅ Save safely
        Student.objects.create(
            name=name,
            image=image,
            place=place
        )

        # messages.success(request, "Photo uploaded successfully!")
        return redirect("stu")

    studata = Student.objects.all()  # Show latest first
    return render(request, "students.html", {"studata": studata})

