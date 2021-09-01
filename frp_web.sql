/*
 Navicat Premium Data Transfer

 Source Server         : 本机
 Source Server Type    : MySQL
 Source Server Version : 50725
 Source Host           : localhost:3306
 Source Schema         : frp_web

 Target Server Type    : MySQL
 Target Server Version : 50725
 File Encoding         : 65001

 Date: 01/09/2021 15:13:45
*/
CREATE DATABASE `frp_web` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci';
use frp_web;
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for frp_config
-- ----------------------------
DROP TABLE IF EXISTS `frp_config`;
CREATE TABLE `frp_config`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '映射名字',
  `local_port` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '内网端口',
  `local_ip` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '内网IP',
  `remote_port` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '远程端口',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of frp_config
-- ----------------------------

-- ----------------------------
-- Table structure for frp_server
-- ----------------------------
DROP TABLE IF EXISTS `frp_server`;
CREATE TABLE `frp_server`  (
  `server_ip` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `server_port` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `remarks` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = 'frp 服务器地址' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of frp_server
-- ----------------------------
INSERT INTO `frp_server` VALUES ('47.96.113.252', '37000', '远程服务器地址47.96.113.252 请设置远程端口范围50000-59999');

SET FOREIGN_KEY_CHECKS = 1;
