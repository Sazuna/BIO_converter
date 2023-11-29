import regex
import sys

def tokenise(text, granularity="all"):
	match granularity:
		case 'all':
			tokens = regex.findall(r"[@#]|\w{2,}’\w+|</?\w+>|\w+|[^\w \n]+", text)
			return tokens
		case 'apostrophe':
			tokens = regex.findall(r"[@#]|\w’|\w{2,}’\w+|</?\w+>|\w+|[^\w \n]+", text)
			return tokens
		case 'hashtag_apostrophe':
			tokens = regex.findall(r"</?\w+>|@|\w’|#?\(\w{2,}’\w+|\w+|[^\w \n]+\)", text)
			return tokens
		case _:
			print(f"Granularity {granularity} for tokenisation must be one of those :\n\t- all\n\n- apostrophe\n\t- hashtag_apostrophe")
			sys.exit(1)
