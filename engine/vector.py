import chatbot as b

from keras.preprocessing.text import Tokenizer

phase = 0
limit = 2
first_word = '魔法'

def dialogue(w):
    global phase, limit
    try:
        phase += 1
        print('phase' + str(phase))
        word1 = b.load_w2v(w)
        sentence1 = b.make_sentence(word1)
        
        texts = ('bot1:' + sentence1)
        
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(texts)
        
        matrix = tokenizer.texts_to_matrix(texts, "tfidf")
        print("bot1:" + str(matrix))
        
        word2 = b.tokenize(sentence1)
        sentence2 = b.make_sentence(word2)
        print('bot2:' + sentence2)
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