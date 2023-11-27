import os


def get_prompts():
    text = open('prompts.txt', 'r').read()
    return text.replace('"', '').replace("- ", '').split("\n")
    

def main():
    prompts = get_prompts()
    for prompt in prompts:
        print(prompt)

if __name__ == '__main__':
    main()