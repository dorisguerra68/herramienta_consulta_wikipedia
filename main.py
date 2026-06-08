
from translator.TranslatorClient import TranslatorClient
from app.App import get_user_input

#UI
text = get_user_input("What would you like to translate?")
src_language = get_user_input("From What language?")
tgt_language = get_user_input("To What language?")

#logic
#Nos crean una instancia de una clase =OBJETO de clase.
translator = TranslatorClient().translate_text(
    text=text,
    source_language=src_language,
    target_language=tgt_language
)


print(translator)