-- ======================= Cart ========================== --
CREATE DATABASE IF NOT EXISTS `cart` ;
GRANT ALL ON `cart`.* TO 'user'@'%';
COMMIT;
-- ======================= Cart END ========================== --

-- ======================= Inventory ========================== --
CREATE DATABASE IF NOT EXISTS `inventory` ;
GRANT ALL ON `inventory`.* TO 'user'@'%';
COMMIT;
{
    "productName": "WOMEN Pocketable UV Protection Parka",
    "quantity": 53,
    "sellerId": 1,
    "itemPrice": 49,
    "id": 1
},
{
    "productName": "MEN Smooth Jersey AIRISM Lined Parka",
    "quantity": 52,
    "sellerId": 1,
    "itemPrice": 59,
    "id": 2
},
{
    "productName": "Pocketable UV Protection Anorak Parka",
    "quantity": 62,
    "sellerId": 1,
    "itemPrice": 49,
    "id": 3,
},
{
    "productName": "Face Towel",
    "quantity": 38,
    "sellerId": 2,
    "itemPrice": 7,
    "id": 4
},
{
    "productName": "Ottoman",
    "quantity": 71,
    "sellerId": 2,
    "itemPrice": 129,
    "id": 5
},
{
    "productName": "Jersey Slippers",
    "quantity": 41,
    "sellerId": 2,
    "itemPrice": 7,
    "id": 6
},
{
    "productName": "Beats Fit Pro",
    "quantity": 36,
    "sellerId": 3,
    "itemPrice": 299,
    "id": 7
},
{
    "productName": "Beats Solo3 Wireless Headphones",
    "quantity": 43,
    "sellerId": 3,
    "itemPrice": 279,
    "id": 8
},
{
    "productName": "Beats Studio Buds",
    "quantity": 13,
    "sellerId": 3,
    "itemPrice": 219,
    "id": 9
}
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
  `custAddress` varchar(64) NOT NULL,
  `custCCNo` int(9) DEFAULT NULL,
  PRIMARY KEY (`custID`)
);
--
-- Dumping data for table `customers`
--
INSERT INTO `customers` (`custID`, `custName`, `custAddress`, `custCCNo`) VALUES
(1, 'Emma Tan','53 Ang Mo Kio Avenue 3 Singapore 569933', '978112947'),
(2, 'Yvonne Kim', 'Blk 145 Lorong 2 Toa Payoh Singapore 310145', '978134947'),
(3, 'Michael Ang', 'Blk 150A Bishan Street 11 Singapore 571150', '978143447');
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
('1', 'maars', '98989898', '7747332773','maars505',202631841),
('2', 'liqing', '91919191', '7747733573','lliqing',202631841);
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
  `productName` VARCHAR(32) NOT NULL,
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
