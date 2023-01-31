import argparse

from jumble import Jumble

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-W', '--word',
                        required=True,
                        help="input a word for which all jumble sub-anagrams will be printed")
    parser.add_argument('-F', '--file', default="word_list.txt",
                        help="input the path to a word list file")
    args = parser.parse_args()
    my_file = open(args.file, "r")
    data = my_file.read()
    # replacing end splitting the text when newline ('\n') is seen.
    word_list = data.split("\n")

    word = args.word.lower()
    jumble_obj = Jumble(word_list, word)
    jumble_obj.gen_char_dict()
    jumble_obj.gen_sub_anagrams()
