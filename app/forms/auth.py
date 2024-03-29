"""
@File : auth.py
@Author: Zyeoh
@Desc :
@Date : 2019/9/27
"""
from wtforms import Form, StringField, PasswordField
from wtforms.validators import length, DataRequired, Email, ValidationError, EqualTo, Length

from app.models.user import User


class RegisterForm(Form):
    email = StringField(
        'email',
        validators=[
            DataRequired(),
            length(8, 64),
            Email(message='电子邮箱不符合规范')
        ])

    password = PasswordField(
        'password',
        validators=[
            DataRequired(message='密码不可以为空，请输入你的密码哦'),
            length(6, 32)
        ])

    nickname = StringField(
        'nickname',
        validators=[
            DataRequired(),
            length(2, 10, message='昵称至少两个字符，最多十个字符')
        ])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已经被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已经存在')


# 重置密码邮箱验证
class EmailForm(Form):
    email = StringField(
        'email',
        validators=[
            DataRequired(),
            length(8, 64),
            Email(message='电子邮箱不符合规范')
        ])


class LoginForm(EmailForm):
    email = StringField(
        'email',
        validators=[
            DataRequired(),
            length(8, 64),
            Email(message='电子邮箱不符合规范')
        ])
    password = PasswordField(
        'password',
        validators=[
            DataRequired(message='密码不可以为空，请输入你的密码哦'),
            length(6, 32)
        ])


# 重置密码，验证密码，确认密码
class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[
        DataRequired(),
        length(6, 32, message='密码长度至少需要在6到32字符之间'),
        EqualTo('password2', message='两次密码不相同')])
    password2 = PasswordField(validators=[
        DataRequired(), Length(6, 32)])


class ChangePasswordForm(Form):
    pass