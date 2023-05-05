-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : jeu. 04 mai 2023 à 14:19
-- Version du serveur : 10.4.25-MariaDB
-- Version de PHP : 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `pfa`
--

-- --------------------------------------------------------

--
-- Structure de la table `categories`
--

CREATE TABLE `categories` (
  `id_categorie` int(11) NOT NULL,
  `nomCat` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `categories`
--

INSERT INTO `categories` (`id_categorie`, `nomCat`) VALUES
(1, 'phone'),
(2, 'PC'),
(3, 'Camera');

-- --------------------------------------------------------

--
-- Structure de la table `client`
--

CREATE TABLE `client` (
  `idC` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) NOT NULL,
  `tel` varchar(255) DEFAULT NULL,
  `mail` varchar(255) NOT NULL,
  `adresse` varchar(255) NOT NULL,
  `dateN` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `client`
--

INSERT INTO `client` (`idC`, `nom`, `prenom`, `tel`, `mail`, `adresse`, `dateN`) VALUES
(1, 'HAKMAOUI', 'Ayoub', '0678365421', 'test@gmail.com', 'Marrakech, 1298', '2001-01-16'),
(2, 'Anassi', 'morad', '0638475639', 'test2@gmail.com', 'agadir, 1346', '1999-04-29'),
(3, 'tablioua', 'EL-habib', '0678654673', 'test3@gmail.com', 'mhamid, 345', '2002-04-29'),
(4, 'aboufariss', 'aida', '0678345678', 'test4@gmail.com', 'asafi, 567', '0000-00-00'),
(5, 'alaoui', 'hassan', '0678654576', 'test5@gmail.com', 'maroc, 456', '2000-01-03'),
(7, 'amrani', 'soulaymane', '0675643998', 'soul@gmail.com', 'tanger,9087', '1998-01-01'),
(8, 'kabaj', 'amal', '066156534', 'amal@gmail.com', 'sale, lbarj 456', '0000-00-00'),
(10, 'hasnaoui', 'siham', '0654576530', 'siham@gmail.com', 'meknas, 654', '2004-03-08');

-- --------------------------------------------------------

--
-- Structure de la table `compte`
--

CREATE TABLE `compte` (
  `idCo` int(11) NOT NULL,
  `nom_utilisateur` varchar(255) NOT NULL,
  `mdp` varchar(255) NOT NULL,
  `user_connecter` varchar(255) DEFAULT 'non'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `compte`
--

INSERT INTO `compte` (`idCo`, `nom_utilisateur`, `mdp`, `user_connecter`) VALUES
(1, 'hakmaoui', '1234', 'non'),
(13, 'ayoub', '1234', 'non'),
(14, 'habib', '1234', 'non'),
(15, 'test4', '1234', 'non'),
(16, 'aida', '$2b$12$kAFF9rVDY8YjZiDEYmbl0.oyA2sCnvDmTFlOnZZFuDkv5izbFCPUS', 'non'),
(17, 'hakmaoui ayoub', '$2b$12$L8EAD47IGysKhVWWB92iB.foSOQgXLRBFFvkrEiy0yTERRBHs0PQG', 'non');

-- --------------------------------------------------------

--
-- Structure de la table `details_commande`
--

CREATE TABLE `details_commande` (
  `IDcommande` int(12) NOT NULL,
  `datecommand` date NOT NULL,
  `nomClient` varchar(255) NOT NULL,
  `produit` varchar(255) NOT NULL,
  `QtiteProd` int(11) NOT NULL,
  `Remise` float NOT NULL,
  `TVA` float NOT NULL,
  `TOTAL_TH` float NOT NULL,
  `TOTAL_TTC` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `details_commande`
--

INSERT INTO `details_commande` (`IDcommande`, `datecommand`, `nomClient`, `produit`, `QtiteProd`, `Remise`, `TVA`, `TOTAL_TH`, `TOTAL_TTC`) VALUES
(2, '2023-01-01', 'HAKMAOUI', 'hp', 3, 10, 20, 12028.5, 14722.9),
(4, '2000-01-01', 'HAKMAOUI', 'lenovo', 2, 5, 10, 9500, 10554.5);

-- --------------------------------------------------------

--
-- Structure de la table `fornisseur`
--

CREATE TABLE `fornisseur` (
  `CodePostalFornisseur` int(11) NOT NULL,
  `NomFornisseur` varchar(30) DEFAULT NULL,
  `VilleFornisseur` varchar(20) DEFAULT NULL,
  `TeleFornisseur` int(11) DEFAULT NULL,
  `EmailFornisseur` varchar(100) DEFAULT NULL,
  `AdresseFornisseur` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `fornisseur`
--

INSERT INTO `fornisseur` (`CodePostalFornisseur`, `NomFornisseur`, `VilleFornisseur`, `TeleFornisseur`, `EmailFornisseur`, `AdresseFornisseur`) VALUES
(3989, 'omar dabaj', 'Agadir', 767876452, 'omar34@gmail.com', 'Agadir, sokani 343'),
(4000, 'Anas', 'Marrakech', 675443120, 'anas54@gmail.com', 'Marrakech, Azli'),
(5000, 'amal', 'Rabat', 767563547, 'amal43@gmail.com', 'Rabat, Agdal 454');

-- --------------------------------------------------------

--
-- Structure de la table `produits`
--

CREATE TABLE `produits` (
  `idp` int(11) NOT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `prix_unitaire` float DEFAULT NULL,
  `quantite_en_stock` int(11) DEFAULT NULL,
  `seuil_alerte_stock` int(11) DEFAULT NULL,
  `date_derniere_entree_stock` date DEFAULT NULL,
  `date_derniere_sortie_stock` date DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `id_categorie` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `produits`
--

INSERT INTO `produits` (`idp`, `nom`, `description`, `prix_unitaire`, `quantite_en_stock`, `seuil_alerte_stock`, `date_derniere_entree_stock`, `date_derniere_sortie_stock`, `image`, `id_categorie`) VALUES
(1, 'hp', 'pc bon etat', 4500, 20, 5, '0000-00-00', '0000-00-00', '', 1),
(2, 'lenovo', 'pc bon etat', 5000, 25, 5, '0000-00-00', '0000-00-00', '', 1);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id_categorie`);

--
-- Index pour la table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`idC`);

--
-- Index pour la table `compte`
--
ALTER TABLE `compte`
  ADD PRIMARY KEY (`idCo`);

--
-- Index pour la table `details_commande`
--
ALTER TABLE `details_commande`
  ADD PRIMARY KEY (`IDcommande`);

--
-- Index pour la table `fornisseur`
--
ALTER TABLE `fornisseur`
  ADD PRIMARY KEY (`CodePostalFornisseur`);

--
-- Index pour la table `produits`
--
ALTER TABLE `produits`
  ADD PRIMARY KEY (`idp`),
  ADD KEY `id_categorie` (`id_categorie`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `client`
--
ALTER TABLE `client`
  MODIFY `idC` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT pour la table `compte`
--
ALTER TABLE `compte`
  MODIFY `idCo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT pour la table `details_commande`
--
ALTER TABLE `details_commande`
  MODIFY `IDcommande` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2024;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `produits`
--
ALTER TABLE `produits`
  ADD CONSTRAINT `produits_ibfk_1` FOREIGN KEY (`id_categorie`) REFERENCES `categories` (`id_categorie`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
