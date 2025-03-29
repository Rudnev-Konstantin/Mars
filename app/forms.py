from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class EmergencyAccessForm(FlaskForm):
    id_astronaut = StringField('id Астронавта', validators=[DataRequired()])
    password_astronaut = PasswordField(
        'Пароль Астронавта',
        validators=[DataRequired()]
        )
    
    id_captain = StringField('id Капитана', validators=[DataRequired()])
    password_captain = PasswordField(
        'Пароль Капитана',
        validators=[DataRequired()]
        )
    
    submit = SubmitField('Войти')
