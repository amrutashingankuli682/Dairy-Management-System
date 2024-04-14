-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 18, 2020 at 09:02 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dfsms`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbladmin`
--

CREATE TABLE `tbladmin` (
  `ID` int(5) NOT NULL,
  `AdminName` varchar(45) DEFAULT NULL,
  `UserName` char(45) DEFAULT NULL,
  `MobileNumber` bigint(11) DEFAULT NULL,
  `Email` varchar(120) DEFAULT NULL,
  `Password` varchar(120) DEFAULT NULL,
  `AdminRegdate` timestamp NULL DEFAULT current_timestamp(),
  `UpdationDate` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbladmin`
--

INSERT INTO `tbladmin` (`ID`, `AdminName`, `UserName`, `MobileNumber`, `Email`, `Password`, `AdminRegdate`, `UpdationDate`) VALUES
(1, 'Admin', 'admin', 1234567899, 'admin@test.com', 'f925916e2754e5e03f75dd58a5733251', '2020-11-22 18:30:00', '2020-11-25 14:56:18'),
(101, 'Staff- 1928', 'Yogesh', 7030527684, 'Yogeswar.manerikar@gmail.com', '827ccb0eea8a706c4c34a16891f84e7b', '2020-11-23 10:31:39', '2020-12-16 13:51:50');

-- --------------------------------------------------------

--
-- Table structure for table `tblcategory`
--

CREATE TABLE `tblcategory` (
  `id` int(11) NOT NULL,
  `CategoryName` varchar(200) DEFAULT NULL,
  `CategoryCode` varchar(50) DEFAULT NULL,
  `PostingDate` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblcategory`
--

INSERT INTO `tblcategory` (`id`, `CategoryName`, `CategoryCode`, `PostingDate`) VALUES
(1, 'Milk', 'MK01', '2020-11-24 16:27:43'),
(2, 'Butter', 'BT01', '2020-11-22 16:27:43'),
(3, 'Bread', 'BD01', '2020-11-24 15:28:12'),
(4, 'Paneer', 'PN01', '2020-11-20 16:27:43'),
(5, 'Soya', 'SY01', '2020-11-20 07:27:43'),
(12, 'Chees', 'CH12', '2020-12-15 13:39:15'),
(13, 'Ghee', 'Gh602', '2020-12-16 11:39:41');

-- --------------------------------------------------------

--
-- Table structure for table `tblcompany`
--

CREATE TABLE `tblcompany` (
  `id` int(11) NOT NULL,
  `CompanyName` varchar(150) DEFAULT NULL,
  `PostingDate` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblcompany`
--

INSERT INTO `tblcompany` (`id`, `CompanyName`, `PostingDate`) VALUES
(1, 'Amul', '2020-11-24 14:50:50'),
(2, 'Mother Diary', '2020-11-22 03:30:59'),
(10, 'Paras', '2020-11-24 14:52:50'),
(11, 'Goa Dairy', '2020-11-25 11:43:18'),
(12, 'Mahaninda', '2020-12-15 13:39:57');

-- --------------------------------------------------------

--
-- Table structure for table `tblorders`
--

CREATE TABLE `tblorders` (
  `id` int(11) NOT NULL,
  `ProductId` int(11) DEFAULT NULL,
  `Quantity` int(11) DEFAULT NULL,
  `InvoiceNumber` int(11) DEFAULT NULL,
  `CustomerName` varchar(150) DEFAULT NULL,
  `CustomerContactNo` bigint(12) DEFAULT NULL,
  `PaymentMode` varchar(100) DEFAULT NULL,
  `InvoiceGenDate` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblorders`
--

INSERT INTO `tblorders` (`id`, `ProductId`, `Quantity`, `InvoiceNumber`, `CustomerName`, `CustomerContactNo`, `PaymentMode`, `InvoiceGenDate`) VALUES
(15, 3, 1, 775316574, 'n', 9182736453, 'cash', '2020-12-15 10:39:24'),
(16, 2, 1, 237046689, 'a', 99, 'card', '2020-12-15 10:49:10'),
(17, 7, 2, 986256324, 'jkaxb', 9182736453, 'cash', '2020-12-15 10:59:07'),
(18, 4, 1, 521146891, 'nkn.n8y7t6r5e', 87654, 'cash', '2020-12-15 11:03:31'),
(19, 7, 2, 422189469, 'Yogeshwar', 99, 'card', '2020-12-15 11:09:50'),
(20, 7, 1, 685538326, 'mkasds', 9182736453, 'cash', '2020-12-15 11:14:09'),
(21, 2, 1, 157999667, 'hhkhvjcvx', 90, 'cash', '2020-12-15 11:44:05'),
(22, 2, 1, 580982524, 'snxsxz', 9182736453, 'cash', '2020-12-15 12:23:16'),
(23, 9, 1, 279575306, 'VVK', 9850484293, 'cash', '2020-12-15 13:42:24'),
(24, 2, 2, 279575306, 'VVK', 9850484293, 'cash', '2020-12-15 13:42:24'),
(25, 2, 1, 719596395, 'gyutds', 899765, 'cash', '2020-12-16 11:44:27'),
(26, 2, 1, 277113529, 'laxuman', 9420720840, 'cash', '2020-12-16 13:44:42'),
(27, 3, 1, 715363357, 'kunal', 9552533693, 'cash', '2020-12-16 13:46:49'),
(28, 7, 4, 409381103, 'Pinki', 2020202, 'cash', '2020-12-17 11:09:20'),
(29, 2, 1, 961693224, 'jdp', 710000000, 'cash', '2020-12-17 12:26:51');

-- --------------------------------------------------------

--
-- Table structure for table `tblproducts`
--

CREATE TABLE `tblproducts` (
  `id` int(11) NOT NULL,
  `CategoryName` varchar(150) DEFAULT NULL,
  `CompanyName` varchar(150) DEFAULT NULL,
  `ProductName` varchar(150) DEFAULT NULL,
  `ProductPrice` decimal(10,0) DEFAULT current_timestamp(),
  `PostingDate` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `UpdationDate` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblproducts`
--

INSERT INTO `tblproducts` (`id`, `CategoryName`, `CompanyName`, `ProductName`, `ProductPrice`, `PostingDate`, `UpdationDate`) VALUES
(2, 'Milk', 'Amul', 'Tetra Pack milk 1ltr', '68', '2020-12-16 11:41:20', '2020-12-16 11:41:20'),
(3, 'Milk', 'Mother Diary', 'Full Cream Milk 500ml', '26', '2019-12-25 06:42:24', '2019-12-25 06:42:24'),
(4, 'Milk', 'Mother Diary', 'Full Cream Milk 1ltr', '50', '2019-12-25 06:42:39', '2019-12-25 06:42:39'),
(5, 'Butter', 'Amul', 'Butter 100mg', '46', '2019-12-25 11:42:56', '2019-12-25 11:42:56'),
(7, 'Ghee', 'Paras', 'Ghee 500mg', '350', '2019-12-25 14:53:33', '2019-12-25 14:53:33'),
(8, 'Milk', 'Goa Dairy', '500', '27', '2020-11-25 11:43:50', NULL),
(9, 'Chees', 'Amul', 'Mozilz chees', '200', '2020-12-15 13:41:15', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbladmin`
--
ALTER TABLE `tbladmin`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `tblcategory`
--
ALTER TABLE `tblcategory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tblcompany`
--
ALTER TABLE `tblcompany`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tblorders`
--
ALTER TABLE `tblorders`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tblproducts`
--
ALTER TABLE `tblproducts`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbladmin`
--
ALTER TABLE `tbladmin`
  MODIFY `ID` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;

--
-- AUTO_INCREMENT for table `tblcategory`
--
ALTER TABLE `tblcategory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `tblcompany`
--
ALTER TABLE `tblcompany`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `tblorders`
--
ALTER TABLE `tblorders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `tblproducts`
--
ALTER TABLE `tblproducts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;