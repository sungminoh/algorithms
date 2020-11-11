#! /bin/sh
#
# solution.sh
# Copyright (C) 2019 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.
#

# Read from the file file.txt and print its transposed content to stdout.

function transpose {
  awk '
  { 
      for (i=1; i<=NF; i++)  {
          a[NR,i] = $i
      }
  }
  NF>p { p = NF }
  END {    
      for(j=1; j<=p; j++) {
          str=a[1,j]
          for(i=2; i<=NR; i++){
              str=str" "a[i,j];
          }
          print str
      }
  }' $1
}

function transpose1 {
  seq $(head -1 $1 | wc -w) | xargs -I '{}' bash -c "cut -d\  -f {} $1 | xargs"
}


transpose1 $1
