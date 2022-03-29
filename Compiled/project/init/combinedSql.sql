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
('1111', 'Emma Tan','53 Ang Mo Kio Avenue 3 Singapore 569933', '978112947'),
('2222', 'Yvonne Kim', 'Blk 145 Lorong 2 Toa Payoh Singapore 310145', '978134947'),
('3333', 'Michael Ang', 'Blk 150A Bishan Street 11 Singapore 571150', '978143447');
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
('1', 'Cindy', '98989898', '7747332773','maars505',93366384),
('2', 'Candy', '91919191', '7747733573','maars505',93366384);
COMMIT;
--
-- ======================= SELLER END ========================== --

-- -- ======================= ORDER ========================== --
CREATE DATABASE IF NOT EXISTS `orders`;
-- ADDED THIS PART TO CREATE MULTIPLE DATABASES:
USE `orders`;
-- --------------------------------------------------------
--
-- TABLE STRUCTURE FOR TABLE `ORDER`
--
DROP TABLE IF EXISTS `order`;
CREATE TABLE IF NOT EXISTS `order` (
  `order_id` INT(11) NOT NULL AUTO_INCREMENT,
  `customerID` VARCHAR(11) NOT NULL,
  `status` VARCHAR(34) NOT NULL DEFAULT "Payment Completed",
  `dateOfPurchase` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `dateOfModification` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_id`)
);
--
-- DUMPING DATA FOR TABLE `ORDER`
--
INSERT INTO `order` (`order_id`, `customerID`, `status`, `dateOfPurchase`, `dateOfModification`) VALUES
(1, '1111', 'NEW', '2020-06-12 02:14:55', '2020-06-12 02:14:55'),
(2, '2222', 'NEW', '2020-06-12 02:14:55', '2020-06-12 02:14:55');

-- --------------------------------------------------------
--
-- TABLE STRUCTURE FOR TABLE `ORDER_ITEM`
--
DROP TABLE IF EXISTS `order_item`;
CREATE TABLE IF NOT EXISTS `order_item` (
  `order_item_id` INT(11) NOT NULL  AUTO_INCREMENT,
  `order_id` INT(11) NOT NULL,
  `sellerID` INT(11) NOT NULL,
  `id` INT(11) NOT NULL, 
  `productName` VARCHAR(32) NOT NULL,
  `itemPrice` DECIMAL(5,2) NOT NULL,
  `quantity` INT(11) NOT NULL,
  PRIMARY KEY (`order_item_id`),
  KEY `FK_order_item_id` (`order_id`)
);
--
-- DUMPING DATA FOR TABLE `ORDER_ITEM`
--
INSERT INTO `order_item` (`order_item_id`, `order_id`, `sellerID`, `productName`, `itemPrice`,`quantity`) VALUES
(1, 1, 1, 'MaarsBar', 100.29, 10),
(2, 1, 1, 'AiWeiJack', 20.29, 10);
--
-- CONSTRAINTS FOR DUMPED TABLES
--
--
-- CONSTRAINTS FOR TABLE `ORDER_ITEM`
--
ALTER TABLE `order_item`
  ADD CONSTRAINT `order_id` FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`) ON DELETE CASCADE ON UPDATE CASCADE;
-- -- ======================= ORDER END ========================== --
