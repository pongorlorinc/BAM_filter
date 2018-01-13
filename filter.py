import pysam
import sys
import os
import os.path

min_alignment_score = 5
max_edit_distance = 3

def get_edit_distance(read):
	intags = read.tags

	for ReadTagsEntry in read.tags:
		if 'NM' in ReadTagsEntry:
			if ReadTagsEntry[1] < max_edit_distance:
				return 1

			else:
				return 0

	return 0

def accept_read(in_read):
	if in_read.mapping_quality < min_alignment_score:
		return 0

	if in_read.is_duplicate:
		return 0

	if in_read.reference_id < 0:
		return 0

	if in_read.next_reference_id < 0:
		return 0

	if in_read.reference_name != in_read.next_reference_name:
		return 0

	if in_read.cigartuples is None:
		return 0

	if in_read.cigartuples[0][0] == 5 or in_read.cigartuples[-1][0] == 5:
		return 0

	return 1

def filter_orientation(read):
	if read.is_reverse:
		if read.mate_is_reverse:
			return 0

		else:
			return 1

	else:
		if read.mate_is_reverse:
			return 1

		else:
			return 0

	return 0
		

def Read_Bam_File(bamfile, out_file):
	r_bam = pysam.AlignmentFile(bamfile, "rb")
	pairedreads = pysam.AlignmentFile(out_file, "wb", template=r_bam)

	for read in r_bam.fetch():
		if filter_orientation(read) == 1:
			if accept_read(read) == 1:
				if get_edit_distance(read) == 1:
					pairedreads.write(read)
				

def print_usage():
	print("Usage: python filter.py <input_bam> <output_bam>\n")
	print ("\tEdit distance: %d" % (max_edit_distance))
	print ("\tMin alignment score: %d" % (min_alignment_score))
	print ("\t[Modify variables in script to change value]\n")	

bamfile = sys.argv[1]
out_file = "filtered.bam"

if len(sys.argv) > 2:
	out_file = sys.argv[2]

if os.path.exists(out_file):
	print("[ERROR] Output file %s already exists\n" % (out_file))
	print_usage()
	
else:
	Read_Bam_File(bamfile, out_file)	
		
