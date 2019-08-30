create table t_dept(
	id int(7) unsigned,
	name varchar(25) not null , 
	region_id int(7) unsigned ,
	primary key (id),
	unique (name, region_id)
);
	
INSERT INTO t_dept VALUES (
   10, 'Finance', 1);
INSERT INTO t_dept VALUES (
   31, 'Sales', 1);
INSERT INTO t_dept VALUES (
   32, 'Sales', 2);
INSERT INTO t_dept VALUES (
   33, 'Sales', 3);
INSERT INTO t_dept VALUES (
   34, 'Sales', 4);
INSERT INTO t_dept VALUES (
   35, 'Sales', 5);
INSERT INTO t_dept VALUES (
   41, 'Operations', 1);
INSERT INTO t_dept VALUES (
   42, 'Operations', 2);
INSERT INTO t_dept VALUES (
   43, 'Operations', 3);
INSERT INTO t_dept VALUES (
   44, 'Operations', 4);
INSERT INTO t_dept VALUES (
   45, 'Operations', 5);
INSERT INTO t_dept VALUES (
   50, 'Administration', 1);
   
create table t_emp(
1id int(7) unsigned,
last_name varchar(25),
userid varchar(8) unique,
 start_date date,
 comments = varchar(255),
 manager_id int(7) unsigned,
 title varchar(25),
 dept_id = (11,2) unsigned,
 salary decimal(11,2) not noull ,
 primary key(id)
 
 );
 
 
 INSERT INTO t_emp VALUES (
  1, 'Velasquez', 'Carmen', 'cvelasqu',
   '1990-03-03', NULL, NULL, 'President',
   50, 2500, NULL);
INSERT INTO t_emp VALUES (
   2, 'Ngao', 'LaDoris', 'lngao',
   '1990-03-08', NULL, 1, 'VP, Operations',
   41, 1450, NULL);
INSERT INTO t_emp VALUES (
   3, 'Nagayama', 'Midori', 'mnagayam',
   '1991-06-17', NULL, 1, 'VP, Sales',
   31, 1400, NULL);
INSERT INTO t_emp VALUES (
   4, 'Quick-To-See', 'Mark', 'mquickto',
   '1990-04-07', NULL, 1, 'VP, Finance',
   10, 1450, NULL);
INSERT INTO t_emp VALUES (
   5, 'Ropeburn', 'Audry', 'aropebur',
   '1990-03-04', NULL, 1, 'VP, Administration',
   50, 1550, NULL);
INSERT INTO t_emp VALUES (
   6, 'Urguhart', 'Molly', 'murguhar',
   '1991-01-18', NULL, 2, 'Warehouse Manager',
   41, 1200, NULL);
INSERT INTO t_emp VALUES (
   7, 'Menchu', 'Roberta', 'rmenchu',
   '1990-05-14', NULL, 2, 'Warehouse Manager',
   42, 1250, NULL);
INSERT INTO t_emp VALUES (
   8, 'Biri', 'Ben', 'bbiri',
   '1990-04-17', NULL, 2, 'Warehouse Manager',
   43, 1100, NULL);
INSERT INTO t_emp VALUES (
   9, 'Catchpole', 'Antoinette', 'acatchpo',
   '1992-02-19', NULL, 2, 'Warehouse Manager',
   44, 1300, NULL);
INSERT INTO t_emp VALUES (
   10, 'Havel', 'Marta', 'mhavel',
   '1991-02-27', NULL, 2, 'Warehouse Manager',
   45, 1307, NULL);
INSERT INTO t_emp VALUES (
   11, 'Magee', 'Colin', 'cmagee',
   '1990-05-14', NULL, 3, 'Sales Representative',
   31, 1400, 10);
INSERT INTO t_emp VALUES (
   12, 'Giljum', 'Henry', 'hgiljum',
   '1992-01-18', NULL, 3, 'Sales Representative',
   32, 1490, 12.5);
INSERT INTO t_emp VALUES (
   13, 'Sedeghi', 'Yasmin', 'ysedeghi',
   '1991-02-18', NULL, 3, 'Sales Representative',
   33, 1515, 10);
INSERT INTO t_emp VALUES (
   14, 'Nguyen', 'Mai', 'mnguyen',
   '1992-01-22', NULL, 3, 'Sales Representative',
   34, 1525, 15);
INSERT INTO t_emp VALUES (
   15, 'Dumas', 'Andre', 'adumas',
   '1991-10-09', NULL, 3, 'Sales Representative',
   35, 1450, 17.5);
INSERT INTO t_emp VALUES (
   16, 'Maduro', 'Elena', 'emaduro',
   '1992-02-07', NULL, 6, 'Stock Clerk',
   41, 1400, NULL);
