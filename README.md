



# Data Sources
https://www.naturalearthdata.com/downloads/110m-cultural-vectors/ -> Admin 1 -> States and Provinces

https://public.opendatasoft.com/explore/dataset/georef-united-states-of-america-zcta5/table/?flg=en-us&disjunctive.ste_code&disjunctive.ste_name&disjunctive.coty_code&disjunctive.coty_name&disjunctive.zcta5_code&disjunctive.zcta5_name&sort=year

https://gist.github.com/Tucker-Eric/6a1a6b164726f21bb699623b06591389

https://simplemaps.com/data/us-zips

https://postalpro.usps.com/ZIP_Locale_Detail



# Analysis

https://docs.google.com/spreadsheets/d/13osRy0mj4zq8cSxxxmjy6RECt3ZOTCPY385EPWaE_9k/edit?gid=806082658#gid=806082658

https://chatgpt.com/c/66e496fb-8fd4-8009-9bf1-9deecd0c6e20?conversationId=66e496fb-8fd4-8009-9bf1-9deecd0c6e20



```bash
cat simplemaps_uszips_basicv1.85/uszips.csv | python3 city_across_states_count.py
```

```bash
cat simplemaps_uszips_basicv1.85/uszips.csv | python3 count_duplicate_cities_with_counts.py
```

