import os

def get_authors(directory):
    authors = []
    for filename in os.listdir(directory):
        author = filename.split('_-_')[0]
        if author not in authors:
            authors.append(author)
    return authors

def remove_strings_with_substring(input_list, substring):
    updated_list = [string for string in input_list if substring not in string]
    return updated_list

def get_databases():
    dirs = [x[0] for x in os.walk('.')]
    ret = remove_strings_with_substring(dirs, '.git')
    ret.remove('.')
    ret.remove('.\\__pycache__')
    ret.remove('.\\Fonts')
    new_ret = []
    for db in ret:
        new_ret.append(db.replace(".\\", ""))
    return new_ret

def get_prints(directory):
    prints = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            prints.append(filename)
    return prints

def read_print(directory, print_name):
    with open(directory + '/' + print_name, 'r') as f:
        return f.read()

def main():
    dbs = get_databases()
    for db in dbs:
        authors = get_authors(db)
        # prints = get_prints(db)
        # print(db, authors, prints)
        print(db,authors)
if __name__ == '__main__':
    main()
    