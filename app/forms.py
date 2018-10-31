from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


class SearchForm(forms.Form):
    stage = forms.CharField(max_length=200, required=False)
    week = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=50, required=True)


class JournalForm(forms.Form):
    ChangePlanChoices = (
        ('无', '无'),
        ('未完成', '未完成'),
        ('改期', '改期'),
        ('中断', '中断'),
    )

    OutPlanTypeChoices = (
        ('无', '无'),
        ('被要求', '被要求'),
        ('工作需求', '工作需求'),
    )

    PlanName = forms.CharField(max_length=200, required=True)
    PlanModule = forms.CharField(max_length=50, required=False)
    PlanBody = forms.CharField(max_length=200, required=False)
    PlanTime = forms.CharField(max_length=50, required=False)

    ChangePlanType = forms.ChoiceField(choices=ChangePlanChoices, required=False)
    ChangePlanModule = forms.CharField(max_length=50, required=False)
    ChangePlanBody = forms.CharField(max_length=200, required=False)
    ChangePlanTime = forms.CharField(max_length=50, required=False)

    OutPlanType = forms.ChoiceField(choices=OutPlanTypeChoices, required=False)
    OutPlanModule = forms.CharField(max_length=50, required=False)
    OutPlanBody = forms.CharField(max_length=200, required=False)
    OutPlanTime = forms.CharField(max_length=50, required=False)

    Week = forms.DateTimeField(required=False)
    Date = forms.DateTimeField(required=False)
    Module = forms.CharField(max_length=50, required=False)
    Content = forms.CharField(max_length=200, required=False)
    time = forms.IntegerField(required=False)