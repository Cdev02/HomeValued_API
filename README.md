## HomeValued Inc

This repository contains a first version of HomeValued, that is a project about an application 
that predicts house prices in Colombia.


*Characteristics of the project*:
- The data collected proceed from both government public datasets and web scrapping real estate pages available in the country.
- The ETL process is performed in another project, and then the data is served in a feature store (in AWS) in order to perform the MLOps process.
- The model that we use to predict the prices are linear models. 
- The input data must pass through a data processing and transformation pipeline before being put into the model.

*Tech stack used for the HomeValued Inc API project*
- Python/Flask
- PostgreSQL
- GitHub Actions for CI
- Docker for containerization and deployment

*Code guide*
https://pep8.org/

*Development branch*
- Dev branch in GitHub repository
*Test Environment*
- test_env branch in GitHub repository
*Production Environment*
- main branch in GitHub repository
