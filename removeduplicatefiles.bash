#!/bin/bash

files=$(echo * | awk '{for(i=NF;i>0;--i)printf "%s%s",$i,(i>1?OFS:ORS)}')

echo $files

for i in $files ; do
	if [ -f $i ]
	then
		echo "i:$i"
		for j in * ; do
			if [ -f "$j" ]
			then
				echo "j:$j"
				if [ "$i" != "$j" ]
				then
					h1=$(sha256sum $i | awk '{print $1}')
					h2=$(sha256sum $j | awk '{print $1}')
					echo "h1 $h1 h2 $h2"
					if [ "$h1" = "$h2" ]
					then
						echo "todelete : $h2 $j"
						rm $j
					fi
				fi
			fi
		done
	fi
done
