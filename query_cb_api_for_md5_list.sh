# This is bash script provides a list of hashes as input 
# and invokes the CB API binary_search.py script to 
# query the CB API for all data related to that binary

# Please rememeber that you need to setup your CB API
# key in your local machine so you can run these scripts
# natively in your desktop terminal

# Example: ./query_cb_api_for_md5_list.sh <list_of_hashes.txt>
# The script will take the list of hashes as an argument
# where $line is each individual hash 

file="$1"
lineknt=0
while IFS= read -r line
do
  lineknt=$(($lineknt+1))
  echo "queryMD5(): Line $lineknt from $file : $line"
  python binary_search.py --query "$line" > binary_search_data.txt
done < "$file"
