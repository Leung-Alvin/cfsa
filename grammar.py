import language_tool_python
import nltk.tokenize
import os
tool = language_tool_python.LanguageTool('en-US')

def grammar_check(text):
    matches = tool.check(text)
    return matches

def generate_ratio_by_token(matches, tokens):
    if len(tokens) == 0 or len(matches) == 0:
        return 0
    else:
        return round(len(matches)/len(tokens)*100, 2)

def generate_ratio_by_characters(matches, string):
    if len(string) == 0 or len(matches) == 0:
        return 0
    else:
        return round(len(matches)/len(string)*100, 2)
    
def main():
    text = ''
    files = os.listdir('survey')
    ratios_by_token = []
    ratios_by_characters = []
    for file in files:
        with open('survey/' + file, 'r', encoding='utf-8') as f:
            text = f.read()
        tokens = nltk.tokenize.word_tokenize(text)
        matches = grammar_check(text)
        error = generate_ratio_by_token(matches, tokens)
        ratios_by_token.append((file,error))
        ratios_by_characters.append((file,generate_ratio_by_characters(matches, text)))
    print(ratios_by_token)
    print(ratios_by_characters)

if __name__ == '__main__':
    main()