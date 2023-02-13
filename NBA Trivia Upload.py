import random

players = [
    {'name': 'Kareem Abdul-Jabbar', 'points': 38387, 'teams': 'Milwaukee Bucks, Los Angeles Lakers'},
    {'name': 'Ray Allen', 'points': 24505, 'teams': 'Milwaukee Bucks, Seattle SuperSonics, Boston Celtics, Miami Heat'},
    {'name': 'Giannis Antetokounmpo', 'points': 12319, 'teams': 'Milwaukee Bucks'},
    {'name': 'Carmelo Anthony', 'points': 27370, 'teams': 'Denver Nuggets, New York Knicks, Oklahoma City Thunder, Houston Rockets, Portland Trail Blazers'},
    {'name': 'Tiny Archibald', 'points': 16481, 'teams': 'Cincinnati Royals / Kansas City-Omaha / Kansas City Kings, New York Nets, Boston Celtics, Milwaukee Bucks'},
    {'name': 'Paul Arizin', 'points': 16266, 'teams': 'Philadelphia Warriors'},
    {'name': 'Charles Barkley', 'points': 23757, 'teams': 'Philadelphia 76ers, Phoenix Suns, Houston Rockets'},
    {'name': 'Rick Barry', 'points': 18395, 'teams': 'San Francisco / Golden State Warriors, Houston Rockets'},
    {'name': 'Elgin Baylor', 'points': 23149, 'teams': 'Minneapolis / Los Angeles Lakers'},
    {'name': 'Dave Bing', 'points': 18327, 'teams': 'Detroit Pistons, Washington Bullets, Boston Celtics'},
    {'name': 'Larry Bird', 'points': 21791, 'teams': 'Boston Celtics'},
    {'name': 'Kobe Bryant', 'points': 33643, 'teams': 'Los Angeles Lakers'},
    {'name': 'Wilt Chamberlain', 'points': 31419, 'teams': 'Philadelphia / San Francisco Warriors, Philadelphia 76ers, Los Angeles Lakers'},
    {'name': 'Bob Cousy', 'points': 16960, 'teams': 'Boston Celtics, Cincinnati Royals'},
    {'name': 'Dave Cowens', 'points': 13516, 'teams': 'Boston Celtics, Milwaukee Bucks'},
    {'name': 'Billy Cunningham', 'points': 13626, 'teams': 'Philadelphia 76ers'},
    {'name': 'Stephen Curry', 'points': 18434, 'teams': 'Golden State Warriors'},
    {'name': 'Anthony Davis', 'points': 13463, 'teams': 'New Orleans Hornets / Pelicans, Los Angeles Lakers'},
    {'name': 'Dave DeBusschere', 'points': 14053, 'teams': 'Detroit Pistons, New York Knicks'},
    {'name': 'Clyde Drexler', 'points': 22195, 'teams': 'Portland Trail Blazers, Houston Rockets'},
    {'name': 'Tim Duncan', 'points': 26496, 'teams': 'San Antonio Spurs'},
    {'name': 'Kevin Durant', 'points': 23883, 'teams': 'Seattle SuperSonics / Oklahoma City Thunder, Golden State Warriors, Brooklyn Nets'},
    {'name': 'Julius Erving', 'points': 18364, 'teams': 'Philadelphia 76ers'},
    {'name': 'Patrick Ewing', 'points': 24815, 'teams': 'New York Knicks, Seattle SuperSonics, Orlando Magic'},
    {'name': 'Walt Frazier', 'points': 15581, 'teams': 'New York Knicks, Cleveland Cavaliers'},
    {'name': 'Kevin Garnett', 'points': 26071, 'teams': 'Minnesota Timberwolves, Boston Celtics, Brooklyn Nets'},
    {'name': 'George Gervin', 'points': 20708, 'teams': 'San Antonio Spurs, Chicago Bulls'},
    {'name': 'Hal Greer', 'points': 21586, 'teams': 'Syracuse Nationals / Philadelphia 76ers'},
    {'name': 'James Harden', 'points': 22045, 'teams': 'Oklahoma City Thunder, Houston Rockets, Brooklyn Nets'},
    {'name': 'John Havlicek', 'points': 26395, 'teams': 'Boston Celtics'},
    {'name': 'Elvin Hayes', 'points': 27313, 'teams': 'San Diego / Houston Rockets, Baltimore / Capital / Washington Bullets'},
    {'name': 'Allen Iverson', 'points': 24368, 'teams': 'Philadelphia 76ers, Denver Nuggets, Detroit Pistons, Memphis Grizzlies'},
    {'name': 'LeBron James', 'points': 35385, 'teams': 'Cleveland Cavaliers, Miami Heat, Los Angeles Lakers'},
    {'name': 'Magic Johnson', 'points': 17707, 'teams': 'Los Angeles Lakers'},
    {'name': 'Sam Jones', 'points': 15411, 'teams': 'Boston Celtics'},
    {'name': 'Michael Jordan', 'points': 32292, 'teams': 'Chicago Bulls, Washington Wizards'},
    {'name': 'Jason Kidd', 'points': 17529, 'teams': 'Dallas Mavericks, Phoenix Suns, New Jersey Nets, New York Knicks'},
    {'name': 'Kawhi Leonard', 'points': 11085, 'teams': 'San Antonio Spurs, Toronto Raptors, Los Angeles Clippers'},
    {'name': 'Damian Lillard', 'points': 16815, 'teams': 'Portland Trail Blazers'},
    {'name': 'Jerry Lucas', 'points': 14053, 'teams': 'Cincinnati Royals, San Francisco Warriors, New York Knicks'},
    {'name': 'Karl Malone', 'points': 36928, 'teams': 'Utah Jazz, Los Angeles Lakers'},
    {'name': 'Moses Malone', 'points': 27409, 'teams': 'Buffalo Braves, Houston Rockets, Philadelphia 76ers, Washington Bullets, Atlanta Hawks, Milwaukee Bucks, San Antonio Spurs'},
    {'name': 'Pete Maravich', 'points': 15948, 'teams': 'Atlanta Hawks, New Orleans / Utah Jazz, Boston Celtics'},
    {'name': 'Bob McAdoo', 'points': 18787, 'teams': 'Buffalo Braves, New York Knicks, Boston Celtics, Detroit Pistons, New Jersey Nets, Los Angeles Lakers, Philadelphia 76ers'},
    {'name': 'Kevin McHale', 'points': 17335, 'teams': 'Boston Celtics'},
    {'name': 'George Mikan', 'points': 10156, 'teams': 'Minneapolis Lakers'},
    {'name': 'Reggie Miller', 'points': 25276, 'teams': 'Indiana Pacers'},
    {'name': 'Earl Monroe', 'points': 17454, 'teams': 'Baltimore Bullets, New York Knicks'},
    {'name': 'Steve Nash', 'points': 17387, 'teams': 'Phoenix Suns, Dallas Mavericks, Los Angeles Lakers'},
    {'name': 'Dirk Nowitzki', 'points': 31560, 'teams': 'Dallas Mavericks'},
    {'name': "Shaquille O'Neal", 'points': 28596, 'teams': 'Orlando Magic, Los Angeles Lakers, Miami Heat, Phoenix Suns, Cleveland Cavaliers, Boston Celtics'},
    {'name': 'Hakeem Olajuwon', 'points': 26946, 'teams': 'Houston Rockets, Toronto Raptors'},
    {'name': 'Robert Parish', 'points': 23334, 'teams': 'Golden State Warriors, Boston Celtics, Charlotte Hornets, Chicago Bulls'},
    {'name': 'Chris Paul', 'points': 19978, 'teams': 'New Orleans Hornets, Los Angeles Clippers, Houston Rockets, Oklahoma City Thunder, Phoenix Suns'},
    {'name': 'Gary Payton', 'points': 21813, 'teams': 'Seattle SuperSonics, Milwaukee Bucks, Los Angeles Lakers, Boston Celtics, Miami Heat'},
    {'name': 'Bob Pettit', 'points': 20880, 'teams': 'Milwaukee / St. Louis Hawks'},
    {'name': 'Paul Pierce', 'points': 26397, 'teams': 'Boston Celtics, Brooklyn Nets, Washington Wizards, Los Angeles Clippers'},
    {'name': 'Scottie Pippen', 'points': 18940, 'teams': '[Chicago Bulls, Houston Rockets, Portland Trail Blazers'},
    {'name': 'Willis Reed', 'points': 12183, 'teams': 'New York Knicks'},
    {'name': 'Oscar Robertson', 'points': 26710, 'teams': 'Cincinnati Royals, Milwaukee Bucks'},
    {'name': 'David Robinson', 'points': 20790, 'teams': 'San Antonio Spurs'},
    {'name': 'Dennis Rodman', 'points': 6683, 'teams': 'Detroit Pistons, San Antonio Spurs, Chicago Bulls, Los Angeles Lakers, Dallas Mavericks'},
    {'name': 'Bill Russell', 'points': 14522, 'teams': 'Boston Celtics'},
    {'name': 'Dolph Schayes', 'points': 18438, 'teams': 'Syracuse Nationals / Philadelphia 76ers'},
    {'name': 'Bill Sharman', 'points': 12665, 'teams': 'Washington Capitols, Boston Celtics'},
    {'name': 'John Stockton', 'points': 19711, 'teams': 'Utah Jazz'},
    {'name': 'Isiah Thomas', 'points': 18822, 'teams': 'Detroit Pistons'},
    {'name': 'Nate Thurmond', 'points': 14437, 'teams': 'San Francisco / Golden State Warriors, Chicago Bulls, Cleveland Cavaliers'},
    {'name': 'Wes Unseld', 'points': 10624, 'teams': 'Baltimore / Capital / Washington Bullets'},
    {'name': 'Dwyane Wade', 'points': 23165, 'teams': 'Miami Heat, Chicago Bulls, Cleveland Cavaliers'},
    {'name': 'Bill Walton', 'points': 6215, 'teams': 'Portland Trail Blazers, San Diego / Los Angeles Clippers, Boston Celtics'},
    {'name': 'Jerry West', 'points': 25192, 'teams': 'Los Angeles Lakers'},
    {'name': 'Russell Westbrook', 'points': 21857, 'teams': 'Oklahoma City Thunder, Houston Rockets, Washington Wizards'},
    {'name': 'Lenny Wilkens', 'points': 17772, 'teams': 'St. Louis Hawks, Seattle SuperSonics, Cleveland Cavaliers, Portland Trail Blazers'},
    {'name': 'Dominique Wilkins', 'points': 26668, 'teams': 'Atlanta Hawks, Los Angeles Clippers, Boston Celtics, San Antonio Spurs, Orlando Magic'},
    {'name': 'James Worthy', 'points': 16320, 'teams': 'Los Angeles Lakers'},

]


def trivia():
    score = 0
    for i in range(5):
        answer = random.choice(players)
        question = input('Who is this basketball player? They had ' + str(answer['points']) + ' points and played for ' + answer['teams'] + '. ')
        if question.lower() == answer['name'].lower():
            print('Correct!')
            score += 1
        if question.lower() != answer['name'].lower():
            print('Incorrect. The player is ' + answer['name'] + '.')
    print('Your final score is ' + str(score) + '/5')


trivia()