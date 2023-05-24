import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.corpus import stopwords

def process_text(text):
    
    # Tokenización de oraciones
    sentences = sent_tokenize(text)
    print("Oraciones:", sentences)

    # Tokenización de palabras
    tokens = word_tokenize(text)
    print("Tokens:", tokens)

    # Etiquetado gramatical
    tagged = pos_tag(tokens)
    print("Etiquetas gramaticales:", tagged)

    # Reconocimiento de entidades nombradas
    named_entities = ne_chunk(tagged)
    print("Entidades nombradas:", named_entities)

    # Eliminación de palabras vacías (stop words)
    stop_words = set(stopwords.words('english'))
    filtered_words = [token for token in tokens if token.lower() not in stop_words]
    print("Palabras filtradas:", filtered_words)

# Abrí el archivo en modo lectura, el programa sólo podrá leer el contenido mas no modificarlo, el texto abierto es asignado a la
# variable archivo
archivo = open('ej_texto.txt', 'r')
# El contenido de la variable archivo es asignado a la variable original texto_ejemplo
texto_ejemplo = archivo.read()

# Procesar el texto
process_text(texto_ejemplo)

# Es necesario cerrar los archivos abiertos una vez que se terminaron de usar
archivo.close()

