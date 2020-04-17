from textwrap import dedent

#To simulate a file
file_content = dedent("""
    hello world ! 
    this is a 
    file containing
    10 words
""")


read_unique_expected_output = {'file_name': 'fichier.txt', 'unique_words': {'!', 'file', 'words', '10', 'a', 'world', 'this', 'is', 'hello', 'containing'}}


#dict containing data for the test_get_commons_words
test_get_commons_words = {
    'set_words' :  {'hello','mehdi','fine'},
    'words_to_match' : {"I","m","mehdi","fine"},
    'expected_rate' : '0.5%'
}

