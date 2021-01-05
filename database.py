import sqlite3


def insert(name, email, password, phone, db):
    db.execute("INSERT INTO user(name, email, password, phone) VALUES (?, ?, ?, ?)", (name, email, password, phone))
    db.commit()


def insert_cart(name, price, user_id, db):
    db.execute("INSERT INTO cart(name, price, user_id) VALUES (?, ?, ?)", (name, price, user_id))
    db.commit()


def read(email, db):
    cur = db.cursor()
    result = cur.execute("SELECT * FROM user WHERE email = ?", (email,))
    return result


def get(user_id, db):
    cur = db.cursor()
    result = cur.execute("SELECT * FROM user WHERE id = ?", (user_id,))
    return result


def get_cart(user_id, db):
    cur = db.cursor()
    result = cur.execute("SELECT * FROM cart WHERE user_id = ?", (user_id,))
    return result


def read_login(email, password, db):
    cur = db.cursor()
    result = cur.execute("SELECT * FROM user WHERE email = ? AND password = ?", (email, password,))
    return result


def update(name, email, password, phone, user_id, db):
    c = db.cursor()
    sql = "UPDATE user SET name = ?, email = ?, password = ?, phone = ? WHERE id = ?"
    my_list = (str(name), str(email), str(password), str(phone), int(user_id),)
    result = c.execute(sql, my_list)
    db.commit()
    return result


def delete(product_id, user_id, db):
    c = db.cursor()
    sql = "DELETE FROM cart WHERE id = ? AND user_id = ?"
    my_list = (int(product_id), int(user_id),)
    result = c.execute(sql, my_list)
    db.commit()
    return result
