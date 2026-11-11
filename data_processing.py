import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

def aggregate(aggregation_key, aggregation_function, dict_list):
    """
    Aggregate values associated with aggregation_key using the
    provided aggregation function.

    Args:
        aggregation_key: The dictionary key whose values should be aggregated.
        aggregation_function: A function such as sum, max, min, etc.
        dict_list: A list of dictionaries.

    Returns:
        The aggregated result.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]

        >>> aggregate("score", sum, students)
        245

        >>> aggregate("score", max, students)
        90

        >>> aggregate("score", min, students)
        70

        >>> aggregate(
        ...     "score",
        ...     lambda scores: sum(scores) / len(scores),
        ...     students
        ... )
        81.66666666666667
    """
    if aggregation_key is None:
        return aggregation_function(dict_list)
    values = [d[aggregation_key] for d in dict_list]
    return aggregation_function(values)


# Print the average temperature of all the cities
print("The average temperature of all the cities:")
print(aggregate('temperature', lambda temp: sum(float(t) for t in temp)/len(temp), cities))
print()

# Print all cities in Germany
print("Cities in Germany:")
print(aggregate(None, 
                lambda dicts: [c['city'] for c in dicts if c['country'] == 'Germany'], 
                cities))
print()

# Print all cities in Spain with a temperature above 12°C
print("all cities in Spain with a temperature above 12°C:")
print(aggregate(None, lambda dicts: [c['city'] for c in dicts if (c['country'] == 'Spain') and (float(c['temperature']) > 12)], cities))
print()

# Count the number of unique countries
print("the number of unique countries:")
print(aggregate('country', lambda uniq: len(set(uniq)), cities))
print()


# Print the average temperature for all the cities in Germany
print("the average temperature for all the cities in Germany:")
print(aggregate(None, lambda dicts: sum([float(c['temperature']) for c in dicts if c['country'] == 'Germany'])/len([c['temperature'] for c in dicts if c['country'] == 'Germany']), cities))
print()

# Print the max temperature for all the cities in Italy
print("the max temperature for all the cities in Italy:")
print(aggregate(None, lambda dicts: max([float(c['temperature']) for c in dicts if c['country'] == 'Italy']), cities))
