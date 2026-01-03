-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 02, 2026 at 06:37 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `results`
--

CREATE TABLE `results` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `roll` varchar(200) NOT NULL,
  `python` float NOT NULL,
  `java` float NOT NULL,
  `php` float NOT NULL,
  `total` float NOT NULL,
  `average` float NOT NULL,
  `grade` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `results`
--

INSERT INTO `results` (`id`, `name`, `roll`, `python`, `java`, `php`, `total`, `average`, `grade`) VALUES
(1, 'arshiya ', '39', 100, 100, 100, 300, 100, 'A'),
(2, 'aadil pathan', '77', 89, 99, 100, 288, 96, 'A'),
(3, 'aazam pathan', '17', 88, 77, 55, 220, 73.3333, 'C'),
(4, 'Tarannum shaikh', '35', 77, 88, 55, 220, 73.3333, 'C'),
(5, 'Roshni Patel', '22', 99, 66, 89, 254, 84.6667, 'B'),
(9, 'Samiya', '59', 99, 100, 66, 265, 88.3333, 'B'),
(10, 'Kaif', '01', 100, 100, 100, 300, 100, 'A');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `results`
--
ALTER TABLE `results`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `results`
--
ALTER TABLE `results`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
