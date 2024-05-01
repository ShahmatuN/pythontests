import requests
def test_get_user():
    url = "https://jsonplaceholder.typicode.com/albums"

    # Отправляем GET запрос
    response = requests.get(url)
    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    data = response.json()

    response2 = requests.get('https://jsonplaceholder.typicode.com/photos?id={data[1]["id"]}')
    assert response2.status_code == 200, "Статус код не соответствует ожидаемому"