# ZFS project Code Instruction

Oh, I hate to write document since I have broken English. If anyone could help me, I will really appreciate.

## Basic ideas
As we discussed before, the basic processdure should be like:

1. Load the dataset from memory. This is done in `dataload.py`.
2. Beofore we feed the data to ChatGpt, we did some classfications. This is be done in `classfication.py`.
3. We use LLM do the recommendation. This is done in `recommendation.py`.
4. We run our program from `ZFS.py`. The command is quite straightforward:
```python
python ZFS.py
```

## Before you run the code
I would suggest VScode as our developing environment.

I would suggest the Github destop App if you are not familiar with the git command. Here is the link: https://desktop.github.com/

Make sure that you have got openai key, and set the configration. Please refer to the documentation: https://platform.openai.com/docs/quickstart/step-2-set-up-your-api-key

## What on earth every file and directory do
**Code**
`ZFS.py`: The program begins from here. Just like the main function in C.

`dataload.py`: This file is used for loading data from the file. Now it only has one function: `read_posts_from_file()`. It should be noted that during the loading process, we finished the classification process.

`classfication.py`: This file is used for the local classfication. Now it has only one function: `is_leasing_post()`, and it always returns True.

`recommendation.py`: This file is used for recommendation. Now we just use ChatGpt to do a lazy implementation. 

**Markdown Documentation**
`Readme.md`: Yes, what you are reading is readme.md.

`Log.md`: As suggested by the name, it is the log file.

**Dataset**
`Dataset_Raw_From_Facebook`: This directory and the dataset inside is by Amen. Well done! There are 3 files, and maybe Amen could explain those files in detail. What I am using now is the raw_overview.csv.

`Dataset_For_Classification`: This directory should be used training the classfication algorithm. Now it is empty.

`Dataset_For_Recommendation`:This directory should be used training the recommendation algorithm. Now it is empty.

## Proposal before midterm
* We may train some classification algorithm and test it.
* We may test the accuracy of the recommendation algorithm.
* We may do some prompt engineering to make the result better.
* We need to finish the presentation.

## Proposal before final
- We may use the web API to read the data from web
- We may redesign the recommendation algorithm. For example, we could try some library, such as langchain, Kor.
- We may design some UI to accept user input.
- We may design some module to push the notifications to client's Email.
- We may do some analysis from the commercial view (E.g., is it possible to gain profit? Who will be our potiental client? ).
- We need to finish the presentation.