# Hospitals-Database
An Example Implementation to generate 15k+ articles on hospitals in telugu

To Generate Articles of Hospitals in Telugu We have to follow the 4 main Steps :-
1. Data Collection.
2. Data Transaltion.
3. Template Creation.
4. Wiki-Article Generation.

# Data Collection
We have many resources to collect details of Hospitals. In this Project we have used data from mainly 3 websites , as we have to collect good number of variables to create article. so, we used data from 3 websites and merged them together. Following are the websites from which we collected the data.

1. www.practo.com
2. https://data.gov.in/catalog/hospital-directory-national-health-portal
3. https://nationalinsurance.nic.co.in/en/health-insurance/city-wise-list-ppn-hospitals

We have Scraped the Data from practo using Beautiful Soup and We have got files from the other 2 websites. After Collection of Data We have to merge the 3 excel files and clean the data.

# Data Transaltion and Transliteration.
After Collecting the data and cleaning it We have to translate the data for article creation. We can use google translator,bing transaltor, python tools such as deep translit, anuvaad etc. We have used google translate for the translation of data and for transaliteration we have used ai4bharat-transliteration.

After the conversion of data using bot the above tools we have data corrected remaining errors manually. We have stored the original data and transalted data for each attribute side by side in the xlsx file present in Translated_Data Folder.

# Template Creation.
We use Jinja2 template engine for creating templates for domain specific Wiki articles. Jinja2 is a powerful template engine which allows users to create diverse templates.

After the Collection and Translation of Data, We wrote a template using jinja2 so that we can render the data and create articles.

# Wiki-Article Generation.
We then integrate the translated data and template using a python program. This generates a wiki XML file, that can be imported to wikipedia.
