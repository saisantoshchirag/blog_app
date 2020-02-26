from django import forms
from captcha.fields import CaptchaField
from simplemathcaptcha.fields import MathCaptchaField
from simplemathcaptcha.widgets import MathCaptchaWidget
class AllauthSignupForm(forms.Form):
    captcha=MathCaptchaField(widget=MathCaptchaWidget(question_tmpl='What is %(num1)i %(operator)s %(num2)i ? '))
    error_messages = {'invalid': ('Please check your math and try again.'), 'invalid_number': ('Enter a whole number.')}

