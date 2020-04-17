from search_engine import *


# Get the argument from the cmd prompt
parser = add_environment_parameters()
args = parser.parse_args()
#Init the search_engine object
search_engine = InteractiveSearchEngine(directory=args.dir,config_file='config.ini')
#Start the interactive cmd prompt
search_engine.start()



