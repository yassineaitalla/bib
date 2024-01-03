-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mer. 02 nov. 2022 à 19:12
-- Version du serveur : 8.0.27
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `compte`
--

-- --------------------------------------------------------

--
-- Structure de la table `ajoutadh`
--

DROP TABLE IF EXISTS `ajoutadh`;
CREATE TABLE IF NOT EXISTS `ajoutadh` (
  `Nom` varchar(100) NOT NULL,
  `Prenom` varchar(100) NOT NULL,
  `Codepostal` int NOT NULL,
  `Ville` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `ajoutadh`
--

INSERT INTO `ajoutadh` (`Nom`, `Prenom`, `Codepostal`, `Ville`) VALUES
('yass', 'y', 0, 'y');

-- --------------------------------------------------------

--
-- Structure de la table `ajoutlivress`
--

DROP TABLE IF EXISTS `ajoutlivress`;
CREATE TABLE IF NOT EXISTS `ajoutlivress` (
  `Titres` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `Auteurs` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `Collections` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `Editeurs` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `NbExemplaires` int NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `ajoutlivress`
--

INSERT INTO `ajoutlivress` (`Titres`, `Auteurs`, `Collections`, `Editeurs`, `NbExemplaires`) VALUES
('i', 'ii', 'ii', 'iii', 0),
('mise', 'ty', 'i', 'yu', 0);

-- --------------------------------------------------------

--
-- Structure de la table `comptes`
--

DROP TABLE IF EXISTS `comptes`;
CREATE TABLE IF NOT EXISTS `comptes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `prenom` varchar(100) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `telephone` int NOT NULL,
  `email` varchar(100) NOT NULL,
  `question` varchar(100) NOT NULL,
  `reponse` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `comptes`
--

INSERT INTO `comptes` (`id`, `prenom`, `nom`, `telephone`, `email`, `question`, `reponse`, `password`) VALUES
(1, 'yassine', 'aitalla', 650015167, 'yass@gmail.com', 'ton prenom', 'yass', 'opopop'),
(2, 'yassine', 'aitalla', 650015167, 'yass@gmail.com', 'ton prenom', 'yass', 'opopop'),
(3, '', '', 0, '', 'Lieu de naissance', 'paname', ''),
(4, '', '', 0, '', 'Lieu de naissance', 'paname', ''),
(5, 'nabil', 'ait', 65222222, 'nabil@gmail.com', 'Lieu de naissance', 'paris', 'nabil@'),
(6, 'nabil', 'ait', 65222222, 'nabil@gmail.com', 'Lieu de naissance', 'paris', 'nabil@'),
(7, 'i', 'ii', 0, 'i', 'ton prenom', 'ii', 'ii'),
(8, 'i', 'ii', 0, 'i', 'ton prenom', 'ii', 'ii'),
(9, 'i', 'ii', 0, 'i', 'ton prenom', 'ii', 'ii'),
(10, 'i', 'ii', 0, 'i', 'ton prenom', 'ii', 'ii'),
(11, 'tt', 'tt', 0, 't', 'ton prenom', 't', 't'),
(12, 'tt', 'tt', 0, 't', 'ton prenom', 't', 't'),
(13, 'ii', 'i', 0, 'ii', 'ton prenom', 'ii', 'ii'),
(14, 'yu', 'y', 0, 'yu', 'ton prenom', 'yu', 'yui'),
(15, 't', 't', 0, 't', 'ton prenom', 't', 't'),
(16, 'walid', 'ait', 0, '025698', 'ton prenom', 'walide', 'nn'),
(17, 'yu', 'yu', 0, 'yu', 'Film préféré', 'miserable', 'yui'),
(18, 'll', 'p', 0, 'p', 'ton prenom', 'p', 'pp');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
