-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mer. 01 fév. 2023 à 14:32
-- Version du serveur :  8.0.27
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `bibyaso`
--

-- --------------------------------------------------------

--
-- Structure de la table `ajouterdesadherents`
--

DROP TABLE IF EXISTS `ajouterdesadherents`;
CREATE TABLE IF NOT EXISTS `ajouterdesadherents` (
  `idAdherent` int NOT NULL AUTO_INCREMENT,
  `nomAdherent` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `prenomAdherent` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `codepostalAdherent` int NOT NULL,
  `villeAdherent` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`idAdherent`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `ajouterdesadherents`
--

INSERT INTO `ajouterdesadherents` (`idAdherent`, `nomAdherent`, `prenomAdherent`, `codepostalAdherent`, `villeAdherent`) VALUES
(1, 'Zaion', 'Sofiane', 92230, 'Gennevilliers'),
(2, 'AIT ALLA', 'Yassine', 92700, 'Colombes');

-- --------------------------------------------------------

--
-- Structure de la table `ajouterdeslivres`
--

DROP TABLE IF EXISTS `ajouterdeslivres`;
CREATE TABLE IF NOT EXISTS `ajouterdeslivres` (
  `idLivre` int NOT NULL AUTO_INCREMENT,
  `TitreLivre` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `Auteurs` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `Collections` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `Editeurs` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `Etat` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`idLivre`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `ajouterdeslivres`
--

INSERT INTO `ajouterdeslivres` (`idLivre`, `TitreLivre`, `Auteurs`, `Collections`, `Editeurs`, `Etat`) VALUES
(1, 'Miserables', 'Victor hugo', 'Yass', 'Laffont', 'Disponible'),
(2, 'Corbeau et le renard ', 'Jean de la fontaine', 'Yass', 'Laffont', 'Emprunter'),
(3, 'Le malade imaginaire', 'Moliere', 'Yass', 'Laffont', 'Emprunter');

-- --------------------------------------------------------

--
-- Structure de la table `comptes`
--

DROP TABLE IF EXISTS `comptes`;
CREATE TABLE IF NOT EXISTS `comptes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `prenom` varchar(100) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `telephone` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `question` varchar(100) NOT NULL,
  `reponse` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `comptes`
--

INSERT INTO `comptes` (`id`, `prenom`, `nom`, `telephone`, `email`, `question`, `reponse`, `password`) VALUES
(1, 'yassine', 'aitalla', '0620202020', 'yassine.aitalla@gmail.com', 'ton prenom', 'yassine', 'YSS/@AIT?+SA%$?'),
(2, 'Zaion', 'Sofiane', '0630303030', 'Sofiane.zaion@gmail.com', 'ton prenom', 'sofiane', 'Sof@10/???/'),
(3, 'Jean', 'delafontaine', '06.40.40.40.40', 'Jeandelafontaine@gmail.com', 'ton prenom', 'Jean', 'Jean@20?//%');

-- --------------------------------------------------------

--
-- Structure de la table `emprunterdeslivres`
--

DROP TABLE IF EXISTS `emprunterdeslivres`;
CREATE TABLE IF NOT EXISTS `emprunterdeslivres` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nomAdherent` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `titreLivre` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `dateEmprunt` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `dateRetour` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=101 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `emprunterdeslivres`
--

INSERT INTO `emprunterdeslivres` (`id`, `nomAdherent`, `titreLivre`, `dateEmprunt`, `dateRetour`) VALUES
(100, 'Zaion', 'Le malade imaginaire', '01/02/23', '24/02/23'),
(99, 'Aitalla', 'Corbeau et le renard ', '02/02/23', '24/02/23');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
