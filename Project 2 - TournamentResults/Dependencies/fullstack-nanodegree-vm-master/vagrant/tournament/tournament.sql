-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


 -- Cleanup any existing  tournament database object
drop database if exists tournament;


-- Create 'Tournament' schemea
CREATE DATABASE tournament;

-- Select (connect to) the active database
\connect tournament

-- Create the tables: matches and players
create table players (players_row_id serial primary key, players_name text );
create table matches (matches_row_id serial primary key, losers_id integer, winners_id integer, 
						foreign key (losers_id) references players (players_row_id),
						foreign key (winners_id) references players (players_row_id) );

--Create a view of the players and their win records, sorted by wins
create view pairingsView as 
		select a.players_row_id as players_row_id, a.players_name,
			(select count(*) from matches where matches.winners_id = a.players_row_id) as who_won_matchup,
			(select count(*) from matches where a.players_row_id in (losers_id, winners_id)) as those_who_played from players a group by a.players_row_id order by who_won_matchup desc;
