# BAM_filter
A script to filter reads based on certain stats (no. of mismatches, alignment qual)

Usage: python filter.py <input BAM> <output BAM>
  
## Defaults (modify script to change value): 
* minimum alignment score: 5
* max edit distance: 3
    
## Filters (additional):
* removes duplicates
* removes if read pair is on different chromosome
* removes reads with no CIGAR code 
* removes reads with hard clipping on either end
* removes reads with same orientation
    
## Dependencies:
* pysam
* sys
* os
* os.path
  
## To install pysam (http://pysam.readthedocs.io/en/latest/api.html):
  
    a) Either install globally on machine: 
          pip install pysam
          
    b) or create a virtualenv:
          virtualenv venv
          source venv/bin/activate
          pip install pysam