INSERT INTO t_emp VALUES (
   17, 'Smith', 'George', 'gsmith',
   '1990-03-08', NULL, 6, 'Stock Clerk',
   41, 940, NULL);
INSERT INTO t_emp VALUES (
   18, 'Nozaki', 'Akira', 'anozaki',
   '1991-02-09', NULL, 7, 'Stock Clerk',
   42, 1200, NULL);
INSERT INTO t_emp VALUES (
   19, 'Patel', 'Vikram', 'vpatel',
   '1991-08-06', NULL, 7, 'Stock Clerk',
   42, 795, NULL);
INSERT INTO t_emp VALUES (
   20, 'Newman', 'Chad', 'cnewman',
   '1991-07-21', NULL, 8, 'Stock Clerk',
   43, 750, NULL);
INSERT INTO t_emp VALUES (
   21, 'Markarian', 'Alexander', 'amarkari',
   '1991-05-26', NULL, 8, 'Stock Clerk',
   43, 850, NULL);
INSERT INTO t_emp VALUES (
   22, 'Chang', 'Eddie', 'echang',
   '1990-11-30', NULL, 9, 'Stock Clerk',
   44, 800, NULL);
INSERT INTO t_emp VALUES (
   23, 'Patel', 'Radha', 'rpatel',
   '1990-10-17', NULL, 9, 'Stock Clerk',
   34, 795, NULL);
INSERT INTO t_emp VALUES (
   24, 'Dancs', 'Bela', 'bdancs',
   '1991-05-17', NULL, 10, 'Stock Clerk',
   45, 860, NULL);
INSERT INTO t_emp VALUES (
   25, 'Schwartz', 'Sylvie', 'sschwart',
   '1991-05-09', NULL, 10, 'Stock Clerk',
   45, 1100, NULL);



create table t_image(
id int(7) unsigned,
format varchar(25),
use_filename char(1),
filename varchar(255),
image BLOB,
primary key(id)
);

INSERT INTO t_image VALUES (
   1001, 'JTIFF', 'Y', 'bunboot.tif', NULL);
INSERT INTO t_image VALUES (
   1002, 'JTIFF', 'Y', 'aceboot.tif', NULL);
INSERT INTO t_image VALUES (
   1003, 'JTIFF', 'Y', 'proboot.tif', NULL);
INSERT INTO t_image VALUES (
   1011, 'JTIFF', 'Y', 'bunpole.tif', NULL);
INSERT INTO t_image VALUES (
   1012, 'JTIFF', 'Y', 'acepole.tif', NULL);
INSERT INTO t_image VALUES (
   1013, 'JTIFF', 'Y', 'propole.tif', NULL);
INSERT INTO t_image VALUES (
   1291, 'JTIFF', 'Y', 'gpbike.tif', NULL);
INSERT INTO t_image VALUES (
   1296, 'JTIFF', 'Y', 'himbike.tif', NULL);
INSERT INTO t_image VALUES (
   1829, 'JTIFF', 'Y', 'safthelm.tif', NULL);
INSERT INTO t_image VALUES (
   1381, 'JTIFF', 'Y', 'probar.tif', NULL);
INSERT INTO t_image VALUES (
   1382, 'JTIFF', 'Y', 'curlbar.tif', NULL);
INSERT INTO t_image VALUES (
   1119, 'JTIFF', 'Y', 'baseball.tif', NULL);
INSERT INTO t_image VALUES (
   1223, 'JTIFF', 'Y', 'chaphelm.tif', NULL);
INSERT INTO t_image VALUES (
   1367, 'JTIFF', 'Y', 'grglove.tif', NULL);
INSERT INTO t_image VALUES (
   1368, 'JTIFF', 'Y', 'alglove.tif', NULL);
INSERT INTO t_image VALUES (
   1369, 'JTIFF', 'Y', 'stglove.tif', NULL);
INSERT INTO t_image VALUES (
   1480, 'JTIFF', 'Y', 'cabbat.tif', NULL);
INSERT INTO t_image VALUES (
   1482, 'JTIFF', 'Y', 'pucbat.tif', NULL);
INSERT INTO t_image VALUES (
   1486, 'JTIFF', 'Y', 'winbat.tif', NULL);
   
  
create table t_inventory(
product_id int(7) unsigned,
warehouse_id int(7) unsigned,
amount_in_stock int(9) unsigned,
reorder_point int (9) unsigned,
max_in_stock int(9) unsigned,
out_of_stock_explanation varchar(255),
restock_date date,
primary key(product_id, warehouse_id)
);


