#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#
import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    databaseConnection = connect()
    cursor = databaseConnection.cursor()
    databaseQuery = "DELETE FROM matches"
    cursor.execute(databaseQuery)
    databaseConnection.commit()
    databaseConnection.close()


def deletePlayers():
    """Remove all the player records from the database."""
    databaseConnection = connect()
    cursor = databaseConnection.cursor()
    databaseQuery = "DELETE FROM players"
    cursor.execute(databaseQuery)
    databaseConnection.commit()
    databaseConnection.close()


def countPlayers():
    """Returns the number of players currently registered."""
    databaseConnection = connect()
    cursor = databaseConnection.cursor()
    databaseQuery = "SELECT COUNT(*) FROM players"
    cursor.execute(databaseQuery)
    count = cursor.fetchone()[0]
    databaseConnection.close()
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """

    databaseConnection = connect()
    cursor = databaseConnection.cursor()
    cursor.execute("insert into players (players_name) values (%s)", (name,))
    databaseConnection.commit()
    databaseConnection.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place,or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    databaseConnection = connect()
    cursor = databaseConnection.cursor()
    databaseQuery = "SELECT * FROM pairingsView;"
    cursor.execute(databaseQuery)
    fetchResults = cursor.fetchall()
    if (fetchResults[0][2] != 0) and (fetchResults[0][2] == fetchResults[1][2]):
        databaseQuery = "select "\
			"players_row_id,players_name,who_won_matchup,those_who_played "\
			"from pairingsView "\
			"order by (cast(who_won_matchup as decimal)/those_who_played) desc;"
    cursor.execute(databaseQuery)
    fetchResults = cursor.fetchall()
    databaseConnection.close()
    return fetchResults


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    databaseConnection = connect()
    cursor = databaseConnection.cursor()
    cursor.execute("INSERT INTO matches (winners_id, losers_id) "\
		"VALUES (%s, %s)", (winner, loser,))
    databaseConnection.commit()
    databaseConnection.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    databaseConnection = connect()
    cursor = databaseConnection.cursor()
    databaseQuery = "SELECT * FROM pairingsView"
    cursor.execute(databaseQuery)
    fetchResults = cursor.fetchall()
    count = len(fetchResults)
    swissPairings = []
    for x in range(0, count - 1, 2):
        pairingsList = (fetchResults[x][0], fetchResults[x][1], fetchResults[x + 1][0], fetchResults[x + 1][1])
        swissPairings.append(pairingsList)
    databaseConnection.close()
    return swissPairings

