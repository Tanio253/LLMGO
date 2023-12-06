import streamlit as st
import subprocess
import pandas as pd
import os


def read_crawl_data(selected_spider):
    file_path = f"vietsov_crawler/vietsov_crawler/formatted_{selected_spider}.json"
    df = pd.read_json(file_path)
    if selected_spider=="GT":
        df['image'] = df['image'].apply(lambda x: [x] if isinstance(x, str) else x)
    return df

# Function to run the selected spider file
def run_crawler(selected_spider):
    st.text("Crawling in progress...")
    # Run the spider using subprocess
    subprocess.run(["scrapy", "crawl", f"{selected_spider}crawler", "-o", f"{selected_spider}.json"])
    subprocess.run(["python", "format_json.py", "--file_path", f"{selected_spider}.json"])
    st.text("Crawling completed!")

# Function to display a download link for the crawled data
def download_crawl_data_json(selected_spider, json_content):
    st.download_button(
        label="Download Crawled Data",
        data=json_content.encode('utf-8'),
        file_name=f"{selected_spider}_crawled_data.json",
        key=f"{selected_spider}_download_button",
    )

# def download_crawl_data_csv(selected_spider, df):
#     csv_data = df.to_csv(index=False).encode('utf-8')
#     st.download_button(
#         label="Download Crawled Data (CSV)",
#         data=csv_data,
#         file_name=f"{selected_spider}_crawled_data.csv",
#         key=f"{selected_spider}_download_button_csv",
#     )


# Function to display a preview of the crawled data
def display_crawl_preview(df):
    st.markdown("### Crawled Data Preview:")
    st.dataframe(df)  # Displaying the first 10 rows

# Streamlit app layout
st.title("Scrapy Crawler App")

# Select list for choosing the spider
selected_spider = st.selectbox("Select Spider", ["GT", "DVTT", "SPDV", "NNL", "CSVC", "DADT", "TT", "TDTS"])
# Button to trigger the crawling process


# Display the preview of crawled data on the right side
file_path = f"vietsov_crawler/vietsov_crawler/formatted_{selected_spider}.json"
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        json_content = file.read()
    df = read_crawl_data(selected_spider)
    download_crawl_data_json(selected_spider, json_content)
    # download_crawl_data_csv(selected_spider, json_content)
    display_crawl_preview(df)
else:
    st.sidebar.warning("No data available. Please run the crawler first.")
