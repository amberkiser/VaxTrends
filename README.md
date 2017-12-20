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
![alt tag](https://user-images.githubusercontent.com/31290421/34189665-d5cd2204-e4f9-11e7-96b8-c47334a7a262.png "Home Page")

Vaccination Coverage 
- Choose a vaccine from the dropdown and hit submit to see the chart of vaccination coverage.
![alt tag](https://user-images.githubusercontent.com/31290421/34189666-d5e318ac-e4f9-11e7-9382-17b1e182e933.png "Coverage Page")

VPD Incidence Rate 
- Choose a vaccine-preventable disease (VPD) from the dropdown and hit submit to see the chart of incidence rate per 100,000 population.
![alt tag](https://user-images.githubusercontent.com/31290421/34189667-d5f71c80-e4f9-11e7-92aa-ba3b6e15e3f7.png "Incidence Rate Page")

- There is also a table that shows which vaccines provide protection against specific diseases and when a vaccine against the disease was first available.
![alt tag](https://user-images.githubusercontent.com/31290421/34189668-d60a2f50-e4f9-11e7-9809-d49462090ea0.png "Incidence Rate Page 2")

Immunization Schedule
- The immunization schedule is directly linked from the CDC.
![alt tag](https://user-images.githubusercontent.com/31290421/34189670-d623bc7c-e4f9-11e7-9205-e19aef918efd.png "Immunization Schedule Page")

Data Sources
- This page links to all the data sources used in this web app.
![alt tag](https://user-images.githubusercontent.com/31290421/34189671-d635f220-e4f9-11e7-8231-d7e3da3bb4ef.png "Data Sources Pages")

# Demo
https://youtu.be/LMq-C_lR7Vg