INSERT INTO t_inventory VALUES (
   10011, 101, 650, 625, 1100, NULL, NULL);
INSERT INTO t_inventory VALUES (
   10012, 101, 600, 560, 1000, NULL, NULL);
INSERT INTO t_inventory VALUES (
   10013, 101, 400, 400, 700, NULL, NULL);
INSERT INTO t_inventory VALUES (
   10021, 101, 500, 425, 740, NULL, NULL);
INSERT INTO t_inventory VALUES (
   10022, 101, 300, 200, 350, NULL, NULL);
INSERT INTO t_inventory VALUES (
   10023, 101, 400, 300, 525, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20106, 101, 993, 625, 1000, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20108, 101, 700, 700, 1225, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20201, 101, 802, 800, 1400, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20510, 101, 1389, 850, 1400, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20512, 101, 850, 850, 1450, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30321, 101, 2000, 1500, 2500, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30326, 101, 2100, 2000, 3500, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30421, 101, 1822, 1800, 3150, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30426, 101, 2250, 2000, 3500, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30433, 101, 650, 600, 1050, NULL, NULL);
INSERT INTO t_inventory VALUES (
   32779, 101, 2120, 1250, 2200, NULL, NULL);
INSERT INTO t_inventory VALUES (
   32861, 101, 505, 500, 875, NULL, NULL);
INSERT INTO t_inventory VALUES (
   40421, 101, 578, 350, 600, NULL, NULL);
INSERT INTO t_inventory VALUES (
   40422, 101, 0, 350, 600, 'Phenomenal sales...', '1993-02-08');
INSERT INTO t_inventory VALUES (
   41010, 101, 250, 250, 437, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41020, 101, 471, 450, 750, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41050, 101, 501, 450, 750, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41080, 101, 400, 400, 700, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41100, 101, 350, 350, 600, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50169, 101, 2530, 1500, 2600, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50273, 101, 233, 200, 350, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50417, 101, 518, 500, 875, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50418, 101, 244, 100, 275, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50419, 101, 230, 120, 310, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50530, 101, 669, 400, 700, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50532, 101, 0, 100, 175, 'Wait for Spring.', '1993-04-12');
INSERT INTO t_inventory VALUES (
   50536, 101, 173, 100, 175, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20106, 201, 220, 150, 260, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20108, 201, 166, 150, 260, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20201, 201, 320, 200, 350, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20510, 201, 175, 100, 175, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20512, 201, 162, 100, 175, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30321, 201, 96, 80, 140, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30326, 201, 147, 120, 210, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30421, 201, 102, 80, 140, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30426, 201, 200, 120, 210, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30433, 201, 130, 130, 230, NULL, NULL);
INSERT INTO t_inventory VALUES (
   32779, 201, 180, 150, 260, NULL, NULL);
INSERT INTO t_inventory VALUES (
   32861, 201, 132, 80, 140, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50169, 201, 225, 220, 385, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50273, 201, 75, 60, 100, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50417, 201, 82, 60, 100, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50418, 201, 98, 60, 100, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50419, 201, 77, 60, 100, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50530, 201, 62, 60, 100, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50532, 201, 67, 60, 100, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50536, 201, 97, 60, 100, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20510, 301, 69, 40, 100, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20512, 301, 28, 20, 50, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30321, 301, 85, 80, 140, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30421, 301, 102, 80, 140, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30433, 301, 35, 20, 35, NULL, NULL);
INSERT INTO t_inventory VALUES (
   32779, 301, 102, 95, 175, NULL, NULL);
INSERT INTO t_inventory VALUES (
   32861, 301, 57, 50, 100, NULL, NULL);
INSERT INTO t_inventory VALUES (
   40421, 301, 70, 40, 70, NULL, NULL);
INSERT INTO t_inventory VALUES (
   40422, 301, 65, 40, 70, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41010, 301, 59, 40, 70, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41020, 301, 61, 40, 70, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41050, 301, 49, 40, 70, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41080, 301, 50, 40, 70, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41100, 301, 42, 40, 70, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20510, 401, 88, 50, 100, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20512, 401, 75, 75, 140, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30321, 401, 102, 80, 140, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30326, 401, 113, 80, 140, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30421, 401, 85, 80, 140, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30426, 401, 135, 80, 140, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30433, 401, 0, 100, 175, concat('A defective shipment was sent to Hong Kong ', 
   'and needed to be returned. The soonest ACME can turn this around is ',
   'early February.'), '1992-09-07');
INSERT INTO t_inventory VALUES (
   32779, 401, 135, 100, 175, NULL, NULL);
INSERT INTO t_inventory VALUES (
   32861, 401, 250, 150, 250, NULL, NULL);
