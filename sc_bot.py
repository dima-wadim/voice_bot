from openai import OpenAI

# Инициализация клиента API OpenAI с вашим API ключом
client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.proxyapi.ru/openai/v1",
)

# Список для хранения истории разговора
conversation_history = []

while True:
    # Запрос ввода пользователя
    user_input = input("Вы: ")

    # Добавление ввода пользователя в историю разговора
    conversation_history.append({"role": "user", "content": user_input})

    # Отправка запроса в нейронную сеть
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=conversation_history
    )

    # Извлечение и вывод ответа нейронной сети
    # Допустим, вы получаете объект ответа и его нужно обработать следующим образом:
    ai_response_content = chat_completion.choices[
        0].message.content  # Предполагаемый правильный способ доступа к содержимому ответа
    print("AI:", ai_response_content)

    # Добавление ответа нейронной сети в историю разговора
    conversation_history.append({"role": "system", "content": ai_response_content})

    # Опционально: условие для выхода из цикла (например, если пользователь ввел 'exit')
    if user_input.lower() == 'exit':
        break
