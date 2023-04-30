import openai
openai.api_key = ("api_key")

def gpt():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"""`{text}` - 
        виведи мені статистику по кількості слів,
        речень та діячів у тексті"""}
        ]
    )

    answ = completion.choices[0].message.content

    return answ

with open('file.txt', 'r', encoding="utf-8") as file:
    text = file.read()

    print(text)

    print("\n\n")

    print(gpt())