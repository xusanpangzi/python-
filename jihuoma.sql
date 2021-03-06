-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: localhost    Database: python
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `jihuoma`
--

DROP TABLE IF EXISTS `jihuoma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `jihuoma` (
  `t` int(3) NOT NULL,
  `number` char(10) NOT NULL,
  PRIMARY KEY (`t`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jihuoma`
--

LOCK TABLES `jihuoma` WRITE;
/*!40000 ALTER TABLE `jihuoma` DISABLE KEYS */;
INSERT INTO `jihuoma` VALUES (1,'HA5148'),(2,'ei6874'),(3,'eC0345'),(4,'RZ8008'),(5,'oz9067'),(6,'yH6688'),(7,'aZ4267'),(8,'Ne9527'),(9,'Eb6215'),(10,'vj9255'),(11,'jj1837'),(12,'bL9012'),(13,'sD2694'),(14,'lp7256'),(15,'tA1818'),(16,'fb3210'),(17,'JW4135'),(18,'bG8890'),(19,'WX3989'),(20,'VH8366'),(21,'Ta9445'),(22,'gg9592'),(23,'dW4354'),(24,'BR8226'),(25,'ed8537'),(26,'el0996'),(27,'Zt9848'),(28,'mY9022'),(29,'GW2942'),(30,'cq5679'),(31,'Mb3153'),(32,'MA5908'),(33,'VJ7248'),(34,'NX2858'),(35,'uj8852'),(36,'YT0810'),(37,'bf8125'),(38,'nr4939'),(39,'vw3314'),(40,'Un7404'),(41,'Yq5637'),(42,'zy8757'),(43,'Jf3988'),(44,'WJ4629'),(45,'ZM5762'),(46,'dv9878'),(47,'Hz5810'),(48,'le8324'),(49,'Zn4336'),(50,'vP8298'),(51,'bj9213'),(52,'hh7359'),(53,'TE1233'),(54,'oX8705'),(55,'gM2345'),(56,'YM9903'),(57,'Ck4047'),(58,'sB8126'),(59,'QK2701'),(60,'pA0662'),(61,'OR1083'),(62,'cj3028'),(63,'dB4911'),(64,'bE6312'),(65,'LH3556'),(66,'be9294'),(67,'PX2814'),(68,'IZ4424'),(69,'WD2972'),(70,'iF5011'),(71,'yB7880'),(72,'cc1693'),(73,'Rj0038'),(74,'MX3581'),(75,'Rg2912'),(76,'Bx2829'),(77,'LH8456'),(78,'zM9141'),(79,'In0754'),(80,'nd2424'),(81,'Tw2360'),(82,'vj2143'),(83,'ZX8112'),(84,'Rr1507'),(85,'ne8596'),(86,'fY3314'),(87,'dW1481'),(88,'wT1421'),(89,'ES0101'),(90,'IP1828'),(91,'fE7579'),(92,'xc4626'),(93,'Iq1884'),(94,'Kf9713'),(95,'jx2696'),(96,'sc9527'),(97,'sB4874'),(98,'aC5723'),(99,'Xz1312'),(100,'es5256'),(101,'bc6562'),(102,'rt2710'),(103,'Hf7680'),(104,'wy5517'),(105,'eb3131'),(106,'nT5961'),(107,'kx9967'),(108,'fD5070'),(109,'iU3325'),(110,'qr8362'),(111,'TY9611'),(112,'YN4461'),(113,'cE5543'),(114,'Vy6022'),(115,'cW0963'),(116,'Qh8353'),(117,'hB8029'),(118,'pA8857'),(119,'XT7833'),(120,'wF5238'),(121,'jS3111'),(122,'PN4670'),(123,'SI8387'),(124,'OW0971'),(125,'Sb4431'),(126,'li2880'),(127,'Ai5577'),(128,'Qe0499'),(129,'YZ0301'),(130,'oz5909'),(131,'Vb8372'),(132,'zs3694'),(133,'Fv4359'),(134,'Ze4328'),(135,'yl7264'),(136,'kU8106'),(137,'Hq6412'),(138,'Dt8796'),(139,'Vb2696'),(140,'hv1685'),(141,'OL2573'),(142,'Ye8515'),(143,'PF3456'),(144,'by7819'),(145,'fN6886'),(146,'Oc6223'),(147,'Lf5661'),(148,'Xr8674'),(149,'nd7855'),(150,'AT0739'),(151,'eo3993'),(152,'AR0695'),(153,'sO0857'),(154,'Hj9891'),(155,'vH3616'),(156,'yQ3208'),(157,'re9517'),(158,'cM5198'),(159,'xK5965'),(160,'dw8507'),(161,'bK0960'),(162,'kX7377'),(163,'xi8466'),(164,'Qc0783'),(165,'Tf8287'),(166,'kw8326'),(167,'ym1469'),(168,'Rc3869'),(169,'oe8376'),(170,'xd6191'),(171,'gc7837'),(172,'nc3760'),(173,'gv6371'),(174,'Ni0496'),(175,'UX4908'),(176,'gZ3159'),(177,'SG9894'),(178,'Yx4927'),(179,'PT1604'),(180,'ym3357'),(181,'de4961'),(182,'FW2220'),(183,'Re1064'),(184,'TK4287'),(185,'lr9824'),(186,'go5528'),(187,'sx7589'),(188,'iX7188'),(189,'SE4932'),(190,'lf8436'),(191,'xW8508'),(192,'KX8390'),(193,'Ki2651'),(194,'ew4213'),(195,'FI6039'),(196,'ed0713'),(197,'ZF9028'),(198,'bg2019'),(199,'cv8666'),(200,'Nd0101');
/*!40000 ALTER TABLE `jihuoma` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-13 19:04:56
