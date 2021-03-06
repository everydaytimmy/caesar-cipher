çfrom corpus_loader import word_list, name_list

candidates = [
    "a dark and stormy night",
    "n qnex naq fgbezl avtug",
    "j mjat jwm bcxavh wrpqc",
    "call me Ishmael",
    "Billy Pilgrim has become unstuck in time",
    "All happy families are alike; each unhappy family is unhappy in its own way.",
    '"Where\'s Papa going with that ax?" said Fern to her mother as they were setting the table for breakfast.',
    "Off the hizzle fo shizzle",
]


def count_words(text):

    candidate_words = text.split()

    word_count = 0

    for candidate in candidate_words:
        word = re.sub(r"[^A-Za-z]+", "", candidate)
        if word.lower() in word_list or word in name_list:
            word_count += 1

    return word_count


for phrase in candidates:
    recognized_word_count = count_words(phrase)
    potential_word_count = len(phrase.split())
    percentage = int(recognized_word_count / potential_word_count * 100)
    if percentage >= 50:
        print(phrase, percentage)
