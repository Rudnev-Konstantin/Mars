from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class AddJob(FlaskForm):
    job = StringField("Job Title", validators=[DataRequired()])
    
    team_leader_id = IntegerField("Team Leader id", validators=[DataRequired()])
    
    work_size = IntegerField("Work Size", validators=[DataRequired()])
    
    collaborations = StringField("Collaborations", validators=[DataRequired()])
    
    finish = BooleanField("Is Job finished?")
    
    submit = SubmitField('Submit')
