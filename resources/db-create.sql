CREATE TABLE IF NOT EXISTS stories(
    id integer PRIMARY KEY,
    user_id varchar(20),
    name varchar(50),
    date_start text,
    date_secondary_bought text,
    date_secondary_sold_date text,
    amount integer,
    full_payment float,
    my_payment float,
    original_installments integer,
    installments_when_bought integer,
    insurance boolean,
    interest_rate float,
    fee float,
    rating varchar(3)
);
CREATE TABLE IF NOT EXISTS history(
    id integer PRIMARY KEY,
    story_id integer,
    status varchar(20),
    date_transaction text,
    date_next_payment text,
    remaining_installments integer,
    current_installments integer,
    original_investment float,
    principal_investment float,
    principal_paid float,
    principal_remaining float,
    principal_sold float,
    principal_late float,
    principal_sell_fee float,
    interest_expected float,
    interest_paid float,
    interest_remaining float,
    interest_late float,
    postponed boolean,
    penalty float
);
CREATE TABLE IF NOT EXISTS files(
    id integer PRIMARY KEY,
    filename varchar(50),
    date_processed text
)
