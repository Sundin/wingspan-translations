import wikipediaapi


def translate_bird(english_name, language):
    wiki_wiki = wikipediaapi.Wikipedia('en')

    bird = english_name.replace(" ", "_").lower()
    page_py = wiki_wiki.page(bird)

    summary = page_py.summary[0:80]

    scientific_name = ""
    x = summary.split("(")
    if (len(x) >= 2):
        xx = x[1].split(")")
        scientific_name = xx[0].replace(";", "").strip()

    translated_name = ""
    if language in page_py.langlinks.keys():
        page_py_sv = page_py.langlinks[language]
        translated_name = page_py_sv.title.replace("_", " ")

    print(f"{english_name}, {scientific_name}, {translated_name}")
    with open('translations.csv', 'a') as the_file:
        the_file.write(f"{english_name}, {scientific_name}, {translated_name}\n")


def run_program(): 
    open('translations.csv', 'w').close()
    with open("birds.txt") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    language_code = "sv"
    for bird in content:
        translate_bird(bird, language_code)


run_program()
