# Tweet Sentiment Analysis

This Python program performs sentiment analysis on Twitter datasets, specifically `twitter_training.csv` and `twitter_validation.csv`. It analyzes the distribution of sentiments (feelings) expressed in tweets and the average length of tweets for each sentiment.

## Purpose

The primary purpose of this program is to:

* **Visualize Sentiment Distribution:** Generate bar charts showing the count of tweets for each sentiment category (e.g., positive, negative, neutral).
* **Analyze Tweet Length:** Generate bar charts showing the average length of tweets for each sentiment category.
* **Provide insights:** help the user understand the sentiment trends and tweet characteristics within the provided Twitter datasets.

## Files

* `twitter_training.csv`: The training dataset containing tweets and their corresponding sentiment labels.
* `twitter_validation.csv`: The validation dataset used to evaluate the analysis.
* `tweet_analysis.py`: The Python script that performs the sentiment analysis and generates the visualizations.
* `Training_feeling_distribution.png`: Bar chart showing the sentiment distribution of the training data.
* `Training_average_tweet_length_by_feeling.png`: Bar chart showing the average tweet length per sentiment for the training data.
* `Validation_feeling_distribution.png`: Bar chart showing the sentiment distribution of the validation data.
* `Validation_average_tweet_length_by_feeling.png`: Bar chart showing the average tweet length per sentiment for the validation data.

## Requirements

* Python 3.x
* pandas (`pip install pandas`)
* matplotlib (`pip install matplotlib`)

## How to Run

1.  **Install Dependencies:** Ensure you have Python and the required libraries installed.
2.  **Place Data Files:** Place `twitter_training.csv` and `twitter_validation.csv` in the same directory as `tweet_analysis.py` or update the file paths within the `tweet_analysis.py` script.
3.  **Run the Script:** Open a terminal or command prompt, navigate to the directory containing the script, and execute:

    ```bash
    python tweet_analysis.py
    ```

4.  **View Results:** The program will generate and display four plots, and save them as PNG files in the same directory. The terminal will show a message indicating that the analysis is complete.

