#!/bin/bash

files=$(echo * | awk '{for(i=NF;i>0;--i)printf "%s%s",$i,(i>1?OFS:ORS)}')
echo *

for i in $files ; do
	if [ -f $i ]
	then
		for j in * ; do
			if [ -f "$j" ]
			then
				if [ "$i" != "$j" ]
				then
					h1=$(sha256sum $i | awk '{print $1}')
					h2=$(sha256sum $j | awk '{print $1}')
					if [ "$h1" = "$h2" ]
					then
						echo "todelete : $j"
						rm $j
					fi
				fi
			fi
		done
	fi
done
