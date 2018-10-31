/*
Navicat MySQL Data Transfer

Source Server         : 103.44.61.204_3306
Source Server Version : 50173
Source Host           : 68.168.143.194:3306
Source Database       : notes

Target Server Type    : MYSQL
Target Server Version : 50173
File Encoding         : 65001

Date: 2018-08-14 11:16:39
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `USERNAME` varchar(8) NOT NULL DEFAULT '',
  `PASSWORD` varchar(12) NOT NULL,
  `HEADPORTRAIT` varchar(255) DEFAULT NULL,
  `ADDTIME` date DEFAULT NULL,
  `EDITTIME` date DEFAULT NULL,
  PRIMARY KEY (`USERNAME`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('nmgwap', 'nmgwap', '', '2018-07-26', '2018-07-26');
INSERT INTO `user` VALUES ('zhuxingm', '123456', '', '2018-07-26', '2018-07-26');
