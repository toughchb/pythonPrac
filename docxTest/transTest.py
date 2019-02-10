from googletrans import Translator
translator = Translator()

output = translator.translate('hi',src='en', dest='ko')

print(type(output.text))