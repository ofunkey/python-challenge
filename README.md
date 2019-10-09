# PyBank and PyPoll

* PyBank: Analysis on monthly Profit/Loss data
* PyPoll: Analysis on election result

## Background

In this work, I created python scripts for analyzing the financial records of PyBank and the election result of PyPoll.


## PyBank

![Revenue](Images/revenue-per-lead.png)

* In this work, I created a Python script for analyzing the financial records of PyBank. With a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv), the dataset is composed of two columns: `Date` and `Profit/Losses`. 

* Create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

  [Financial_Analysis](https://github.com/ofunkey/python-challenge/blob/master/PyBank/Output/budget_data.txt)

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```


## PyPoll

![Vote_Counting](Images/Vote_counting.png)

* In this work, I created a Python script for analyzing the votes of election result of PyPoll.

* With a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv), the dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

* Create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

 [Election_Results](https://github.com/ofunkey/python-challenge/blob/master/PyPoll/Output/election_data.txt)

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```




## Funke Olaleye | Data Analytics and Visualization

