-- MySQL dump 10.13  Distrib 5.1.73, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: CMDB_v10
-- ------------------------------------------------------
-- Server version	5.6.16-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cabinet`
--

DROP TABLE IF EXISTS `cabinet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cabinet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL COMMENT '机柜名称',
  `idc_id` int(11) DEFAULT NULL COMMENT '所在机房ID',
  `u_num` varchar(10) DEFAULT NULL COMMENT 'U位',
  `power` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COMMENT='机柜表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cabinet`
--

LOCK TABLES `cabinet` WRITE;
/*!40000 ALTER TABLE `cabinet` DISABLE KEYS */;
INSERT INTO `cabinet` VALUES (8,'F01',9,'4U','220V'),(12,'F03',12,'2u','220V'),(13,'F02',12,'42U','220V'),(14,'F04',12,'42U','220V');
/*!40000 ALTER TABLE `cabinet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `idc`
--

DROP TABLE IF EXISTS `idc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `idc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL COMMENT '机房英文简写',
  `name_cn` varchar(50) DEFAULT NULL COMMENT '机房中文名',
  `address` varchar(128) DEFAULT NULL COMMENT '机房地址',
  `adminer` varchar(32) DEFAULT NULL COMMENT '机房联系人',
  `phone` varchar(11) DEFAULT NULL COMMENT '联系电话',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COMMENT='机房表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `idc`
--

LOCK TABLES `idc` WRITE;
/*!40000 ALTER TABLE `idc` DISABLE KEYS */;
INSERT INTO `idc` VALUES (9,'shanghai','上海机房','上海','eagle','1234578'),(12,'dongguan','东莞','东莞樟木头','汤米','1231');
/*!40000 ALTER TABLE `idc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job`
--

DROP TABLE IF EXISTS `job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `job` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `apply_name` varchar(255) DEFAULT NULL COMMENT '申请人',
  `handle_name` varchar(255) DEFAULT NULL COMMENT '处理人',
  `apply_type` int(255) DEFAULT NULL COMMENT '类型',
  `apply_desc` varchar(255) DEFAULT NULL COMMENT '申请人描述',
  `handle_desc` varchar(255) DEFAULT NULL COMMENT '处理人描述',
  `status` int(255) DEFAULT '0',
  `created` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `modified` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job`
--

LOCK TABLES `job` WRITE;
/*!40000 ALTER TABLE `job` DISABLE KEYS */;
INSERT INTO `job` VALUES (61,'ll','ll',1,'mysql','处理完毕',2,'2017-09-15 11:54:07','2017-09-15 12:30:46'),(62,'ll','ll',2,'请帮忙配置个 PHP 环境',NULL,1,'2017-09-15 12:21:10','2017-09-15 12:30:36'),(63,'ll',NULL,1,'增加数据库',NULL,0,'2017-09-15 12:30:28','2017-09-15 12:30:28'),(64,'ll','ll',1,'添加数据库服务器','服务器已经添加',2,'2017-09-15 13:10:27','2017-09-15 13:10:45');
/*!40000 ALTER TABLE `job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `server`
--

DROP TABLE IF EXISTS `server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(255) DEFAULT NULL,
  `ip` varchar(255) DEFAULT NULL,
  `mac` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `port` int(255) DEFAULT NULL,
  `idc` int(255) DEFAULT NULL,
  `brand` varchar(255) DEFAULT NULL,
  `cpu` varchar(255) DEFAULT NULL,
  `memory` varchar(255) DEFAULT NULL,
  `disk` varchar(255) DEFAULT NULL,
  `system_type` varchar(255) DEFAULT NULL,
  `number` varchar(255) DEFAULT NULL,
  `cabinet` int(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hostname` (`hostname`),
  UNIQUE KEY `ip` (`ip`),
  UNIQUE KEY `number` (`number`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `server`
--

LOCK TABLES `server` WRITE;
/*!40000 ALTER TABLE `server` DISABLE KEYS */;
INSERT INTO `server` VALUES (61,'192.168.8.114','180.169.17.14','111111111111','root','1234561',22,12,'DELL','1','128g','40T','CentOs_6.5 X64','001',14),(62,'192.168.8.115','180.169.17.115','1111','root','123456',22,12,'DELL','1','128g','40T','CentOs_6.5 X64','002',8),(65,'192.168.8.117','192.168.8.117','11111111111','root','123456',22,12,'DELL','1','128g','500G','CentOs_6.5 X64','007',12),(66,'192.168.8.116','192.168.8.116','11111111','root','123456',22,9,'DELL','4','128G','500G','CentOs_6.5 X64','005',13);
/*!40000 ALTER TABLE `server` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `name_cn` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `mobile` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `role` int(255) DEFAULT NULL,
  `status` int(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (61,'pc','pc','123456','110','11111111110@qq.com',1,0),(62,'ll','ll','1','1211111','11112@qq.com',0,0),(71,'demo','demo','123456','112233','1111112@qq.com',1,0),(74,'令狐冲','令狐','123456','1234511','l1in1ghuchong@163.com',1,0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-09-15 21:19:32
