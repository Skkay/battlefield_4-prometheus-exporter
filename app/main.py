import os
import time
import datetime
import requests
from prometheus_client import start_http_server, Gauge, Info

BATTLELOG_URL = os.environ.get('BATTLELOG_URL')

if BATTLELOG_URL == None:
    raise Exception('BATTLELOG_URL is not defined')

info = Info('battlefield_4_player', 'todo')
overviewStats_rank = Gauge('battlefield_4_overviewStats_rank', 'todo')
overviewStats_skill = Gauge('battlefield_4_overviewStats_skill', 'todo')
overviewStats_kills = Gauge('battlefield_4_overviewStats_kills_total', 'todo')
overviewStats_deaths = Gauge('battlefield_4_overviewStats_deaths_total', 'todo')
overviewStats_numWins = Gauge('battlefield_4_overviewStats_wins_total', 'todo')
overviewStats_numLosses = Gauge('battlefield_4_overviewStats_losses_total', 'todo')
overviewStats_numRounds = Gauge('battlefield_4_overviewStats_rounds_total', 'todo')
overviewStats_totalScore = Gauge('battlefield_4_overviewStats_score__total', 'todo')
overviewStats_timePlayed = Gauge('battlefield_4_overviewStats_timePlayed__total', 'todo')


def main():
    start_http_server(8080)

    while True:
        print('[{}] Refreshing metrics...'.format(datetime.datetime.now().isoformat()))

        data = requests.get(BATTLELOG_URL).json()

        refresh_metrics(data['data'])
        time.sleep(60 * 5)


def refresh_metrics(data):
    info.info({k: str(v) for k, v in data['viewedPersonaInfo'].items()})
    overviewStats_rank.set(data['overviewStats']['rank'])
    overviewStats_skill.set(data['overviewStats']['skill'])
    overviewStats_kills.set(data['overviewStats']['kills'])
    overviewStats_deaths.set(data['overviewStats']['deaths'])
    overviewStats_numWins.set(data['overviewStats']['numWins'])
    overviewStats_numLosses.set(data['overviewStats']['numLosses'])
    overviewStats_numRounds.set(data['overviewStats']['numRounds'])
    overviewStats_totalScore.set(data['overviewStats']['totalScore'])
    overviewStats_timePlayed.set(data['overviewStats']['timePlayed'])


if __name__ == '__main__':
    print('Application started.')
    main()
