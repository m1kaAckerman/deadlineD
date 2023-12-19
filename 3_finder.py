import logging

def search_word_in_file(file_path, search_word):
    count = 0
    positions = []

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            words = line.split()
            for position, word in enumerate(words, 1):
                if word == search_word:
                    count += 1
                    positions.append((line_number, position))

    logging.info(f"количество найденных слов '{search_word}': {count}")
    logging.info(f"расположение слова '{search_word}': {positions}")

