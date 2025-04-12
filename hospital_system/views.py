from django.shortcuts import render

def home(request):
    """
    Renders the homepage with a fancy design.
    """
    # You could pass additional context data here if needed.
    return render(request, 'home.html', {})
