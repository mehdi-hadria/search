import logging
import getpass
import time
import os

from helpers import *
from datetime import datetime


class InteractiveSearchEngine():

    """
    Class to run the entire program by : defining a logger to see the user session (search requests),
    launch a sort of prompt cmd and run all search queries

    """


    def __init__(self,
                 directory,
                 config_file):

        """
        Method to initialize the cluster

        :param directory: Directory of text files
        :type directory: string

        """

        self.files_words_mapping = build_files_words_mapping(directory)
        self.user = getpass.getuser()
        self.config = get_configuration(config_file)
        self.logger = logging.getLogger(name='search_engine')
        self.logger.setLevel(logging.INFO)



    def set_logger(self):

        """
        Method to set a handler for the logger : Filehandler to store the logs the cluster
        """
        date= datetime.now().strftime('%Y%m%d')
        handler = logging.FileHandler(os.path.join(self.config['logging']['logs_path'], "search_engine_{}.log".format(date)),
                                      mode='a',
                                      encoding='utf-8')
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s::%(name)s::%(levelname)s::user:{}::%(message)s'.format(self.user))
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)


    def hello(self):

        print("Welcome to this sample search engine : please tape a list of words (splitted by space)."
              "\n To exit the program please tape :quit")


    def start(self):

        self.set_logger()
        self.logger.info("Starting new search session")
        if len(self.files_words_mapping) < 1:
            print('No text file has been found in this directory\n'
                  'Looking for files recursively is not supported. '
                  'Please try another directory')
            self.logger.info("End of the search session without any request"
                             "Unable to find text files in directory")
            return -1
        self.hello()


        while True:
            words = input("search> ")
            words = words.lower()
            start_time = time.time()
            self.logger.info("User input :  {} ".format(words))



            if words==':quit':
                self.logger.info("User has end the session. Session duration {}s".format(time.time()-start_time))
                break

            else:
                self.logger.info("Searching for words in files :")
                words= set(words.rstrip().split(' '))
                result = get_search_score(self.files_words_mapping,
                                          words)
                self.logger.info(msg="Returning results to user...")
                if len(result)==0:
                    print('no matches found')
                    continue
                for file,score in result:
                    print('{} : {} '.format(file,score))
                self.logger.info("End of the search request. Search duration {}s".format(time.time()-start_time))









