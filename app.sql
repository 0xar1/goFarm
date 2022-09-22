-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 22, 2022 at 06:51 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `app`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auction`
--

CREATE TABLE `auction` (
  `aid` int(11) NOT NULL,
  `sellerId` int(11) DEFAULT NULL,
  `cropId` int(11) DEFAULT NULL,
  `variety` varchar(50) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `minPrice` int(11) DEFAULT NULL,
  `datetime` datetime NOT NULL,
  `currentBid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auction`
--

INSERT INTO `auction` (`aid`, `sellerId`, `cropId`, `variety`, `amount`, `minPrice`, `datetime`, `currentBid`) VALUES
(14, 1, 2, 'Rohini', '50', 2000, '2022-09-22 09:46:00', 0),
(16, 6, 18, 'Harith', '50', 1250, '2022-09-22 12:32:00', 0),
(17, 6, 25, 'BRS-2', '500', 20000, '2022-09-22 10:30:00', 0),
(18, 5, 27, 'Keraganga', '1000', 35000, '2022-09-22 10:50:00', 0),
(19, 8, 22, 'PV 2', '10', 20000, '2022-09-22 09:38:00', 0),
(20, 7, 15, 'Haritha', '20', 500, '2022-09-22 09:24:00', 0),
(21, 3, 22, 'PV 2', '20', 40000, '2022-09-22 09:20:00', 0);

-- --------------------------------------------------------

--
-- Table structure for table `crops`
--

CREATE TABLE `crops` (
  `name` varchar(50) DEFAULT NULL,
  `cropId` int(11) NOT NULL,
  `variety` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `crops`
--

INSERT INTO `crops` (`name`, `cropId`, `variety`) VALUES
('Rice', 1, 'Annapurna'),
('Rice', 2, 'Rohini'),
('Rice', 3, 'Triveni'),
('Rice', 4, 'Kairali'),
('Rice', 5, 'Jaya'),
('Rice', 6, 'Uma'),
('Tomato', 7, 'Sakthi'),
('Tomato', 8, 'Mukthi'),
('Tomato', 9, 'Vellayani Vijai'),
('Tomato', 10, 'Akshaya'),
('Tomato', 11, 'Manulakshmi'),
('Tomato', 12, 'Manuprabha'),
('Brinjal', 13, 'Surya'),
('Brinjal', 14, 'Swetha'),
('Brinjal', 15, 'Haritha'),
('Brinjal', 16, 'Neelima'),
('Brinjal', 17, 'Ponny'),
('Cucumber', 18, 'Harith'),
('Cucumber', 19, 'Shubra'),
('Cucumber', 20, 'KPCH 1'),
('Cardamom', 21, 'PV 1'),
('Cardamom', 22, 'PV 2'),
('Cardamom', 23, 'PV 3'),
('Banana', 24, 'BRS-1'),
('Banana', 25, 'BRS-2'),
('Coconut', 26, 'Lakshaganga'),
('Coconut', 27, 'Keraganga'),
('Coconut', 28, 'Anandaganga'),
('Coconut', 29, 'Kerasree'),
('Coconut', 30, 'Kerasagara');

-- --------------------------------------------------------

--
-- Table structure for table `current_auction`
--

CREATE TABLE `current_auction` (
  `aid` int(11) NOT NULL,
  `sellerId` int(11) DEFAULT NULL,
  `cropId` int(11) DEFAULT NULL,
  `variety` varchar(50) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `minPrice` int(11) DEFAULT NULL,
  `datetime` datetime NOT NULL,
  `currentBid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `current_auction`
--

INSERT INTO `current_auction` (`aid`, `sellerId`, `cropId`, `variety`, `amount`, `minPrice`, `datetime`, `currentBid`) VALUES
(15, 2, 4, 'Kairali', '100', 3000, '2022-09-22 05:17:00', 0);

-- --------------------------------------------------------

--
-- Table structure for table `ledger`
--

