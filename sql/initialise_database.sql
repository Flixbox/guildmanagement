CREATE TABLE IF NOT EXISTS `users` (
  `id` int(10) NOT NULL,
  `salutation` varchar(255) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `street` varchar(255) NOT NULL,
  `zipcode` int(11) NOT NULL,
  `city` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  `birthday` date NOT NULL,
  `job` varchar(255) NOT NULL,
  `conditions` int(11) NOT NULL,
  `iban` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
);