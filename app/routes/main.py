from flask import Blueprint, current_app

from sqlalchemy.orm import joinedload
from ..data.models.user import User
from ..data.models.jobs import Jobs

from flask_login import current_user, login_required, login_user, logout_user

from ..forms.login import LoginForm
from ..forms.register import RegisterForm
from ..forms.add_job import AddJob

from flask import render_template, url_for, redirect


bp = Blueprint('main', __name__)


@bp.route("/")
@bp.route("/index/")
@bp.route("/<title>")
@bp.route("/index/<title>")
def index(title=''):
    with current_app.db_connect.get_session() as session:
        jobs = session.query(Jobs).options(joinedload(Jobs.user)).all()
    
    models_struct_data = {
        "table_titles": [
            "Title of activity",
            "Team leader",
            "Duration",
            "List of collaborations",
            "is finished"
        ],
        "jobs": []
    }
    
    for job in jobs:
        job_struct = list()
        
        job_struct.append(job.id)
        job_struct.append(job.job)
        job_struct.append(job.user.surname + ' ' + job.user.name)
        job_struct.append(str(job.work_size) + " hours")
        job_struct.append(job.collaborators)
        job_struct.append("is finished" if job.is_finished else "is not finished")
        
        models_struct_data["jobs"].append(job_struct)
    
    return render_template(
        "index.html",
        title=title,
        data_jobs=models_struct_data,
        style_path=url_for("static", filename="css/style_table.css")
    )

@bp.route("/table/<gender>/<int:age>")
def table(gender, age):
    color = [250, 50, 20] if gender == "male" else [0, 100, 250]
    if age >= 21:
        transparent, martian = 1, url_for("static", filename="images/martians/big.png")
    else:
        transparent, martian = 0.5, url_for("static", filename="images/martians/little.png")
    
    return render_template(
        "table.html",
        color = "rgba" + str(tuple(color + [transparent])),
        style_path=url_for("static", filename="css/style_table.css"),
        image_path = martian
    )

@bp.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        with current_app.db_connect.get_session() as session:
            user = User()
            user.surname = form.surname.data
            user.name = form.name.data
            user.speciality = form.speciality.data
            user.email = form.email.data
            user.hashed_password = form.password.data
            
            session.add(user)
            session.commit()
        
        with current_app.db_connect.get_session() as session:
            user = session.query(User).filter(User.email == form.email.data).first()
            login_user(user, remember=form.remember_me.data)
        
        return redirect('/')
    return render_template("forms/register.html", title="Регистрация", form=form)

@bp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        with current_app.db_connect.get_session() as session:
            user = session.query(User).filter(User.email == form.email.data).first()
        
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        return render_template(
            "forms/login.html",
            message="Неправильный логин или пароль",
            form=form
        )
    return render_template("forms/login.html", title="Авторизация", form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@bp.route("/add_job", methods=['GET', 'POST'])
@login_required
def add_job():
    form = AddJob()
    if form.validate_on_submit():
        with current_app.db_connect.get_session() as session:
            job = Jobs()
            job.team_leader = form.team_leader_id.data
            job.job = form.job.data
            job.work_size = form.work_size.data
            job.collaborators = form.collaborations.data
            job.is_finished = form.finish.data
            
            current_user.jobs.append(job)
            session.merge(current_user)
            session.commit()
        
        return redirect('/')
    return render_template('forms/add_job.html', title='Добавление работы', form=form)