INSERT INTO t_inventory VALUES (
   40421, 401, 47, 40, 70, NULL, NULL);
INSERT INTO t_inventory VALUES (
   40422, 401, 50, 40, 70, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41010, 401, 80, 70, 220, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41020, 401, 91, 70, 220, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41050, 401, 169, 70, 220, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41080, 401, 100, 70, 220, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41100, 401, 75, 70, 220, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50169, 401, 240, 200, 350, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50273, 401, 224, 150, 280, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50417, 401, 130, 120, 210, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50418, 401, 156, 100, 175, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50419, 401, 151, 150, 280, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50530, 401, 119, 100, 175, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50532, 401, 233, 200, 350, NULL, NULL);
INSERT INTO t_inventory VALUES (
   50536, 401, 138, 100, 175, NULL, NULL);
INSERT INTO t_inventory VALUES (
   10012, 10501, 300, 300, 525, NULL, NULL);
INSERT INTO t_inventory VALUES (
   10013, 10501, 314, 300, 525, NULL, NULL);
INSERT INTO t_inventory VALUES (
   10022, 10501, 502, 300, 525, NULL, NULL);
INSERT INTO t_inventory VALUES (
   10023, 10501, 500, 300, 525, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20106, 10501, 150, 100, 175, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20108, 10501, 222, 200, 350, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20201, 10501, 275, 200, 350, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20510, 10501, 57, 50, 87, NULL, NULL);
INSERT INTO t_inventory VALUES (
   20512, 10501, 62, 50, 87, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30321, 10501, 194, 150, 275, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30326, 10501, 277, 250, 440, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30421, 10501, 190, 150, 275, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30426, 10501, 423, 250, 450, NULL, NULL);
INSERT INTO t_inventory VALUES (
   30433, 10501, 273, 200, 350, NULL, NULL);
INSERT INTO t_inventory VALUES (
   32779, 10501, 280, 200, 350, NULL, NULL);
INSERT INTO t_inventory VALUES (
   32861, 10501, 288, 200, 350, NULL, NULL);
INSERT INTO t_inventory VALUES (
   40421, 10501, 97, 80, 140, NULL, NULL);
INSERT INTO t_inventory VALUES (
   40422, 10501, 90, 80, 140, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41010, 10501, 151, 140, 245, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41020, 10501, 224, 140, 245, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41050, 10501, 157, 140, 245, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41080, 10501, 159, 140, 245, NULL, NULL);
INSERT INTO t_inventory VALUES (
   41100, 10501, 141, 140, 245, NULL, NULL);
COMMIT;



create table t_customer(
	id int(7) unsigned,
	name varchar(50),
	phone varchar(25),
	address varchar(400),
	city varchar(30),
	state varchar(20),
	country varchar(30),
	zip_code varchar(75),
	credit_rating enum('EXCELLENT','GOOD','POOR'),
	sales_rep_id int(7) unsigned,
	region_id int(7) unsigned,
	comments varchar(255),
	primary key(id)
	
);

INSERT INTO t_customer VALUES (
   201, 'Unisports', '55-2066101',
   '72 Via Bahia', 'Sao Paolo', NULL, 'Brazil', NULL,
   'EXCELLENT', 12, 2, NULL);
INSERT INTO t_customer VALUES (
   202, 'OJ Atheletics', '81-20101',
   '6741 Takashi Blvd.', 'Osaka', NULL, 'Japan', NULL,
   'POOR', 14, 4, NULL);
INSERT INTO t_customer VALUES (
   203, 'Delhi Sports', '91-10351',
   '11368 Chanakya', 'New Delhi', NULL, 'India', NULL,
   'GOOD', 14, 4, NULL);
INSERT INTO t_customer VALUES (
   204, 'Womansport', '1-206-104-0103',
   '281 King Street', 'Seattle', 'Washington', 'USA', NULL,
   'EXCELLENT', 11, 1, NULL);
INSERT INTO t_customer VALUES (
   205, 'Kam''s Sporting Goods', '852-3692888',
   '15 Henessey Road', 'Hong Kong', NULL, NULL, NULL,
   'EXCELLENT', 15, 4, NULL);
INSERT INTO t_customer VALUES (
   206, 'Sportique', '33-2257201',
   '172 Rue de Rivoli', 'Cannes', NULL, 'France', NULL,
   'EXCELLENT', 15, 5, NULL);
INSERT INTO t_customer VALUES (
   207, 'Sweet Rock Sports', '234-6036201',
   '6 Saint Antoine', 'Lagos', NULL, 'Nigeria', NULL,
   'GOOD', NULL, 3, NULL);
