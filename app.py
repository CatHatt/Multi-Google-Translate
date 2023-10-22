from googletrans import Translator;
translator = Translator()

target = input('What do you want the target language to be? (Default: English)\n')
if target == '':
    target = 'en'
times = input('How many times do you want it to translate?\n')
print(translator.translate('こんにちは', dest=target).text)