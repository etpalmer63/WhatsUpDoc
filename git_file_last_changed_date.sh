#!/bin/bash

git ls-tree -r --name-only HEAD | while read filename;
do   
    echo "$(git log -1 --format="%ad" -- $filename) $filename"; 
done > git_file_last_changed_date.tmp

#echo "bash script complete"
