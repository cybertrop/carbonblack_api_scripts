# This bash script will take your CB API binary_search.py output data
# and parse it into a JSON format for further data ingestion or what have you

file="$1"
for x in file; do
  cat binary_search_data.txt
  | sed "s/u'/'/g"
  | sed "s/'/\"/g" 
  | sed "s/True/\"True\"/g" 
  | grep -Ei "{.*}" 
  | sed "s/Original Document    : //g"
done
