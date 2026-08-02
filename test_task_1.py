import pytest
from task_1_code import fio, words_count, encrypt


@pytest.mark.parametrize(
    'initials, expected',
    [
        (['Гагарин', 'Юрий', 'Алексеевич'], 'ГЮА'),
        (['Бисмарк', 'Отто', 'фон'], 'БОф'),
        (['Пушкин', 'Александр', 'Сергеевич'], 'ПАС'),
    ]
)
def test_fio(initials, expected):
    """Тестирование функции создания инициалов."""
    assert fio(initials) == expected


@pytest.mark.parametrize(
    'phrase, expected',
    [
        ('Это простое предложение, без шуток', 5),
        ('Привет мир', 2),
        ('Тест', 1),
    ]
)
def test_words_count(phrase, expected):
    """Тестирование функции подсчета слов."""
    assert words_count(phrase) == expected


@pytest.mark.parametrize(
    'text, expected',
    [
        ("телефон", "тлфнеео"),  # Нечетное количество символов
        ("привет", "ветпри"),    # Четное количество символов
        ("код", "кдо"),          # Короткое нечетное
        ("а", "а"),              # Один символ
    ]
)
def test_encrypt(text, expected):
    """Тестирование функции шифрования текста."""
    assert encrypt(text) == expected
