import rethinkdb
conn = rethinkdb.connect(db='todo')

# Delete all exising rows
rethinkdb.table('todos').delete().run(conn)

# Add records
rethinkdb.table('todos').insert({'name': 'Sail to the moon.'}).run(conn)
rethinkdb.table('todos').insert({'name': 'Jump in the ocean.'}).run(conn)
rethinkdb.table('todos').insert(
    {'name': 'Go on a walkabout in the Australian outback.'}).run(conn)
rethinkdb.table('todos').insert(
    {'name': 'Ride in a hot air balloon.'}).run(conn)
rethinkdb.table('todos').insert({'name': 'Swim with dolphins.'}).run(conn)
rethinkdb.table('todos').insert(
    {'name': 'Learn a foreign language and actually use it.'}).run(conn)
rethinkdb.table('todos').insert(
    {'name': 'Watch a Stanley Cup playoff game.'}).run(conn)
rethinkdb.table('todos').insert({'name': 'Visit New Zealand.'}).run(conn)
rethinkdb.table('todos').insert({'name': 'Skydive.'}).run(conn)
rethinkdb.table('todos').insert({'name': 'Scuba dive with sharks.'}).run(conn)
rethinkdb.table('todos').insert(
    {'name': 'Make a big whack of chicken wings.'}).run(conn)
rethinkdb.table('todos').insert({'name': 'Ride a train though the Canadian rockies.'}).run(conn)
rethinkdb.table('todos').insert(
    {'name': 'Walk the east coast trail.'}).run(conn)
rethinkdb.table('todos').insert(
    {'name': 'Go to Miami and eat another Cuban sandwich.'}).run(conn)
