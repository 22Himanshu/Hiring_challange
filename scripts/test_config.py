import os
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.utils.config import settings


def test_config_loading():
    """
    Tests if the configuration settings are loaded correctly.
    """
    print("Testing configuration loading...")
    try:
        assert settings.database_url is not None
        assert "sqlite" in settings.database_url
        assert settings.gemini_api_key is not None
        print("✅ `database_url` and `gemini_api_key` are present.")

        assert isinstance(settings.rate_limit_per_user, int)
        print(f"✅ `rate_limit_per_user` is an integer: {settings.rate_limit_per_user}")

        print("\nConfiguration settings loaded successfully:")
        print(f"  - Environment: {settings.environment}")
        print(f"  - Debug Mode: {settings.debug}")
        print(f"  - Database URL: {settings.database_url}")

        print("\nConfiguration test passed! ✅")

    except Exception as e:
        print(f"\nConfiguration test failed! ❌")
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    test_config_loading()
