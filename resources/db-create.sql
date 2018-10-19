CREATE TABLE IF NOT EXISTS stories(
    id integer PRIMARY KEY,
    user_id integer,
    name varchar(50),
    status varchar(20),
    date_start real,
    date_next_payment real,
    date_secondary_bought real,
    date_secondary_sold_date real,
    amount integer,
    full_payment float,
    my_payment float,
    installments integer,
    installments_when_bought integer,
    insurance boolean,
    postponed boolean,
    interest_rate float,
    fee float,
    rating varchar(3)
);
CREATE TABLE IF NOT EXISTS history(
    id integer PRIMARY KEY,
    story_id integer,
    date_transaction real,
    remaining_installments integer,
    paid_installments integer,
    original_investment float,
    my_investment float,
    principal_paid float,
    principal_remaining float,
    principal_sold float,
    principal_late float,
    principal_sell_fee float,
    interest_expected float,
    interest_paid float,
    interest_remaining float,
    interest_late float,
    penalty float
);
CREATE TABLE IF NOT EXISTS files(
    id integer PRIMARY KEY,
    filename varchar(50),
    date_processed text
)
