from deep_translator import GoogleTranslator

class TranslatorClient:
    def __init__(self):
        pass
    def translate_text(self,text:str, source_language:str, target_language:str):
            translated_text = GoogleTranslator(
                source=source_language,
                target=target_language
            ).translate(text)
            return translated_text

translator = TranslatorClient()

print(translator.translate_text(text='Hola familia', source_language='auto', target_language='it'))


