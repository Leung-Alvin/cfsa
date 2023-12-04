import language_tool_python
import nltk.tokenize
import os

tool = language_tool_python.LanguageTool("en-US")


def grammar_check(text):
    matches = tool.check(text)
    return matches


def generate_ratio_by_token(matches, tokens):
    if len(tokens) == 0 or len(matches) == 0:
        return 0
    else:
        return len(matches) / len(tokens)


def generate_ratio_by_characters(matches, string):
    if len(string) == 0 or len(matches) == 0:
        return 0
    else:
        return len(matches) / len(string)


def average_number_of_errors(input_num_tokens, text, author):
    text_tokens = nltk.tokenize.word_tokenize(text)
    if len(input_num_tokens) > len(text_tokens):
        # print("too big", len(text_tokens))
        # print(author,len(grammar_check(text)))
        return (author, len(grammar_check(text)))
    sample_text = " ".join(text_tokens)
    sample_errors = []
    # print("avg",len(sample_text))
    # print(range(len(sample_text)//len(input_num_tokens)))
    for i in range(len(text_tokens) // len(input_num_tokens)):
        part = sample_text[i * len(input_num_tokens) : (i + 1) * len(input_num_tokens)]
        part_tokens = nltk.tokenize.word_tokenize(part)
        # print(author,len(grammar_check(part)))
        sample_errors.append(len(grammar_check(part)))
    return (author, sum(sample_errors) / len(sample_errors))


def find_closest_authors(authors_list, target_value):
    # Calculate the absolute difference between target_value and each author's value
    differences = [
        (author, abs(value - target_value)) for author, value in authors_list
    ]

    # Sort the authors based on the absolute differences
    sorted_authors = sorted(differences, key=lambda x: x[1])

    # Get the top 3 authors closest to the target value
    top_3_authors = sorted_authors[:3]

    return top_3_authors


def grammar_analyis(text):
    text_tokens = nltk.tokenize.word_tokenize(text)
    text_error = len(grammar_check(text))
    files = os.listdir("survey")
    analyses = []
    for file in files:
        with open("survey/" + file, "r", encoding="utf-8") as f:
            text = f.read()
            tokens = nltk.tokenize.word_tokenize(text)
            author = file.split("_-_")[0]
            error_analysis = list(average_number_of_errors(text_tokens, text, author))
            analyses.append(error_analysis)
    top_3 = find_closest_authors(analyses, text_error)
    top_3 = [author for author, value in top_3]
    return top_3


def main():
    # text = ''
    # files = os.listdir('survey')
    # # ratios_by_token = []
    # # ratios_by_characters = []
    # for file in files:
    #     with open('survey/' + file, 'r', encoding='utf-8') as f:
    #         text = f.read()
    #     tokens = nltk.tokenize.word_tokenize(text)
    #     matches = grammar_check(text)
    #     error = generate_ratio_by_token(matches, tokens)
    #     ratios_by_token.append((file,error))
    #     ratios_by_characters.append((file,generate_ratio_by_characters(matches, text)))
    # print(ratios_by_token)
    # print(ratios_by_characters)
    file_name = "test.txt"
    central_text = ""
    central_tokens = []
    with open(file_name, "r", encoding="utf-8") as f:
        central_text = f.read()
        central_tokens = nltk.tokenize.word_tokenize(central_text)
        # print(file_name,len(central_tokens))
    sample_error = len(grammar_check(central_text))
    files = os.listdir("survey")
    analyses = []
    for file in files:
        with open("survey/" + file, "r", encoding="utf-8") as f:
            text = f.read()
            tokens = nltk.tokenize.word_tokenize(text)
            # print(file,len(tokens))
            author = file.split("_-_")[0]
            error_analysis = list(
                average_number_of_errors(central_tokens, text, author)
            )
            analyses.append(error_analysis)
    top_3 = find_closest_authors(analyses, sample_error)
    print(top_3)


if __name__ == "__main__":
    main()
