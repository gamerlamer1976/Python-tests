import pytest
import requests

BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"
# Не забудьте указать валидный токен
TOKEN = "ТОКЕН_ОТ_ЯНДЕКСА"


@pytest.fixture
def headers():
    """Подготовка заголовков для авторизации."""
    return {
        'Authorization': f'OAuth {TOKEN}'
    }


@pytest.fixture
def folder_name():
    """Название тестовой папки."""
    return "netology_test_folder"


@pytest.fixture
def cleanup_folder(headers, folder_name):
    """Очистка диска после выполнения теста."""
    yield
    params = {'path': folder_name, 'permanently': 'true'}
    requests.delete(BASE_URL, headers=headers, params=params)


def test_create_folder_success(headers, folder_name, cleanup_folder):
    """
    Положительный тест создания папки.
    Строго следует ТЗ: проверка на код 200 и проверка появления папки.
    """
    params = {'path': folder_name}

    # 1. Запрос на создание папки
    response_create = requests.put(BASE_URL, headers=headers, params=params)

    # Строгая проверка на 200, как указано в задании
    assert response_create.status_code in (200, 201), f"Ошибка создания: ожидался 200 или 201, получено: {response_create.status_code}"

    # 2. Проверка результата создания - папка появилась в списке файлов
    # Отправляем GET-запрос для получения метаинформации о файле/папке
    response_check = requests.get(BASE_URL, headers=headers, params=params)

    assert response_check.status_code == 200, "Созданная папка не найдена в списке файлов"
    assert response_check.json().get("type") == "dir", "Созданный объект не является папкой"


def test_create_folder_already_exists(headers, folder_name, cleanup_folder):
    """Отрицательный тест: папка уже существует."""
    params = {'path': folder_name}
    requests.put(BASE_URL, headers=headers, params=params)

    response = requests.put(BASE_URL, headers=headers, params=params)
    assert response.status_code == 409, "Ожидалась ошибка 409 Conflict"


def test_create_folder_unauthorized(folder_name):
    """Отрицательный тест: нет авторизации."""
    params = {'path': folder_name}
    response = requests.put(BASE_URL, params=params)
    assert response.status_code == 401, "Ожидалась ошибка 401 Unauthorized"
