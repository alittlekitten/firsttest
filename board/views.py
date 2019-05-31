from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Board
from .forms import BoardPost

# Create your views here.
def home(request):
    boards=Board.objects
    board_list=Board.objects.all()
    paginator = Paginator(board_list,3)
    page = request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'home.html',{'boards':boards,'posts':posts})

def detail(request, board_id):
    board_detail=get_object_or_404(Board, pk=board_id)
    return render(request,'detail.html',{'board':board_detail})

def new(request):
    return render(request, 'new.html')
    
def create(request):
    # board라는 변수에 Board Model class를 저장하는 겁니다.
    board = Board()
    # Get 방식을 사용하여 name='title'에 적힌 정보를 board.title로 저장하겠다
    board.title = request.GET['title']
    board.body = request.GET['body']
    board.pub_date = timezone.datetime.now()
    board.save()
    return redirect('/detail/' + str(board.id))

def delete(request, board_id):
    board_delete = get_object_or_404(Board,pk=board_id)
    board_delete.delete()
    return redirect('home') 

def update(request,board_id):
    board_update=get_object_or_404(Board,pk=board_id)
    return render(request,'update.html',{"boardupdate":board_update})

def updatesend(request, board_id):
    updatesendboard=get_object_or_404(Board,pk=board_id)
    updatesendboard.title=request.GET['updatetitle']
    updatesendboard.body=request.GET['updatebody']
    updatesendboard.pub_date=timezone.datetime.now()
    updatesendboard.save()
    return redirect('home') 
    
# 그럼 수정된걸 수정됐다고 표시하는 방법은 없을까? 
# 그러려면 db 안에 무슨 다른 값을 부여해야 하는가?

def boardpost(request):
    if request.method == 'POST':
        form = BoardPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BoardPost()
        return render(request,'new.html',{'form':form})
