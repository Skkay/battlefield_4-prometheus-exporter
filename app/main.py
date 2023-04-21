import os
import time
import datetime
import requests
from prometheus_client import start_http_server, Gauge

BATTLELOG_PLAYER_ID = os.environ.get('BATTLELOG_PLAYER_ID')

if BATTLELOG_PLAYER_ID == None:
    raise Exception('BATTLELOG_PLAYER_ID is not defined')

BATTLELOG_GENERAL_STATS_URL = f'https://battlelog.battlefield.com/bf4/warsawdetailedstatspopulate/{BATTLELOG_PLAYER_ID}/1'

generalStats_skill = Gauge('battlefield_4_generalStats_skill', 'Current skill')
generalStats_timePlayed = Gauge('battlefield_4_generalStats_timePlayed', 'Time played in seconds')
generalStats_rank = Gauge('battlefield_4_generalStats_rank', 'Current rank')
generalStats_scoreTotal = Gauge('battlefield_4_generalStats_scoreTotal', 'Total player score')
generalStats_scoreVehicle = Gauge('battlefield_4_generalStats_scoreVehicle', 'Total vehicle score')
generalStats_scoreUnlock = Gauge('battlefield_4_generalStats_scoreUnlock', 'Total unlock score')
generalStats_scoreAward = Gauge('battlefield_4_generalStats_scoreAward', 'Total award score')
generalStats_scoreSquad = Gauge('battlefield_4_generalStats_scoreSquad', 'Total squad score')
generalStats_scoreAssault = Gauge('battlefield_4_generalStats_scoreAssault', 'Total assault score')
generalStats_scoreEngineer = Gauge('battlefield_4_generalStats_scoreEngineer', 'Total engineer score')
generalStats_scoreSupport = Gauge('battlefield_4_generalStats_scoreSupport', 'Total support score')
generalStats_scoreRecon = Gauge('battlefield_4_generalStats_scoreRecon', 'Total recon score')
generalStats_scoreCommander = Gauge('battlefield_4_generalStats_scoreCommander', 'Total commander score')
generalStats_deaths = Gauge('battlefield_4_generalStats_deaths', 'Number of deaths')
generalStats_kills = Gauge('battlefield_4_generalStats_kills', 'Number of kills')
generalStats_killsAssault = Gauge('battlefield_4_generalStats_killsAssault', 'Number of kills with assault kit')
generalStats_killsRecon = Gauge('battlefield_4_generalStats_killsRecon', 'Number of kills with recon kit')
generalStats_killsSupport = Gauge('battlefield_4_generalStats_killsSupport', 'Number of kills with support kit')
generalStats_killsEngineer = Gauge('battlefield_4_generalStats_killsEngineer', 'Number of kills with engineer kit')
generalStats_avengerKills = Gauge('battlefield_4_generalStats_avengerKills', 'Number of avenger kills')
generalStats_saviorKills = Gauge('battlefield_4_generalStats_saviorKills', 'Number of savior kills')
generalStats_headshots = Gauge('battlefield_4_generalStats_headshots', 'Number of headshots')
generalStats_longestHeadshot = Gauge('battlefield_4_generalStats_longestHeadshot', 'Longest headshot in meters')
generalStats_highestKillStreak = Gauge('battlefield_4_generalStats_highestKillStreak', 'Highest kill streak')
generalStats_killAssists = Gauge('battlefield_4_generalStats_killAssists', 'Number of kill assists')
generalStats_wins = Gauge('battlefield_4_generalStats_wins', 'Number of rounds won')
generalStats_losses = Gauge('battlefield_4_generalStats_losses', 'Number of rounds lost')
generalStats_rounds = Gauge('battlefield_4_generalStats_rounds', 'Numer of rounds played')
generalStats_shotsFired = Gauge('battlefield_4_generalStats_shotsFired', 'Number of shots fired')
generalStats_shotsHit = Gauge('battlefield_4_generalStats_shotsHit', 'Number of shots hit')
generalStats_repairs = Gauge('battlefield_4_generalStats_repairs', 'Number of repairs')
generalStats_resupplies = Gauge('battlefield_4_generalStats_resupplies', 'Number of resupplies')
generalStats_revives = Gauge('battlefield_4_generalStats_revives', 'Number of revives')
generalStats_heals = Gauge('battlefield_4_generalStats_heals', 'Number of heals')
generalStats_suppressionAssists = Gauge('battlefield_4_generalStats_suppressionAssists', 'Number of suppression assists')
generalStats_vehiclesDestroyed = Gauge('battlefield_4_generalStats_vehiclesDestroyed', 'Number of vehicles destroyed')
generalStats_vehicleDamage = Gauge('battlefield_4_generalStats_vehicleDamage', 'Total vehicle damage')
generalStats_flagCaptured = Gauge('battlefield_4_generalStats_flagCaptured', 'Number of flag captured')
generalStats_flagDefend = Gauge('battlefield_4_generalStats_flagDefend', 'Number of flag defend')


