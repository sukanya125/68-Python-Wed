def sort_word_in_sentence(sentence):
    words = sentence.split()
    words.sort(key=str.lower)
    sorted_sentence = ' '.join(words)
    return sorted_sentence

sentence = "This is a man word"
sorted_result = sort_word_in_sentence(sentence)
print("Sorted sentence:", sorted_result)