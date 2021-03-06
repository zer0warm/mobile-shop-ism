DROP TABLE IF EXISTS Phones;

CREATE TABLE Phones (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	brand TEXT NOT NULL,
	name TEXT NOT NULL,
	color TEXT NOT NULL,
	storage INTEGER NOT NULL,
	price INTEGER NOT NULL,
	qty INTEGER NOT NULL
);


INSERT INTO Phones VALUES
	(1, "Apple", "Iphone XR", "Black", "64GB", 12490000, 100),
	(2, "Apple", "Iphone XR", "Red", "64GB", 12490000, 100),
	(3, "Apple", "Iphone XR", "Black ", "128GB", 16490000, 100),
	(4, "Apple", "Iphone XR", "Red", "128GB", 16490000, 100),
	(5, "Apple", "Iphone 12", "Green", "64GB", 20990000, 100),
	(6, "Apple", "Iphone 12", "White", "64GB", 20990000, 100),
	(7, "Apple", "Iphone 12", "Black", "64GB", 20990000, 100),
	(8, "Apple", "Iphone 12", "Blue", "64GB", 20990000, 100),
	(9, "Apple", "Iphone 12", "Red", "64GB", 20990000, 100),
	(10, "Apple", "Iphone 12", "Purple", "64GB", 20990000, 100),
	(11, "Apple", "Iphone 12", "Green", "128GB", 22990000, 100),
	(12, "Apple", "Iphone 12", "White", "128GB", 22990000, 100),
	(13, "Apple", "Iphone 12", "Black", "128GB", 22990000, 100),
	(14, "Apple", "Iphone 12", "Blue", "128GB", 22990000, 100),
	(15, "Apple", "Iphone 12", "Red", "128GB", 22990000, 100),
	(16, "Apple", "Iphone 12", "Purple", "128GB", 22990000, 100),
	(17, "Apple", "Iphone 12", "Green", "256GB", 24490000, 100),
	(18, "Apple", "Iphone 12", "White", "256GB", 24490000, 100),
	(19, "Apple", "Iphone 12", "Black", "256GB", 24490000, 100),
	(20, "Apple", "Iphone 12", "Blue", "256GB", 24490000, 100),
	(21, "Apple", "Iphone 12", "Red", "256GB", 24490000, 100),
	(22, "Apple", "Iphone 12", "Purple", "256GB", 24490000, 100),
	(23, "Apple", "Iphone SE", "Red", "64GB", 10990000, 100),
	(24, "Apple", "Iphone SE", "White", "64GB", 10990000, 100),
	(25, "Apple", "Iphone SE", "Black", "64GB", 10990000, 100),
	(26, "Oppo", "OPPO A94", "Grey", "128GB", 7690000, 100),
	(27, "Oppo", "OPPO A94", "Black", "128GB", 7690000, 100),
	(28, "Oppo", "OPPO A94", "Purple", "128GB", 7690000, 100),
	(29, "Oppo", "OPPO Reno4", "Purple", "128GB", 6490000, 100),
	(30, "Oppo", "OPPO Reno4", "Green", "128GB", 6490000, 100),
	(31, "Oppo", "OPPO Reno4", "Black", "128GB", 6490000, 100),
	(32, "Oppo", "OPPO Reno5", "Grey ", "128GB", 8690000, 100),
	(33, "Oppo", "OPPO Reno5", "Black", "128GB", 8690000, 100),
	(34, "Oppo", "OPPO Reno5", "Grey", "128GB", 11990000, 100),
	(35, "Oppo", "OPPO Reno5", "Black", "128GB", 11990000, 100),
	(36, "Vinsmart", "Vsmart Aris", "Grey", "64GB", 5090000, 100),
	(37, "Vinsmart", "Vsmart Aris", "Emerald", "64GB", 5090000, 100),
	(38, "Vinsmart", "Vsmart Aris", "Blue", "64GB", 5090000, 100),
	(39, "Vinsmart", "Vsmart Aris", "Grey", "128GB", 5490000, 100),
	(40, "Vinsmart", "Vsmart Aris", "Emerald", "128GB", 5490000, 100),
	(41, "Vinsmart", "Vsmart Aris", "Blue", "128GB", 5490000, 100),
	(42, "Vinsmart", "Vsmart Active", "Black", "64GB", 3990000, 100),
	(43, "Vinsmart", "Vsmart Active", "Green", "64GB", 3990000, 100),
	(44, "Vinsmart", "Vsmart Active", "Purple", "64GB", 3990000, 100),
	(45, "Vinsmart", "Vsmart Active", "Green", "64GB", 3990000, 100),
	(46, "Vinsmart", "Vsmart Live", "Black", "64GB", 4290000, 100),
	(47, "Vinsmart", "Vsmart Live", "Green", "64GB", 4290000, 100),
	(48, "Vinsmart", "Vsmart Live", "White", "64GB", 4290000, 100),
	(49, "Nokia", "Nokia 5.4", "Green", "128GB", 3290000, 100),
	(50, "Nokia", "Nokia 5.4", "Purple", "128GB", 3290000, 100),
	(51, "Nokia", "Nokia C20", "Green", "32GB", 2290000, 100),
	(52, "Nokia", "Nokia C20", "Yellow", "32GB", 2290000, 100),
	(53, "Nokia", "Nokia 6300", "Black", "4GB", 1129000, 100),
	(54, "Nokia", "Nokia 6300", "White", "4GB", 1129000, 100),
	(55, "Vivo", "Vivo Y20", "Green ", "64GB", 3690000, 100),
	(56, "Vivo", "Vivo Y20", "White", "64GB", 3690000, 100),
	(57, "Xiaomi", "Xiaomi Redmi Note 9", "Grey ", "128GB", 4490000, 100),
	(58, "Xiaomi", "Xiaomi Redmi Note 9", "Green", "128GB", 4490000, 100),
	(59, "Xiaomi", "Xiaomi Redmi Note 9", "Black", "128GB", 4490000, 100),
	(60, "Xiaomi", "Xiaomi Redmi Note 9", "White", "128GB", 4490000, 100),
	(61, "Xiaomi", "Xiaomi Redmi 9C", "Grey", "64GB", 2690000, 100),
	(62, "Xiaomi", "Xiaomi Redmi 9C", "Orange", "64GB", 2690000, 100),
	(63, "Xiaomi", "Xiaomi Redmi 9C", "Green", "64GB", 2690000, 100),
	(64, "Xiaomi", "Xiaomi Redmi Note 10 Pro", "Grey", "128GB", 6990000, 100),
	(65, "Xiaomi", "Xiaomi Redmi Note 10 Pro", "Yellow", "128GB", 6990000, 100),
	(66, "Xiaomi", "Xiaomi Redmi Note 10 Pro", "Green", "128GB", 6990000, 100),
	(67, "Xiaomi", "Xiaomi Redmi Note 10 Pro", "Grey", "128GB", 7490000, 100),
	(68, "Xiaomi", "Xiaomi Redmi Note 10 Pro", "Yellow", "128GB", 7490000, 100),
	(69, "Xiaomi", "Xiaomi Redmi Note 10 Pro", "Green", "128GB", 7490000, 100),
	(70, "Samsung", "Samsung Galaxy Z Fold2 5G", "Mystic Bronze", "256GB", 50000000, 100),
	(71, "Samsung", "Samsung Galaxy Z Fold2 5G", "Mystic Black", "256GB", 50000000, 100),
	(72, "Samsung", "Samsung Galaxy S21 Ultra", "Black", "128GB", 30990000, 100),
	(73, "Samsung", "Samsung Galaxy S21 Ultra", "Silver", "128GB", 30990000, 100),
	(74, "Samsung", "Samsung Galaxy S21 Ultra", "Black", "256GB", 33990000, 100),
	(75, "Samsung", "Samsung Galaxy S21 Ultra", "Silver", "256GB", 33990000, 100),
	(76, "Samsung", "Samsung Galaxy S21+", "Silver", "128GB", 25990000, 100),
	(77, "Samsung", "Samsung Galaxy S21+", "Black", "128GB", 25990000, 100),
	(78, "Samsung", "Samsung Galaxy S21+", "Purple", "128GB", 25990000, 100),
	(79, "Samsung", "Samsung Galaxy S21+", "Silver", "256GB", 28990000, 100),
	(80, "Samsung", "Samsung Galaxy S21+", "Black", "256GB", 28990000, 100),
	(81, "Samsung", "Samsung Galaxy S21+", "Purple", "256GB", 28990000, 100),
	(82, "Samsung", "Samsung Galaxy A72", "Green", "256GB", 11490000, 100),
	(83, "Samsung", "Samsung Galaxy A72", "Black", "256GB", 11490000, 100),
	(84, "Samsung", "Samsung Galaxy A72", "Purple", "256GB", 11490000, 100),
	(85, "Samsung", "Samsung Galaxy A72", "White", "256GB", 11490000, 100),
	(86, "Realme", "Realme 8", "Grey", "128GB", 7290000, 100),
	(87, "Realme", "Realme 8", "Black", "128GB", 7290000, 100),
	(88, "Realme", "Realme C17", "Green", "128GB", 5290000, 100),
	(89, "Realme", "Realme C17", "Green Navy", "128GB", 5290000, 100),
	(90, "Realme", "Realme 7i", "Blue", "128GB", 6290000, 100),
	(91, "Realme", "Realme 7i", "Green", "128GB", 6290000, 100),
	(92, "Huawei", "Huawei Y6p", "Black", "64GB", 3490000, 100),
	(93, "Huawei", "Huawei Y6p", "Purple", "64GB", 3490000, 100),
	(94, "Huawei", "Huawei Y6p", "Green", "64GB", 3490000, 100),
	(95, "OnePlus", "OnePlus Nord N10", "Black", "128GB", 7990000, 100),
	(96, "Mastel", "Mastel Hapi 10 Fami", "Yellow", "16GB", 1190000, 100),
	(97, "Mastel", "Mastel Hapi 10 Fami", "Green Navy", "16GB", 1190000, 100),
	(98, "Mastel", "Mastel Hapi 10 Fami", "Black", "16GB", 1190000, 100),
	(99, "Mobell", "Mobell P41", "Black", "8GB", 990000, 100),
	(100, "Mobell", "Mobell P41", "Red", "8GB", 990000, 100),
	(101, "Mobell", "Mobell P41", "Yellow", "8GB", 990000, 100),
	(102, "Xiaomi", "Xiaomi Redmi 9T", "Blue", "64GB", 3990000, 100),
	(103, "Xiaomi", "Xiaomi Redmi 9T", "Orange", "64GB", 3990000, 100),
	(104, "Xiaomi", "Xiaomi Redmi 9T", "Black", "64GB", 3990000, 100),
	(105, "Xiaomi", "Xiaomi Redmi 9T", "Green", "64GB", 3990000, 100),
	(106, "Xiaomi", "Xiaomi Poco X3", "Grey", "64GB", 6690000, 100),
	(107, "Xiaomi", "Xiaomi Poco X3", "Green", "64GB", 6690000, 100),
	(108, "Xiaomi", "Xiaomi Poco X3", "Grey", "128GB", 6990000, 100),
	(109, "Xiaomi", "Xiaomi Poco X3", "Green", "128GB", 6990000, 100),
	(110, "Samsung", "Samsung Galazy Z Flip", "Purple", "256GB", 36000000, 100),
	(111, "Samsung", "Samsung Galazy Z Flip", "Yellow", "256GB", 36000000, 100),
	(112, "Samsung", "Samsung Galazy Z Flip", "Black", "256GB", 36000000, 100),
	(113, "Apple", "Iphone 11", "Purple", "64GB", 18800000, 100),
	(114, "Apple", "Iphone 11", "White", "64GB", 18800000, 100),
	(115, "Apple", "Iphone 11", "Yellow", "64GB", 18800000, 100),
	(116, "Apple", "Iphone 11", "Green", "64GB", 18800000, 100),
	(117, "Apple", "Iphone 11", "Black", "64GB", 18800000, 100),
	(118, "Apple", "Iphone 11", "Red", "64GB", 18800000, 100),
	(119, "Apple", "Iphone 11", "Purple", "128GB", 19900000, 100),
	(120, "Apple", "Iphone 11", "White", "128GB", 19900000, 100),
	(121, "Apple", "Iphone 11", "Yellow", "128GB", 19900000, 100),
	(122, "Apple", "Iphone 11", "Green", "128GB", 19900000, 100),
	(123, "Apple", "Iphone 11", "Black", "128GB", 19900000, 100),
	(124, "Apple", "Iphone 11", "Red", "128GB", 19900000, 100),
	(125, "Apple", "Iphone 11", "Purple", "256GB", 22000000, 100),
	(126, "Apple", "Iphone 11", "White", "256GB", 22000000, 100),
	(127, "Apple", "Iphone 11", "Yellow", "256GB", 22000000, 100),
	(128, "Apple", "Iphone 11", "Green", "256GB", 22000000, 100),
	(129, "Apple", "Iphone 11", "Black", "256GB", 22000000, 100),
	(130, "Apple", "Iphone 11", "Red", "256GB", 22000000, 100),
	(131, "Nokia", "Nokia 2.4", "Purple", "32GB", 2690000, 100),
	(132, "Nokia", "Nokia 2.4", "Grey", "32GB", 2690000, 100),
	(133, "Nokia", "Nokia 2.4", "Green", "32GB", 2690000, 100);
