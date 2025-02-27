from bs4 import BeautifulSoup
import pandas as pd
import unicodedata

def clean_text(text):
    """Normalize and clean text to handle special French characters."""
    return unicodedata.normalize("NFKC", text).strip()

# Load the downloaded HTML file
file_path = "Duolingo.html"  # Update with your actual file path

with open(file_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Find all <li> elements containing vocabulary pairs
word_elements = soup.find_all("li", class_="_2g-qq")

# Extract French words from <h3> and English translations from <p>
words = []
for element in word_elements:
    french_word = element.find("h3")
    english_translation = element.find("p")

    if french_word and english_translation:
        words.append(f"{clean_text(french_word.text)} | {clean_text(english_translation.text)}")
    elif french_word:
        words.append(f"{clean_text(french_word.text)} | Unknown")  # If translation is missing

# Save to CSV with proper encoding
df = pd.DataFrame(words, columns=["French | English"])
df.to_csv("duolingo_vocabulary_1.csv", index=False, encoding="utf-8-sig")

print("Words extracted and saved to 'duolingo_vocabulary_1.csv'.")
