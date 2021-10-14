# Surfs Up
## Overview of the analysis:
The purpose of this analysis is to gather information on the temperatures during the month of June and December. Finding this summary statistics will assist in determining the success of a Surf/Icecream shop. 

## Results: 
The three key differences in weather between June and December:

- the count of June temperatures are 1700 where December's count is 1517
- the avg temp in June is 75 where in December it is 71 
- the range of June temperatures are between 64 and 85 where in December the range is largers, between 56 and 83
- ![June Summary](https://github.com/HappyM0f0/surfs_up/blob/main/images/June_description.png)
![December Summary](https://github.com/HappyM0f0/surfs_up/blob/main/images/Dec_description.png)


## Summary:

Analyzed months show temperature differences between Dec and June do not vary greatly, and 71 degrees or more is typical surfing weather requiring no wetsuit or just a 1-2mm top as reported by [Perfect Wetsuit](https://perfectwetsuit.com/guide/wetsuit-thickness-and-temperature-guide). This ideal weather can assist with the success of a Surf/Icecream shop as it requires less to start surfing, increase the chances of interested customers both young and old.

Further expansion of the code could include precipitation data for these months, which would be the most significant barrier to customer traffic.

```python
# find and filter percepitation for the month of June
session.query(Measurement.prcp).filter(func.strftime("%m", Measurement.date) == "06")
```
The significant difference in counts may bias the existing data. Selecting a specific station (preferred the most active) will reduce the overall count number but bring them closer in range, reducing bias.

```python
# filter to station to most active station
filter(Measurement.station == 'USC00519281')
```