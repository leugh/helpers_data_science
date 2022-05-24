# Version: 0.0.3
* Added helpers for text analytics

# Version: 0.0.4
* Added function to search newsapi using sources
* Applied small formatting changes to code

# Version: 0.0.5
* Added get_data_using_catalog

# Version: 0.0.6
* Moved get_data_using_catalog into own file

# Version: 1
* Added functions for normalization pipeline

# Version: 1.1
* Params for stemming and removing stopwords

# Version: 2
* Helpers for Azure

# Version: 2.1
* Changed file name of Helpers for Azure and added more comments there

# Version: 2.2
* Improved get_entities_for_category

# Version: 2.3
* Added get_value_counts_as_df

# Version: 2.4
* Put helpers for newsapi from helpers_misc into own file

# Version: 2.5
* Helps for Azure now support sentiment

# Version: 2.5.1
* Fixed issues with src/target-columns in get_sentiment

# Version: 2.5.2
* Improvements in get_sentiment

# Version: 2.6
* Added get_key_phrases

# Version: 2.6.1
* Fixed issue in get_key_phrases

# Version: 2.7
* Added helpers for mongodb

# Version: 2.7.1
* Using parse_uri for connection to pymongo

# Version: 2.7.2
* Rm unused stuff in get_mongo_collection

# Version: 2.7.3
* collection_name in get_mongo_collection can be passed in

# Version: 2.7.5
* remove stopwords only returns if len(token) > 1

# Version 2.8
* Added helpers for time series

# Version 2.8.1
* Added calculation for residuals to get_baseline()

# Version 2.8.2
* Can now define whether get_baseline() should drop_nas when getting the lagged values

# Version 2.8.5
* replace_special_characters in normalize_text now with substitution_string

# Version 2.9.0
* stem_words in helpers_text.py now getting spacy-model as param (speed reasons)

# Version 2.9.1
* stem_words in helpers_text.py now getting spacy-model as param (speed reasons)

# Version 2.9.2
* stem_words in helpers_text.py now getting spacy-model as param (speed reasons)

# Version 3
* New version for get_mongo_db_collection

# Version 3.0.1
* Split up get_mongo_db_collection (get_db, get_collection, get_client)

# Version 3.0.2
* Added check for existing collection