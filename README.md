# Duolingo Vocabulary Scraper 📝

## 📌 About
This Python script extracts **French vocabulary words** and their **English translations** from a **static HTML file** that you manually download from Duolingo. It does **not** interact with Duolingo’s website directly and follows ethical data extraction practices.

The extracted vocabulary corresponds to **Duolingo’s CEFR-120 level**, covering up to **B1-level French (about 5000 words).** 📚

---

## 🔧 How to Use

### 1️⃣ **Download Your Vocabulary Page**
1. **Log in to Duolingo** and go to the **Practice Hub** or any vocabulary list page.
2. **Save the page** as a **Complete Webpage (HTML only)**:
   - On Chrome: `Right-click → Save As... → HTML File`
   - On Firefox: `File → Save Page As... → HTML File`
3. Name the file **`Duolingo.html`** and place it in the same folder as the script.

### 2️⃣ **Run the Python Script**
Make sure you have **Python installed**. Then, install **BeautifulSoup** and **Pandas** if you haven't already:

```bash
pip install beautifulsoup4 pandas
```

Then, run the script:

```bash
python scrape_duolingo.py
```

### 3️⃣ **Check the Extracted Vocabulary**
The script will create a CSV file:  
📄 **`duolingo_vocabulary.csv`** → This file contains **French words** and their **English translations**, separated by `|`. Example output:

```
French | English
assaisonné | dressed, seasoned
savoureux | tasty
```

---

## ⚠️ **Disclaimer**
This script **does not violate Duolingo’s Terms of Service**, as it only processes **a manually downloaded static file**. It does **not** scrape live data, bypass security measures, or interact with Duolingo’s servers.

You are responsible for using this script **only for personal learning purposes**. 🚀

---

## 🐜 License
This project is licensed under the **MIT License** – feel free to use and modify it for personal learning.

📩 If you have any questions or need improvements, feel free to contribute!

