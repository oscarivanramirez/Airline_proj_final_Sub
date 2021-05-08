-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: May 08, 2021 at 03:28 AM
-- Server version: 5.7.32
-- PHP Version: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `travel`
--

-- --------------------------------------------------------

--
-- Table structure for table `Airline`
--

CREATE TABLE `Airline` (
  `Airline_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Airline`
--

INSERT INTO `Airline` (`Airline_name`) VALUES
('China Eastern'),
('Delta'),
('Spirit');

-- --------------------------------------------------------

--
-- Table structure for table `Airplane`
--

CREATE TABLE `Airplane` (
  `airplane_ID` int(11) NOT NULL,
  `seats` int(11) DEFAULT NULL,
  `airline_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Airplane`
--

INSERT INTO `Airplane` (`airplane_ID`, `seats`, `airline_name`) VALUES
(274018285, 900, 'Spirit'),
(317892572, 800, 'Delta'),
(1234567890, 800, 'China Eastern');

-- --------------------------------------------------------

--
-- Table structure for table `Airport`
--

CREATE TABLE `Airport` (
  `airport_name` varchar(255) NOT NULL,
  `city` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Airport`
--

INSERT INTO `Airport` (`airport_name`, `city`) VALUES
('JFK', 'NYC'),
('LaG', 'NYC'),
('PVG', 'Shanghai');

-- --------------------------------------------------------

--
-- Table structure for table `Booking_Agent`
--

CREATE TABLE `Booking_Agent` (
  `email` varchar(255) NOT NULL,
  `passwrd` varchar(255) DEFAULT NULL,
  `ID` int(11) DEFAULT NULL,
  `commission` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Booking_Agent`
--

INSERT INTO `Booking_Agent` (`email`, `passwrd`, `ID`, `commission`) VALUES
('chris_da_agent@gmail.com', 'lengthypassword456', 12345, 10);

-- --------------------------------------------------------

--
-- Table structure for table `Customer`
--

CREATE TABLE `Customer` (
  `email` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) DEFAULT NULL,
  `passport_number` int(11) DEFAULT NULL,
  `passport_expiration` int(11) DEFAULT NULL,
  `passport_country` varchar(255) DEFAULT NULL,
  `DOB` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Customer`
--

INSERT INTO `Customer` (`email`, `password`, `name`, `phone_number`, `passport_number`, `passport_expiration`, `passport_country`, `DOB`) VALUES
('ab7975@nyu.edu', 'password123', 'Abdelkarim Bisharat', '3473147466', 173816381, 12312025, 'UNITED STATES', 2262000),
('oir209@nyu.edu', 'mypassword351', 'Oscar Ramirez', '6465059863', 123456789, 1312028, 'UNITED STATES', 9242000);

-- --------------------------------------------------------

--
-- Table structure for table `Feedback`
--

CREATE TABLE `Feedback` (
  `airline_name` varchar(255) DEFAULT NULL,
  `airplane_ID` int(11) DEFAULT NULL,
  `flight_number` int(11) DEFAULT NULL,
  `depart_time` time DEFAULT NULL,
  `depart_date` date DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `comments` varchar(255) DEFAULT NULL,
  `ratings` int(11) DEFAULT NULL,
  `airport_name_arrival` varchar(255) DEFAULT NULL,
  `airport_name_depart` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Feedback`
--

INSERT INTO `Feedback` (`airline_name`, `airplane_ID`, `flight_number`, `depart_time`, `depart_date`, `email`, `comments`, `ratings`, `airport_name_arrival`, `airport_name_depart`) VALUES
('China Eastern', 1234567890, 924200, '03:45:00', '2021-05-19', 'oir209@nyu.edu', NULL, NULL, 'JFK', 'PVG'),
('China Eastern', 1234567890, 123456, '02:40:55', '2021-03-31', 'oir209@nyu.edu', NULL, NULL, 'JFK', 'PVG');

-- --------------------------------------------------------

--
-- Table structure for table `Flight`
--

CREATE TABLE `Flight` (
  `airline_name` varchar(255) NOT NULL,
  `airplane_ID` int(11) NOT NULL,
  `flight_number` int(11) NOT NULL,
  `depart_time` time(6) NOT NULL,
  `depart_date` date NOT NULL,
  `arrival_date` date DEFAULT NULL,
  `arrival_time` time(6) DEFAULT NULL,
  `base_price` float DEFAULT NULL,
  `airport_name_arrival` varchar(255) NOT NULL,
  `airport_name_depart` varchar(255) NOT NULL,
  `status_F` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Flight`
--

INSERT INTO `Flight` (`airline_name`, `airplane_ID`, `flight_number`, `depart_time`, `depart_date`, `arrival_date`, `arrival_time`, `base_price`, `airport_name_arrival`, `airport_name_depart`, `status_F`) VALUES
('China Eastern', 1234567890, 123456, '02:40:55.000000', '2021-03-31', '2021-03-31', '08:50:58.000000', 345, 'JFK', 'PVG', 'delayed'),
('China Eastern', 1234567890, 351890, '06:40:55.000000', '2021-03-31', '2021-04-01', '04:50:58.000000', 345, 'LaG', 'PVG', 'on-time'),
('China Eastern', 1234567890, 924200, '03:45:00.000000', '2021-05-19', '2021-05-20', '03:45:00.000000', 200, 'JFK', 'PVG', 'on-time'),
('Delta', 317892572, 510985, '04:30:55.000000', '2021-04-02', '2021-04-02', '10:50:58.000000', 345, 'JFK', 'LaG', 'on-time');

-- --------------------------------------------------------

--
-- Table structure for table `Phones`
--

CREATE TABLE `Phones` (
  `username` varchar(255) NOT NULL,
  `number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Purchase_by_BA`
--

CREATE TABLE `Purchase_by_BA` (
  `customer_email` varchar(255) DEFAULT NULL,
  `BA_email` varchar(255) DEFAULT NULL,
  `ticket_ID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Purchase_by_BA`
--

INSERT INTO `Purchase_by_BA` (`customer_email`, `BA_email`, `ticket_ID`) VALUES
('ab7975@nyu.edu', 'chris_da_agent@gmail.com', 987657),
('oir209@nyu.edu', 'chris_da_agent@gmail.com', 103497);

-- --------------------------------------------------------

--
-- Table structure for table `Purchase_by_Customer`
--

CREATE TABLE `Purchase_by_Customer` (
  `customer_email` varchar(255) DEFAULT NULL,
  `ticket_ID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Purchase_by_Customer`
--

INSERT INTO `Purchase_by_Customer` (`customer_email`, `ticket_ID`) VALUES
('oir209@nyu.edu', 987654),
('oir209@nyu.edu', 987655),
('ab7975@nyu.edu', 987656),
('oir209@nyu.edu', 955513),
('oir209@nyu.edu', 282667);

-- --------------------------------------------------------

--
-- Table structure for table `Staff`
--

CREATE TABLE `Staff` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `DOB` int(11) DEFAULT NULL,
  `airline_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Staff`
--

INSERT INTO `Staff` (`username`, `password`, `first_name`, `last_name`, `DOB`, `airline_name`) VALUES
('Tony123@gmail.com', 'goodpass69', 'Tony', 'Stark', 5291970, 'China Eastern');

-- --------------------------------------------------------

--
-- Table structure for table `Ticket`
--

CREATE TABLE `Ticket` (
  `airline_name` varchar(255) DEFAULT NULL,
  `airplane_ID` int(11) DEFAULT NULL,
  `flight_number` int(11) DEFAULT NULL,
  `depart_time` time(6) DEFAULT NULL,
  `depart_date` date DEFAULT NULL,
  `ticket_ID` int(11) NOT NULL,
  `sold_price` float DEFAULT NULL,
  `airport_name_arrival` varchar(255) DEFAULT NULL,
  `airport_name_depart` varchar(255) DEFAULT NULL,
  `purchase_date` date DEFAULT NULL,
  `purchase_time` time DEFAULT NULL,
  `card_type` varchar(255) DEFAULT NULL,
  `card_name` varchar(255) DEFAULT NULL,
  `card_expiration` date DEFAULT NULL,
  `card_num` varchar(16) DEFAULT NULL,
  `booking_agent_ID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Ticket`
--

INSERT INTO `Ticket` (`airline_name`, `airplane_ID`, `flight_number`, `depart_time`, `depart_date`, `ticket_ID`, `sold_price`, `airport_name_arrival`, `airport_name_depart`, `purchase_date`, `purchase_time`, `card_type`, `card_name`, `card_expiration`, `card_num`, `booking_agent_ID`) VALUES
('China Eastern', 1234567890, 123456, '02:40:55.000000', '2021-03-31', 103497, 345, 'JFK', 'PVG', '2021-05-07', '22:03:41', 'MasterCard', 'Oscar Ramirez', '2028-09-29', '1717272727251987', 12345),
('China Eastern', 1234567890, 924200, '03:45:00.000000', '2021-05-19', 282667, 200, 'JFK', 'PVG', '2021-05-07', '16:50:13', 'MasterCard', 'Oscar Ramirez', '2028-09-29', '1717272727251987', NULL),
('China Eastern', 1234567890, 924200, '03:45:00.000000', '2021-05-19', 955513, 200, 'JFK', 'PVG', '2021-05-07', '16:44:10', 'MasterCard', 'Oscar Ramirez', '2028-09-29', '1717272727251987', NULL),
('Delta', 317892572, 510985, '04:30:55.000000', '2021-04-02', 987654, 500, 'JFK', 'LaG', '2021-03-27', '05:30:55', 'MasterCard', 'Oscar Ramirez', '2028-09-29', '1717272727251987', NULL),
('Delta', 317892572, 510985, '04:30:55.000000', '2021-04-02', 987655, 500, 'JFK', 'LaG', '2021-03-27', '05:32:55', 'MasterCard', 'Oscar Ramirez', '2028-09-29', '1717272727251987', NULL),
('China Eastern', 1234567890, 351890, '06:40:55.000000', '2021-03-31', 987656, 600, 'LaG', 'PVG', '2021-03-28', '07:32:55', 'Visa', 'Abdelkarim Bisharat', '2026-06-29', '1717298767251987', NULL),
('China Eastern', 1234567890, 123456, '02:40:55.000000', '2021-03-31', 987657, 700, 'JFK', 'PVG', '2021-03-29', '06:32:55', 'Visa', 'Abdelkarim Bisharat', '2026-06-29', '1717298767251987', 12345);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Airline`
--
ALTER TABLE `Airline`
  ADD PRIMARY KEY (`Airline_name`);

--
-- Indexes for table `Airplane`
--
ALTER TABLE `Airplane`
  ADD PRIMARY KEY (`airplane_ID`,`airline_name`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `Airport`
--
ALTER TABLE `Airport`
  ADD PRIMARY KEY (`airport_name`);

--
-- Indexes for table `Booking_Agent`
--
ALTER TABLE `Booking_Agent`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `Customer`
--
ALTER TABLE `Customer`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `Feedback`
--
ALTER TABLE `Feedback`
  ADD KEY `airline_name` (`airline_name`),
  ADD KEY `airplane_ID` (`airplane_ID`),
  ADD KEY `email` (`email`),
  ADD KEY `airport_name_arrival` (`airport_name_arrival`),
  ADD KEY `airport_name_depart` (`airport_name_depart`);

--
-- Indexes for table `Flight`
--
ALTER TABLE `Flight`
  ADD PRIMARY KEY (`airline_name`,`airplane_ID`,`flight_number`,`depart_time`,`depart_date`,`airport_name_arrival`,`airport_name_depart`),
  ADD KEY `airplane_ID` (`airplane_ID`),
  ADD KEY `airport_name_arrival` (`airport_name_arrival`),
  ADD KEY `airport_name_depart` (`airport_name_depart`);

--
-- Indexes for table `Phones`
--
ALTER TABLE `Phones`
  ADD PRIMARY KEY (`number`,`username`),
  ADD KEY `username` (`username`);

--
-- Indexes for table `Purchase_by_BA`
--
ALTER TABLE `Purchase_by_BA`
  ADD KEY `customer_email` (`customer_email`),
  ADD KEY `BA_email` (`BA_email`),
  ADD KEY `ticket_ID` (`ticket_ID`);

--
-- Indexes for table `Purchase_by_Customer`
--
ALTER TABLE `Purchase_by_Customer`
  ADD KEY `customer_email` (`customer_email`),
  ADD KEY `ticket_ID` (`ticket_ID`);

--
-- Indexes for table `Staff`
--
ALTER TABLE `Staff`
  ADD PRIMARY KEY (`username`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `Ticket`
--
ALTER TABLE `Ticket`
  ADD PRIMARY KEY (`ticket_ID`),
  ADD KEY `airline_name` (`airline_name`),
  ADD KEY `airplane_ID` (`airplane_ID`),
  ADD KEY `airport_name_arrival` (`airport_name_arrival`),
  ADD KEY `airport_name_depart` (`airport_name_depart`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Airplane`
--
ALTER TABLE `Airplane`
  ADD CONSTRAINT `airplane_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `Airline` (`Airline_name`);

--
-- Constraints for table `Feedback`
--
ALTER TABLE `Feedback`
  ADD CONSTRAINT `feedback_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `Flight` (`airline_name`),
  ADD CONSTRAINT `feedback_ibfk_2` FOREIGN KEY (`airplane_ID`) REFERENCES `Flight` (`airplane_ID`),
  ADD CONSTRAINT `feedback_ibfk_3` FOREIGN KEY (`email`) REFERENCES `Customer` (`email`),
  ADD CONSTRAINT `feedback_ibfk_4` FOREIGN KEY (`airport_name_arrival`) REFERENCES `Flight` (`airport_name_arrival`),
  ADD CONSTRAINT `feedback_ibfk_5` FOREIGN KEY (`airport_name_depart`) REFERENCES `Flight` (`airport_name_depart`);

--
-- Constraints for table `Flight`
--
ALTER TABLE `Flight`
  ADD CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `Airline` (`Airline_name`),
  ADD CONSTRAINT `flight_ibfk_2` FOREIGN KEY (`airplane_ID`) REFERENCES `Airplane` (`airplane_ID`),
  ADD CONSTRAINT `flight_ibfk_3` FOREIGN KEY (`airport_name_arrival`) REFERENCES `Airport` (`airport_name`),
  ADD CONSTRAINT `flight_ibfk_4` FOREIGN KEY (`airport_name_depart`) REFERENCES `Airport` (`airport_name`);

--
-- Constraints for table `Phones`
--
ALTER TABLE `Phones`
  ADD CONSTRAINT `phones_ibfk_1` FOREIGN KEY (`username`) REFERENCES `Staff` (`username`);

--
-- Constraints for table `Purchase_by_BA`
--
ALTER TABLE `Purchase_by_BA`
  ADD CONSTRAINT `purchase_by_ba_ibfk_1` FOREIGN KEY (`customer_email`) REFERENCES `Customer` (`email`),
  ADD CONSTRAINT `purchase_by_ba_ibfk_2` FOREIGN KEY (`BA_email`) REFERENCES `Booking_Agent` (`email`),
  ADD CONSTRAINT `purchase_by_ba_ibfk_3` FOREIGN KEY (`ticket_ID`) REFERENCES `Ticket` (`ticket_ID`);

--
-- Constraints for table `Purchase_by_Customer`
--
ALTER TABLE `Purchase_by_Customer`
  ADD CONSTRAINT `purchase_by_customer_ibfk_1` FOREIGN KEY (`customer_email`) REFERENCES `Customer` (`email`),
  ADD CONSTRAINT `purchase_by_customer_ibfk_2` FOREIGN KEY (`ticket_ID`) REFERENCES `Ticket` (`ticket_ID`);

--
-- Constraints for table `Staff`
--
ALTER TABLE `Staff`
  ADD CONSTRAINT `staff_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `Airline` (`Airline_name`);

--
-- Constraints for table `Ticket`
--
ALTER TABLE `Ticket`
  ADD CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `Flight` (`airline_name`),
  ADD CONSTRAINT `ticket_ibfk_2` FOREIGN KEY (`airplane_ID`) REFERENCES `Flight` (`airplane_ID`),
  ADD CONSTRAINT `ticket_ibfk_3` FOREIGN KEY (`airport_name_arrival`) REFERENCES `Flight` (`airport_name_arrival`),
  ADD CONSTRAINT `ticket_ibfk_4` FOREIGN KEY (`airport_name_depart`) REFERENCES `Flight` (`airport_name_depart`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
