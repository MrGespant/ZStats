CREATE TABLE IF NOT EXISTS investment(
    id integer PRIMARY KEY,
    ext_client_id varchar(20),
    inv_name varchar(50),
    ext_id integer,
    inv_date text NULL,
    full_investment integer,
    full_installment integer,
    installment float,
    insurance varchar(15),
    original_investment float,
    my_investment float,
    reservation_investment integer NULL,
    interest_expected float,
    interest_rate float,
    rating varchar(3) NULL,
    fee float,
    original_installments integer,
    bought_installments integer NULL,
    bought_secondary_date text NULL,
    sold_secondary_date text NULL
);
CREATE TABLE IF NOT EXISTS status(
    id integer PRIMARY KEY,
    investment_id integer,
    export_id integer,
    status varchar(15),
    status_created text,
    remaining_installments integer,
    postponed_installment varchar(3),
    principal_paid float,
    principal_left float,
    sold_for float NULL,
    sell_fee float NULL,
    principal_due float,
    interest_paid float,
    interest_left float,
    interest_due float,
    penalty float,
    current_installments integer,
    next_installment_date text NULL
);
CREATE TABLE IF NOT EXISTS export(
    id integer PRIMARY KEY,
    filename varchar(50),
    date text,
    status varchar(10)
)
