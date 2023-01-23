CREATE TABLE Metals
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    metal NVARCHAR(160) NOT NULL,
    price NUMERIC(5,2) NOT NULL
);
CREATE TABLE Styles
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    style NVARCHAR(160) NOT NULL,
    price NUMERIC(5,2) NOT NULL
);
CREATE TABLE Sizes
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    carets NUMERIC(5,2) NOT NULL,
    price NUMERIC(5,2) NOT NULL
);

CREATE TABLE Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    metal_id INTEGER NOT NULL, 
    size_id INTEGER NOT NULL, 
    style_id INTEGER NOT NULL, 
    FOREIGN KEY (metal_id) REFERENCES Metals(id),
    FOREIGN KEY (size_id) REFERENCES Sizes(id),
    FOREIGN KEY (style_id) REFERENCES Styles(id) 
);

--Query to display tables info and headers
SELECT sql 
  FROM sqlite_master
 where name = 'Styles'


CREATE TABLE student (
id INT PRIMARY KEY,
first_name VARCHAR(100) NOT NULL,
last_name VARCHAR(100) NOT NULL,
city_id INT FOREIGN KEY REFERENCES city(id)
);

INSERT INTO `Metals` VALUES (null, "Gold", 400.00);
INSERT INTO `Metals` VALUES (null, "Silver", 300.00);
INSERT INTO `Metals` VALUES (null, "Brass", 200.00);
INSERT INTO `Metals` VALUES (null, "Stainless Steel", 100.00);

SELECT * FROM Orders

INSERT INTO `Sizes` VALUES (null, 24, 500.00);
INSERT INTO `Sizes` VALUES (null, 12, 250.00);
INSERT INTO `Sizes` VALUES (null, 8, 200.00);
INSERT INTO `Sizes` VALUES (null, 6, 100.00);

INSERT INTO `Styles` VALUES (null, "Classic", 400.00);
INSERT INTO `Styles` VALUES (null, "Modern", 250.00);
INSERT INTO `Styles` VALUES (null, "Vintage", 300.00);
INSERT INTO `Styles` VALUES (null, "Ballin", 800.00);


INSERT INTO `Orders` VALUES (null, 1, 1, 1);
INSERT INTO `Orders` VALUES (null, 2, 2, 2);
INSERT INTO `Orders` VALUES (null, 3, 3, 3);
INSERT INTO `Orders` VALUES (null, 4, 4, 4);


SELECT * FROM Metals