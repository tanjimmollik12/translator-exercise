from translate import Translator

translator= Translator(to_lang="ja")
try:
    with open('./text.txt',mode='r') as file:
        text= file.read()
        translation = translator.translate(text)
        with open('./ja.txt',mode='w',encoding="utf-8") as t_file:
            t_file.write(translation)
except FileNotFoundError as e:
    print(e)