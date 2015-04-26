# aws_ec2_price_calculator

This program that takes AWS credentials as command line arguments and:

    1. List the number of server of each type/size, Viz. for AWS,
       m1.small -> 12
       m1.large -> 7
       .... and so on
    2. Calculate the total cost incurred on servers per hour and per month from all regions.
    
# Dependencies  
    Python with Boto module 
    
# Usage
    Just pass the region, aws access and aws secret key with the python file
     python price_calculation.py ap-southeast-1 ******************** ************************
    
# output
    ***********************************************************
               $ Monthly Calculator in USD $   
    ***********************************************************
    Instance_type Count total_per_hour_cost total_cost_per_month
    ______________ _____ ___________________ _______________________
    m1.medium      3      $0.48          $345.6 
    m3.medium      3      $0.0          $0.0
    m1.large      1      $0.32          $230.4
    m1.small      2      $0.16          $115.2
    c1.medium      1      $0.183          $131.76
    t1.micro      2      $0.04          $28.8

    

