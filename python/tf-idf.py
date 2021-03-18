# >> Importing modules
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string
nltk.download('stopwords')
s_words = list(stopwords.words('english'))
punctuation = list(string.punctuation().split(''))

# >> Initializing classes
ps = PorterStemmer()

# >> Preprocessing Function
def preprocessing(text):
    # >>> Removing Punctuations
    text = [c for c in text if not c in punctuation]

    # >>> Lowering the text
    text.lower()

    # >>> Stemming
    arr = list(text.split())
    n = len(arr)
    for i in range(n):
        arr[i] = ps.stem(arr[i])

    # >>> Removing Stopwords
    arr = [word for word in arr if not word in s_words]
    return arr