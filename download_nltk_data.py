"""
This script sets up the necessary resources for Natural Language Processing (NLP)
using the NLTK (Natural Language Toolkit) library. It handles SSL connectivity issues
and downloads specific NLTK resources required for tokenization, lemmatization,
and lexical database functionality.

Modules Used:
--------------
- `nltk`: Provides tools for tasks such as tokenization, lemmatization, and working
          with the WordNet lexical database.
- `ssl`: Used to configure secure HTTPS network connections.

Functionality:
--------------
1. Fixes SSL certificate validation issues for HTTPS connections, especially on older systems.
2. Downloads the following NLTK resources:
   - `punkt_tab`: Likely for tokenization tables (might be part of the `punkt` tokenizer).
   - `wordnet`: The WordNet lexical database (used for synonyms, lemmatization, etc.).
   - `omw-1.4`: Open Multilingual WordNet to extend WordNet's functionality with multilingual support.

Usage:
------
Run this script to ensure that all necessary NLTK resources are downloaded and installed
into the local `nltk_data` directory.

Notes:
------
- If you encounter SSL errors during downloading, the unverified SSL context resolves them.
- The downloaded data is stored under the default `~/nltk_data` directory.

"""
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt_tab')  # Download the punkt_tab resource
nltk.download('wordnet')  # For WordNetLemmatizer
nltk.download('omw-1.4')  # Needed for extended WordNet functionality