CREATE TABLE `ledger` (
  `aid` int(11) NOT NULL,
  `sellerId` int(11) DEFAULT NULL,
  `buyerId` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ledger`
--

INSERT INTO `ledger` (`aid`, `sellerId`, `buyerId`, `price`, `datetime`) VALUES
(1, 3, 1, 1000, '2022-09-22 03:24:58');

-- --------------------------------------------------------

--
-- Table structure for table `temp_table`
--

CREATE TABLE `temp_table` (
  `id` int(11) NOT NULL,
  `aid` int(11) DEFAULT NULL,
  `userBid` int(11) DEFAULT NULL,
  `buyerid` int(11) DEFAULT NULL,
  `buyerName` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `temp_table`
--

INSERT INTO `temp_table` (`id`, `aid`, `userBid`, `buyerid`, `buyerName`) VALUES
(36, 1, 1000, 1, 'Arun'),
(37, 15, 3100, 3, 'Adithye'),
(38, 15, 3200, 7, 'Antony');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `uid` int(11) NOT NULL,
  `email` varchar(120) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `verified` tinyint(1) NOT NULL,
  `full_name` varchar(200) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  `location` varchar(200) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`uid`, `email`, `password`, `verified`, `full_name`, `website`, `location`, `created_at`) VALUES
(1, 'arun@gmail.com', 'pbkdf2:sha256:260000$EhpO2Uowi7bxJ7Q7$bf3983c5fe1ac5e8b8311d7824d4a79d09aba94efea151c4557055c321bad836', 0, 'Arun', 'user@gofarm.in', 'India', '2022-09-20 19:09:04'),
(2, 'gokul@gmail.com', 'pbkdf2:sha256:260000$3OnMHSVtJUqC0NSh$cfffb024cd93c61870dd0c79e7f32fe490f657337c907e3267e4afce599765b0', 0, 'Gokul', 'user@gofarm.in', 'India', '2022-09-21 04:33:10'),
(3, 'adithye@gmail.com', 'pbkdf2:sha256:260000$IPoKpZigIpnhCFs5$8f7b44a7648282ea7d9ec0078e9ad4ad6ea6feb4d61941af2ec9394f2fb3e0bd', 0, 'Adithye', 'user@gofarm.in', 'India', '2022-09-21 20:27:25'),
(4, 'arwell@gmail.com', 'pbkdf2:sha256:260000$WvKaPKgGpSaJJVB2$33e8e4b483082d68a480bc3ced67d29d720032ae39976516383db901c3bb7293', 0, 'Arwell', 'user@gofarm.in', 'India', '2022-09-21 20:28:12'),
(5, 'arjun@gmail.com', 'pbkdf2:sha256:260000$1aNvXT9OLflMwWR0$8693dbdf9991fea8233e575ffa0f71212dfb2e44803531a8d13e3d6fe4e2d60b', 0, 'Arjun', 'user@gofarm.in', 'India', '2022-09-21 20:28:48'),
(6, 'savio@gmail.com', 'pbkdf2:sha256:260000$WecI9EL7MseAdSS5$f34d927efd260dd86db0f4835173810916f450d76778a68b4d39aaaa35ad60bd', 0, 'Savio', 'user@gofarm.in', 'India', '2022-09-21 20:29:23'),
(7, 'antony@gmail.com', 'pbkdf2:sha256:260000$BtwGAoTUyGqIG6qV$cbef6342402a63d19be0bbdb1ef38ae790b72a44a8b8da3fbfe6a787d3b47b82', 0, 'Antony', 'user@gofarm.in', 'India', '2022-09-21 20:30:00'),
(8, 'karthik@gmail.com', 'pbkdf2:sha256:260000$9frDsXjVEXGvuWBW$4a26f324d580064495042e085179773d3c6d406a3710d4e91cd40c0cd529d541', 0, 'Karthik', 'user@gofarm.in', 'India', '2022-09-21 20:30:49');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `auction`
--
ALTER TABLE `auction`
  ADD PRIMARY KEY (`aid`),
  ADD KEY `cropId` (`cropId`),
  ADD KEY `sellerId` (`sellerId`),
  ADD KEY `ix_auction_datetime` (`datetime`);

--
-- Indexes for table `crops`
--
ALTER TABLE `crops`
  ADD PRIMARY KEY (`cropId`);

--
-- Indexes for table `current_auction`
--
ALTER TABLE `current_auction`
  ADD PRIMARY KEY (`aid`),
  ADD KEY `cropId` (`cropId`),
  ADD KEY `sellerId` (`sellerId`),
  ADD KEY `ix_current_auction_datetime` (`datetime`);

--
-- Indexes for table `ledger`
--
ALTER TABLE `ledger`
  ADD PRIMARY KEY (`aid`),
  ADD KEY `ix_ledger_datetime` (`datetime`);

--
-- Indexes for table `temp_table`
--
ALTER TABLE `temp_table`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`uid`),
  ADD UNIQUE KEY `ix_user_email` (`email`),
  ADD KEY `ix_user_created_at` (`created_at`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auction`
--
ALTER TABLE `auction`
  MODIFY `aid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `crops`
--
ALTER TABLE `crops`
  MODIFY `cropId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

--
-- AUTO_INCREMENT for table `current_auction`
--
ALTER TABLE `current_auction`
  MODIFY `aid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `ledger`
--
ALTER TABLE `ledger`
  MODIFY `aid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- AUTO_INCREMENT for table `temp_table`
--
ALTER TABLE `temp_table`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auction`
--
ALTER TABLE `auction`
  ADD CONSTRAINT `auction_ibfk_1` FOREIGN KEY (`cropId`) REFERENCES `crops` (`cropId`),
  ADD CONSTRAINT `auction_ibfk_2` FOREIGN KEY (`sellerId`) REFERENCES `user` (`uid`);

--
-- Constraints for table `current_auction`
--
ALTER TABLE `current_auction`
  ADD CONSTRAINT `current_auction_ibfk_1` FOREIGN KEY (`cropId`) REFERENCES `crops` (`cropId`),
  ADD CONSTRAINT `current_auction_ibfk_2` FOREIGN KEY (`sellerId`) REFERENCES `user` (`uid`);

DELIMITER $$
--
-- Events
--
CREATE DEFINER=`root`@`localhost` EVENT `auction to currentAuction` ON SCHEDULE EVERY 1 MINUTE STARTS '2022-07-25 19:11:41' ON COMPLETION PRESERVE ENABLE COMMENT 'move from auction to current auction' DO BEGIN
 insert into current_auction(select * from auction where datetime < now());
 delete from auction where datetime < now();
 END$$

CREATE DEFINER=`root`@`localhost` EVENT `to edger` ON SCHEDULE EVERY 1 MINUTE STARTS '2022-09-21 12:14:22' ON COMPLETION NOT PRESERVE ENABLE DO BEGIN
INSERT INTO ledger (aid, sellerId, buyerId, price, datetime)
 SELECT current_auction.aid, current_auction.sellerId,
 temp_table.buyerid, temp_table.userBid,
 current_auction.datetime FROM  current_auction INNER JOIN temp_table ON 
 current_auction.aid = temp_table.aid where current_auction.datetime < now() - INTERVAL 1 HOUR AND
 temp_table.userBid = (SELECT 
 MAX(userBid) FROM temp_table);
 
delete FROM current_auction where datetime < now() - INTERVAL 1 HOUR;
 END$$

DELIMITER ;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
