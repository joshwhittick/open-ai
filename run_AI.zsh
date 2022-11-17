while true
do 
	echo "Do you want to query OpenAI (y/n)?"
	read inp
	if [ $inp == "y" ]; then 
		python3 /PATH/TO/FOLDER/open_AI/AI_with_audio_input.py
	elif [ $inp == "n" ]; then 
		exit
	elif [ $inp != "y" ] | [ $inp != "n" ]; then
		echo "Please enter 'y' or 'n'"
	fi
done
