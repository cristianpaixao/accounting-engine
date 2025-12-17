from app.core.settings import get_settings


def test_settings_defaults():
    settings = get_settings()
    assert settings.app_name
    assert settings.environment
