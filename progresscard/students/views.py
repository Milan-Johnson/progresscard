from django.shortcuts import render

# Create your views here.
def postmarks(request):
    
    if request.method == 'POST':
        malayaam = request.POST['malayalam']
        english = request.POST['english']
        hindi = request.POST['hindi']
        maths = request.POST['maths']
        science = request.POST['science']
        socialacience = request.POST['socialscience']

    else:
        pass
        return render (request,'postmarks.html')