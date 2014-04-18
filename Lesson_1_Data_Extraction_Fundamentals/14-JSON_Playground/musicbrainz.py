# To experiment with this code freely you will have to run this code locally.
# We have provided an example json output here for you to look at,
# but you will not be able to run any queries through our UI.
import json
import requests


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


def main():
    # results = query_by_name(ARTIST_URL, query_type["simple"], "Girls Generation")
    # pretty_print(results)

    # artist_id = results["artist"][1]["id"]
    # print "\nARTIST:"
    # pretty_print(results["artist"][1])

    # artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    # releases = artist_data["releases"]
    # print "\nONE RELEASE:"
    # pretty_print(releases[0], indent=2)
    # release_titles = [r["title"] for r in releases]

    # print "\nALL TITLES:"
    # for t in release_titles:
    #     print t

# What is the number of bands named "First Aid Kit"? "2"

    # Search for band by name
    results = query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")
    # Generate number of bands that have the exact name "First Aid Kit"
    number_of_bands = sum(1 for artist in results["artist"] if artist["name"] == "First Aid Kit")
    # Print that number, which is: 2
    print "First Aid", number_of_bands 

# What is the begin_area for Queen? "London"
    
    # Search for band by name
    results = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
    # How many bands have the name "Queen"? If 1, then just go ahead and print
    number_of_artists = sum(1 for artist in results["artist"] if artist["name"] == "Queen")
    # Damn, there are 3 bands with the name "Queen"
    print "The number of artists with the name 'Queen'", number_of_artists
    # What do I know about Queen? They released "Bohemian Rhapsody," they play in UK, they are named
    print [artist["disambiguation"] for artist in results["artist"] if artist["name"] == "Queen"]
    # Narrowed it down to one, so they started in London
    print [artist["begin-area"]["name"] for artist in results["artist"] if artist["name"] == "Queen" and artist["disambiguation"] =="UK rock group"]

    # pretty_print(results)
# What is the Spanish name for The Beatles? "Los Beatles"
    results = query_by_name(ARTIST_URL, query_type["simple"], "The Beatles")
    # Only 1 artist named "The Beatles"
    print sum(1 for artist in results["artist"] if artist["name"] == "The Beatles")
    # grab that one result
    for artist in results["artist"]:
        if artist["name"] == "The Beatles":
            for alias in artist["aliases"]:
                if alias["locale"] == "es":
                    print alias["name"]
    # Their Spanish alias is "Los Beatles"
    # if I knew all of this beforehand, I could drill down
    # more easily, but I searched as if I didn't know already


# Nirvana Disambiguation: "90s US grunge band"
    results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    # Only 3 artists named "Nirvana"
    print sum(1 for artist in results["artist"] if artist["name"] == "Nirvana")
    # I know that Nirvana is a US band in the 90s
    for artist in results["artist"]:
        if artist["name"] == "Nirvana":
            print artist["disambiguation"]
    # 90s US grunge band
    # 60s band from the UK
    # Early 1980's Finnish punk band

# When was One Direction formed? "2010"
    results = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
    # Only one banded named "One Direction"
    print sum(1 for artist in results["artist"] if artist["name"] == "One Direction")
    # find the 
    for artist in results["artist"]:
        if artist["name"] == "One Direction":
            print artist["life-span"]["begin"]
    # They started in 2010


if __name__ == '__main__':
    main()
