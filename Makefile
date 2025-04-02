export:
	./export
	echo 'Download the file from Notion when it's ready, because we can't get it via API anymore, and put it in export.zip'

continue:
	./extract && ./commit
