-- Creating session staging table
CREATE TABLE google_analytics_staging.sessions(
cookie_id varchar(30),
click_timestamp varchar(30),
medium varchar(30),
source varchar(30),
click_date varchar(30),
click_dateHour varchar(30)
);