INSERT INTO t_customer VALUES (
   208, 'Muench Sports', '49-527454',
   '435 Gruenestrasse', 'Stuttgart', NULL, 'Germany', NULL,
   'GOOD', 15, 5, NULL);
INSERT INTO t_customer VALUES (
   209, 'Beisbol Si!', '809-352689',
   '792 Playa Del Mar', 'San Pedro de Macon''s', NULL, 'Dominican Republic',
   NULL, 'EXCELLENT', 11, 1, NULL);
INSERT INTO t_customer VALUES (
   210, 'Futbol Sonora', '52-404562',
   '3 Via Saguaro', 'Nogales', NULL, 'Mexico', NULL,
   'EXCELLENT', 12, 2, NULL);
INSERT INTO t_customer VALUES (
   211, 'Kuhn''s Sports', '42-111292',
   '7 Modrany', 'Prague', NULL, 'Czechoslovakia', NULL,
   'EXCELLENT', 15, 5, NULL);
INSERT INTO t_customer VALUES (
   212, 'Hamada Sport', '20-1209211',
   '57A Corniche', 'Alexandria', NULL, 'Egypt', NULL,
   'EXCELLENT', 13, 3, NULL);
INSERT INTO t_customer VALUES (
   213, 'Big John''s Sports Emporium', '1-415-555-6281',
   '4783 18th Street', 'San Francisco', 'CA', 'USA', NULL,
   'EXCELLENT', 11, 1, NULL);
INSERT INTO t_customer VALUES (
   214, 'Ojibway Retail', '1-716-555-7171',
   '415 Main Street', 'Buffalo', 'NY', 'USA', NULL,
   'POOR', 11, 1, NULL);
INSERT INTO t_customer VALUES (
   215, 'Sporta Russia', '7-3892456',
   '6000 Yekatamina', 'Saint Petersburg', NULL, 'Russia', NULL,
   'POOR', 15, 5, NULL);
COMMIT;


create table t_item(
	ord_id int(7) unsigned not null,
	item_id int(7) unsigned not null,
	product_id int(7) unsigned not null,
	price decimal(11,2),
	quantity int(9) unsigned,
	quantity_shipped int(9) unsigned,
	primary key(ord_id,product_id),
	unique(ord_id,product_id)
);

INSERT INTO t_item VALUES (
   100, 1, 10011, 135, 500, 500);
INSERT INTO t_item VALUES (
   100, 2, 10013, 380, 400, 400);
INSERT INTO t_item VALUES (
   100, 3, 10021, 14, 500, 500);
INSERT INTO t_item VALUES (
   100, 5, 30326, 582, 600, 600);
INSERT INTO t_item VALUES (
   100, 7, 41010, 8, 250, 250);
INSERT INTO t_item VALUES (
   100, 6, 30433, 20, 450, 450);
INSERT INTO t_item VALUES (
   100, 4, 10023, 36, 400, 400);
INSERT INTO t_item VALUES (
   101, 1, 30421, 16, 15, 15);
INSERT INTO t_item VALUES (
   101, 3, 41010, 8, 20, 20);
INSERT INTO t_item VALUES (
   101, 5, 50169, 4.29, 40, 40);
INSERT INTO t_item VALUES (
   101, 6, 50417, 80, 27, 27);
INSERT INTO t_item VALUES (
   101, 7, 50530, 45, 50, 50);
INSERT INTO t_item VALUES (
   101, 4, 41100, 45, 35, 35);
INSERT INTO t_item VALUES (
   101, 2, 40422, 50, 30, 30);
INSERT INTO t_item VALUES (
   102, 1, 20108, 28, 100, 100);
INSERT INTO t_item VALUES (
   102, 2, 20201, 123, 45, 45);
INSERT INTO t_item VALUES (
   103, 1, 30433, 20, 15, 15);
INSERT INTO t_item VALUES (
   103, 2, 32779, 7, 11, 11);
INSERT INTO t_item VALUES (
   104, 1, 20510, 9, 7, 7);
INSERT INTO t_item VALUES (
   104, 4, 30421, 16, 35, 35);
INSERT INTO t_item VALUES (
   104, 2, 20512, 8, 12, 12);
INSERT INTO t_item VALUES (
   104, 3, 30321, 1669, 19, 19);
INSERT INTO t_item VALUES (
   105, 1, 50273, 22.89, 16, 16);
INSERT INTO t_item VALUES (
   105, 3, 50532, 47, 28, 28);
INSERT INTO t_item VALUES (
   105, 2, 50419, 80, 13, 13);
INSERT INTO t_item VALUES (
   106, 1, 20108, 28, 46, 46);
