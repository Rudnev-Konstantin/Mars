from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    
    speciality = StringField('Специальность', validators=[DataRequired()])
    
    email = EmailField('Почта', validators=[DataRequired()])
    
    password = PasswordField('Пароль', validators=[DataRequired()])
    
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
