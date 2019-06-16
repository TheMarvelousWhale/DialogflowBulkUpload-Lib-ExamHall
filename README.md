# Dialogflow Bulk Upload for Library and Exam Hall
#### _This is a watered down version of the TR code_
#### _For Simplicity, only Exam Hall will be uploaded, but Lib files will work the same (with the modification in regex pattern)_


#Instructions
Create a new folder and dump ALL the json file and the py file inside.
Extract the zip and put the Lyon - Template folder in the newly created folder.
The QnVarTemplate excel use 00 as placeholder for the location name
The main file has two columns, one for Q and one for A

### Now Open the python file

Make sure that the files from line 20-25 (json files) and 40-41 (excel files) are named correctly (if it doesn't then again, FileNotFound Error from Python) 
Make sure the 6 libraries are in your system

And hit RUN. Hopefully the following will happen:

1. Shutil lib creates a copy of "Lyona Template" folder

2. Pandas reads the two excel files into its Dataframes for processing

3. Json reads the 2 json into python format

4. Python goes down the row of the main DF and during which...

5. Regex extracts the info out of the DF. *You may wish to update examp (stands for exam - pattern) raw string on line 35*

6. Deepcopy makes a copy of the json files and Python slots the info in the correct place

7. Json exports the python thing into json and puts the json directly into the "Lyona Template - Copy" folder.

8. Shutil zips the folder up into file called "New Intents.zip" and deletes the folder

Now you need to pray that everything works correctly and upload this zip into the Dialogflow agent.

### EXPECTED OUTPUT

There will be as many intents as there are intended in the excel files. These intents will have a message and a link button to the NTU map (formatted to Kommunicate custom payload)