INSERT INTO t_item VALUES (
   106, 4, 50273, 22.89, 75, 75);
INSERT INTO t_item VALUES (
   106, 5, 50418, 75, 98, 98);
INSERT INTO t_item VALUES (
   106, 6, 50419, 80, 27, 27);
INSERT INTO t_item VALUES (
   106, 2, 20201, 123, 21, 21);
INSERT INTO t_item VALUES (
   106, 3, 50169, 4.29, 125, 125);
INSERT INTO t_item VALUES (
   107, 1, 20106, 11, 50, 50);
INSERT INTO t_item VALUES (
   107, 3, 20201, 115, 130, 130);
INSERT INTO t_item VALUES (
   107, 5, 30421, 16, 55, 55);
INSERT INTO t_item VALUES (
   107, 4, 30321, 1669, 75, 75);
INSERT INTO t_item VALUES (
   107, 2, 20108, 28, 22, 22);
INSERT INTO t_item VALUES (
   108, 1, 20510, 9, 9, 9);
INSERT INTO t_item VALUES (
   108, 6, 41080, 35, 50, 50);
INSERT INTO t_item VALUES (
   108, 7, 41100, 45, 42, 42);
INSERT INTO t_item VALUES (
   108, 5, 32861, 60, 57, 57);
INSERT INTO t_item VALUES (
   108, 2, 20512, 8, 18, 18);
INSERT INTO t_item VALUES (
   108, 4, 32779, 7, 60, 60);
INSERT INTO t_item VALUES (
   108, 3, 30321, 1669, 85, 85);
INSERT INTO t_item VALUES (
   109, 1, 10011, 140, 150, 150);
INSERT INTO t_item VALUES (
   109, 5, 30426, 18.25, 500, 500);
INSERT INTO t_item VALUES (
   109, 7, 50418, 75, 43, 43);
INSERT INTO t_item VALUES (
   109, 6, 32861, 60, 50, 50);
INSERT INTO t_item VALUES (
   109, 4, 30326, 582, 1500, 1500);
INSERT INTO t_item VALUES (
   109, 2, 10012, 175, 600, 600);
INSERT INTO t_item VALUES (
   109, 3, 10022, 21.95, 300, 300);
INSERT INTO t_item VALUES (
   110, 1, 50273, 22.89, 17, 17);
INSERT INTO t_item VALUES (
   110, 2, 50536, 50, 23, 23);
INSERT INTO t_item VALUES (
   111, 1, 40421, 65, 27, 27);
INSERT INTO t_item VALUES (
   111, 2, 41080, 35, 29, 29);
INSERT INTO t_item VALUES (
   97, 1, 20106, 9, 1000, 1000);
INSERT INTO t_item VALUES (
   97, 2, 30321, 1500, 50, 50);
INSERT INTO t_item VALUES (
   98, 1, 40421, 85, 7, 7);
INSERT INTO t_item VALUES (
   99, 1, 20510, 9, 18, 18);
INSERT INTO t_item VALUES (
   99, 2, 20512, 8, 25, 25);
INSERT INTO t_item VALUES (
   99, 3, 50417, 80, 53, 53);
INSERT INTO t_item VALUES (
   99, 4, 50530, 45, 69, 69);
INSERT INTO t_item VALUES (
   112, 1, 20106, 11, 50, 50);
COMMIT;

	
		
create table t_title(title varchar(25) not null,primary key(title));


INSERT INTO t_title VALUES ('President');
INSERT INTO t_title VALUES ('Sales Representative');
INSERT INTO t_title VALUES ('Stock Clerk');
INSERT INTO t_title VALUES ('VP, Administration');
INSERT INTO t_title VALUES ('VP, Finance');
INSERT INTO t_title VALUES ('VP, Operations');
INSERT INTO t_title VALUES ('VP, Sales');
INSERT INTO t_title VALUES ('Warehouse Manager');
COMMIT;


create table t_region(
	id int(7) not null,
	name varchar(50) not null,
	primary key (id),
	unique (name)
);

INSERT INTO t_region VALUES (
   1, 'North America');
INSERT INTO t_region VALUES (
   2, 'South America');
INSERT INTO t_region VALUES (
   3, 'Africa / Middle East');
INSERT INTO t_region VALUES (
   4, 'Asia');
INSERT INTO t_region VALUES (
   5, 'Europe');


create table t_longtext(
id int(7) unsigned not null,
user_filename enum('y','n'),
filename varchar(255),
text TEXT,
primary key (id));

