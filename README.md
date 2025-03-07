# flo-rider.github.io
# Airbnb prices in European cities

### Aim of this analysis:

* Data prep
    - add city field
    - add weekend/weekday flag
    - 
    - combine all files
* EDA
    - distribution of prices by city
    - distribution of room type

* Regression modellng to estimate how different attributes affect listing price

* Identify spatial clusters of listings
* Plot clusters on a map
* Does being close to the cluster centre affect prices?

* Is there a superhost premium? (Do superhosts charge more?)

* Are listing prices more expensive on weekends? To what extent? Do we observe the same in all cities?
    - logistic re
    - propensity score matching between a weekday and weekend listing
    - 
    

### About the data
I used a data set that contains Airbnb listings in 10 European cities, with the following attributes available for each listing:
* realSum (the total price of the listing)
* room_type (private/shared/entire home/apt)
* host_is_superhost (boolean value indicating if host is a superhost or not)
* multi (indicator whether listing is for multiple rooms or not)
* biz (business indicator)
* guest_satisfaction_overall (overall rating from guests camparing all listings offered by host)
* bedrooms, dist (distance from city center)
* lng & lat coordinates for location identification etc. 

Data source: Kaggle https://www.kaggle.com/datasets/thedevastator/airbnb-prices-in-european-cities