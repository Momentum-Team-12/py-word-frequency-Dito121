STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    result = {}

    with open(file, 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.translate(str.maketrans('', '', '?!,.'))
            line = line.lower()
            words = line.split()
            for word in words:
                if word not in STOP_WORDS:
                    if word not in result:
                        result[word] = 1
                        continue
                    result[word] += 1


    sorted_result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

    keys = sorted_result.keys()
    for key in keys:
        print(f"{key:<15}" + ' | ' + str(sorted_result[key]) + ' ' + '*'*sorted_result[key])


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
