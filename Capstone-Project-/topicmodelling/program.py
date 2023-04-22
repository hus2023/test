
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import xlrd
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import gensim
from gensim import corpora
import nltk

nltk.download('stopwords')
nltk.download('wordnet')

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()
def clean(doc):
    if doc is not None:
      stop_free = " ".join([i for i in str(doc).lower().split() if i not in stop])
      punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
      normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
      return normalized
    else:
      return doc

file_path = ("datasetds.xlsx")
data = pd.read_excel(file_path, 
                              sheet_name = 'All common workers from both ')

electric_data = data['Description']
doc_clean = [clean(doc).split() for doc in electric_data] 
dictionary = corpora.Dictionary(doc_clean) 
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

base_model_lda = gensim.models.ldamodel.LdaModel
ldamodel = base_model_lda(doc_term_matrix, num_topics=3, 
                          id2word = dictionary, passes=50)

print(ldamodel.print_topics(num_topics=20, num_words=3))

def predict(new_text):
  if new_text is not None and str(new_text).strip() != '':
    cleaned_data = clean(new_text).split()
    bow_vector = dictionary.doc2bow(cleaned_data)
    for index, score in sorted(ldamodel[bow_vector], key=lambda tup: -1*tup[1]):
      print("Score: {}\n Topic: {}".format(score, ldamodel.print_topic(index, 5)))
  else:
    return None

d = electric_data[0]
print(d)
predict(d)

coherence_model_lda = CoherenceModel(model=ldamodel, 
                                     texts=doc_clean, 
                                     dictionary=dictionary, 
                                     coherence="c_v")
coherence_lda = coherence_model_lda.get_coherence()
print('\nLDA Coherence Score: ', coherence_lda)

lda_model_multi = gensim.models.LdaMulticore(corpus=doc_term_matrix,
                                       id2word=dictionary,
                                       num_topics=2, 
                                       random_state=100,
                                       chunksize=100,
                                       alpha=0.01,
                                       eta=0.01,
                                       passes=5,
                                       per_word_topics=True)

coherence_model_multicore = CoherenceModel(model=lda_model_multi, 
                                     texts=doc_clean, 
                                     dictionary=dictionary, 
                                     coherence="c_v")
coherence_multicore = coherence_model_multicore.get_coherence()
print('\nMulticore Coherence Score: ', coherence_multicore)