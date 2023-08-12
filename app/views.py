from django.shortcuts import render

# Create your views here.
def MDB5(request):
    return render(request,'MDB5.html')

def backgroundimage(request):
    return render(request,'backgroundimage.html')

def carousel(request):
    return render(request,'carousel.html')

def spinners(request):
    return render(request,'spinners.html')

def card(request):
    return render(request,'card.html')
