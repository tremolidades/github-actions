from app.core.config import Settings

settings = Settings()


def test_info(test_app):
    response = test_app.get(settings.API_STR + "/info")
    assert response.status_code == 200
    assert response.json() == {"app_name": settings.PROJECT_NAME, "release": settings.release}