create table t_ord(
	id int(7) unsigned not null,
	customer_id int(7) unsigned not null,
	date_ordered date,
	date_shipped date,
	sales_rep_id int(7),
	total decimal(11,2),
	payment_type varchar(6),
	order_filled varchar(1),
primary key(id)
);

INSERT INTO t_ord VALUES (
   100, 204, '1992-08-31', '1992-09-10',
   11, 601100, 'CREDIT', 'Y');
INSERT INTO t_ord VALUES (
   101, 205, '1992-08-31', '1992-09-15',
   14, 8056.6, 'CREDIT', 'Y');
INSERT INTO t_ord VALUES (
   102, 206, '1992-09-01', '1992-09-08',
   15, 8335, 'CREDIT', 'Y');
INSERT INTO t_ord VALUES (
   103, 208, '1992-09-02', '1992-09-22',
   15, 377, 'CASH', 'Y');
INSERT INTO t_ord VALUES (
   104, 208, '1992-09-04', '1992-09-23',
   15, 32430, 'CREDIT', 'Y');
INSERT INTO t_ord VALUES (
   105, 209, '1992-09-04', '1992-09-18',
   11, 2722.24, 'CREDIT', 'Y');
INSERT INTO t_ord VALUES (
   106, 210, '1992-09-07', '1992-09-15',
   12, 15634, 'CREDIT', 'Y');
INSERT INTO t_ord VALUES (
   107, 211, '1992-09-07', '1992-09-21',
   15, 142171, 'CREDIT', 'Y');
INSERT INTO t_ord VALUES (
   108, 212, '1992-09-07', '1992-09-10',
   13, 149570, 'CREDIT', 'Y');
INSERT INTO t_ord VALUES (
   109, 213, '1992-09-08', '1992-09-28',
   11, 1020935, 'CREDIT', 'Y');
INSERT INTO t_ord VALUES (
   110, 214, '1992-09-09', '1992-09-21',
   11, 1539.13, 'CASH', 'Y');
INSERT INTO t_ord VALUES (
   111, 204, '1992-09-09', '1992-09-21',
   11, 2770, 'CASH', 'Y');
INSERT INTO t_ord VALUES (
   97, 201, '1992-08-28', '1992-09-17',
   12, 84000, 'CREDIT', 'Y');
INSERT INTO t_ord VALUES (
   98, 202, '1992-08-31', '1992-09-10',
   14, 595, 'CASH', 'Y');
INSERT INTO t_ord VALUES (
   99, 203, '1992-08-31', '1992-09-18',
   14, 7707, 'CREDIT', 'Y');
INSERT INTO t_ord VALUES (
   112, 210, '1992-08-31', '1992-09-10',
   12, 550, 'CREDIT', 'Y');



create table t_warehouse(id int(7) unsigned,
	region_id int(7) unsigned not null,
	address longtext,city varchar(30),
	state varchar(20),country varchar(30),
	zip_code varchar(75),phone varchar(25),
	manager_id int(7) unsigned,
	primary key(id)
);

INSERT INTO t_warehouse VALUES (
   101, 1,
   '283 King Street',
   'Seattle', 'WA', 'USA',
   NULL,
   NULL, 6);
INSERT INTO t_warehouse VALUES (
   10501, 5,
   '5 Modrany',
   'Bratislava', NULL, 'Czechozlovakia',
   NULL,
   NULL, 10);
INSERT INTO t_warehouse VALUES (
   201, 2,
   '68 Via Centrale',
   'Sao Paolo', NULL, 'Brazil',
   NULL,
   NULL, 7);
INSERT INTO t_warehouse VALUES (
   301, 3,
   '6921 King Way',
   'Lagos', NULL, 'Nigeria',
   NULL,
   NULL, 8);
INSERT INTO t_warehouse VALUES (
   401, 4,
   '86 Chu Street',
   'Hong Kong', NULL, NULL,
   NULL,
   NULL, 9);
COMMIT;

CREATE TABLE t_product(
id int(7)   not null,
name varchar(50) unique not null,
short_desc varchar(255) ,
longtext_id int(7),
image_id  int(7),
suggested_whlsl_price  decimal(11,2),
whlsl_units varchar(25),
PRIMARY KEY (id)
);

INSERT INTO t_product VALUES (
   10011, 'Bunny Boot',
   'Beginner''s ski boot',
   518, 1001,
   150, NULL);
INSERT INTO t_product VALUES (
   10012, 'Ace Ski Boot',
   'Intermediate ski boot',
   519, 1002,
   200, NULL);
INSERT INTO t_product VALUES (
   10013, 'Pro Ski Boot',
   'Advanced ski boot',
   520, 1003,
   410, NULL);
