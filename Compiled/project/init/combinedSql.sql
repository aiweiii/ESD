-- ======================= Cart ========================== --
CREATE DATABASE IF NOT EXISTS `cart` ;
GRANT ALL ON `cart`.* TO 'user'@'%';
COMMIT;
-- ======================= Cart END ========================== --

-- ======================= Inventory ========================== --
CREATE DATABASE IF NOT EXISTS `inventory` ;
GRANT ALL ON `inventory`.* TO 'user'@'%';
COMMIT;
-- ======================= Inventory END ========================== --

-- ======================= CUSTOMERS ========================== --
CREATE DATABASE IF NOT EXISTS `customers`;
GRANT ALL ON `customers`.* TO 'user'@'%';
USE `customers`;
-- --------------------------------------------------------
--
-- Table structure for table `books`
--
DROP TABLE IF EXISTS `customers`;
CREATE TABLE IF NOT EXISTS `customers` (
  `custID` varchar(64) NOT NULL,
  `custName` varchar(64) NOT NULL,
  `custAddress` varchar(64) NOT NULL,
  `custCCNo` int(9) DEFAULT NULL,
  PRIMARY KEY (`custID`)
);
--
-- Dumping data for table `customers`
--
INSERT INTO `customers` (`custID`, `custName`, `custAddress`, `custCCNo`) VALUES
('A01', 'Emma Tan','53 Ang Mo Kio Avenue 3 Singapore 569933', '978112947'),
('A02', 'Yvonne Kim', 'Blk 145 Lorong 2 Toa Payoh Singapore 310145', '978134947'),
('A03', 'Michael Ang', 'Blk 150A Bishan Street 11 Singapore 571150', '978143447');
COMMIT;
--
-- ======================= CUSTOMERS END ========================== --

-- ======================= SELLER ========================== --
CREATE DATABASE IF NOT EXISTS `sellers`;
-- CREATE DATABASE "sellers";
GRANT ALL ON `sellers`.* TO 'user'@'%';
USE `sellers`;
--
-- Table structure for table `seller`
--
DROP TABLE IF EXISTS `seller`;
CREATE TABLE IF NOT EXISTS `seller` (
  `sellerID` int(11) NOT NULL AUTO_INCREMENT, 
  `sellerName` varchar(32) NOT NULL,
  `sellerCtcNo` int(11) NOT NULL,
  `sellerBankAccNo` int(24) NOT NULL,
  PRIMARY KEY (`sellerID`)
); 
--
-- Dumping data for table `seller`
--
INSERT INTO `seller` (`sellerID`, `sellerName`, `sellerCtcNo`, `sellerBankAccNo`) VALUES
('1', 'Cindy', '98989898', '774777773'),
('1', 'Cindy', '98989898', '774777773');
COMMIT;
--
-- ======================= SELLER END ========================== --

-- -- ======================= ORDER ========================== --
CREATE DATABASE IF NOT EXISTS `ORDER`;
GRANT ALL ON `ORDER`.* TO 'USER'@'%';
-- ADDED THIS PART TO CREATE MULTIPLE DATABASES:
USE `ORDER`;
-- --------------------------------------------------------
--
-- TABLE STRUCTURE FOR TABLE `ORDER`
--
DROP TABLE IF EXISTS `ORDER`;
CREATE TABLE IF NOT EXISTS `ORDER` (
  `ORDER_ID` INT(11) NOT NULL AUTO_INCREMENT,
  `CUSTOMER_ID` VARCHAR(32) NOT NULL,
  `STATUS` VARCHAR(10) NOT NULL DEFAULT 'NEW',
  `CREATED` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `MODIFIED` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ORDER_ID`)
);
--
-- DUMPING DATA FOR TABLE `ORDER`
--
INSERT INTO `ORDER` (`ORDER_ID`, `CUSTOMER_ID`, `STATUS`, `CREATED`, `MODIFIED`) VALUES
(1, 'APPLE TAN', 'NEW', '2020-06-12 02:14:55', '2020-06-12 02:14:55');

-- --------------------------------------------------------
--
-- TABLE STRUCTURE FOR TABLE `ORDER_ITEM`
--
DROP TABLE IF EXISTS `ORDER_ITEM`;
CREATE TABLE IF NOT EXISTS `ORDER_ITEM` (
  `ITEM_ID` INT(11) NOT NULL AUTO_INCREMENT,
  `ORDER_ID` INT(11) NOT NULL,
  `BOOK_ID` CHAR(13) NOT NULL,
  `QUANTITY` INT(11) NOT NULL,
  PRIMARY KEY (`ITEM_ID`),
  KEY `FK_ORDER_ID` (`ORDER_ID`)
) ENGINE=INNODB AUTO_INCREMENT=3 DEFAULT CHARSET=UTF8;
--
-- DUMPING DATA FOR TABLE `ORDER_ITEM`
--
INSERT INTO `ORDER_ITEM` (`ITEM_ID`, `ORDER_ID`, `BOOK_ID`, `QUANTITY`) VALUES
(1, 1, '9781434474234', 1),
(2, 1, '9781449474212', 1);
--
-- CONSTRAINTS FOR DUMPED TABLES
--
--
-- CONSTRAINTS FOR TABLE `ORDER_ITEM`
--
ALTER TABLE `ORDER_ITEM`
  ADD CONSTRAINT `FK_ORDER_ID` FOREIGN KEY (`ORDER_ID`) REFERENCES `ORDER` (`ORDER_ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;
-- ======================= ORDER END ========================== --