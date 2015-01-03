# SFLT PARSING PROGRAM VER 1.7


"""Includes:
Parses through file for both a and A lettered nodes.
Requires definition of input file, output file and bom csv file.
Ensure sflt document


STill to do:


make function for checking for unique records only

BOM parser with item counter returns values that suggest 
not all part numbers have a presense in the part 
reference section

make cross platform GUI

"""


# Parsing is done with minidom as main xml reader. 
# csv module imported for creation of csv file output

from xml.dom import minidom
import csv
import os
import sys
import glob

list_of_files = glob.glob('/home/thomas/PythonProjects/parser/ver1/*.sflt')
print(list_of_files)

# Initially setting xmldoc to the file I am parsing. Will need to set this up with a user generated filename.


for each in list_of_files:
	infile = each
	billofmaterialsfile = os.path.basename(each).lower().replace("sflt", "csv")
	outputfile = ('master_stock_list.csv')
	#billofmaterialsfile = ('bom.csv')

		

	#TESTING FILE EXTENSION BEFORE RUNNING SCRIPT
	def infile_ext_checker():
		"""Checks whether the file used for xml parsing is a correct SFLT file. If it isnt, the script ends"""
		ext = os.path.splitext(infile)[-1].lower()
		if ext == '.sflt':
			print 'File is a %s file' %ext
		else:	
			print 'FILE ERROR - Your %s file is not correct' %ext
			print 'Parsing will not continue, please select correct file'
			sys.exit()
			

	def run_parsing():
		""" Parse defined document into global variables to be used by other functions"""
		global xmldoc
		global outfile
		global bomfile
		global flatNet
		global partNumbers
		global partReferences
		xmldoc = minidom.parse(infile)
		# Open output file for editing:
		outfile = open(outputfile, "a")
		bomfile = open(billofmaterialsfile, "a")
		# Global variables that _should_ be the same in all sflt documents.
		flatNet = xmldoc.getElementsByTagName("flatNet")[0]
		partNumbers = flatNet.getElementsByTagName("partNumbers")[0]
		partReferences = flatNet.getElementsByTagName("partReferences")[0]


	# Exporting File
	def partnumberlist(tal):
		"""Function will get the partnumber section of the document by running through flatNet => partNumbers => Partnumber 
		and for each node with the designator 'bokstav' it will print out the key and value initially."""
		PartNumber = partNumbers.getElementsByTagName("PartNumber")[tal]
		alist = PartNumber.getElementsByTagName("a")
		Alist = PartNumber.getElementsByTagName("A")

		listing = [""] *10
		for each in alist:
				if each.getAttribute("Key") == "PARTNAME":
					listing[2] = each.getAttribute("Value")
				elif each.getAttribute("Key") == "DESC":
					listing[3] = each.getAttribute("Value")	
				elif each.getAttribute("Key") == "MFR":
					listing[4] = each.getAttribute("Value")	
				elif each.getAttribute("Key") == "MFR_PN":
					listing[5] = each.getAttribute("Value")
					listing[1] = each.getAttribute("Value")
				elif each.getAttribute("Key") == "DST":
					listing[6] = each.getAttribute("Value")	
				elif each.getAttribute("Key") == "DST_PN":
					listing[7] = each.getAttribute("Value")	
				elif each.getAttribute("Key") == "MIN_QTY":
					listing[8] = each.getAttribute("Value")								
				elif each.getAttribute("Key") == "PRICE":
					listing[9] = each.getAttribute("Value")
				else:
					pass

		for each in Alist:
				if each.getAttribute("Key") == "PARTNAME":
					listing[2] = each.getAttribute("Value")
				elif each.getAttribute("Key") == "DESC":
					listing[3] = each.getAttribute("Value")	
				elif each.getAttribute("Key") == "MFR":
					listing[4] = each.getAttribute("Value")	
				elif each.getAttribute("Key") == "MFR_PN":
					listing[5] = each.getAttribute("Value")
					listing[1] = each.getAttribute("Value")
				elif each.getAttribute("Key") == "DST":
					listing[6] = each.getAttribute("Value")	
				elif each.getAttribute("Key") == "DST_PN":
					listing[7] = each.getAttribute("Value")	
				elif each.getAttribute("Key") == "MIN_QTY":
					listing[8] = each.getAttribute("Value")								
				elif each.getAttribute("Key") == "PRICE":
					listing[9] = each.getAttribute("Value")
				else:
					pass
		wr = csv.writer(outfile, dialect='excel')
		wr.writerow(listing)
			
			
	# Needed to get count for total amount of partnumbers listed:
	def part_number_counter():
		"""Counts the number of 'PartNumber' nodes in the 
		parsed file"""
		return len(partNumbers.getElementsByTagName('PartNumber'))


	# WRITES OUTPUT TO CSV FILE
	def run_partnumberlist():
		"""Runs the function for part numbers to master stock list via for loop"""
		for each in range(1, part_number_counter()):
			print "PARSING PARTNUMBER " + str(each)
			partnumberlist(each)


	#item counter for BOM creation
	def itemCounter(tal):
		"""Function will get the partnumber section of the document by running through flatNet => partNumbers => Partnumber 
		and for each node with the designator 'bokstav' it will print out the key and value initially.
		foo_A and foo_a as well as list_a and list_A ensures it checks for both a and A nodes.
		Basic functionality is that it runs through all part numbers in partnumbers section of document and adds to a listing
		then it runs through all part numbers from total file and then checks how many times a part number 
		from list created in partnumbers appears in the other list.
		"""
		PartNumber = partNumbers.getElementsByTagName("PartNumber")[tal]
		foo_A = xmldoc.getElementsByTagName("A")
		foo_a = xmldoc.getElementsByTagName("a")
		list_A = PartNumber.getElementsByTagName("A")
		list_a = PartNumber.getElementsByTagName("a")
		listofnumbers = []
		foolist = []
		wr = csv.writer(bomfile, dialect='excel')
		goat = []

		for each in foo_A:
			if each.getAttribute("Key") == "MFR_PN":
				foolist.append(each.getAttribute("Value"))
			else:
				pass
		for each in foo_a:
			if each.getAttribute("Key") == "MFR_PN":
				foolist.append(each.getAttribute("Value"))
			else:
				pass			
		for each in list_A:
			if each.getAttribute("Key") == "MFR_PN":
				listofnumbers.append(each.getAttribute("Value"))
			else:
				pass
		for each in list_a:
			if each.getAttribute("Key") == "MFR_PN":
				listofnumbers.append(each.getAttribute("Value"))
			else:
				pass		
		for each in listofnumbers:
			#print each, foolist.count(each)
			goat.append(each)
			goat.append(str(foolist.count(each)))
		
		wr.writerow(goat)

	def run_bom():
		"""Runs function for BOM creation via for loop"""
		for each in range(1, part_number_counter()):
			itemCounter(each)


	infile_ext_checker()
	run_parsing()	
	run_partnumberlist()
	run_bom()	