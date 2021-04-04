# Election-Analysis
## Overview of Election Audit: 
The purpose of this election audit is to provide the election commission with results from their most recent election. This audit will assist the commission in understanding voter turnout from each county, the percentage of votes from each county out of the total count, as well as the county with the highest voter turnout.    

## Election-Audit Results: 
The following information can be observed by clicking the link below:

•	Number of votes cast in this congressional election

•	Number of votes and the percentage of total votes for each county

•	County with the largest number of votes

•	Number of votes and the percentage of the total votes each candidate received

•	Winning candidate, total vote count for winning candidate, and the percentage of the total votes received by winning candidate
 
https://github.com/lmiles77/Election-Analysis/blob/main/Election_Results_txt.PNG







## Election-Audit Summary:
The script provided can be utilized by the election commission to analyze future election data by first ensuring file to load follows similar path as one provided. The future election results (csv file) should be stored in the “Resources” folder of programmer or changed to suitable location. If location is changed it will also need to reflect in the os.path. The title of the election results file (csv) to be analyzed will need to be changed to the title of the file to be analyzed.  The title of the election results (csv file) will also need to be changed throughout the Pypoll Challenge.py file to reflect the name of the file to be analyzed. This will need to be done to avoid analyzing incorrect data.

(Add a variable to load a file from a path.)
file_to_load = os.path.join("Resources", "election_results.csv")

Additionally, a text file will need to be created in the “analysis folder” to store results for the election. The title of the txt file will need to be changed throughout the PyPoll Challenge.py to reflect the txt file title. This will create a txt file that will store current election results in the “analysis folder”. Making these changes will allow the election commission to utilize the PyPoll Challenge.py for analysis on future election data. 

(Add a variable to save the file to a path.)
file_to_save = os.path.join("analysis","election_results.txt")



