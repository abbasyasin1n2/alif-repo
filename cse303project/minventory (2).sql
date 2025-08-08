-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 03, 2025 at 07:25 AM
-- Server version: 8.0.42
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `minventory`
--

-- --------------------------------------------------------

--
-- Table structure for table `activity_log`
--

CREATE TABLE `activity_log` (
  `id` int NOT NULL,
  `user_id` int DEFAULT NULL,
  `action` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb4_unicode_ci,
  `ip_address` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `activity_log`
--

INSERT INTO `activity_log` (`id`, `user_id`, `action`, `description`, `ip_address`, `created_at`) VALUES
(1, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 03:47:06'),
(2, 1, 'logout', 'User logged out', '127.0.0.1', '2025-07-31 03:55:59'),
(3, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 03:56:59'),
(4, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 04:44:29'),
(5, 1, 'logout', 'User logged out', '127.0.0.1', '2025-07-31 04:46:48'),
(6, 2, 'login', 'User logged in', '127.0.0.1', '2025-07-31 04:47:32'),
(7, 2, 'logout', 'User logged out', '127.0.0.1', '2025-07-31 04:55:10'),
(8, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 04:55:21'),
(9, 1, 'logout', 'User logged out', '127.0.0.1', '2025-07-31 04:55:33'),
(10, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 05:07:48'),
(11, 1, 'logout', 'User logged out', '127.0.0.1', '2025-07-31 05:16:44'),
(12, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 05:16:48'),
(13, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 11:09:17'),
(14, 1, 'logout', 'User logged out', '127.0.0.1', '2025-07-31 11:09:26'),
(15, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 11:18:40'),
(16, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 12:48:08'),
(17, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 12:58:37'),
(18, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 13:18:20'),
(19, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 13:34:02'),
(20, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 14:02:47'),
(21, 1, 'logout', 'User logged out', '127.0.0.1', '2025-07-31 14:10:53'),
(22, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 14:10:58'),
(23, 1, 'logout', 'User logged out', '127.0.0.1', '2025-07-31 15:22:18'),
(24, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 15:22:21'),
(25, 1, 'logout', 'User logged out', '127.0.0.1', '2025-07-31 15:58:56'),
(26, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 15:59:10'),
(27, 1, 'logout', 'User logged out', '127.0.0.1', '2025-07-31 16:23:55'),
(28, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 16:24:02'),
(29, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 16:57:07'),
(30, 1, 'login', 'User logged in', '127.0.0.1', '2025-07-31 17:14:39'),
(31, 1, 'logout', 'User logged out', '127.0.0.1', '2025-07-31 17:16:59'),
(32, 1, 'login', 'User logged in', '127.0.0.1', '2025-08-01 16:25:19'),
(33, 1, 'logout', 'User logged out', '127.0.0.1', '2025-08-01 16:25:57'),
(34, 1, 'login', 'User logged in', '127.0.0.1', '2025-08-01 16:26:03'),
(35, 1, 'logout', 'User logged out', '127.0.0.1', '2025-08-01 16:36:44'),
(36, 1, 'login', 'User logged in', '127.0.0.1', '2025-08-01 16:36:55'),
(37, 1, 'logout', 'User logged out', '127.0.0.1', '2025-08-01 17:42:26');

-- --------------------------------------------------------

--
-- Table structure for table `batch_recalls`
--

CREATE TABLE `batch_recalls` (
  `id` int NOT NULL,
  `recall_number` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `reason` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `severity_level` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT 'initiated',
  `initiated_by` int NOT NULL,
  `initiated_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `completed_date` timestamp NULL DEFAULT NULL,
  `customer_notification_sent` tinyint(1) DEFAULT '0',
  `regulatory_notification_sent` tinyint(1) DEFAULT '0',
  `notes` text COLLATE utf8mb4_unicode_ci,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `batch_recalls`
--

INSERT INTO `batch_recalls` (`id`, `recall_number`, `title`, `reason`, `severity_level`, `status`, `initiated_by`, `initiated_date`, `completed_date`, `customer_notification_sent`, `regulatory_notification_sent`, `notes`, `created_at`, `updated_at`) VALUES
(1, 'RCL-2025-0001', 'contamination', 'contamination', 'high', 'completed', 1, '2025-07-31 15:09:55', '2025-07-31 15:10:25', 0, 0, NULL, '2025-07-31 15:09:55', '2025-07-31 15:10:25'),
(2, 'RCL-2025-0002', 'test recall', 'testing recall ', 'high', 'completed', 1, '2025-07-31 15:56:17', '2025-07-31 15:57:23', 0, 0, NULL, '2025-07-31 15:56:17', '2025-07-31 15:57:23'),
(3, 'RCL-2025-0003', 'yousuf said ', 'yousuf said so', 'low', 'completed', 1, '2025-07-31 16:02:34', '2025-07-31 16:03:04', 0, 0, NULL, '2025-07-31 16:02:34', '2025-07-31 16:03:04'),
(4, 'RCL-2025-0004', 'virus', 'virus attack', 'high', 'completed', 1, '2025-07-31 16:04:29', '2025-07-31 16:14:46', 0, 0, NULL, '2025-07-31 16:04:29', '2025-07-31 16:14:46');

-- --------------------------------------------------------

--
-- Table structure for table `compliance_audits`
--

CREATE TABLE `compliance_audits` (
  `id` int NOT NULL,
  `audit_type` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `auditor_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `audit_date` date NOT NULL,
  `scope` text COLLATE utf8mb4_unicode_ci,
  `findings` text COLLATE utf8mb4_unicode_ci,
  `recommendations` text COLLATE utf8mb4_unicode_ci,
  `overall_rating` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT 'completed',
  `follow_up_required` tinyint(1) DEFAULT '0',
  `follow_up_date` date DEFAULT NULL,
  `report_file_path` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `conducted_by` int NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `compliance_audits`
--

INSERT INTO `compliance_audits` (`id`, `audit_type`, `auditor_name`, `audit_date`, `scope`, `findings`, `recommendations`, `overall_rating`, `status`, `follow_up_required`, `follow_up_date`, `report_file_path`, `conducted_by`, `created_at`, `updated_at`) VALUES
(1, 'internal', 'yousuf', '2025-07-31', 'check safety', 'all good', 'be more clean', 'excellent', 'completed', 0, NULL, NULL, 1, '2025-07-31 14:17:14', '2025-07-31 14:17:14'),
(2, 'regulatory', 'asif', '2025-07-31', 'yearly inspection', 'all good', 'more efficentcy needed', 'excellent', 'completed', 0, NULL, NULL, 1, '2025-07-31 16:29:03', '2025-07-31 16:29:03');

-- --------------------------------------------------------

--
-- Table structure for table `compliance_records`
--

CREATE TABLE `compliance_records` (
  `id` int NOT NULL,
  `record_type` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb4_unicode_ci,
  `certificate_number` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `issuing_authority` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `issue_date` date DEFAULT NULL,
  `expiration_date` date DEFAULT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT 'active',
  `file_path` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_by` int NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `compliance_records`
--

INSERT INTO `compliance_records` (`id`, `record_type`, `title`, `description`, `certificate_number`, `issuing_authority`, `issue_date`, `expiration_date`, `status`, `file_path`, `created_by`, `created_at`, `updated_at`) VALUES
(1, 'certificate', 'asddd', 'permited', '123456', 'abbas', '2025-07-25', '2025-08-30', 'active', NULL, 1, '2025-07-31 14:12:34', '2025-07-31 14:12:34');

-- --------------------------------------------------------

--
-- Table structure for table `food_safety_incidents`
--

CREATE TABLE `food_safety_incidents` (
  `id` int NOT NULL,
  `incident_number` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `incident_type` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `severity_level` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT 'open',
  `reported_by` int NOT NULL,
  `reported_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `investigation_notes` text COLLATE utf8mb4_unicode_ci,
  `corrective_actions` text COLLATE utf8mb4_unicode_ci,
  `root_cause` text COLLATE utf8mb4_unicode_ci,
  `closed_date` timestamp NULL DEFAULT NULL,
  `closed_by` int DEFAULT NULL,
  `regulatory_reported` tinyint(1) DEFAULT '0',
  `regulatory_report_date` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `food_safety_incidents`
--

INSERT INTO `food_safety_incidents` (`id`, `incident_number`, `incident_type`, `title`, `description`, `severity_level`, `status`, `reported_by`, `reported_date`, `investigation_notes`, `corrective_actions`, `root_cause`, `closed_date`, `closed_by`, `regulatory_reported`, `regulatory_report_date`, `created_at`, `updated_at`) VALUES
(1, 'INC-2025-0001', 'contamination', 'food contaminated', 'food got contamiated', 'high', 'open', 1, '2025-07-31 14:13:26', NULL, NULL, NULL, NULL, NULL, 0, NULL, '2025-07-31 14:13:26', '2025-07-31 14:13:26'),
(2, 'INC-2025-0002', 'contamination', 'food contaminated', 'flood caused contamination', 'high', 'open', 1, '2025-07-31 14:54:46', NULL, NULL, NULL, NULL, NULL, 0, NULL, '2025-07-31 14:54:46', '2025-07-31 14:54:46'),
(3, 'INC-2025-0003', 'other', 'suspicion', 'no info about prduct trace', 'low', 'resolved', 1, '2025-07-31 16:09:37', NULL, 'found details', NULL, NULL, NULL, 0, NULL, '2025-07-31 16:09:37', '2025-07-31 16:10:31');

-- --------------------------------------------------------

--
-- Table structure for table `incident_batches`
--

CREATE TABLE `incident_batches` (
  `id` int NOT NULL,
  `incident_id` int NOT NULL,
  `batch_id` int NOT NULL,
  `involvement_level` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `notes` text COLLATE utf8mb4_unicode_ci,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inventory_batches`
--

CREATE TABLE `inventory_batches` (
  `id` int NOT NULL,
  `product_id` int NOT NULL,
  `batch_number` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `quantity` decimal(10,2) NOT NULL,
  `arrival_date` date DEFAULT NULL,
  `expiration_date` date DEFAULT NULL,
  `storage_location` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `inventory_batches`
--

INSERT INTO `inventory_batches` (`id`, `product_id`, `batch_number`, `quantity`, `arrival_date`, `expiration_date`, `storage_location`, `created_at`, `updated_at`) VALUES
(1, 1, '123456789', 150.00, '2025-07-31', '2026-02-28', 'bashundhara', '2025-07-31 03:51:57', '2025-07-31 03:53:15'),
(2, 2, '987654321', 800.00, '2025-08-03', '2025-08-05', 'bashundhara', '2025-07-31 04:51:10', '2025-07-31 04:53:13'),
(3, 3, '32456789', 200.00, '2025-07-31', '2025-08-27', '2', '2025-07-31 12:49:46', '2025-07-31 12:50:34'),
(4, 3, '998887766', 40.00, '2025-07-31', '2025-08-13', '1', '2025-07-31 13:03:00', '2025-07-31 13:04:03'),
(5, 5, '4959690909', 600.00, '2025-08-06', '2025-08-30', '2', '2025-07-31 14:51:17', '2025-07-31 14:52:25'),
(6, 6, '345987652', 350.00, '2025-08-01', '2025-08-04', '2', '2025-07-31 16:07:54', '2025-07-31 16:13:21'),
(7, 7, '97567845673', 400.00, '2025-07-31', '2025-08-10', '3', '2025-07-31 16:20:34', '2025-07-31 16:21:51');

-- --------------------------------------------------------

--
-- Table structure for table `processing_inputs`
--

CREATE TABLE `processing_inputs` (
  `id` int NOT NULL,
  `session_id` int NOT NULL,
  `batch_id` int NOT NULL,
  `quantity_used` decimal(10,2) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `processing_inputs`
--

INSERT INTO `processing_inputs` (`id`, `session_id`, `batch_id`, `quantity_used`, `created_at`) VALUES
(1, 1, 1, 50.00, '2025-07-31 03:53:15'),
(2, 2, 2, 300.00, '2025-07-31 04:53:13'),
(3, 3, 3, 100.00, '2025-07-31 12:50:34'),
(4, 4, 4, 20.00, '2025-07-31 13:04:03'),
(5, 5, 5, 300.00, '2025-07-31 14:52:25'),
(6, 6, 6, 150.00, '2025-07-31 16:13:21'),
(7, 7, 7, 200.00, '2025-07-31 16:21:51');

-- --------------------------------------------------------

--
-- Table structure for table `processing_outputs`
--

CREATE TABLE `processing_outputs` (
  `id` int NOT NULL,
  `session_id` int NOT NULL,
  `product_id` int NOT NULL,
  `output_type` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `weight` decimal(10,2) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `processing_outputs`
--

INSERT INTO `processing_outputs` (`id`, `session_id`, `product_id`, `output_type`, `weight`, `created_at`) VALUES
(1, 1, 1, 'Main Product', 25.00, '2025-07-31 03:53:42'),
(2, 1, 1, 'Main Product', 25.00, '2025-07-31 03:53:43'),
(3, 2, 2, 'Main Product', 200.00, '2025-07-31 04:53:35'),
(4, 3, 3, 'Main Product', 80.00, '2025-07-31 12:50:51'),
(5, 4, 3, 'Main Product', 15.00, '2025-07-31 13:04:19'),
(6, 5, 5, 'Trimming', 100.00, '2025-07-31 14:52:46'),
(7, 6, 6, 'Main Product', 100.00, '2025-07-31 16:13:35'),
(8, 7, 7, 'Main Product', 100.00, '2025-07-31 16:22:31'),
(9, 7, 7, 'Trimming', 20.00, '2025-07-31 16:23:25');

-- --------------------------------------------------------

--
-- Table structure for table `processing_sessions`
--

CREATE TABLE `processing_sessions` (
  `id` int NOT NULL,
  `session_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_date` date DEFAULT NULL,
  `notes` text COLLATE utf8mb4_unicode_ci,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `processing_sessions`
--

INSERT INTO `processing_sessions` (`id`, `session_name`, `session_date`, `notes`, `created_at`, `updated_at`) VALUES
(1, 'wagyu processing', '2025-08-08', 'please be careful expensive', '2025-07-31 03:52:54', '2025-07-31 03:52:54'),
(2, 'brisket-processing', '2025-08-04', 'trim-fats', '2025-07-31 04:51:52', '2025-07-31 04:51:52'),
(3, 'asdfgt', '2025-08-02', 'sdfkkg', '2025-07-31 12:50:11', '2025-07-31 12:50:11'),
(4, 'test1', '2025-08-22', 'njnj', '2025-07-31 13:03:41', '2025-07-31 13:03:41'),
(5, 'testsession', '2025-08-21', 'first processing ', '2025-07-31 14:51:59', '2025-07-31 14:51:59'),
(6, 'lambchoptrim', '2025-08-01', 'lambbb', '2025-07-31 16:13:01', '2025-07-31 16:13:01'),
(7, 'testmeatprocess', '2025-08-05', 'testmeatprocess', '2025-07-31 16:21:13', '2025-07-31 16:21:13');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `animal_type` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cut_type` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `processing_date` date DEFAULT NULL,
  `storage_requirements` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `shelf_life` int DEFAULT NULL,
  `packaging_details` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `supplier_id` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `name`, `animal_type`, `cut_type`, `processing_date`, `storage_requirements`, `shelf_life`, `packaging_details`, `supplier_id`, `created_at`, `updated_at`) VALUES
(1, 'wagyu', 'Beef', 'sirloin', '2025-07-31', 'cold Storage', 365, 'freezer(-18c)', 1, '2025-07-31 03:51:03', '2025-07-31 03:51:03'),
(2, 'brisket', 'Beef', 'brisket(shoulder)', '2025-08-01', 'cold-storage', 365, 'dry', 2, '2025-07-31 04:50:23', '2025-07-31 04:50:23'),
(3, 'asd', 'Lamb', 'asdfg', '2025-07-31', 'Cold Storage', 234, 'freezer(-18c)', 1, '2025-07-31 12:49:07', '2025-07-31 12:49:07'),
(4, 'ccmcnmc', 'Poultry', 'fjfkjfkjgf', '2025-08-05', 'Dry Storage', 340, 'adsdsdsd', 1, '2025-07-31 14:05:00', '2025-07-31 14:05:00'),
(5, 'testmeat', 'Beef', 'dine', '2025-08-06', 'Cold Storage', 300, 'good', 1, '2025-07-31 14:49:16', '2025-07-31 14:49:16'),
(6, 'lambchop', 'Lamb', 'chop', '2025-08-02', 'Cold Storage', 365, 'good', 3, '2025-07-31 16:06:57', '2025-07-31 16:06:57'),
(7, 'meatTest1', 'Poultry', 'thigh', '2025-08-04', 'Processing Room', 10, 'process fast', 3, '2025-07-31 16:19:50', '2025-07-31 16:19:50');

-- --------------------------------------------------------

--
-- Table structure for table `recall_batches`
--

CREATE TABLE `recall_batches` (
  `id` int NOT NULL,
  `recall_id` int NOT NULL,
  `batch_id` int NOT NULL,
  `quantity_affected` decimal(10,2) DEFAULT NULL,
  `recovery_status` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT 'pending',
  `recovery_date` timestamp NULL DEFAULT NULL,
  `notes` text COLLATE utf8mb4_unicode_ci,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `recall_batches`
--

INSERT INTO `recall_batches` (`id`, `recall_id`, `batch_id`, `quantity_affected`, `recovery_status`, `recovery_date`, `notes`, `created_at`) VALUES
(1, 1, 5, NULL, 'recovered', '2025-08-01 17:40:19', 'fixed contamination', '2025-07-31 15:09:55'),
(2, 2, 4, NULL, 'in_progress', '2025-07-31 15:57:28', 'recovered', '2025-07-31 15:56:17'),
(3, 3, 3, NULL, 'recovered', '2025-07-31 16:03:42', 'recovered', '2025-07-31 16:02:35'),
(4, 4, 1, NULL, 'recovered', '2025-07-31 16:14:59', 'recovered', '2025-07-31 16:04:30');

-- --------------------------------------------------------

--
-- Table structure for table `sensor_readings`
--

CREATE TABLE `sensor_readings` (
  `id` int NOT NULL,
  `sensor_id` int NOT NULL,
  `temperature` decimal(5,2) DEFAULT NULL,
  `humidity` decimal(5,2) DEFAULT NULL,
  `alert_status` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT 'normal',
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `sensor_readings`
--

INSERT INTO `sensor_readings` (`id`, `sensor_id`, `temperature`, `humidity`, `alert_status`, `timestamp`) VALUES
(1, 1, 2.50, 90.00, 'normal', '2025-07-31 12:20:47'),
(2, 2, -0.92, 89.32, 'normal', '2025-07-31 12:23:11'),
(3, 3, 1.57, 88.26, 'normal', '2025-07-31 12:24:53'),
(4, 4, 1.57, 89.07, 'normal', '2025-07-31 16:17:16'),
(5, 5, 1.19, 91.81, 'normal', '2025-07-31 16:17:18'),
(6, 6, 0.15, 89.45, 'normal', '2025-07-31 16:17:20'),
(7, 2, 1.65, 90.90, 'normal', '2025-08-01 16:26:33'),
(8, 3, 0.33, 88.18, 'normal', '2025-08-01 16:26:35'),
(9, 2, 2.81, 89.98, 'normal', '2025-08-01 16:37:16'),
(10, 3, 0.30, 90.24, 'normal', '2025-08-01 16:37:18'),
(11, 4, -0.45, 88.29, 'normal', '2025-08-01 16:37:28'),
(12, 5, 2.37, 91.70, 'normal', '2025-08-01 16:37:30'),
(13, 6, 1.13, 90.39, 'normal', '2025-08-01 16:37:32');

-- --------------------------------------------------------

--
-- Table structure for table `storage_locations`
--

CREATE TABLE `storage_locations` (
  `id` int NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb4_unicode_ci,
  `location_type` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `capacity` decimal(10,2) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `storage_locations`
--

INSERT INTO `storage_locations` (`id`, `name`, `description`, `location_type`, `capacity`, `created_at`, `updated_at`) VALUES
(1, 'Test Cold Storage', 'Test storage for meat products', 'Cold Storage', 1000.00, '2025-07-31 12:20:11', '2025-07-31 12:20:11'),
(2, 'cold34', 'for normal use', 'Refrigerator', 100.00, '2025-07-31 12:22:26', '2025-07-31 12:22:26'),
(3, 'storage1', 'meat processed here', 'Processing Room', 100000.00, '2025-07-31 16:16:17', '2025-07-31 16:16:17');

-- --------------------------------------------------------

--
-- Table structure for table `storage_sensors`
--

CREATE TABLE `storage_sensors` (
  `id` int NOT NULL,
  `storage_id` int NOT NULL,
  `sensor_type` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `sensor_id` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT 'active',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `storage_sensors`
--

INSERT INTO `storage_sensors` (`id`, `storage_id`, `sensor_type`, `sensor_id`, `status`, `created_at`, `updated_at`) VALUES
(1, 1, 'Temperature_Humidity', 'SENSOR001', 'active', '2025-07-31 12:20:25', '2025-07-31 12:20:25'),
(2, 2, 'Temperature', '1234', 'active', '2025-07-31 12:22:56', '2025-07-31 12:22:56'),
(3, 2, 'Environmental', '4321', 'active', '2025-07-31 12:24:48', '2025-07-31 12:24:48'),
(4, 3, 'Temperature', '5434', 'active', '2025-07-31 16:16:40', '2025-07-31 16:16:40'),
(5, 3, 'Humidity', '3243', 'active', '2025-07-31 16:16:53', '2025-07-31 16:16:53'),
(6, 3, 'Environmental', '9090', 'active', '2025-07-31 16:17:12', '2025-07-31 16:17:12');

-- --------------------------------------------------------

--
-- Table structure for table `suppliers`
--

CREATE TABLE `suppliers` (
  `id` int NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `contact_person` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `address` text COLLATE utf8mb4_unicode_ci,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `suppliers`
--

INSERT INTO `suppliers` (`id`, `name`, `contact_person`, `phone`, `email`, `address`, `created_at`, `updated_at`) VALUES
(1, 'AbbasMeat', 'abbas yasin', '01924451724', 'abbasyasin1n2@gmail.com', 'savar', '2025-07-31 03:50:10', '2025-07-31 03:50:10'),
(2, 'AlifsMeat', 'alif', '017643424646', 'alif1n2@gmail.com', 'bashundhara', '2025-07-31 04:48:52', '2025-07-31 04:48:52'),
(3, 'yousufMeat', 'yousuf', '01923334576', 'mdyousuf1n2@gmail.com', 'jamgora', '2025-07-31 14:50:11', '2025-07-31 14:50:11');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `username` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password_hash` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password_hash`, `created_at`, `updated_at`) VALUES
(1, 'alif', 'alif1n2@gmail.com', 'ee7096ce421059665eda7e285668af303f08feb7c384e318dee7ed76a8d4349d', '2025-07-31 03:47:01', '2025-07-31 03:47:01'),
(2, 'abbas', 'abbas1n2@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', '2025-07-31 04:47:18', '2025-07-31 04:47:18');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `activity_log`
--
ALTER TABLE `activity_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `batch_recalls`
--
ALTER TABLE `batch_recalls`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `recall_number` (`recall_number`),
  ADD KEY `initiated_by` (`initiated_by`),
  ADD KEY `idx_recall_number` (`recall_number`),
  ADD KEY `idx_severity_level` (`severity_level`),
  ADD KEY `idx_status` (`status`);

--
-- Indexes for table `compliance_audits`
--
ALTER TABLE `compliance_audits`
  ADD PRIMARY KEY (`id`),
  ADD KEY `conducted_by` (`conducted_by`),
  ADD KEY `idx_audit_type` (`audit_type`),
  ADD KEY `idx_audit_date` (`audit_date`),
  ADD KEY `idx_status` (`status`);

--
-- Indexes for table `compliance_records`
--
ALTER TABLE `compliance_records`
  ADD PRIMARY KEY (`id`),
  ADD KEY `created_by` (`created_by`),
  ADD KEY `idx_record_type` (`record_type`),
  ADD KEY `idx_expiration_date` (`expiration_date`),
  ADD KEY `idx_status` (`status`);

--
-- Indexes for table `food_safety_incidents`
--
ALTER TABLE `food_safety_incidents`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `incident_number` (`incident_number`),
  ADD KEY `reported_by` (`reported_by`),
  ADD KEY `closed_by` (`closed_by`),
  ADD KEY `idx_incident_number` (`incident_number`),
  ADD KEY `idx_incident_type` (`incident_type`),
  ADD KEY `idx_status` (`status`);

--
-- Indexes for table `incident_batches`
--
ALTER TABLE `incident_batches`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_incident_batch` (`incident_id`,`batch_id`),
  ADD KEY `idx_incident_id` (`incident_id`),
  ADD KEY `idx_batch_id` (`batch_id`);

--
-- Indexes for table `inventory_batches`
--
ALTER TABLE `inventory_batches`
  ADD PRIMARY KEY (`id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `processing_inputs`
--
ALTER TABLE `processing_inputs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `session_id` (`session_id`),
  ADD KEY `batch_id` (`batch_id`);

--
-- Indexes for table `processing_outputs`
--
ALTER TABLE `processing_outputs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `session_id` (`session_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `processing_sessions`
--
ALTER TABLE `processing_sessions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`),
  ADD KEY `supplier_id` (`supplier_id`);

--
-- Indexes for table `recall_batches`
--
ALTER TABLE `recall_batches`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_recall_batch` (`recall_id`,`batch_id`),
  ADD KEY `idx_recall_id` (`recall_id`),
  ADD KEY `idx_batch_id` (`batch_id`);

--
-- Indexes for table `sensor_readings`
--
ALTER TABLE `sensor_readings`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sensor_id` (`sensor_id`);

--
-- Indexes for table `storage_locations`
--
ALTER TABLE `storage_locations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `storage_sensors`
--
ALTER TABLE `storage_sensors`
  ADD PRIMARY KEY (`id`),
  ADD KEY `storage_id` (`storage_id`);

--
-- Indexes for table `suppliers`
--
ALTER TABLE `suppliers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `activity_log`
--
ALTER TABLE `activity_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `batch_recalls`
--
ALTER TABLE `batch_recalls`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `compliance_audits`
--
ALTER TABLE `compliance_audits`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `compliance_records`
--
ALTER TABLE `compliance_records`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `food_safety_incidents`
--
ALTER TABLE `food_safety_incidents`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `incident_batches`
--
ALTER TABLE `incident_batches`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inventory_batches`
--
ALTER TABLE `inventory_batches`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `processing_inputs`
--
ALTER TABLE `processing_inputs`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `processing_outputs`
--
ALTER TABLE `processing_outputs`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `processing_sessions`
--
ALTER TABLE `processing_sessions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `recall_batches`
--
ALTER TABLE `recall_batches`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `sensor_readings`
--
ALTER TABLE `sensor_readings`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `storage_locations`
--
ALTER TABLE `storage_locations`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `storage_sensors`
--
ALTER TABLE `storage_sensors`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `suppliers`
--
ALTER TABLE `suppliers`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `activity_log`
--
ALTER TABLE `activity_log`
  ADD CONSTRAINT `activity_log_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `batch_recalls`
--
ALTER TABLE `batch_recalls`
  ADD CONSTRAINT `batch_recalls_ibfk_1` FOREIGN KEY (`initiated_by`) REFERENCES `users` (`id`);

--
-- Constraints for table `compliance_audits`
--
ALTER TABLE `compliance_audits`
  ADD CONSTRAINT `compliance_audits_ibfk_1` FOREIGN KEY (`conducted_by`) REFERENCES `users` (`id`);

--
-- Constraints for table `compliance_records`
--
ALTER TABLE `compliance_records`
  ADD CONSTRAINT `compliance_records_ibfk_1` FOREIGN KEY (`created_by`) REFERENCES `users` (`id`);

--
-- Constraints for table `food_safety_incidents`
--
ALTER TABLE `food_safety_incidents`
  ADD CONSTRAINT `food_safety_incidents_ibfk_1` FOREIGN KEY (`reported_by`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `food_safety_incidents_ibfk_2` FOREIGN KEY (`closed_by`) REFERENCES `users` (`id`);

--
-- Constraints for table `incident_batches`
--
ALTER TABLE `incident_batches`
  ADD CONSTRAINT `incident_batches_ibfk_1` FOREIGN KEY (`incident_id`) REFERENCES `food_safety_incidents` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `incident_batches_ibfk_2` FOREIGN KEY (`batch_id`) REFERENCES `inventory_batches` (`id`);

--
-- Constraints for table `inventory_batches`
--
ALTER TABLE `inventory_batches`
  ADD CONSTRAINT `inventory_batches_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `processing_inputs`
--
ALTER TABLE `processing_inputs`
  ADD CONSTRAINT `processing_inputs_ibfk_1` FOREIGN KEY (`session_id`) REFERENCES `processing_sessions` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `processing_inputs_ibfk_2` FOREIGN KEY (`batch_id`) REFERENCES `inventory_batches` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `processing_outputs`
--
ALTER TABLE `processing_outputs`
  ADD CONSTRAINT `processing_outputs_ibfk_1` FOREIGN KEY (`session_id`) REFERENCES `processing_sessions` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `processing_outputs_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `products_ibfk_1` FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`id`) ON DELETE SET NULL;

--
-- Constraints for table `recall_batches`
--
ALTER TABLE `recall_batches`
  ADD CONSTRAINT `recall_batches_ibfk_1` FOREIGN KEY (`recall_id`) REFERENCES `batch_recalls` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `recall_batches_ibfk_2` FOREIGN KEY (`batch_id`) REFERENCES `inventory_batches` (`id`);

--
-- Constraints for table `sensor_readings`
--
ALTER TABLE `sensor_readings`
  ADD CONSTRAINT `sensor_readings_ibfk_1` FOREIGN KEY (`sensor_id`) REFERENCES `storage_sensors` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `storage_sensors`
--
ALTER TABLE `storage_sensors`
  ADD CONSTRAINT `storage_sensors_ibfk_1` FOREIGN KEY (`storage_id`) REFERENCES `storage_locations` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
