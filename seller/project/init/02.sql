
-- ======================= ORDER ========================== --
CREATE DATABASE IF NOT EXISTS `order`;
GRANT ALL ON `order`.* TO 'user'@'%';
-- -- added this part to create multiple databases:
USE `order`;
-- --------------------------------------------------------
--
-- Table structure for table `order`
--
DROP TABLE IF EXISTS `order`;
CREATE TABLE IF NOT EXISTS `order` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` varchar(32) NOT NULL,
  `status` varchar(10) NOT NULL DEFAULT 'NEW',
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_id`)
);
--
-- Dumping data for table `order`
--
INSERT INTO `order` (`order_id`, `customer_id`, `status`, `created`, `modified`) VALUES
(1, 'Apple TAN', 'NEW', '2020-06-12 02:14:55', '2020-06-12 02:14:55');

-- --------------------------------------------------------
--
-- Table structure for table `order_item`
--
DROP TABLE IF EXISTS `order_item`;
CREATE TABLE IF NOT EXISTS `order_item` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `book_id` char(13) NOT NULL,
  `quantity` int(11) NOT NULL,
  PRIMARY KEY (`item_id`),
  KEY `FK_order_id` (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
--
-- Dumping data for table `order_item`
--
INSERT INTO `order_item` (`item_id`, `order_id`, `book_id`, `quantity`) VALUES
(1, 1, '9781434474234', 1),
(2, 1, '9781449474212', 1);
--
-- Constraints for dumped tables
--
--
-- Constraints for table `order_item`
--
ALTER TABLE `order_item`
  ADD CONSTRAINT `FK_order_id` FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;
-- ======================= ORDER END ========================== --



CREATE DATABASE IF NOT EXISTS `test4`;
GRANT ALL ON `test4`.* TO 'user'@'%';
