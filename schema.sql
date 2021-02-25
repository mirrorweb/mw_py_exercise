CREATE Database test;
use test;
CREATE TABLE Company (
id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) UNIQUE NOT NULL,
safe_name varchar(100) NOT NULL,
address text null,
telephone Bigint null,
enterprise bool default false,
active bool default True,
created timestamp default current_timestamp,
updated timestamp default current_timestamp on update current_timestamp
)
;
CREATE TABLE Employee (
employee_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(100) NOT NULL,
email varchar(100) not null,
firstname varchar(50) NOT NULL,
lastname varchar(50) not null,
address text null,
department varchar(255) null,
job varchar(100) not null,
created timestamp default current_timestamp,
updated timestamp default current_timestamp on update current_timestamp,
company_id int UNSIGNED ,
 FOREIGN KEY (company_id) REFERENCES Company(id)
)
