import pytest

# 最基本的fixture
@pytest.fixture
def sample_user():
    """返回一个用户字典"""
    print("setup")
    return {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com"
    }
    print("teardowm")

# 使用fixture
def test_user_name(sample_user):
    assert sample_user["name"] == "Alice"

def test_user_email(sample_user):
    assert "@" in sample_user["email"]