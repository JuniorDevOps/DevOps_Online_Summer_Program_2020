# Database Administration: **task 3.1**


## Main Terms

- ### Database
- ### Table
- ### Column
- ### Row
- ### Primary Key
- ### Foreign Key
- ### Compound Key
- ### Index
- ### Redundancy

![Image](./img/img1.png)
![Image](./img/img2.png)
![Image](./img/img3.png)
![Image](./img/img4.png)



## **1.** Download & Install MySQL server on VM

```bash
sudo apt-get install mysql-server
```
![Image](./img/mysql1.png)

```bash
sudo apt-get install mysql-client
```
![Image](./img/mysql2.png)

```bash
mysqladmin --version
```

![Image](./img/mysql3.png)

```bash
sudo mysql
```

![Image](./img/mysql4.png)

```bash
SHOW DATABASES;
```

![Image](./img/mysql5.png)

```bash
sudo mysql -u root -p
```

![Image](./img/mysql6.png)



## **2.** Create, Delete User Accounts and Grant Privileges

- ### Creating user

![Image](./img/mysql7.png)
![Image](./img/mysql8.png)

- ### Cheking privileges

![Image](./img/mysql9.png)
![Image](./img/mysql10.png)

> ### [Link to official MySQL Documentation on **Privileges**](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html)

- ### Assigning Priviledges

![Image](./img/mysql11.png)
![Image](./img/mysql12.png)

- ### Deleting user

![Image](./img/mysql13.png)






## **3.** Create a database on the server through the console

```bash
show databases;
```
![Image](./img/mysql14.png)


```bash
create database my_database;
```
![Image](./img/mysql15.png)

```bash
drop database my_database;
```
![Image](./img/mysql16.png)



## **4.** Fill in tables

- ### Main data types


![Image](./img/mysql17.png)

> ### CREATE TABLE teamstb1(column_name column_type)

```bash
CREATE TABLE teamstb1(
    team_id INT NOT NULL AUTO_INCREMENT,team_name VARCHAR(100) NOT NULL,team_captain VARCHAR(40) NOT NULL,establishment_date DATE,PRIMARY KEY ( team_id )
    );
```

```bash
CREATE TABLE resultstb1(
    result_id INT NOT NULL AUTO_INCREMENT,
    team_id INT NOT NULL,
    result_type VARCHAR(4) NOT NULL,
    game_date DATE,
    PRIMARY KEY ( result_id )
    );
```

![Image](./img/mysql18.png)

![Image](./img/mysql19.png)

![Image](./img/mysql24.png)


> ### INSERT INTO table_name ( field1, field2, field3 ) VALUES ( value1, value2, value3 );

```bash
INSERT INTO teamstb1 
(team_name, team_captain, establishment_date)
VALUES
('Dinos', 'Nick Sergienko', '2020-05-06');

INSERT INTO resultstb1 
(team_id, result_type, game_date)
VALUES
(3, 'Draw', '2020-07-08');
```

![Image](./img/mysql20.png)

```bash 
SELECT * from teamstb1
```

![Image](./img/mysql21.png)


## **5.** Describe the database schema, (minimum 3 tables)

### Importing two sample databases to our MySQL Server
> ### Original tutorials for sample databases:
> - [Employees Sample Database](https://dev.mysql.com/doc/employee/en/sakila-structure.html)
> - [MySQL Sample Database](https://www.mysqltutorial.org/mysql-sample-database.aspx)

- ### **employees.slq** Schema

![Image](./img/mysql25.png)

- ### **classicmodels.slq** Schema

![Image](./img/mysql26.png)

![Image](./img/mysql27.png)
![Image](./img/mysql28.png)
![Image](./img/mysql29.png)
![Image](./img/mysql30.png)


## **6.** Execute SQL queries DDL, DML, DCL

### **SELECT** [ what to select ] **FROM** table(s) **WHERE** [ conditions that data must satisfy ];


### Comparison operators are: **<  <=  =  !=  <>  >=  >**


### Logical operators are: **AND OR NOT**


### Comparison operator for special value **NULL**: **IS**


![Image](./img/mysql22.png)
![Image](./img/mysql23.png)
![Image](./img/mysql33.png)
![Image](./img/mysql34.png)
![Image](./img/mysql35.png)
![Image](./img/mysql36.png)
![Image](./img/mysql37.png)
![Image](./img/mysql38.png)
![Image](./img/mysql39.png)
![Image](./img/mysql40.png)





```bash
CREATE TABLE crowds_tb1(
    game_id INT NOT NULL,
    game_date DATE NOT NULL,
    crowd_count INT NOT NULL,
    total_sales DOUBLE(12,2) NOT NULL DEFAULT 0.00
    );
```

CREATE TABLE `clone_teamstb1` (
  `team_id` int(11) NOT NULL AUTO_INCREMENT,
  `team_name` varchar(100) NOT NULL,
  `team_captain` varchar(40) NOT NULL,
  `establishment_date` date DEFAULT NULL,
  PRIMARY KEY (`team_id`),
  KEY `date_of_est` (`establishment_date`),
  KEY `name_of_the_team` (`team_name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;


### **7.** Make a selection from the main table DB MySQL

![Image](./img/mysql31.png)
![Image](./img/mysql32.png)

 


