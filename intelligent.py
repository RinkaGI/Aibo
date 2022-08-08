import requests, json
from deep_translator import GoogleTranslator

class Values:
    def __init__(self) -> None:
        self.bid = '168480'
        self.key = 'JxqTfBS5OOVIEDWJ'
        self.uid = 'usuario'

values = Values()
translator = GoogleTranslator(source = 'auto', target = 'es')
secondTranslator = GoogleTranslator(source = 'auto', target = 'en')

def send_message(message: str):
    mensajeTraducido = secondTranslator.translate(message)
    url = f'http://api.brainshop.ai/get?bid={values.bid}&key={values.key}&uid={values.uid}&msg={mensajeTraducido}'
    response = requests.get(url)
    repuesta = json.loads(response.content)
    respuesta = repuesta['cnt']
    respuestaDefinitiva = translator.translate(respuesta)
    return respuestaDefinitiva.encode('utf-8').decode()
