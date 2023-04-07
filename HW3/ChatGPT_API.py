import openai

with open('./data/程式語言_Week3_Python基礎02.txt', 'r', encoding='utf-8') as fh:
    tmp = fh.read()
    itemlist = tmp.split(',')


itemlist = str(itemlist)

keyfile = open("key.txt", "r")
key = keyfile.readline()

openai.api_key = key

start_idx = 0
result = ''
while start_idx < len(itemlist):
    end_idx = min(start_idx + 1600, len(itemlist))
    sub_list = itemlist[start_idx:end_idx]

    print(start_idx)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": f"提供以下文字之繁體中文摘要：{sub_list}"}
        ]
    )  
    for choice in response.choices:
        result += choice.message.content
    start_idx = end_idx

with open('output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(result)