from django import forms


def min_length_3_validator(value):
    if len(value) < 3:
            raise forms.ValidationError('3글자 이상 입력해주세요')


class PostForm(forms.Form):
    class Meta:
        title = forms.CharField(validators=[min_length_3_validator])
        content = forms.CharField(widget=forms.Textarea )  # widget으로 CharField 이지만 모형은 Textarea 로 출력
