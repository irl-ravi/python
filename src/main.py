# src/main.py
from word_frequency import compute_word_frequency
from remove_repeated_words import remove_repeated_words

def main():
    text = "2 3 python better is or python which"
    result_frequency = compute_word_frequency(text)
    for item in result_frequency:
        print(item)

    input_text = "Hello Hello World"
    result_remove_repeated = remove_repeated_words(input_text)
    print(result_remove_repeated)

if __name__ == "__main__":
    main()
