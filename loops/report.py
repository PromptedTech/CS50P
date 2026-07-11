def main():
    spacecraft = {
        'name': 'James Webb Space Telescope',
    }
    # spacecraft['distance'] = 0.01 ts is one method to add some key and value to da existing dict
    spacecraft.update({'distance': 0.01, 'orbit': 'Sun'}) # ts is the other way to add sm value to da existing dict
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
=========  REPORT  =========


Name: {spacecraft.get('name', 'Unknown')}
Distance: {spacecraft.get('distance', 'Unknown')} AU
Orbit = {spacecraft.get('orbit', 'Unknown')}

============================
"""

main()