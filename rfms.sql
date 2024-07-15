-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 12, 2024 at 09:42 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rfms`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminstrative_secretary`
--

CREATE TABLE `adminstrative_secretary` (
  `id` bigint(20) NOT NULL,
  `employee_id` varchar(50) NOT NULL,
  `profile_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can view permission', 1, 'view_permission'),
(5, 'Can add group', 2, 'add_group'),
(6, 'Can change group', 2, 'change_group'),
(7, 'Can delete group', 2, 'delete_group'),
(8, 'Can view group', 2, 'view_group'),
(9, 'Can add user', 3, 'add_user'),
(10, 'Can change user', 3, 'change_user'),
(11, 'Can delete user', 3, 'delete_user'),
(12, 'Can view user', 3, 'view_user'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add log entry', 6, 'add_logentry'),
(22, 'Can change log entry', 6, 'change_logentry'),
(23, 'Can delete log entry', 6, 'delete_logentry'),
(24, 'Can view log entry', 6, 'view_logentry'),
(25, 'Can add distric t_account', 7, 'add_district_account'),
(26, 'Can change distric t_account', 7, 'change_district_account'),
(27, 'Can delete distric t_account', 7, 'delete_district_account'),
(28, 'Can view distric t_account', 7, 'view_district_account'),
(29, 'Can add group', 8, 'add_group'),
(30, 'Can change group', 8, 'change_group'),
(31, 'Can delete group', 8, 'delete_group'),
(32, 'Can view group', 8, 'view_group'),
(33, 'Can add village', 9, 'add_village'),
(34, 'Can change village', 9, 'change_village'),
(35, 'Can delete village', 9, 'delete_village'),
(36, 'Can view village', 9, 'view_village'),
(37, 'Can add ward', 10, 'add_ward'),
(38, 'Can change ward', 10, 'change_ward'),
(39, 'Can delete ward', 10, 'delete_ward'),
(40, 'Can view ward', 10, 'view_ward'),
(41, 'Can add group account', 11, 'add_groupaccount'),
(42, 'Can change group account', 11, 'change_groupaccount'),
(43, 'Can delete group account', 11, 'delete_groupaccount'),
(44, 'Can view group account', 11, 'view_groupaccount'),
(45, 'Can add group transaction', 12, 'add_grouptransaction'),
(46, 'Can change group transaction', 12, 'change_grouptransaction'),
(47, 'Can delete group transaction', 12, 'delete_grouptransaction'),
(48, 'Can view group transaction', 12, 'view_grouptransaction'),
(49, 'Can add profile', 13, 'add_profile'),
(50, 'Can change profile', 13, 'change_profile'),
(51, 'Can delete profile', 13, 'delete_profile'),
(52, 'Can view profile', 13, 'view_profile'),
(53, 'Can add member', 14, 'add_member'),
(54, 'Can change member', 14, 'change_member'),
(55, 'Can delete member', 14, 'delete_member'),
(56, 'Can view member', 14, 'view_member'),
(57, 'Can add notification', 15, 'add_notification'),
(58, 'Can change notification', 15, 'change_notification'),
(59, 'Can delete notification', 15, 'delete_notification'),
(60, 'Can view notification', 15, 'view_notification'),
(61, 'Can add distric t_transaction', 16, 'add_district_transaction'),
(62, 'Can change distric t_transaction', 16, 'change_district_transaction'),
(63, 'Can delete distric t_transaction', 16, 'delete_district_transaction'),
(64, 'Can view distric t_transaction', 16, 'view_district_transaction'),
(65, 'Can add adminstrative secretary', 17, 'add_adminstrativesecretary'),
(66, 'Can change adminstrative secretary', 17, 'change_adminstrativesecretary'),
(67, 'Can delete adminstrative secretary', 17, 'delete_adminstrativesecretary'),
(68, 'Can view adminstrative secretary', 17, 'view_adminstrativesecretary'),
(69, 'Can add development officer', 18, 'add_developmentofficer'),
(70, 'Can change development officer', 18, 'change_developmentofficer'),
(71, 'Can delete development officer', 18, 'delete_developmentofficer'),
(72, 'Can view development officer', 18, 'view_developmentofficer'),
(73, 'Can add loan schedule', 19, 'add_loanschedule'),
(74, 'Can change loan schedule', 19, 'change_loanschedule'),
(75, 'Can delete loan schedule', 19, 'delete_loanschedule'),
(76, 'Can view loan schedule', 19, 'view_loanschedule'),
(77, 'Can add return transaction', 20, 'add_returntransaction'),
(78, 'Can change return transaction', 20, 'change_returntransaction'),
(79, 'Can delete return transaction', 20, 'delete_returntransaction'),
(80, 'Can view return transaction', 20, 'view_returntransaction'),
(81, 'Can add Login History', 21, 'add_loginhistory'),
(82, 'Can change Login History', 21, 'change_loginhistory'),
(83, 'Can delete Login History', 21, 'delete_loginhistory'),
(84, 'Can view Login History', 21, 'view_loginhistory');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `development_officers`
--

CREATE TABLE `development_officers` (
  `id` bigint(20) NOT NULL,
  `employee_id` varchar(50) NOT NULL,
  `profile_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `district`
--

CREATE TABLE `district` (
  `id` bigint(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `account_name` varchar(20) NOT NULL,
  `account_number` varchar(30) NOT NULL,
  `balance_amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `district_transaction`
--

CREATE TABLE `district_transaction` (
  `id` bigint(20) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `transaction_type` varchar(20) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `from_account_id` bigint(20) NOT NULL,
  `destination_account_id` bigint(20) DEFAULT NULL,
  `adminstrative_officer_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(6, 'admin', 'logentry'),
(2, 'auth', 'group'),
(1, 'auth', 'permission'),
(3, 'auth', 'user'),
(4, 'contenttypes', 'contenttype'),
(21, 'login_history', 'loginhistory'),
(5, 'sessions', 'session'),
(17, 'trial', 'adminstrativesecretary'),
(18, 'trial', 'developmentofficer'),
(7, 'trial', 'district_account'),
(16, 'trial', 'district_transaction'),
(8, 'trial', 'group'),
(11, 'trial', 'groupaccount'),
(12, 'trial', 'grouptransaction'),
(19, 'trial', 'loanschedule'),
(14, 'trial', 'member'),
(15, 'trial', 'notification'),
(13, 'trial', 'profile'),
(20, 'trial', 'returntransaction'),
(9, 'trial', 'village'),
(10, 'trial', 'ward');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-06-25 17:37:52.448157'),
(2, 'auth', '0001_initial', '2024-06-25 17:37:53.023664'),
(3, 'admin', '0001_initial', '2024-06-25 17:37:53.166807'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-06-25 17:37:53.210846'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-06-25 17:37:53.224770'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-06-25 17:37:53.307041'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-06-25 17:37:53.375557'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-06-25 17:37:53.392803'),
(9, 'auth', '0004_alter_user_username_opts', '2024-06-25 17:37:53.407264'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-06-25 17:37:53.462777'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-06-25 17:37:53.465081'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-06-25 17:37:53.478581'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-06-25 17:37:53.494802'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-06-25 17:37:53.510917'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-06-25 17:37:53.537806'),
(16, 'auth', '0011_update_proxy_permissions', '2024-06-25 17:37:53.555139'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-06-25 17:37:53.576697'),
(18, 'login_history', '0001_initial', '2024-06-25 17:37:53.670731'),
(19, 'login_history', '0002_loginhistory_is_login', '2024-06-25 17:37:53.692995'),
(20, 'login_history', '0003_alter_loginhistory_id', '2024-06-25 17:37:53.766624'),
(21, 'sessions', '0001_initial', '2024-06-25 17:37:53.806268'),
(22, 'trial', '0001_initial', '2024-06-25 17:37:55.108413'),
(23, 'trial', '0002_rename_sponsor_adminstrativesecretary_and_more', '2024-06-25 17:37:56.053213'),
(24, 'trial', '0003_rename_sponsor_district_transaction_adminstrative_officer', '2024-06-25 17:37:56.445717'),
(25, 'trial', '0004_loanschedule', '2024-06-25 17:37:56.551140'),
(26, 'trial', '0005_returntransaction', '2024-06-25 17:37:56.763454'),
(27, 'trial', '0006_remove_returntransaction_group_transaction_and_more', '2024-06-25 17:37:57.169818');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `group`
--

CREATE TABLE `group` (
  `id` bigint(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `group_account` varchar(20) NOT NULL,
  `total_members` int(11) NOT NULL,
  `group_no` int(11) NOT NULL,
  `constitution` varchar(100) DEFAULT NULL,
  `village_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `groupaccount`
--

CREATE TABLE `groupaccount` (
  `id` bigint(20) NOT NULL,
  `balance` decimal(10,2) NOT NULL,
  `group_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `grouptransaction`
--

CREATE TABLE `grouptransaction` (
  `id` bigint(20) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `transaction_type` varchar(20) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `group_id` bigint(20) NOT NULL,
  `account_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `login_history_loginhistory`
--

CREATE TABLE `login_history_loginhistory` (
  `id` bigint(20) NOT NULL,
  `ip` varchar(15) DEFAULT NULL,
  `user_agent` longtext NOT NULL,
  `date_time` datetime(6) NOT NULL,
  `is_logged_in` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  `is_login` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `id` bigint(20) NOT NULL,
  `position` varchar(14) NOT NULL,
  `group_id` bigint(20) NOT NULL,
  `profile_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `notification`
--

CREATE TABLE `notification` (
  `id` bigint(20) NOT NULL,
  `content` longtext NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `Member_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `trial_loanschedule`
--

CREATE TABLE `trial_loanschedule` (
  `id` bigint(20) NOT NULL,
  `start_date` datetime(6) NOT NULL,
  `end_date` datetime(6) NOT NULL,
  `amount_received` decimal(10,2) NOT NULL,
  `returned` tinyint(1) NOT NULL,
  `group_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `trial_profile`
--

CREATE TABLE `trial_profile` (
  `id` bigint(20) NOT NULL,
  `sex` varchar(6) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `role` varchar(25) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `trial_returntransaction`
--

CREATE TABLE `trial_returntransaction` (
  `id` bigint(20) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `district_transaction_id` bigint(20) NOT NULL,
  `member_id` bigint(20) NOT NULL,
  `group_account_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `village`
--

CREATE TABLE `village` (
  `id` bigint(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `ward_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ward`
--

CREATE TABLE `ward` (
  `id` bigint(20) NOT NULL,
  `name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminstrative_secretary`
--
ALTER TABLE `adminstrative_secretary`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Sponsor_profile_id_bd67031f_fk_trial_profile_id` (`profile_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `development_officers`
--
ALTER TABLE `development_officers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `development_officers_profile_id_4e83f7da_fk_trial_profile_id` (`profile_id`);

--
-- Indexes for table `district`
--
ALTER TABLE `district`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `district_transaction`
--
ALTER TABLE `district_transaction`
  ADD PRIMARY KEY (`id`),
  ADD KEY `DISTRICT_TRANSACTION_from_account_id_facc231d_fk_District_id` (`from_account_id`),
  ADD KEY `DISTRICT_TRANSACTION_destination_account_id_ce719481_fk_Group_id` (`destination_account_id`),
  ADD KEY `DISTRICT_TRANSACTION_adminstrative_office_d0d760b8_fk_adminstra` (`adminstrative_officer_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `group`
--
ALTER TABLE `group`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Group_village_id_5986fdc4_fk_Village_id` (`village_id`);

--
-- Indexes for table `groupaccount`
--
ALTER TABLE `groupaccount`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `group_id` (`group_id`);

--
-- Indexes for table `grouptransaction`
--
ALTER TABLE `grouptransaction`
  ADD PRIMARY KEY (`id`),
  ADD KEY `GroupTransaction_group_id_bc231fec_fk_Group_id` (`group_id`),
  ADD KEY `GroupTransaction_account_id_e15f7f1f_fk_GroupAccount_id` (`account_id`);

--
-- Indexes for table `login_history_loginhistory`
--
ALTER TABLE `login_history_loginhistory`
  ADD PRIMARY KEY (`id`),
  ADD KEY `login_history_loginhistory_user_id_195fb57c_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Member_group_id_bdb7ae46_fk_Group_id` (`group_id`),
  ADD KEY `Member_profile_id_cf1e9870_fk_trial_profile_id` (`profile_id`);

--
-- Indexes for table `notification`
--
ALTER TABLE `notification`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Notification_Member_id_c817113b_fk_Member_id` (`Member_id`),
  ADD KEY `Notification_user_id_27901a99_fk_Sponsor_id` (`user_id`);

--
-- Indexes for table `trial_loanschedule`
--
ALTER TABLE `trial_loanschedule`
  ADD PRIMARY KEY (`id`),
  ADD KEY `trial_loanschedule_group_id_a84b56e5_fk_Group_id` (`group_id`);

--
-- Indexes for table `trial_profile`
--
ALTER TABLE `trial_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `trial_returntransaction`
--
ALTER TABLE `trial_returntransaction`
  ADD PRIMARY KEY (`id`),
  ADD KEY `trial_returntransact_district_transaction_c95139ec_fk_DISTRICT_` (`district_transaction_id`),
  ADD KEY `trial_returntransaction_member_id_56a551a5_fk_Member_id` (`member_id`),
  ADD KEY `trial_returntransact_group_account_id_275c9c3f_fk_GroupAcco` (`group_account_id`);

--
-- Indexes for table `village`
--
ALTER TABLE `village`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Village_ward_id_a3b8555e_fk_Ward_id` (`ward_id`);

--
-- Indexes for table `ward`
--
ALTER TABLE `ward`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adminstrative_secretary`
--
ALTER TABLE `adminstrative_secretary`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=85;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `development_officers`
--
ALTER TABLE `development_officers`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `district`
--
ALTER TABLE `district`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `district_transaction`
--
ALTER TABLE `district_transaction`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `group`
--
ALTER TABLE `group`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `groupaccount`
--
ALTER TABLE `groupaccount`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `grouptransaction`
--
ALTER TABLE `grouptransaction`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `login_history_loginhistory`
--
ALTER TABLE `login_history_loginhistory`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `member`
--
ALTER TABLE `member`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `notification`
--
ALTER TABLE `notification`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `trial_loanschedule`
--
ALTER TABLE `trial_loanschedule`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `trial_profile`
--
ALTER TABLE `trial_profile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `trial_returntransaction`
--
ALTER TABLE `trial_returntransaction`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `village`
--
ALTER TABLE `village`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `ward`
--
ALTER TABLE `ward`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `adminstrative_secretary`
--
ALTER TABLE `adminstrative_secretary`
  ADD CONSTRAINT `Sponsor_profile_id_bd67031f_fk_trial_profile_id` FOREIGN KEY (`profile_id`) REFERENCES `trial_profile` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `development_officers`
--
ALTER TABLE `development_officers`
  ADD CONSTRAINT `development_officers_profile_id_4e83f7da_fk_trial_profile_id` FOREIGN KEY (`profile_id`) REFERENCES `trial_profile` (`id`);

--
-- Constraints for table `district_transaction`
--
ALTER TABLE `district_transaction`
  ADD CONSTRAINT `DISTRICT_TRANSACTION_adminstrative_office_d0d760b8_fk_adminstra` FOREIGN KEY (`adminstrative_officer_id`) REFERENCES `adminstrative_secretary` (`id`),
  ADD CONSTRAINT `DISTRICT_TRANSACTION_destination_account_id_ce719481_fk_Group_id` FOREIGN KEY (`destination_account_id`) REFERENCES `group` (`id`),
  ADD CONSTRAINT `DISTRICT_TRANSACTION_from_account_id_facc231d_fk_District_id` FOREIGN KEY (`from_account_id`) REFERENCES `district` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `group`
--
ALTER TABLE `group`
  ADD CONSTRAINT `Group_village_id_5986fdc4_fk_Village_id` FOREIGN KEY (`village_id`) REFERENCES `village` (`id`);

--
-- Constraints for table `groupaccount`
--
ALTER TABLE `groupaccount`
  ADD CONSTRAINT `GroupAccount_group_id_d5d13ba7_fk_Group_id` FOREIGN KEY (`group_id`) REFERENCES `group` (`id`);

--
-- Constraints for table `grouptransaction`
--
ALTER TABLE `grouptransaction`
  ADD CONSTRAINT `GroupTransaction_account_id_e15f7f1f_fk_GroupAccount_id` FOREIGN KEY (`account_id`) REFERENCES `groupaccount` (`id`),
  ADD CONSTRAINT `GroupTransaction_group_id_bc231fec_fk_Group_id` FOREIGN KEY (`group_id`) REFERENCES `group` (`id`);

--
-- Constraints for table `login_history_loginhistory`
--
ALTER TABLE `login_history_loginhistory`
  ADD CONSTRAINT `login_history_loginhistory_user_id_195fb57c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `member`
--
ALTER TABLE `member`
  ADD CONSTRAINT `Member_group_id_bdb7ae46_fk_Group_id` FOREIGN KEY (`group_id`) REFERENCES `group` (`id`),
  ADD CONSTRAINT `Member_profile_id_cf1e9870_fk_trial_profile_id` FOREIGN KEY (`profile_id`) REFERENCES `trial_profile` (`id`);

--
-- Constraints for table `notification`
--
ALTER TABLE `notification`
  ADD CONSTRAINT `Notification_Member_id_c817113b_fk_Member_id` FOREIGN KEY (`Member_id`) REFERENCES `member` (`id`),
  ADD CONSTRAINT `Notification_user_id_27901a99_fk_Sponsor_id` FOREIGN KEY (`user_id`) REFERENCES `adminstrative_secretary` (`id`);

--
-- Constraints for table `trial_loanschedule`
--
ALTER TABLE `trial_loanschedule`
  ADD CONSTRAINT `trial_loanschedule_group_id_a84b56e5_fk_Group_id` FOREIGN KEY (`group_id`) REFERENCES `group` (`id`);

--
-- Constraints for table `trial_profile`
--
ALTER TABLE `trial_profile`
  ADD CONSTRAINT `trial_profile_user_id_ea78c7ae_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `trial_returntransaction`
--
ALTER TABLE `trial_returntransaction`
  ADD CONSTRAINT `trial_returntransact_district_transaction_c95139ec_fk_DISTRICT_` FOREIGN KEY (`district_transaction_id`) REFERENCES `district_transaction` (`id`),
  ADD CONSTRAINT `trial_returntransact_group_account_id_275c9c3f_fk_GroupAcco` FOREIGN KEY (`group_account_id`) REFERENCES `groupaccount` (`id`),
  ADD CONSTRAINT `trial_returntransaction_member_id_56a551a5_fk_Member_id` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`);

--
-- Constraints for table `village`
--
ALTER TABLE `village`
  ADD CONSTRAINT `Village_ward_id_a3b8555e_fk_Ward_id` FOREIGN KEY (`ward_id`) REFERENCES `ward` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
