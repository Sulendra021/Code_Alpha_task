# Web Scraping: Largest Companies in India (Forbes 2025)

## Overview

This project demonstrates how to perform web scraping using **Python**, **Requests**, **BeautifulSoup**, and **Pandas** to extract data from the Wikipedia page **"List of largest companies in India"**.

The script automatically locates the **2025 Forbes list** table, extracts company information, converts it into a structured Pandas DataFrame, and exports the data as a CSV file.

This project is intended for educational purposes and demonstrates fundamental web scraping, HTML parsing, and data preprocessing techniques.

---

## Dataset

The extracted dataset contains the following attributes:

| Rank | Forbes 2000 Rank | Name | Headquarters | Revenue (Billions US$) | Profit (Billions US$) | Assets (Billions US$) | Value (Billions US$) | Industry |
|------|-------------------|------|--------------|-------------------------|------------------------|------------------------|----------------------|----------|
---

## Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- Pandas

---



## Installation

Clone the repository

```bash
git clone https://github.com/Sulendra021/Code_Alpha_task.git
```

Move into the project directory

```bash
cd Code_Alpha_task
```

Install the required libraries

```bash
pip install requests beautifulsoup4 pandas
```

---

## How the Script Works

The script performs the following steps:

1. Sends an HTTP request to the Wikipedia page.
2. Parses the HTML using BeautifulSoup.
3. Searches for the **2025 Forbes list** section.
4. Locates the corresponding Wikipedia table.
5. Extracts table headers and rows.
6. Converts the extracted data into a Pandas DataFrame.
7. Displays the first few records.
8. Saves the dataset as a CSV file.

---

## Output

After execution, the script generates

```
forbes_2025_india.csv
```


## Learning Objectives

This project demonstrates:

- Web scraping using Requests
- HTML parsing with BeautifulSoup
- Extracting HTML tables
- Data cleaning
- Creating Pandas DataFrames
- Exporting data to CSV
- Basic automation using Python

---

## Project Documentation

A detailed explanation of the implementation, methodology, and workflow is available in the attached PDF file:

**[Web_Scraping_Code_Explanation.pdf](./Web_Scraping_Code_Explanation.pdf)**

The document includes:

- Project overview
- Code explanation
- Web scraping workflow
- Libraries used
- Dataset description
- Output screenshots (if included)
- Conclusion

---

## Source

Data is collected from the Wikipedia page:

https://en.wikipedia.org/wiki/List_of_largest_companies_in_India

---



## Author

**Sulendra**

Linkedin: https://www.linkedin.com/in/sulendra-kumar-728782278/

---

