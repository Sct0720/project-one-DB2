
CREATE DATABASE inventory_management;
USE inventory_management;

CREATE TABLE categories (
    id_category INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    description VARCHAR(255)
);

CREATE TABLE suppliers (
    id_supplier INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(15)
);

CREATE TABLE products (
    id_product INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    id_category INT,
    id_supplier INT,
    FOREIGN KEY (id_category) REFERENCES categories(id_category),
    FOREIGN KEY (id_supplier) REFERENCES suppliers(id_supplier)
);

------------o-------------------------o----------------
INSERT INTO categories (name, description) VALUES
('Electronics', 'Devices like phones, laptops, and tablets'),
('Clothing', 'Apparel items including shirts, pants, and jackets'),
('Home Appliances', 'Large and small household appliances'),
('Sports', 'Sporting goods and equipment'),
('Toys', 'Toys and games for children of all ages'),
('Books', 'Printed and electronic books of various genres'),
('Beauty', 'Cosmetics and skincare products'),
('Furniture', 'Home and office furniture items'),
('Stationery', 'Office supplies and stationery products'),
('Footwear', 'Various types of shoes and sandals'),
('Jewelry', 'Jewelry including necklaces, bracelets, and rings'),
('Automotive', 'Car accessories and parts'),
('Gardening', 'Tools and products for gardening'),
('Health', 'Health and wellness products'),
('Kitchenware', 'Cookware, utensils, and kitchen gadgets'),
('Pet Supplies', 'Products for pets like food and accessories'),
('Groceries', 'Everyday grocery items and snacks'),
('Tools', 'Hand tools, power tools, and hardware'),
('Music', 'Musical instruments and accessories'),
('Video Games', 'Games and consoles for various platforms');

INSERT INTO suppliers (name, email, phone) VALUES
('ABC Electronics', 'abc@electronics.com', '123-456-7890'),
('Global Clothing Co.', 'contact@globalclothing.com', '123-456-7891'),
('Home Appliance Experts', 'support@homeappliances.com', '123-456-7892'),
('Sportify', 'info@sportify.com', '123-456-7893'),
('Toy World', 'sales@toyworld.com', '123-456-7894'),
('Book Haven', 'contact@bookhaven.com', '123-456-7895'),
('Beauty Hub', 'service@beautyhub.com', '123-456-7896'),
('Furniture Factory', 'orders@furniturefactory.com', '123-456-7897'),
('Office Supplies Ltd.', 'sales@officesupplies.com', '123-456-7898'),
('Shoe Corner', 'info@shoecorner.com', '123-456-7899'),
('Gemstone Jewelers', 'support@gemstonejewelers.com', '123-456-7800'),
('Auto Parts World', 'contact@autopartsworld.com', '123-456-7801'),
('Garden Goods', 'sales@gardengoods.com', '123-456-7802'),
('Health First', 'support@healthfirst.com', '123-456-7803'),
('Kitchen Pro', 'service@kitchenpro.com', '123-456-7804'),
('Pet Kingdom', 'contact@petkingdom.com', '123-456-7805'),
('Fresh Groceries', 'orders@freshgroceries.com', '123-456-7806'),
('Tool Time', 'info@tooltime.com', '123-456-7807'),
('Musica World', 'support@musicaworld.com', '123-456-7808'),
('Game Zone', 'contact@gamezone.com', '123-456-7809');

INSERT INTO products (name, description, price, quantity, id_category, id_supplier) VALUES
('Smartphone', 'Latest model smartphone with high resolution screen', 799.99, 50, 1, 1),
('Laptop', 'High-performance laptop for gaming and work', 1299.99, 30, 1, 1),
('T-Shirt', '100% cotton t-shirt in various colors', 19.99, 200, 2, 2),
('Blender', 'Powerful kitchen blender with multiple settings', 49.99, 80, 3, 3),
('Basketball', 'Standard size basketball for indoor/outdoor use', 29.99, 60, 4, 4),
('Doll', 'Doll with customizable outfits', 24.99, 150, 5, 5),
('Novel', 'Best-selling fiction novel', 14.99, 120, 6, 6),
('Lipstick', 'Matte finish lipstick in multiple shades', 9.99, 300, 7, 7),
('Office Chair', 'Ergonomic office chair with lumbar support', 149.99, 40, 8, 8),
('Notebook', 'Spiral notebook with 200 pages', 4.99, 500, 9, 9),
('Sneakers', 'Comfortable sneakers for everyday wear', 59.99, 100, 10, 10),
('Necklace', 'Gold-plated necklace with gemstone pendant', 99.99, 70, 11, 11),
('Car Battery', 'High-capacity car battery for all models', 89.99, 35, 12, 12),
('Garden Shovel', 'Durable garden shovel with wooden handle', 19.99, 80, 13, 13),
('Vitamin C', 'Immune-boosting Vitamin C tablets', 12.99, 150, 14, 14),
('Cookware Set', 'Non-stick cookware set with pots and pans', 89.99, 25, 15, 15),
('Dog Food', 'Premium dry dog food with high protein content', 29.99, 200, 16, 16),
('Olive Oil', 'Extra virgin olive oil for cooking and salads', 10.99, 120, 17, 17),
('Hammer', 'Heavy-duty hammer with ergonomic grip', 14.99, 90, 18, 18),
('Guitar', 'Acoustic guitar suitable for beginners and pros', 129.99, 20, 19, 19),
('Video Game', 'Latest adventure video game for PlayStation', 59.99, 50, 20, 20);


