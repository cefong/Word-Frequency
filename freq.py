# -----------------------------------
# Name: Celine Fong
# ID: 1580124
# CMPUT 274, Fall 2019
#
# Weekly Assignment 3: Word Frequency
# -----------------------------------

import sys

def take_cdline_argument():
	'''
	Reads the second token as the command line argument and check for errors
	'''
	if len(sys.argv) < 2:
		raise Exception('Sorry, too few command-line arguments. Please provide one valid filename after calling freq.\nFor example: python3 freq.py filename')
	elif len(sys.argv) > 2: 
		raise Exception('Sorry, too many command-line arguments. Please provide only one filename after calling freq.\nFor example: python3 freq.py filename')
	argument = sys.argv[1]
	return argument

def file_to_list(filename):
	''' 
	Takes the name of a file as a string argument and returns the contents of the file as a list
	of strings that were separated by a space in the original file
	'''
	# use context manager to open the file when it is in use and close it automatically after
	with open(filename,'r') as fin:
		file_string = fin.read().strip('\n')
		file_list = file_string.split()
	return file_list

def count_occurence(listname):
	'''
	Takes a list as an argument and returns the number of times each item in the list appears as a dictionary
	'''
	# initialize dictionary
	item_counter = {}

	# iterate through list and add values to dictionary
	for word in listname:
		if word in item_counter.keys():
			item_counter[word] += 1
		else:
			item_counter[word] = 1
	return item_counter

def format_freq_table(dictname):
	'''
	Takes a dictionary as an argument and returns a formatted frequency table in a list
	'''
	# calculate total words
	total = sum(dictname.values())

	# initialize empty list to store table entries
	table = []

	# create formatted entries and store in list
	for word in sorted(dictname):
		word_count = dictname[word]
		word_freq = round(word_count/total,3)
		table.append('{} {} {}\n'.format(word, word_count, word_freq))
	return table

def write_to_file(tablename, newfile):
	'''
	Takes a list as an argument and writes each item to a new file with name given by newfile
	'''
	# use context manager to open the file when it is in use and close it automatically after
	with open(newfile +'.out', 'w') as fwrite:
		for entry in tablename:
			fwrite.write(entry)



if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to 
    # this exercise, so you should call your code from here.
	fname = take_cdline_argument()
	word_list = file_to_list(fname)
	occurence_dict = count_occurence(word_list)
	table_list = format_freq_table(occurence_dict)
	write_to_file(table_list, fname)

