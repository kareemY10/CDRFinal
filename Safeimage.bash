xxd sample.jpeg | egrep -B 1000000 "ff ?d9" > ImageHex

echo "" > ImageHexText

xxd -r ImageHex > ima.jpeg 

