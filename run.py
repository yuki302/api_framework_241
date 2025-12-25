import pytest
import os
import allure_pytest
pytest.main()

os.system('allure generate -c -o report temps')