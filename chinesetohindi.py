from googletrans import Translator

translator = Translator()


def chinese_to_hindi(text):
    return translator.translate(text, dest='hi')
