class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            raise TypeError("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        
        temp_value = self.value.replace('?', '.').replace('!', '.')
       
        sentences = temp_value.split('.')
        
        valid_sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(valid_sentences)
