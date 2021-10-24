# COVIDPearsonCorrelation
Get the Pearson Correlation between 2 countries  
  
  
## Dependencies  
[Pandas:](https://pypi.org/project/pandas/)  
```
pip install pandas
```
## Usage  
Git clone the repo. In the `pear_corr.py` file, there are 2 lines for changing the country:  
```python
COUNTRY_1: str = "Australia"
COUNTRY_2: str = "Bangladesh"
```
Change these two to any combination of any country available in the `WHO-COVID-19-global-data.csv` file. Following that, run the python file:  
```
python pear_corr.py
```
Or, if you are on Linux:
```
python3 pear_corr.py
```


## External data
If this information feels outdated, download the file from:  
- [Daily cases and deaths by date reported to WHO](https://covid19.who.int/WHO-COVID-19-global-data.csv)  

and replace the `WHO-COVID-19-global-data.csv` file. If the file is no longer available, check [WHO website's COVID information area](https://covid19.who.int/info/)
