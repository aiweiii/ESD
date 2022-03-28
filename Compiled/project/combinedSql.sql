-- ======================= Cart ========================== --
CREATE DATABASE IF NOT EXISTS `cart` ;
GRANT ALL ON `cart`.* TO 'user'@'%';
COMMIT;
-- ======================= Cart END ========================== --


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

-- ======================= Inventory ========================== --
CREATE DATABASE IF NOT EXISTS `inventory` ;
GRANT ALL ON `inventory`.* TO 'user'@'%';
COMMIT;
-- ======================= Inventory END ========================== --
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


-- -- ======================= ORDER ========================== --
-- CREATE DATABASE IF NOT EXISTS `order`;
-- GRANT ALL ON `order`.* TO 'user'@'%';
-- -- -- added this part to create multiple databases:
-- USE `order`;
-- -- --------------------------------------------------------
-- --
-- -- Table structure for table `order`
-- --
-- -- DROP TABLE IF EXISTS `order`;
-- CREATE TABLE IF NOT EXISTS `order` (
--   `order_id` int(11) NOT NULL AUTO_INCREMENT,
--   `customer_id` varchar(32) NOT NULL,
--   `status` varchar(10) NOT NULL DEFAULT 'NEW',
--   `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
--   `modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
--   PRIMARY KEY (`order_id`)
-- );
-- --
-- -- Dumping data for table `order`
-- --
-- INSERT INTO `order` (`order_id`, `customer_id`, `status`, `created`, `modified`) VALUES
-- (1, 'Apple TAN', 'NEW', '2020-06-12 02:14:55', '2020-06-12 02:14:55');

-- -- --------------------------------------------------------
-- --
-- -- Table structure for table `order_item`
-- --
-- -- DROP TABLE IF EXISTS `order_item`;
-- CREATE TABLE IF NOT EXISTS `order_item` (
--   `item_id` int(11) NOT NULL AUTO_INCREMENT,
--   `order_id` int(11) NOT NULL,
--   `book_id` char(13) NOT NULL,
--   `quantity` int(11) NOT NULL,
--   PRIMARY KEY (`item_id`),
--   KEY `FK_order_id` (`order_id`)
-- ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
-- --
-- -- Dumping data for table `order_item`
-- --
-- INSERT INTO `order_item` (`item_id`, `order_id`, `book_id`, `quantity`) VALUES
-- (1, 1, '9781434474234', 1),
-- (2, 1, '9781449474212', 1);
-- --
-- -- Constraints for dumped tables
-- --
-- --
-- -- Constraints for table `order_item`
-- --
-- ALTER TABLE `order_item`
--   ADD CONSTRAINT `FK_order_id` FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`) ON DELETE CASCADE ON UPDATE CASCADE;
-- COMMIT;
-- -- ======================= ORDER END ========================== --

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
('1', 'Cindy', '98989898', '774777773');
--
-- ======================= SELLER END ========================== --

