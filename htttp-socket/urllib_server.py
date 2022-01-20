from urllib import request

response = request.urlopen("http://example.com")
# Статус-код
print(response.status)
# Статус-код 1.0
print(response.getcode())
# Message
print(response.msg)
print(response.reason)
# Получаем заголовки в виде внутреннего объекта
print(response.headers)
# Полулчаем словарь всех заголовков
print(response.getheaders())
# Получение заголовка
print(response.headers.get("Content-Type"))
print(response.getheader('Content-Type'))