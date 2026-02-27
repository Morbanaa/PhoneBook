-- Blueprint For phone_book database Set up in MySQL...

CREATE TABLE phone_book (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(15)
);
