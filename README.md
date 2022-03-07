# Warning!!!
- Don't execute this script.
- Yahoo Finance does not allow web-scraping.
- This code was developed before I found the policy.

---

# Description
The script retrieves USD/Yen exchange rate of a specified date.

```
% python main.py 2021 3 2
                    0           1           2           3
日付                 始値          高値          安値          終値
2022年3月2日  114.890000  115.680000  114.770000  115.500000
```

---

# Requirements

## python packages
- selenium
- pandas

## external libraries
- chromewebdriver
```
brew install chromedriver
```

## Browser
- Chrome
  - chromewebdriver may require you to upgrade your Chrome
  