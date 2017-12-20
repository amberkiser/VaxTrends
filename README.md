# VaxTrends
Django web app with charts and information from the CDC regarding vaccination coverage in children age 19-35 months and incidence rates of vaccine-preventable diseases.

Every year the Centers for Disease Control and Prevention publish data about vaccination coverage and incidence rates of nationally notifiable infectious diseases. 

The following pages illustrate the estimated vaccination coverage in children age 19-35 months in the US. This means the percentage of children who have received appropriate doses for a given vaccine. To understand what the appropriate dose and recommended vaccines are, please see the linked immunization schedule published by the CDC. 

Also included are charts showing the incidence rate of specific vaccine-preventable diseases (VPDs) per 100,000 population. These are based on the reported cases published by the CDC in the Morbidity and Mortality Weekly Report as well as the population estimates published by the US Census Bureau.

# Dependencies
This web app uses the following packages:
- python v3.6.3
- django v1.11.8
- bokeh v0.12.13
- pandas v0.21.1
- os 

See the environment.yml file for full details.

# Use Cases
Home Page
![alt tag](https://user-images.githubusercontent.com/31290421/34189059-db542194-e4f6-11e7-9181-0e1a7ca0481e.png "Home Page")

Vaccination Coverage 
- Choose a vaccine from the dropdown and hit submit to see the chart of vaccination coverage.
![alt tag](https://user-images.githubusercontent.com/31290421/34189060-db68868e-e4f6-11e7-904f-b68394a44bab.png "Coverage Page")

VPD Incidence Rate 
- Choose a vaccine-preventable disease (VPD) from the dropdown and hit submit to see the chart of incidence rate per 100,000 population.
![alt tag](https://user-images.githubusercontent.com/31290421/34189061-db7d977c-e4f6-11e7-84b8-d63a32b8a610.png "Incidence Rate Page")

- There is also a table that shows which vaccines provide protection against specific diseases and when a vaccine against the disease was first available.
![alt tag](https://user-images.githubusercontent.com/31290421/34189062-db9684f8-e4f6-11e7-8c93-9ddf2c41e88b.png "Incidence Rate Page 2")

Immunization Schedule
- The immunization schedule is directly linked from the CDC.
![alt tag](https://user-images.githubusercontent.com/31290421/34189063-dba983d2-e4f6-11e7-8ae0-404d8cf3f8da.png "Immunization Schedule Page")

Data Sources
- This page links to all the data sources used in this web app.
![alt tag](https://user-images.githubusercontent.com/31290421/34189064-dbbf6792-e4f6-11e7-8184-775413dc3d54.png "Data Sources Pages")
