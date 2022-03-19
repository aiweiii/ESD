-- ======================= Inventory ========================== --
CREATE DATABASE IF NOT EXISTS `inventory` ;
GRANT ALL ON `inventory`.* TO 'user'@'%';
-- USE `inventory`;
-- --
-- -- Table structure for table `item`
-- --
-- DROP TABLE IF EXISTS `item`;
-- CREATE TABLE IF NOT EXISTS `item` (
--   `itemID` int(11) NOT NULL AUTO_INCREMENT,
--   `itemName` varchar(32) NOT NULL,
--   `quantity` varchar(10) NOT NULL DEFAULT 1,
--   `sellerID` int(11) NOT NULL,
--   `modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
--   PRIMARY KEY (`itemID`)
-- );
-- --
-- -- Dumping data for table `item`
-- --
-- INSERT INTO `item` (`itemID`, `itemName`, `quantity`, `sellerID`) VALUES
-- (1, 'Gillette Electronic Shaver', 100, 1);
-- --
-- Indexes for table `item`
--
-- ALTER TABLE `item`
--   ADD PRIMARY KEY (`itemID`);
COMMIT;
-- ======================= Inventory END ========================== --

CREATE DATABASE IF NOT EXISTS `test4`;
GRANT ALL ON `test4`.* TO 'user'@'%';
