from django.shortcuts import get_object_or_404, render
from .models import Board
# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request,'boards/home.html',{'boards':boards})

# def board_topics(request,board_id):
#     boards = get_object_or_404(pk=board_id)
#     return render(request,'boards/board_topic.html',{'boards':boards})