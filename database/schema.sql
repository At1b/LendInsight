CREATE TABLE loan_data (
    id INT PRIMARY KEY,
    income BIGINT,
    age INT,
    experience INT,
    marital_status VARCHAR(20),
    house_ownership VARCHAR(30),
    car_ownership VARCHAR(10),
    profession VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    current_job_yrs INT,
    current_house_yrs INT,
    risk_flag INT
);