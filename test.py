import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# Load dataset from a CSV file
def load_data(file_location):
    dataframe = pd.read_csv(file_location)
    dataframe.columns = ["ID", "Topic", "Feeling", "Text"]
    dataframe = dataframe.dropna(subset=["Text"])
    dataframe["Text"] = dataframe["Text"].astype(str)
    dataframe["Text_Size"] = dataframe["Text"].apply(len)
    return dataframe

# Analyze and visualize sentiment distribution
def show_feeling_counts(dataframe, dataset_name):
    feeling_counts = dataframe["Feeling"].value_counts()
    feeling_counts.plot(kind='bar', color=['red', 'blue', 'green', 'gray'])
    plt.xlabel("Feeling")
    plt.ylabel("Number of Tweets")
    plt.title(f"Distribution of Feelings in {dataset_name} Tweets")
    plt.savefig(f"{dataset_name}_feeling_distribution.png")
    plt.show(block=True)

# Analyze and visualize average tweet length per sentiment
def show_average_tweet_length_by_feeling(dataframe, dataset_name):
    average_length = dataframe.groupby("Feeling")["Text_Size"].mean()
    average_length.plot(kind='bar', color=['red', 'blue', 'green', 'gray'])
    plt.xlabel("Feeling")
    plt.ylabel("Average Tweet Length")
    plt.title(f"Average Tweet Length for Each Feeling in {dataset_name}")
    plt.savefig(f"{dataset_name}_average_tweet_length_by_feeling.png")
    plt.show(block=True)

# Main execution block
if __name__ == "__main__":
    training_file = r"C:\Users\gargs\OneDrive\Desktop\Indolike\Social Media Engagement Analysis\twitter_training.csv"
    validation_file = r"C:\Users\gargs\OneDrive\Desktop\Indolike\Social Media Engagement Analysis\twitter_validation.csv"

    # Analyze training data
    training_data = load_data(training_file)  # Corrected: Use training_file variable
    show_feeling_counts(training_data, "Training")
    show_average_tweet_length_by_feeling(training_data, "Training")

    # Analyze validation data
    validation_data = load_data(validation_file) # Corrected: Use validation_file variable
    show_feeling_counts(validation_data, "Validation")
    show_average_tweet_length_by_feeling(validation_data, "Validation")

    print("Analysis complete. Check the generated plots.")