def main():
    start_http_server(8080)

    while True:
        print('[{}] Refreshing metrics...'.format(datetime.datetime.now().isoformat()))

        refresh_generalStats_metrics()

        time.sleep(60 * 5)


def refresh_generalStats_metrics():
    res = requests.get(BATTLELOG_GENERAL_STATS_URL)
    res.raise_for_status()

    data = res.json()['data']['generalStats']

    generalStats_skill.set(int(data['skill']))
    generalStats_timePlayed.set(int(data['timePlayed']))
    generalStats_rank.set(int(data['rank']))
    generalStats_scoreTotal.set(int(data['score']))
    generalStats_scoreVehicle.set(int(data['sc_vehicle']))
    generalStats_scoreUnlock.set(int(data['sc_unlock']))
    generalStats_scoreAward.set(int(data['sc_award']))
    generalStats_scoreSquad.set(int(data['sc_squad']))
    generalStats_scoreAssault.set(int(data['assault']))
    generalStats_scoreEngineer.set(int(data['engineer']))
    generalStats_scoreSupport.set(int(data['support']))
    generalStats_scoreRecon.set(int(data['recon']))
    generalStats_scoreCommander.set(int(data['commander']))
    generalStats_deaths.set(int(data['deaths']))
    generalStats_kills.set(int(data['kills']))
    generalStats_killsAssault.set(int(data['kills_assault']))
    generalStats_killsRecon.set(int(data['kills_recon']))
    generalStats_killsSupport.set(int(data['kills_support']))
    generalStats_killsEngineer.set(int(data['kills_engineer']))
    generalStats_avengerKills.set(int(data['avengerKills']))
    generalStats_saviorKills.set(int(data['saviorKills']))
    generalStats_headshots.set(int(data['headshots']))
    generalStats_longestHeadshot.set(data['longestHeadshot'])
    generalStats_highestKillStreak.set(int(data['killStreakBonus']))
    generalStats_killAssists.set(int(data['killAssists']))
    generalStats_wins.set(int(data['numWins']))
    generalStats_losses.set(int(data['numLosses']))
    generalStats_rounds.set(int(data['numRounds']))
    generalStats_shotsFired.set(int(data['shotsFired']))
    generalStats_shotsHit.set(int(data['shotsHit']))
    generalStats_repairs.set(int(data['repairs']))
    generalStats_resupplies.set(int(data['resupplies']))
    generalStats_revives.set(int(data['revives']))
    generalStats_heals.set(int(data['heals']))
    generalStats_suppressionAssists.set(int(data['suppressionAssists']))
    generalStats_vehiclesDestroyed.set(int(data['vehiclesDestroyed']))
    generalStats_vehicleDamage.set(int(data['vehicleDamage']))
    generalStats_flagCaptured.set(int(data['flagCaptures']))
    generalStats_flagDefend.set(int(data['flagDefend']))


if __name__ == '__main__':
    print('Application started.')
    main()
