# -*- coding: utf-8 -*-

import json
import glob

# This function reads a json file into an object
def read_json_file(filename):
    with open(filename) as json_file:
        return json.load(json_file)


# This function checks if a file without extension exists in current directory
def check_file_exists(filename, extension=".*"):
    if not extension:
        return glob.glob(filename)
    else:
        return glob.glob(filename + extension)


# This function finds all json files in current directory
def find_json_files():
    return glob.glob("*.json")


VALID_KOMKODES = [
    "101",
    "147",
    "151",
    "153",
    "155",
    "157",
    "159",
    "161",
    "163",
    "165",
    "167",
    "169",
    "173",
    "175",
    "183",
    "185",
    "187",
    "190",
    "201",
    "210",
    "217",
    "219",
    "223",
    "230",
    "240",
    "250",
    "253",
    "259",
    "260",
    "265",
    "269",
    "270",
    "306",
    "316",
    "320",
    "326",
    "329",
    "330",
    "336",
    "340",
    "350",
    "360",
    "370",
    "376",
    "390",
    "400",
    "410",
    "411",
    "420",
    "430",
    "440",
    "450",
    "461",
    "479",
    "480",
    "482",
    "492",
    "510",
    "530",
    "540",
    "550",
    "561",
    "563",
    "573",
    "575",
    "580",
    "607",
    "615",
    "621",
    "630",
    "657",
    "661",
    "665",
    "671",
    "706",
    "707",
    "710",
    "727",
    "730",
    "740",
    "741",
    "746",
    "751",
    "756",
    "760",
    "766",
    "773",
    "779",
    "787",
    "791",
    "810",
    "813",
    "820",
    "825",
    "840",
    "846",
    "849",
    "851",
    "860",
    "*",
]


if __name__ == "__main__":
    errs = []
    cfgs = find_json_files()

    try:
        for cfg in cfgs:
            config = read_json_file(cfg)

            # This function adds a line to the error list starting with the configuration file name
            def add_error(error):
                errs.append(f"{cfg}: {error}")

            # Check if print configuration exists
            if "enabledPrints" in config:
                for templates in config["enabledPrints"]:
                    if templates == "print": #"print" is the default print configuration
                        continue
                    if not check_file_exists(templates, ".tmpl"):
                        add_error(f"Print configuration '{templates}' does not exist")

            # Check if css configuration exists
            if "cssFiles" in config:
                for css in config["cssFiles"]:
                    if not check_file_exists(css, None):
                        add_error(f"CSS configuration '{css}' does not exist")

            # Check if kommunekodes are valid
            if "searchConfig" in config and "komkode" in config["searchConfig"]:
                komlist = config["searchConfig"]["komkode"]

                # if komlist is a string, convert it to a list
                if isinstance(komlist, str):
                    komlist = [komlist]

                for komkode in komlist:
                    if komkode not in VALID_KOMKODES:
                        add_error(f"Kommunekode '{komkode}' does not exist")

        # If there are errors, print them and exit with error code 1
        if errs:
            for err in errs:
                print(err)
            exit(1)

    except Exception as e:
        print(f"Error: {e}")
        exit(1)
