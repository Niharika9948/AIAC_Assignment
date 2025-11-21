CREATE DATABASE IF NOT EXISTS library;
USE library;

-- Prevent duplicate errors
DROP TABLE IF EXISTS loans;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS books;

-------------------------------------------------
-- 1. CREATE TABLES
-------------------------------------------------

CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    publication_year INT CHECK (publication_year >= 1500),
    available_copies INT DEFAULT 0 CHECK (available_copies >= 0)
);

CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    join_date DATE NOT NULL,
    membership_type ENUM('Standard', 'Premium', 'Student') NOT NULL
);

CREATE TABLE loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    loan_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE NULL,

    FOREIGN KEY (book_id) REFERENCES books(book_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES members(member_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

-------------------------------------------------
-- 2. INSERT SAMPLE DATA
-------------------------------------------------

-- BOOKS (4 books, 2 authors used multiple times)
INSERT INTO books (title, author, isbn, publication_year, available_copies) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565', 1925, 1),
('This Side of Paradise', 'F. Scott Fitzgerald', '9780743273566', 1920, 2),  -- same author → helps most popular author
('1984', 'George Orwell', '9780451524935', 1949, 0),   -- fully borrowed
('Animal Farm', 'George Orwell', '9780451526342', 1945, 1);  -- same author

-- MEMBERS (3 members)
INSERT INTO members (name, email, join_date, membership_type) VALUES
('Alice Johnson', 'alice@gmail.com', '2023-01-10', 'Standard'),
('Bob Smith', 'bob@gmail.com', '2023-02-15', 'Premium'),
('Charlie Ray', 'charlie@gmail.com', '2023-03-01', 'Student');

-- LOANS
-- Overdue loans + returned loans to ensure ALL queries produce output
INSERT INTO loans (book_id, member_id, loan_date, due_date, return_date) VALUES
(3, 1, '2023-01-01', '2023-01-10', NULL),         -- 1984 → overdue
(1, 2, '2023-02-01', '2023-02-12', NULL),         -- Gatsby → overdue
(2, 3, '2024-02-01', '2024-02-15', '2024-02-14'), -- This Side of Paradise → returned
(4, 1, '2024-03-01', '2024-03-20', '2024-03-18'); -- Animal Farm → returned

SELECT 
    l.loan_id,
    b.title,
    b.author,
    m.name AS borrowed_by,
    l.loan_date,
    l.due_date
FROM loans l
JOIN books b ON l.book_id = b.book_id
JOIN members m ON l.member_id = m.member_id
WHERE l.return_date IS NULL
  AND l.due_date < CURDATE();

SELECT 
    b.author,
    COUNT(*) AS total_loans
FROM loans l
JOIN books b ON l.book_id = b.book_id
GROUP BY b.author
ORDER BY total_loans DESC
LIMIT 1;
