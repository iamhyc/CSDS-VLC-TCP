#!/bin/bash
diff -Z $1 $2 > result.txt
a=`wc -l text_tx.txt | awk -F" " '{print $1}'`
b=`cat result.txt | grep -e "c" | wc -l`
echo -e "Total Lines:\t\t$a"
echo -e "Different Lines:\t$b"
echo -e "Error Rate (Frame):\t `echo "scale=6;$b/$a" | bc` "
