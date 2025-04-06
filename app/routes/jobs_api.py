from flask import Blueprint

from ..data.db import DataBaseConnect
from ..data.models.jobs import Jobs


bp = Blueprint('news_api', __name__, url_prefix="/api")


@bp.route('/jobs')
def get_news():
    return "Обработчик в news_api"
