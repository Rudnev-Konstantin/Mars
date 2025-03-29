from flask import Blueprint
from . import forms

from flask import render_template
from flask import url_for


bp = Blueprint('main', __name__)


@bp.route("/")
@bp.route("/index/")
@bp.route("/<title>")
@bp.route("/index/<title>")
def index(title=''):
    return render_template(
        "index.html",
        title=title
        )

@bp.route("/training/<prof>")
def training(prof):
    if "инженер" in prof or "строитель" in prof:
        prof_type = "engineering"
    else:
        prof_type = "ology"
    
    return render_template(
        "training.html",
        title="training",
        image_path=url_for("static", filename="images/MARS-2-2.png"),
        prof=prof_type
    )

@bp.route("/list_prof/<sp_style>")
def list_prof(sp_style):
    list_prof = [
        "пилот",
        "строитель",
        "врач",
    ]
    
    if sp_style not in {"ol", "ul"}:
        sp_style = "None"
    
    return render_template(
        "list_prof.html",
        sp_style=sp_style,
        list_prof=list_prof
    )

@bp.route("/auto_answer")
@bp.route("/answer")
def answer():
    user_data = {
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": " Всегда мечтал застрять на Марсе!",
        "ready": True,
    }
    
    return render_template(
        "auto_answer.html",
        title="Анкета",
        style_path=url_for("static", filename="css/style_answer.css"),
        user_data=user_data
    )

@bp.route("/login", methods=['GET', 'POST'])
def emergency_access_form():
    form = forms.EmergencyAccessForm()
    
    if form.validate_on_submit():
        return "<h1>Форма отправлена</h1>"
    return render_template(
        "forms/emergency_access.html",
        title="Аварийный доступ",
        form=form,
        emblem_path=url_for("static", filename="images/MARS-2-7.png")
        )

@bp.route("/distribution")
def distribution():
    sp_astronauts = [
        "Ридли Скотт",
        "Энди Уир",
        "Марк Уотни",
        "Венката Капур",
        "Тедди Сандерс",
        "Шон Бин",
        "Кто-то Ещё"
    ]
    
    return render_template(
        "distribution.html",
        sp_astronauts=sp_astronauts
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
