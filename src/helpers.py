import os
import configparser
import argparse
from itertools import islice


def get_configuration(config_path):

    print(config_path)

    """
    Function to load configuration from a file to a dictionary

    :param config_path: the path of config.ini file
    :type config_path: str
    :return: A dictionary containing all configuration per sections
    :rtype: dict
    """

    config = configparser.ConfigParser()
    config.read(config_path)
    job_config = {}
    for section in config.sections():
        job_config[section] = dict(config.items(section))

    return job_config


def build_files_words_mapping(directory):

    """
    Function to build a list of dict where keys are file names and values are a set of the file unique words

    :param directory: A directory where text files are located
    :type directory: str
    :return: A list containing all dicts (one per file) with key as file name and value is  words set
    :rtype: list
    """

    files = get_all_text_files(directory)
    files_words_list = []
    for file in files:
        files_words_list.append(read_unique_words(file))
    print('{} files read in {}'.format(len(files),directory))
    return files_words_list


def read_unique_words(file_path):

    """
    Function to read file and store in a dict : file name as key and unique words as value

    :param directory: A directory where text files are located
    :type directory: str
    :return: A list containing all dicts (one per file) with key as file name and value is  words set
    :rtype: list
    """

    file_name = os.path.basename(file_path)
    with open(file_path, 'r') as file:
        lines = [line.rstrip().split() for line in file]
        words = set([word.lower() for words in lines for word in words])
    return {
        'file_name': file_name,
        'unique_words': words
    }


def get_all_text_files(directory):

    """
    Function to list all text files within a directory

    :param directory: A directory where text files are located
    :type directory: str
    :return: A list containing all text files
    :rtype: list
    """

    files = []
    if not os.path.isdir(directory):
        raise ValueError("directory argument must be a path to a directory")
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            files.append(directory + '/' + file)
    return files


def get_commons_words(input_words_list,
                      file_words_list):

    """
    Function to define how match (in percentage %) the first set match the second one

    :param input_words_list: A set of words
    :type input_words_list: set
    :param file_words_list: A second set of words
    :type file_words_list: set
    :return: A string to represent the matching rate of the first set to the second one
    :rtype: str
    """

    common_elements = len(input_words_list.intersection(file_words_list))
    similarity_rate = (common_elements / len(file_words_list))*100
    percent_as_str = "{}%".format(similarity_rate)
    return percent_as_str


def get_search_score(files_words_mapping,
                     words_list,
                     top=10):

    """
    Function to get the matching score of the words to the text files content

    :param files_words_mapping: A list of mapping (file_name : unique_words)
    :type files_words_mapping: list
    :param words_list:  list or set of words to search in the text files
    :type words_list: set
    :param top:  Number of top elements to get
    :type top: int
    :return: A list of dict having the highest score
    :rtype: list
    """

    result = dict()
    for mapping in files_words_mapping:
        result[mapping["file_name"]] = get_commons_words(set(words_list), mapping["unique_words"])

    sorted_results = {file: score for file, score in sorted(result.items(), key=lambda item: item[1], reverse=True)
                      if float(score.replace('%','')) > 0 }
    top_results = list(islice(sorted_results.items(), top))
    return top_results


def add_environment_parameters():

    """
    Function to parse argument

    :param files_words_mapping: A list of mapping (file_name : unique_words)
    :type files_words_mapping: list
    :param words_list:  list or set of words to search in the text files
    :type words_list: set
    :param top:  Number of top elements to get
    :type top: int
    :return: A Argparser object containing the arguments
    :rtype: argparse.ArgumentParser
    """

    parser = argparse.ArgumentParser(description='text files directory where to search for the words')
    parser.add_argument('dir', help='directory')
    return parser
