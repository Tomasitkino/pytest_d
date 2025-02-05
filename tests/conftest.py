import pytest
import allure
#
# # Фикстура для добавления данных об окружении
# @pytest.fixture(scope="session", autouse=True)
# def set_environment():
#     # Добавляем информацию об окружении
#     allure.add_environment("OS", "Windows 10")
#     allure.add_environment("Browser", "Chrome 95")
#     allure.add_environment("Python Version", "3.8")
#     allure.add_environment("JDK", "11")  # Если это важно для вашего проекта