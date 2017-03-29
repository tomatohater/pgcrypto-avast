--
-- Restore sample legacy users table.
--


CREATE TABLE legacy_users (
    username character varying(50) NOT NULL,
    password character varying(100) NOT NULL
);


COPY legacy_users (username, password) FROM stdin;
kingdiamond	$1$AEm9NDkI$z9YLtNHjckjz5ZMmsNUrX1
kingbuzzo	$1$Pop9WeOo$2XqJ67vVoIh74Ybk6gSqK1
\.


ALTER TABLE ONLY legacy_users
    ADD CONSTRAINT legacy_users_pkey PRIMARY KEY (username);
