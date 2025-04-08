import pytest

from app import create_app
from app.data.models.jobs import Jobs
from app.data.models.user import User


@pytest.fixture
def client():
    # Создаём временную БД в памяти
    app = create_app("testing", db_cone_url="sqlite:///:memory:")
    
    with app.app_context():
        with app.db_connect.get_session() as session:
            test_user = User(id=1, name="Test User")
            test_jobs = [
                Jobs(
                    id=1,
                    team_leader=1,
                    job="Initial Job",
                    work_size=10,
                    collaborators="2,3",
                    is_finished=False
                ),
                Jobs(
                    id=2,
                    team_leader=1,
                    job="Finished Job",
                    work_size=5,
                    collaborators="4",
                    is_finished=True
                )
            ]
            
            session.add_all([test_user, *test_jobs])
            session.commit()
        
        session.begin_nested()
        yield app.test_client()
        session.rollback()
        session.close()
