from api import PetFriends
from settings import valid_email, valid_password
from settings import pet_name, pet_type, pet_age, invalid_photo

pf = PetFriends()


# Ввод пустого пароля
def test_get_api_key_without_password(email=valid_email, password=''):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


# Ввод неверного пароля
def test_get_api_key_with_wrong_password(email=valid_email, password=valid_password + '3'):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


#  Ввод незарегистрированной почты
def test_get_api_key_with_invalid_email(email='nagibator2000@yandex.ru', password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


# В поле {age} ввести буквы при добавлении нового питомца
def test_add_new_pet_without_photo_with_incorrect_age(name=pet_name, animal_type=pet_type, age='seven'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 400


# В поле {age} ввести отрицательное значение при добавлении нового питомца
def test_add_new_pet_without_photo_with_negative_num_age(name=pet_name, animal_type=pet_type, age='-22'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 400


# В поле {age} ввести буквы при изменении данных своего питомца
def test_update_pets_info_with_incorrect_age(name=pet_name, animal_type=pet_type, age='twelve'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pets_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 400
    else:
        raise Exception('There are no my pets')


# В поле {age} ввести отрицательное значение при изменении данных своего питомца
def test_update_pets_info_with_negative_num_age(name=pet_name, animal_type=pet_type, age='-22'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pets_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 400
    else:
        raise Exception('There are no my pets')


# Загрузить ГИФ изображение
def test_try_add_invalid_type_photo_of_a_pet(pet_photo=invalid_photo):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
        assert result['pet_photo'] is not None
    else:
        raise Exception('There are no my pets')


# Удаление чужого питомца из БД
def test_try_delete_not_my_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, all_pets = pf.get_list_of_pets(auth_key, '')
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Берём id первого питомца из общего списка
    pet_id = all_pets['pets'][0]['id']

    # Проверяем, не является ли этот питомец нашим, в ином случае отправляем запрос на удаление
    if pet_id not in my_pets['pets'][0]['id']:
        status, _ = pf.delete_pet(auth_key, pet_id)
    else:
        raise Exception("This is one of MY pets. Let's try another one")

    # Ещё раз запрашиваем список всех питомцев
    _, all_pets = pf.get_list_of_pets(auth_key, '')

    assert status == 200
    assert pet_id not in all_pets.values()


# Изменение данных чужого питомца
def test_try_change_not_my_pets_info(name=pet_name, animal_type=pet_type, age=pet_age):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, all_pets = pf.get_list_of_pets(auth_key, '')
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Берём id первого питомца из общего списка
    pet_id = all_pets['pets'][0]['id']

    # Проверяем, не является ли этот питомец нашим, в ином случае отправляем запрос на изменение данных
    if pet_id not in my_pets['pets'][0]['id']:
        status, result = pf.update_pets_info(auth_key, all_pets['pets'][0]['id'], name, animal_type, age)
    else:
        raise Exception("This is one of MY pets. Let's try another one")

    assert status == 200
    assert result['name'] == name
