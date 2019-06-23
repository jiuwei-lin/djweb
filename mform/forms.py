from django import forms
from .models import Post


class ContactForm(forms.Form):
    CITY = [
        ['TP', 'Taipei'],
        ['TN', 'Tainan'],
    ]
    user_name = forms.CharField(label='name', max_length=50, initial='John')
    user_city = forms.ChoiceField(label='city', choices=CITY)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['mood', 'nickname', 'message', 'del_pass']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = '現在心情'
        self.fields['nickname'].label = '暱稱'
        self.fields['message'].label = '留言'
        self.fields['del_pass'].label = '設定密碼'
