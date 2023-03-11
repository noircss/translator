from googletrans import Translator

def translate_text(text):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src='en', dest='fr')
    return translation.text

# Prompt the user for input
text = input(' ')

# Print the translated text
translated_text = translate_text(text)
print(translated_text)
