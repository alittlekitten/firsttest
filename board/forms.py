from django import forms
from .models import Board

class BoardPost(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title','body'] 
        # 메타클래스는 클래스의 클래스! 검색해서 찾아보자!
        # 어떤 모델을 기반으로 Form을 생성할지 model에 적고, 
        # 입력받기를 원하는 속성만 fields에 작성한다.