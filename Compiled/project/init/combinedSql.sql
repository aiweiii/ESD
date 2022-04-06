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
-- Table structure for table `customers`
--
DROP TABLE IF EXISTS `customers`;
CREATE TABLE IF NOT EXISTS `customers` (
  `custID` int(11) NOT NULL AUTO_INCREMENT,
  `custName` varchar(64) NOT NULL,
  `custAddress` varchar(64) NULL,
  PRIMARY KEY (`custID`)
);
--
-- Dumping data for table `customers`
--
INSERT INTO `customers` (`custID`, `custName`, `custAddress`) VALUES
(1, 'Emma Tan','53 Ang Mo Kio Avenue 3 Singapore 569933'),
(2, 'Yvonne Kim', 'Blk 145 Lorong 2 Toa Payoh Singapore 310145'),
(3, 'Michael Ang', 'Blk 150A Bishan Street 11 Singapore 571150');
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
  `telegramId` VARCHAR(24) NOT NULL, 
  `chatId` int(24) NOT NULL,
  PRIMARY KEY (`sellerID`)
); 
--
-- Dumping data for table `seller`
--
INSERT INTO `seller` (`sellerID`, `sellerName`, `sellerCtcNo`, `sellerBankAccNo`,`telegramId`,`chatId`) VALUES
('1', 'maars', '98989898', '7747332773','maars505',493366384),
('2', 'liqing', '91919191', '9947733573','lliqing',202631841),
('3', 'aiwei', '92929292', '2347733573','aiwei',503151420);
COMMIT;
--
-- ======================= SELLER END ========================== --

-- -- ======================= ORDER ========================== --
CREATE DATABASE IF NOT EXISTS `order`;
-- ADDED THIS PART TO CREATE MULTIPLE DATABASES:
USE `order`;
-- --------------------------------------------------------
--
-- TABLE STRUCTURE FOR TABLE `ORDER`
--
DROP TABLE IF EXISTS `order`;
CREATE TABLE IF NOT EXISTS `order` (
  `order_id` INT(11) NOT NULL AUTO_INCREMENT,
  `customerID` int(11) NOT NULL,
  `status` VARCHAR(34) NOT NULL DEFAULT "Payment Completed",
  `dateOfPurchase` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `dateOfModification` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_id`)
);
--
-- DUMPING DATA FOR TABLE `ORDER`
--
INSERT INTO `order` (`order_id`, `customerID`, `status`, `dateOfPurchase`, `dateOfModification`) VALUES
(1, 1, 'NEW', '2020-06-12 02:14:55', '2020-06-12 02:14:55'),
(2, 2, 'NEW', '2020-06-12 02:14:55', '2020-06-12 02:14:55');

-- --------------------------------------------------------
--
-- TABLE STRUCTURE FOR TABLE `ORDER_ITEM`
--
DROP TABLE IF EXISTS `order_item`;
CREATE TABLE IF NOT EXISTS `order_item` (
  `order_item_id` INT(11) NOT NULL  AUTO_INCREMENT,
  `order_id` INT(11) NOT NULL,
  `sellerID` INT(11) NOT NULL,
  `itemID` INT(11) NOT NULL, 
  `productName` VARCHAR(104) NOT NULL,
  `itemPrice` DECIMAL(5,2) NOT NULL,
  `quantity` INT(11) NOT NULL,
  PRIMARY KEY (`order_item_id`),
  KEY `FK_order_item_id` (`order_id`)
);
--
-- DUMPING DATA FOR TABLE `ORDER_ITEM`
--
INSERT INTO `order_item` (`order_item_id`, `order_id`, `sellerID`, `itemID`, `productName`, `itemPrice`,`quantity`) VALUES
(1, 1, 1, 3, 'APPLE', 6, 30),
(2, 1, 1, 1, 'FRUIT', 10, 20);
--
-- CONSTRAINTS FOR DUMPED TABLES
--
--
-- CONSTRAINTS FOR TABLE `ORDER_ITEM`
--
ALTER TABLE `order_item`
  ADD CONSTRAINT `order_id` FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`) ON DELETE CASCADE ON UPDATE CASCADE;
-- -- ======================= ORDER END ========================== --
