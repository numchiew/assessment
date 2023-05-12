# Requirement

1. User Should able to create as many store as they like.\
2. Store will have 2 type of store. ( StoreFront and MicroStore )\
3. User Should able to register product as many as they like.\
4. Product will have 2 type. (Special and Normal) and should able to store image in system.\
5. MicroStore can only displayed 'Special Product'\
6. StoreFront can display every type of product.\
7. User should able to choose which product to display on which stored.\
8. Should able to search product by criterias. ( title, description, stock, availability, last_updated and tags )


# How to Store a data from Client side ? 
We can store most of metadata from client directly in database except product image.
We could stored a product image in S3 bucket and then setup visibility to allow access from client side. 
The reason why we choose S3 in this case is ability to serve a content globally without need of CDN and AWS will handle the load for us.

# How to do search by filter and long-term support of schema evolution ? 
We could implement a basic search function by search with existing attribute in database schema. (title, description, stock, price, time, category..)
To consider we grow a lot of SKUs later on we could 'grouping' the product in our system by letting user input 'category' as freetext so once we have more data, we could build a suggestion feature to suggest a client to register their product with precise category. 
and we think that we should able to store JSON data as 'tags' attribute. 
this will let customer customized their product in our system and we can expect to use this data to improve our search service. 

# Architecture
To able to deliver MVP of this product we could focus only minimum effrot. 
so if we dont think about scalability, we can apply basic 3-tier web service architecture as a monolithic first. 
to scale this system we can do
1. breakdown our Store Management Service into micro-service achitecture.
2. Put load balancer or API gateway to handle traffic from client.
3. Caching
4. Scale-out our database, we may separate a database by user journey.
4.1 store/product management can used nosql database like mongoDB to acheive scale-out like sharding.
4.2 to integrate with payment service in the future, we can use sql database to store a transaction and extract 'quantity' or 'product availability' from product schema to acheive strong consistency. 

![ScreenShot](https://github.com/numchiew/assessment/blob/main/architecture/database_schema.png)
![ScreenShot](https://github.com/numchiew/assessment/blob/main/architecture/simeple_architecture.png)
