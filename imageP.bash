#! /bin/bash




xxd ima.jpeg | egrep -A 10000 "ff ?d9" > ImageHex

echo "" > ImageHexText
xxd -r ImageHex >> ImageHexText 

