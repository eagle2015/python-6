-- MySQL dump 10.13  Distrib 5.1.73, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: cmdb_v10
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
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COMMENT='机柜表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cabinet`
--

LOCK TABLES `cabinet` WRITE;
/*!40000 ALTER TABLE `cabinet` DISABLE KEYS */;
INSERT INTO `cabinet` VALUES (8,'F01',12,'42U','220V'),(12,'F03',13,'42u','220V'),(13,'F02',12,'42U','220V'),(14,'F04',12,'42U','220V'),(15,'F05',12,'42U','220V'),(16,'F06',9,'42U','220V'),(17,'F07',13,'42U','220V');
/*!40000 ALTER TABLE `cabinet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dns_records`
--

DROP TABLE IF EXISTS `dns_records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dns_records` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `zone` varchar(255) NOT NULL,
  `host` varchar(255) NOT NULL DEFAULT '@',
  `type` enum('A','MX','CNAME','NS','SOA','PTR','TXT','AAAA','SVR','URL') NOT NULL,
  `data` varchar(255) DEFAULT NULL,
  `ttl` int(11) NOT NULL DEFAULT '3600',
  `mx_priority` int(11) DEFAULT NULL,
  `view` enum('any','Telecom','Unicom','CMCC','ours') NOT NULL DEFAULT 'any',
  `priority` tinyint(3) unsigned NOT NULL DEFAULT '255',
  `refresh` int(11) NOT NULL DEFAULT '28800',
  `retry` int(11) NOT NULL DEFAULT '14400',
  `expire` int(11) NOT NULL DEFAULT '86400',
  `minimum` int(11) NOT NULL DEFAULT '86400',
  `serial` bigint(20) NOT NULL DEFAULT '2015050917',
  `resp_person` varchar(64) NOT NULL DEFAULT 'ddns.net',
  `primary_ns` varchar(64) NOT NULL DEFAULT 'ns.ddns.net.',
  PRIMARY KEY (`id`),
  KEY `type` (`type`),
  KEY `host` (`host`),
  KEY `zone` (`zone`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dns_records`
--

LOCK TABLES `dns_records` WRITE;
/*!40000 ALTER TABLE `dns_records` DISABLE KEYS */;
INSERT INTO `dns_records` VALUES (21,'test.info','w','CNAME','www',60,NULL,'any',255,28800,14400,86400,86400,2015050917,'ddns.net','ns.ddns.net.'),(23,'test.info','www','A','3.3.3.3',60,NULL,'any',255,28800,14400,86400,86400,2015050917,'ddns.net','ns.ddns.net.'),(22,'test.info','www','A','1.1.1.1',60,NULL,'any',255,28800,14400,86400,86400,2015050917,'ddns.net','ns.ddns.net.');
/*!40000 ALTER TABLE `dns_records` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COMMENT='机房表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `idc`
--

LOCK TABLES `idc` WRITE;
/*!40000 ALTER TABLE `idc` DISABLE KEYS */;
INSERT INTO `idc` VALUES (9,'shanghai','上海机房','上海','eagle','1234578'),(12,'dongguan','东莞','东莞樟木头','汤米','12345671'),(13,'feizhou','坦桑尼亚','坦桑尼亚','塔米','1234567'),(14,'beijing','北京机房','北京','老田','1234568');
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
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job`
--

LOCK TABLES `job` WRITE;
/*!40000 ALTER TABLE `job` DISABLE KEYS */;
INSERT INTO `job` VALUES (61,'ll','ll',1,'mysql','处理完毕',2,'2017-09-15 11:54:07','2017-09-15 12:30:46'),(62,'ll','ll',2,'请帮忙配置个 PHP 环境',NULL,1,'2017-09-15 12:21:10','2017-09-15 12:30:36'),(63,'ll','ll',1,'增加数据库','处理完成',2,'2017-09-15 12:30:28','2017-09-15 13:40:34'),(64,'ll','ll',1,'添加数据库服务器','服务器已经添加',2,'2017-09-15 13:10:27','2017-09-15 13:10:45'),(65,'ll','ll',0,'asdfasd','完成',2,'2017-09-15 13:40:17','2017-09-15 13:45:19'),(66,'eagle','feiying',1,'配置数据库',NULL,1,'2017-09-26 06:44:06','2017-09-26 08:15:14'),(67,'eagle',NULL,0,'添加新用户，test',NULL,0,'2017-09-26 06:47:18','2017-09-26 06:47:18');
/*!40000 ALTER TABLE `job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `memory`
--

DROP TABLE IF EXISTS `memory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `memory` (
  `memory` int(11) DEFAULT NULL,
  `time` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `memory`
--

LOCK TABLES `memory` WRITE;
/*!40000 ALTER TABLE `memory` DISABLE KEYS */;
INSERT INTO `memory` VALUES (1837,1506498821),(1837,1506498831),(1837,1506498841);
/*!40000 ALTER TABLE `memory` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `server`
--

LOCK TABLES `server` WRITE;
/*!40000 ALTER TABLE `server` DISABLE KEYS */;
INSERT INTO `server` VALUES (61,'192.168.8.114','180.169.17.14','111111111111','root','1234561',22,12,'DELL','1','128g','40T','CentOs_6.5 X64','001',15),(62,'192.168.8.115','180.169.17.115','1111','root','123456',22,12,'DELL','1','128g','40T','CentOs_6.5 X64','002',8),(65,'192.168.8.117','192.168.8.117','11111111111','root','123456',22,12,'DELL','1','128g','500G','CentOs_6.5 X64','007',12),(66,'192.168.8.116','192.168.8.116','11111111','root','123456',22,9,'DELL','4','128G','500G','CentOs_6.5 X64','005',13),(67,'192.168.8.118','192.168.8.118','111111111111111','root','123456',22,9,'DELL','4颗','128G','500G','CentOs_7.1_X64','008',8);
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
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (61,'pc','pc','123456','110','11111111110@qq.com',1,0),(71,'demo','demo','123456','112233','11111112@qq.com',1,0),(74,'令狐冲','令狐','123456','1234511','1ghuchong@163.com',1,0),(76,'老王','laowang','123456','187*****346','110@qq.com',1,0),(77,'feiying','feiying','123456','112233','112@qq.com',0,0),(78,'laotao','laotao','123456','13725578065','112@qq.com',1,0),(79,'tami','tami','123456','13725578065','110@qq.com',1,0),(80,'feilong','飞龙','1234561','112233','112@qq.com',1,0),(81,'meichaofeng','梅超风','123456','112233','112@qq.com',1,0),(82,'yangguo','杨过','123456','232','112@qq.com',1,0),(83,'eagle','eagle','123456','112233','1@qq.com',0,0),(86,'llllll','demo','123456','13725578061','112@qq.com',0,0);
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

-- Dump completed on 2017-10-17 14:56:35