INSERT INTO t_product VALUES (
   10021, 'Bunny Ski Pole',
   'Beginner''s ski pole',
   528, 1011,
   16.25, NULL);
INSERT INTO t_product VALUES (
   10022, 'Ace Ski Pole',
   'Intermediate ski pole',
   529, 1012,
   21.95, NULL);
INSERT INTO t_product VALUES (
   10023, 'Pro Ski Pole',
   'Advanced ski pole',
   530, 1013,
   40.95, NULL);
INSERT INTO t_product VALUES (
   20106, 'Junior Soccer Ball',
   'Junior soccer ball',
   613, NULL,
   11, NULL);
INSERT INTO t_product VALUES (
   20108, 'World Cup Soccer Ball',
   'World cup soccer ball',
   615, NULL,
   28, NULL);
INSERT INTO t_product VALUES (
   20201, 'World Cup Net',
   'World cup net',
   708, NULL,
   123, NULL);
INSERT INTO t_product VALUES (
   20510, 'Black Hawk Knee Pads',
   'Knee pads, pair',
   1017, NULL,
   9, NULL);
INSERT INTO t_product VALUES (
   20512, 'Black Hawk Elbow Pads',
   'Elbow pads, pair',
   1019, NULL,
   8, NULL);
INSERT INTO t_product VALUES (
   30321, 'Grand Prix Bicycle',
   'Road bicycle',
   828, 1291,
   1669, NULL);
INSERT INTO t_product VALUES (
   30326, 'Himalaya Bicycle',
   'Mountain bicycle',
   833, 1296,
   582, NULL);
INSERT INTO t_product VALUES (
   30421, 'Grand Prix Bicycle Tires',
   'Road bicycle tires',
   927, NULL,
   16, NULL);
INSERT INTO t_product VALUES (
   30426, 'Himalaya Tires',
   'Mountain bicycle tires',
   933, NULL,
   18.25, NULL);
INSERT INTO t_product VALUES (
   30433, 'New Air Pump',
   'Tire pump',
   940, NULL,
   20, NULL);
INSERT INTO t_product VALUES (
   32779, 'Slaker Water Bottle',
   'Water bottle',
   1286, NULL,
   7, NULL);
INSERT INTO t_product VALUES (
   32861, 'Safe-T Helmet',
   'Bicycle helmet',
   1368, 1829,
   60, NULL);
INSERT INTO t_product VALUES (
   40421, 'Alexeyer Pro Lifting Bar',
   'Straight bar',
   928, 1381,
   65, NULL);
INSERT INTO t_product VALUES (
   40422, 'Pro Curling Bar',
   'Curling bar',
   929, 1382,
   50, NULL);
INSERT INTO t_product VALUES (
   41010, 'Prostar 10 Pound Weight',
   'Ten pound weight',
   517, NULL,
   8, NULL);
INSERT INTO t_product VALUES (
   41020, 'Prostar 20 Pound Weight',
   'Twenty pound weight',
   527, NULL,
   12, NULL);
INSERT INTO t_product VALUES (
   41050, 'Prostar 50 Pound Weight',
   'Fifty pound weight',
   557, NULL,
   25, NULL);
INSERT INTO t_product VALUES (
   41080, 'Prostar 80 Pound Weight',
   'Eighty pound weight',
   587, NULL,
   35, NULL);
INSERT INTO t_product VALUES (
   41100, 'Prostar 100 Pound Weight',
   'One hundred pound weight',
   607, NULL,
   45, NULL);
INSERT INTO t_product VALUES (
   50169, 'Major League Baseball',
   'Baseball',
   676, 1119,
   4.29, NULL);
INSERT INTO t_product VALUES (
   50273, 'Chapman Helmet',
   'Batting helmet',
   780, 1223,
   22.89, NULL);
INSERT INTO t_product VALUES (
   50417, 'Griffey Glove',
   'Outfielder''s glove',
   924, 1367,
   80, NULL);
INSERT INTO t_product VALUES (
   50418, 'Alomar Glove',
   'Infielder''s glove',
   925, 1368,
   75, NULL);
INSERT INTO t_product VALUES (
   50419, 'Steinbach Glove',
   'Catcher''s glove',
   926, 1369,
   80, NULL);
INSERT INTO t_product VALUES (
   50530, 'Cabrera Bat',
   'Thirty inch bat',
   1037, 1480,
   45, NULL);
INSERT INTO t_product VALUES (
   50532, 'Puckett Bat',
   'Thirty-two inch bat',
   1039, 1482,
   47, NULL);
INSERT INTO t_product VALUES (
   50536, 'Winfield Bat',
   'Thirty-six inch bat',
   1043, 1486,
   50, NULL);
