import chatbot as b

from janome.tokenizer import Tokenizer

from keras.preprocessing.text import Tokenizer as TOKEN

phase = 0
limit = 3
first_word = '魔法'

def dialogue(w):
    global phase, limit
    try:
        phase += 1
        print('phase' + str(phase))
        word1 = b.load_w2v(w)
        sentence1 = b.make_sentence(word1)

        t = Tokenizer()
        s = sentence1 

        x = (t.tokenize(s,wakati=True))

        texts = (str(x))

        tokenizer = TOKEN()
        tokenizer.fit_on_texts(texts)

        matrix = tokenizer.texts_to_matrix(texts, "tfidf")
        print("bot1:" + str(matrix))

        word2 = b.tokenize(sentence1)
        sentence2 = b.make_sentence(word2)
        
        s2 = sentence2
        y = (t.tokenize(s2,wakati=True))

        texts2 = (str(y))

        matrix2 = tokenizer.texts_to_matrix(texts, "tfidf")
        print("bot2:" + str(matrix2))
        
        next_word_base = b.tokenize(sentence2)
        if not phase >= limit:
            dialogue(next_word_base)
        else:
            return
    except Exception as e:
        print('occur an error.' + e)
        exit(0)
def main():
    dialogue(first_word)


if __name__ == '__main__':
    main()