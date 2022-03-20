-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `book`
--
CREATE DATABASE IF NOT EXISTS `customers` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`custID`, `custName`, `custAddress`, `custCCNo`) VALUES
('A01', 'Emma Tan','53 Ang Mo Kio Avenue 3 Singapore 569933', '978112947'),
('A02', 'Yvonne Kim', 'Blk 145 Lorong 2 Toa Payoh Singapore 310145', '978134947'),
('A03', 'Michael Ang', 'Blk 150A Bishan Street 11 Singapore 571150', '978143447');
COMMIT;
-- ('Jason Lu', '9781442374221'),
-- ('Eason Chen', '9781449474211'),
-- ('Jolin Wee', '9781449474212'),
-- ('Randy Lu', '9781449474221'),
-- ('Shandy Ling', '9781449474223'),
-- ('Josiah Lau', '9781449474254'),
-- ('Joanne Chng', '9781449474256'),



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;